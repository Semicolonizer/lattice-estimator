from .pce_parameters import PCEParameters
from .cost import Cost
from sage.all import oo, log, binomial, exp, sqrt

class BOS():
    """
    Estimate cost of solving PCE using the Bardet, Otmani, and Saeed-Taha(BOS) algorithm.
    """

    def __call__(
        self,
        params: PCEParameters,
        log_level=1,
        **kwds,
    ):
        """
        Estimate cost of solving PCE using BOS.

        :param params: PCE parameters.
        :return: A cost dictionary.

        The returned cost dictionary has the following entries:

        - ``rop``: Total number of word operations (≈ CPU cycles).

        """

        cost = Cost()
        sqrt_log_n_value = sqrt(log(params.n))

        # Weighted graph isomorphism cost
        C_wgi = exp(exp(sqrt_log_n_value))

        # Estimated cost of finding a permutation between codes
        if params.h == 0:
            cost['rop'] = params.n**params.w  * C_wgi
        else:
            cost['rop'] = params.h * params.n**(params.w + [params.h] + 1) * C_wgi
        
        cost["tag"] = "bos"
        cost["problem"] = params
        
        return cost

bos = BOS()