from .lip_parameters import LIPParameters
from .cost import Cost
from sage.all import oo, is_prime


class GeometricInvariants():
    """
    Estimate cost of using geometric invariants.
    """

    def __call__(
        self,
        params: LIPParameters,
        log_level=1,
        **kwds,
    ):
        """
        Estimate cost of using geometric invariants.

        :param params: LIP parameters.
        :return: A cost dictionary.

        The returned cost dictionary has the following entries:

        - ``rop``: Total number of word operations (≈ CPU cycles).
        - ``d``: Lattice dimension.

        EXAMPLES:
        # TODO: list examples

        """
        
        # Cost for all geometric invariants is enumerated cost, which is already implemented
        # TODO: call also here

        cost = Cost()
        cost["tag"] = "geometric invariant"
        cost["problem"] = params
        
        return cost.sanity_check()

geominv = GeometricInvariants()