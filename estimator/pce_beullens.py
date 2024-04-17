from .pce_parameters import PCEParameters
from .cost import Cost
from .ISD import ISDCost
from sage.all import oo, log, binomial

class Beullen():
    """
    Estimate cost of solving PCE using Beullens' algorithm.
    """

    def __call__(
        self,
        params: PCEParameters,
        log_level=1,
        **kwds,
    ):
        """
        Estimate cost of solving PCE using Beullens' algorithm.

        :param params: PCE parameters.
        :return: A cost dictionary.

        The returned cost dictionary has the following entries:

        - ``rop``: Total number of word operations (≈ CPU cycles).

        """

        cost = Cost()

        # Approximated expected cardinality of A_w
        N_w = binomial(params.n, params.w) * (params.q-1) ** (params.w-2) * params.q ** (params.k-params.n+1)
        
        # Estimated cost of finding low-weight codewords
        isd_cost = ISDCost.lee_brickell(params.q, params.n, params.k, params.w, N_w, L=1)

        cost['rop'] = isd_cost
        cost["tag"] = "beullen"
        cost["problem"] = params
        
        return cost

beullen = Beullen()