"""
Fast and straightforward implementation of specific formulas
"""
from cmath import exp as cexp
from math import pi

from numba import njit, types


@njit
def cubic_equation(a: float, b: float, c: float, d: float) -> list[complex]:
    """
    Solves the cubic equation:

        ax^3 + bx^2 + cx + d = 0

    Following the formula found here:
        https://en.wikipedia.org/wiki/Cubic_equation#General_cubic_formula
    Of the solutions, either all three are real or only one is.

    Returns (
        list of the 3 solutions
    )
    """
    # Numba casts floats as numpy.float64's. One can do e.g. (-3)^(1/2) with python
    # floats but not with numpy floats. So explicitly cast as complex types.
    a = types.complex128(a)
    b = types.complex128(b)
    c = types.complex128(c)
    d = types.complex128(d)

    # Intermediates
    Delta0 = b**2 - 3 * a * c
    Delta1 = 2 * b**3 - 9 * a * b * c + 27 * a**2 * d
    D = (Delta1**2 - 4 * Delta0**3) ** (1 / 2)

    # Normally, + or - doesn't matter because D is made via a square root. But if one
    # sign causes C=0, then we must go with the other. So we check here.
    sign = -1
    if abs(Delta1 - D) < 1e-3:
        sign = +1
    C = ((Delta1 + sign * D) / 2) ** (1 / 3)

    xi = cexp(2j * pi / 3)
    x = []
    for k in [0, 1, 2]:
        phase = xi**k

        xk = -(b + phase * C + Delta0 / (phase * C)) / (3 * a)
        x.append(xk)

    return x
