from math import log, comb

class ISDCost:
    @staticmethod
    def lee_brickell(q, n, k, w, L=1):
        """
        Estimate the cost of the Lee-Brickell algorithm for ISD. [?:LIP-UPKE]

        Parameters:
        q (int): The size of the finite field.
        n (int): The length of the codeword.
        k (int): The dimension of the code.
        w (int): The weight of the codeword.
        L (int): The number of codewords to find.
        
        Returns:
        cost (float): The estimated cost.
        """

        #Approximateed expected cardinality of A_w
        N_w = comb(n, w) * ((q-1) ** (w-2) * q ** (k-n+1))

        #Complexity for C_inf
        C_inf = (q * comb(n, w)) / comb(n-k,w-2)

        #Estimated complexity
        if L == N_w:
            cost = C_inf * log(N_w)
        else:
            cost = (L / N_w) * C_inf
        
        return log(cost,2)

