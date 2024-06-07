from .lip_parameters import LIPParameters as Parameters
from .lip_hull import hullattack
from .util import batch_estimate, f_name
from sage.all import oo

class Estimate:

    def rough(self, params, jobs=1, catch_exceptions=True):
        """
        Provides a rough estimation for the Lattice Isomorphism Problem.

        Parameters:
        params (dict): A dictionary of parameters necessary for the estimation.

        Returns:
        res (dict): The rough cost estimation results.
        """

        algorithms = {}
        algorithms['hull'] = hullattack
        
        res_raw = batch_estimate(
            params, algorithms.values(), log_level=1, jobs=jobs, catch_exceptions=catch_exceptions
        )
        res_raw = res_raw[params]
        res = {
            algorithm: v
            for algorithm, attack in algorithms.items()
            for k, v in res_raw.items()
            if f_name(attack) == k
        }

        for algorithm in algorithms:
            if algorithm not in res:
                continue
            result = res[algorithm]
            if result["rop"] != oo:
                print(f"{algorithm:8s} :: {result!r}")

        return res
    
    def __call__(self, lip_parameters):
        """
        Provides a full estimation for the Lattice Isomorphism Problem when the class instance is called.

        Parameters:
        lip_parameters (dict): A dictionary of parameters necessary for the precise estimation.

        Returns:
        res (dict): The cost estimation results for attacks.
        """

        algorithms = {}

        # Compute estimations based on the parameters
        res = 0  # TODO: Replace with actual logic
        return res

estimate = Estimate()