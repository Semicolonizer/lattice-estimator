from dataclasses import dataclass

@dataclass
class PCEParameters:
    # Parameters for a LIP instance.

    n: int  #: the dimension. 
    k: int  #: the dimenson of the vector subspace 
    q: int  #: the modulus.
    h: int  #: the hull.
    w: int  #: the target weight of codewords for ISD


    def updated(self, **kwds):  
        """
        Return a new set of parameters updated according to ``kwds``.

        :param kwds: We set ``key`` to ``value`` in the new set of parameters.

        EXAMPLE::

            >>> p = PCE.Parameters(q=7, n=128, k=64, h=50, w=5)
            PCEParameters(n=128, k=64, q=7, h=50, w=5)
            >>> p.updated(q=7, n=128, k=64, h=5, w=5)
            PCEParameters(n=128, k=64, q=7, h=5, w=5)

            >>> p = PCE.Parameters(q=7, n=128, k=64, h=5, w=5)
            PCEParameters(n=128, k=64, q=7, h=5, w=5)
            >>> p.updated(q=7, n=128, k=64, h=50, w=5)
            PCEParameters(n=128, k=64, q=7, h=50, w=5)
            

        """
        d = dict(self.__dict__)
        d.update(kwds)
        return PCEParameters(**d)
    
    def __hash__(self):
        return hash((self.n, self.k, self.q, self.w))