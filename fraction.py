from math import gcd

class Fraction:
    """A fraction with a numerator and denominator and arithmetic operations.

    Fractions are always stored in proper form, without common factors in 
    numerator and denominator, and denominator >= 0.
    Since Fractions are stored in proper form, each value has a
    unique representation, e.g. 4/5, 24/30, and -20/-25 have the same
    internal representation.
    """

    def __init__(self, numerator, denominator=1):
        """Initialize a new fraction with the given numerator
           and denominator (default 1).
        """
        # Check type and raise exception
        if isinstance(denominator, float) or not isinstance(denominator, int):
            raise TypeError
        if isinstance(numerator, float) or not isinstance(numerator, int):
            raise TypeError

        if denominator == 0:
            if numerator == 0:
                raise ValueError("The denominator and the numerator cannot be zero")
            else:
                if numerator > 0:
                    numerator = 1
                else:
                    numerator = -1
                denominator = 0
        else:
            if denominator < 0 and numerator < 0:
                denominator = abs(denominator)
                numerator = abs(numerator)
            elif denominator < 0 and numerator > 0:
                denominator = abs(denominator)
                numerator = -numerator

        # make fractions
        self.numerator = numerator // gcd(numerator, denominator)
        self.denominator = denominator // gcd(numerator, denominator)

    def __add__(self, frac):
        """Return the sum of two fractions as a new fraction.
           Use the standard formula  a/b + c/d = (ad+bc)/(b*d)
        """
        result_nume = ((self.numerator * frac.denominator) +
                       (self.denominator * frac.numerator))
        result_deno = (self.denominator * frac.denominator)
        return Fraction(result_nume, result_deno)

    def __mul__(self, frac):
        result_nume = self.numerator * frac.numerator
        result_deno = self.denominator * frac.denominator
        return Fraction(result_nume, result_deno)

    def __sub__(self, frac):
        result_nume = ((self.numerator * frac.denominator) -
                       (self.denominator * frac.numerator))
        result_deno = (self.denominator * frac.denominator)
        return Fraction(result_nume, result_deno)

    def __gt__(self, frac):
        check_self = self.numerator * frac.denominator
        check_other = self.denominator * frac.numerator
        return check_self > check_other

    def __neg__(self):
        return Fraction(-self.numerator, self.denominator)

    def __str__(self):
        if self.numerator % self.denominator == 0:
            return f"{int(self.numerator / self.denominator)}"
        return f"{int(self.numerator)}/{int(self.denominator)}"

    def __eq__(self, frac):
        """Two fractions are equal if they have the same value.
           Fractions are stored in proper form so the internal representation
           is unique (3/6 is same as 1/2).
        """
        return self.numerator == frac.numerator and self.denominator == frac.denominator
