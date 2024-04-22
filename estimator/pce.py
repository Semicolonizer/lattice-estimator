from .pce_leon import leon
from .pce_beullens import beullen
from .pce_ssa import ssa
from .pce_bos import bos
from .util import batch_estimate, f_name
from sage.all import oo
from .pce_parameters import PCEParameters as Parameters

class Estimate:

    def rough(self, params, jobs=1, catch_exceptions=True):
        """
        Provides a rough estimation for the Permutation Code Equivalence problem.

        Parameters:
        pce_parameters (PCEParameters): Parameters necessary for estimation.

        Returns:
        res (dict): The rough cost estimation results.
        """

        algorithms = {}
        algorithms['beullen'] = beullen
        algorithms['ssa'] = ssa
        
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
        Provides a full estimation for the Permutation Code Equivalence problem when the class instance is called.

        Parameters:
        pce_parameters (PCEParameters): Parameters necessary for estimation.

        Returns:
        res (dict): The cost estimation results for attacks.
        """

        algorithms = {}
        algorithms['beullen'] = beullen
        algorithms['leon'] = leon
        algorithms['ssa'] = ssa
        algorithms['bos'] = bos
        
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