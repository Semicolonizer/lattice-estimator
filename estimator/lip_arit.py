from .lip_parameters import LIPParameters
from .cost import Cost
from sage.all import oo, is_prime


class ArithmeticInvariants():
    """
    Estimate cost of using arithmetic invariants.
    """

    def discriminant(form):
        """
        Compute the discriminant of the quadratic form.
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        
        Returns:
        Integer: The discriminant of the quadratic form.
        """
        return form.discriminant()

    def rank(form):
        """
        Compute the rank (dimension) of the quadratic form.
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        
        Returns:
        Integer: The rank of the quadratic form.
        """
        return form.dimension()

    def gcd_invariant(form):
        """
        Compute the gcd invariant of the quadratic form (gcd of the diagonal elements).
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        
        Returns:
        Integer: The gcd invariant of the quadratic form.
        """
        matrix = form.matrix()
        diagonal_elements = [matrix[i, i] for i in range(matrix.nrows())]
        return gcd(diagonal_elements)

    def parity(form):
        """
        Compute the parity of the quadratic form.
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        
        Returns:
        Integer: 1 if the form is odd, 0 if the form is even.
        """
        matrix = form.matrix()
        diagonal_elements = [matrix[i, i] for i in range(matrix.nrows())]
        gcd_val = gcd(diagonal_elements)
        even_parity = all(d % 2 == 0 for d in diagonal_elements)
        return 0 if even_parity else 1

    def signature(form):
        """
        Compute the signature of the quadratic form.
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        
        Returns:
        tuple: (number of positive squares, number of negative squares)
        """
        return form.signature()

    def hasse_invariant(form, p):
        """
        Compute the Hasse invariant of the quadratic form at a prime p.
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        p (int): A prime number.
        
        Returns:
        Integer: The Hasse invariant at prime p, using the Hilbert symbol.
        """
        D = form.matrix().diagonal()
        hasse_symbol = 1
        for i in range(len(D)):
            for j in range(i + 1, len(D)):
                hasse_symbol *= kronecker_symbol(D[i], D[j], p)
        return hasse_symbol

    def spinor_norm(form):
        """
        Compute the spinor norm of the quadratic form.
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        
        Returns:
        Integer or element in the appropriate ring, representing the spinor norm.
        """
        # SageMath does not seem to have direct support for spinor norms in its QuadraticForm class.
        # Placeholder, as calculating spinor norm explicitly may require advanced symbolic computations.
        raise NotImplementedError("Spinor norm computation not yet implemented.")

    def witt_invariant(form):
        """
        Compute the Witt invariant of the quadratic form (Witt index).
        
        Parameters:
        form (QuadraticForm): A quadratic form in SageMath.
        
        Returns:
        Integer: The Witt index of the quadratic form.
        """
        return form.witt_invariant()


    def __call__(
        self,
        params: LIPParameters,
        log_level=1,
        **kwds,
    ):
        """
        Estimate cost of using arithmetic invariants.

        :param params: LIP parameters.
        :return: A cost dictionary.

        The returned cost dictionary has the following entries:

        - ``rop``: Total number of word operations (≈ CPU cycles).
        - ``d``: Lattice dimension.

        EXAMPLES:
        # TODO: list examples

        """


        invariants = {
        "discriminant": discriminant(form),
        "rank": rank(form),
        "gcd_invariant": gcd_invariant(form),
        "parity": parity(form),
        "signature": signature(form),
        "witt_invariant": witt_invariant(form)
        }
        
        # Hasse invariants for specified primes (if provided)
        if primes is not None:
            invariants["hasse_invariants"] = {p: hasse_invariant(form, p) for p in primes}
        
        # Add spinor norm
        try:
            invariants["spinor_norm"] = spinor_norm(form)
        except NotImplementedError:
            invariants["spinor_norm"] = "Spinor norm not implemented"

        cost = Cost()
        # Return invariant list for comparison, or compare here_
        cost["tag"] = "arithmetic invariant"
        cost["problem"] = params
        
        return cost.sanity_check()

aritinv = ArithmeticInvariants()