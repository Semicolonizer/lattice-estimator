from sage.all import log, binomial

class ISDCost:
    @staticmethod
    def lee_brickell(q, n, k, w, N_w=0, L=1):
        """
        Estimate the cost of the Lee-Brickell algorithm for ISD. [?:LIP-UPKE]

        Parameters:
        q (int): The size of the finite field.
        n (int): The length of the codeword.
        k (int): The dimension of the code.
        w (int): The target weight of the codewords.
        N_w (int): The estimated cardinality of set of codewords of weight w, up to scalar multiplication.
        L (int): The number of codewords to find.
        
        
        Returns:
        cost (float): The estimated cost of finding L codewords with weight w.
        """

        #Approximateed expected cardinality of A_w
        if N_w == 0:
            N_w = binomial(n, w) * ((q-1) ** (w-2)) * (q ** (k-n+1))

        # Number of possible codewords of weight w
        N = (q-1)*N_w

        #Complexity for C_inf
        C_inf = (q * binomial(n, w)) / binomial(n-k,w-2)

        #Estimated complexity
        if L == N:
            cost = C_inf * log(N)
        else:
            cost = (L / N) * C_inf
        
        return cost

