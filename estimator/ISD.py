from math import log, comb

class ISDCost:
    @staticmethod
    def lee_brickell(q, n, k, w, N_w=0, L=1):
        """
        Estimate the cost of the Lee-Brickell algorithm for ISD. [?:LIP-UPKE]

        Parameters:
        q (int): The size of the finite field.
        n (int): The length of the codeword.
        k (int): The dimension of the code.
        w (int): The weight of the codeword.
        L (int): The number of codewords to find.
        N_w (int): The cardinality of 
        
        Returns:
        cost (float): The estimated cost.
        """

        #Approximateed expected cardinality of A_w
        if N_w == 0:
            N_w = comb(n, w) * ((q-1) ** (w-2)) * (q ** (k-n+1))

        # Number of codewords of weight w
        N = (q-1)*N_w

        #Complexity for C_inf
        C_inf = (q * comb(n, w)) / comb(n-k,w-2)

        #Estimated complexity
        if L == N:
            cost = C_inf * log(N)
        else:
            cost = (L / N) * C_inf
        
        return cost

