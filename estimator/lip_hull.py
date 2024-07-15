from .lip_parameters import LIPParameters
from .pce_parameters import PCEParameters
from .cost import Cost
from .conf import red_cost_model as red_cost_model_default
from .conf import red_shape_model as red_shape_model_default
from .conf import red_simulator as red_simulator_default
from .reduction import cost as costf
from .reduction import beta as betaf
from .util import local_minimum
from .pce_ssa import ssa
from sage.all import oo, is_prime, sqrt, log, RR, floor, cached_function


class HullAttack():
    """
    Estimate cost of solving LIP using the Hull Attack.
    """

    def find_d(params):
        """
        Finds the dimension d for the reduction.

        :param params: The LIP parameters.
        :return d: The dimension.
        """
        # Extend evaluation to include special cases

        return 2*params.n

    def __call__(
        self,
        params: LIPParameters,
        red_cost_model=red_cost_model_default,
        red_shape_model = red_shape_model_default,
        log_level=1,
        **kwds,
    ):
        """
        Estimate cost of solving LIP using the Hull Attack.

        :param params: LIP parameters.
        :return: A cost dictionary.

        The returned cost dictionary has the following entries:

        - ``rop``: Total number of word operations (≈ CPU cycles).
        - ``red``: Number of word operations in lattice reduction.
        - ``δ``: Root-Hermite factor targeted by lattice reduction.
        - ``β``: BKZ block size.
        - ``d``: Lattice dimension.
        - ``non_red``: Number of non-reduction word operations.

        EXAMPLES:
        # TODO: list examples

        """
        
        cost = Cost()
        cost["tag"] = "hull_attack"
        cost["problem"] = params

        # Check viability
        if not is_prime(params.q):
            cost['rop'] = oo
            return cost.sanity_check()
        
        
        d = 2*params.n
        # Verify blocksize 
        if d < 2:
            cost['rop'] = oo
            return cost.sanity_check()

        # Currently only supports GSA 
        if red_shape_model == "gsa":
            cost = costf(red_cost_model, d/2+log(params.n), d, predicate=True)
            
        # Assume trivial hull as in []
        code_length = params.n
        code_dimension = params.n
        field_mod = params.q
        pce_inst = PCEParameters(q=field_mod, n=code_length, k=code_dimension, h=0, w=5)
        pce_cost = ssa(pce_inst)

        cost = cost.__add__(pce_cost)
        cost['non_red'] = pce_cost['rop']
        
        return cost.sanity_check()

hullattack = HullAttack()