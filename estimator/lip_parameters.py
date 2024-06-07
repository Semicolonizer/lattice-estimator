from dataclasses import dataclass

@dataclass
class LIPParameters:
    # Parameters for a LIP instance.

    n: int  #: the dimension.
    q: int  #: the modulus.


    def updated(self, **kwds):  
        """
        Return a new set of parameters updated according to ``kwds``.

        :param kwds: We set ``key`` to ``value`` in the new set of parameters.

        EXAMPLE::

            TODO: Add example 

        """
        d = dict(self.__dict__)
        d.update(kwds)
        return LIPParameters(**d)
    
    def __hash__(self):
        return hash((self.n, self.q))