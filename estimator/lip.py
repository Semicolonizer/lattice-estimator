from .lip_parameters import LIPParameters as Parameters
from .lip_hull import hullattack
from .lip_havreg import havreg
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

        
        EXAMPLES:
        
        >>> from estimator import *
        >>> _ = LIP.estimate.rough(LIP.Parameters(200,127))
        hull     :: rop: ≈2^86.7, tag: ssa, red: ≈2^86.7, δ: 1.006187, β: log(200) + 200.0, d: 400, non_red: ≈2^23.0
        havreg   :: rop: ≈2^132.9, red: ≈2^132.9, δ: 1.003982, β: 400, d: 400
        """

        algorithms = {}
        algorithms['hull'] = hullattack
        algorithms['havreg'] = havreg 
        
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
    
    def __call__(self, params, jobs=1, catch_exceptions=True):
        """
        Provides a full estimation for the Lattice Isomorphism Problem when the class instance is called.

        Parameters:
        params (dict): A dictionary of parameters necessary for the precise estimation.

        Returns:
        res (dict): The cost estimation results for attacks.

        EXAMPLES:

        >>> _ = LIP.estimate(LIP.Parameters(300,127))
        hull     :: rop: ≈2^115.0, tag: ssa, red: ≈2^115.0, δ: 1.004779, β: log(300) + 300.0, d: 600, non_red: ≈2^24.7
        havreg   :: rop: ≈2^188.6, red: ≈2^188.6, δ: 1.002986, β: 600, d: 600

        """

        algorithms = {}
        algorithms['hull'] = hullattack
        algorithms['havreg'] = havreg 
        
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

estimate = Estimate()