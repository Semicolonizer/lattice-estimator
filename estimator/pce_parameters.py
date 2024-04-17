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

            TODO: Add example 

        """
        d = dict(self.__dict__)
        d.update(kwds)
        return PCEParameters(**d)
    
    def __hash__(self):
        return hash((self.n, self.k, self.q, self.w))