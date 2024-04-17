from .pce_parameters import PCEParameters
from .cost import Cost
from sage.all import oo, log, binomial

class SSA():
    """
    Estimate cost of solving PCE using the Support Splitting Algorithm(SSA).
    """

    def __call__(
        self,
        params: PCEParameters,
        log_level=1,
        **kwds,
    ):
        """
        Estimate cost of solving PCE using SSA.

        :param params: PCE parameters.
        :return: A cost dictionary.

        The returned cost dictionary has the following entries:

        - ``rop``: Total number of word operations (≈ CPU cycles).

        """

        cost = Cost()

        # Estimated cost of finding a permutation between codes
        if params.h <= min(params.k, params.n-params.k):
            cost['rop'] = params.n**3 + params.n**2 * params.q**params.h * log(params.n)
        else:
            cost['rop'] = oo
        

        
        cost["tag"] = "ssa"
        cost["problem"] = params
        
        return cost

ssa = SSA()