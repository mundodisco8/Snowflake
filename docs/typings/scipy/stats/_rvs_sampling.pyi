"""
This type stub file was generated by pyright.
"""

from scipy._lib.deprecation import _deprecated

def rvs_ratio_uniforms(pdf, umax, vmin, vmax, size=..., c=..., random_state=...): # -> NDArray[float64]:
    """
    Generate random samples from a probability density function using the
    ratio-of-uniforms method.

    Parameters
    ----------
    pdf : callable
        A function with signature `pdf(x)` that is proportional to the
        probability density function of the distribution.
    umax : float
        The upper bound of the bounding rectangle in the u-direction.
    vmin : float
        The lower bound of the bounding rectangle in the v-direction.
    vmax : float
        The upper bound of the bounding rectangle in the v-direction.
    size : int or tuple of ints, optional
        Defining number of random variates (default is 1).
    c : float, optional.
        Shift parameter of ratio-of-uniforms method, see Notes. Default is 0.
    random_state : {None, int, `numpy.random.Generator`,
                    `numpy.random.RandomState`}, optional

        If `seed` is None (or `np.random`), the `numpy.random.RandomState`
        singleton is used.
        If `seed` is an int, a new ``RandomState`` instance is used,
        seeded with `seed`.
        If `seed` is already a ``Generator`` or ``RandomState`` instance then
        that instance is used.

    Returns
    -------
    rvs : ndarray
        The random variates distributed according to the probability
        distribution defined by the pdf.

    Notes
    -----
    Given a univariate probability density function `pdf` and a constant `c`,
    define the set ``A = {(u, v) : 0 < u <= sqrt(pdf(v/u + c))}``.
    If `(U, V)` is a random vector uniformly distributed over `A`,
    then `V/U + c` follows a distribution according to `pdf`.

    The above result (see [1]_, [2]_) can be used to sample random variables
    using only the pdf, i.e. no inversion of the cdf is required. Typical
    choices of `c` are zero or the mode of `pdf`. The set `A` is a subset of
    the rectangle ``R = [0, umax] x [vmin, vmax]`` where

    - ``umax = sup sqrt(pdf(x))``
    - ``vmin = inf (x - c) sqrt(pdf(x))``
    - ``vmax = sup (x - c) sqrt(pdf(x))``

    In particular, these values are finite if `pdf` is bounded and
    ``x**2 * pdf(x)`` is bounded (i.e. subquadratic tails).
    One can generate `(U, V)` uniformly on `R` and return
    `V/U + c` if `(U, V)` are also in `A` which can be directly
    verified.

    The algorithm is not changed if one replaces `pdf` by k * `pdf` for any
    constant k > 0. Thus, it is often convenient to work with a function
    that is proportional to the probability density function by dropping
    unneccessary normalization factors.

    Intuitively, the method works well if `A` fills up most of the
    enclosing rectangle such that the probability is high that `(U, V)`
    lies in `A` whenever it lies in `R` as the number of required
    iterations becomes too large otherwise. To be more precise, note that
    the expected number of iterations to draw `(U, V)` uniformly
    distributed on `R` such that `(U, V)` is also in `A` is given by
    the ratio ``area(R) / area(A) = 2 * umax * (vmax - vmin) / area(pdf)``,
    where `area(pdf)` is the integral of `pdf` (which is equal to one if the
    probability density function is used but can take on other values if a
    function proportional to the density is used). The equality holds since
    the area of `A` is equal to 0.5 * area(pdf) (Theorem 7.1 in [1]_).
    If the sampling fails to generate a single random variate after 50000
    iterations (i.e. not a single draw is in `A`), an exception is raised.

    If the bounding rectangle is not correctly specified (i.e. if it does not
    contain `A`), the algorithm samples from a distribution different from
    the one given by `pdf`. It is therefore recommended to perform a
    test such as `~scipy.stats.kstest` as a check.

    References
    ----------
    .. [1] L. Devroye, "Non-Uniform Random Variate Generation",
       Springer-Verlag, 1986.

    .. [2] W. Hoermann and J. Leydold, "Generating generalized inverse Gaussian
       random variates", Statistics and Computing, 24(4), p. 547--557, 2014.

    .. [3] A.J. Kinderman and J.F. Monahan, "Computer Generation of Random
       Variables Using the Ratio of Uniform Deviates",
       ACM Transactions on Mathematical Software, 3(3), p. 257--260, 1977.

    Examples
    --------
    >>> from scipy import stats
    >>> rng = np.random.default_rng()

    Simulate normally distributed random variables. It is easy to compute the
    bounding rectangle explicitly in that case. For simplicity, we drop the
    normalization factor of the density.

    >>> f = lambda x: np.exp(-x**2 / 2)
    >>> v_bound = np.sqrt(f(np.sqrt(2))) * np.sqrt(2)
    >>> umax, vmin, vmax = np.sqrt(f(0)), -v_bound, v_bound
    >>> rvs = stats.rvs_ratio_uniforms(f, umax, vmin, vmax, size=2500,
    ...                                random_state=rng)

    The K-S test confirms that the random variates are indeed normally
    distributed (normality is not rejected at 5% significance level):

    >>> stats.kstest(rvs, 'norm')[1]
    0.250634764150542

    The exponential distribution provides another example where the bounding
    rectangle can be determined explicitly.

    >>> rvs = stats.rvs_ratio_uniforms(lambda x: np.exp(-x), umax=1,
    ...                                vmin=0, vmax=2*np.exp(-1), size=1000,
    ...                                random_state=rng)
    >>> stats.kstest(rvs, 'expon')[1]
    0.21121052054580314

    """
    ...

class NumericalInverseHermite:
    @_deprecated("NumericalInverseHermite has been deprecated from `scipy.stats` " "and will be removed in SciPy 1.10.0. " " To use `NumericalInverseHermite`, import/use it from " "`scipy.stats.sampling` module instead. " "i.e. `from scipy.stats.sampling import NumericalInverseHermite`")
    def __init__(self, *args, **kwargs) -> None:
        ...
    
    def rvs(self, *args, **kwargs): # -> float | int:
        ...
    
    def ppf(self, *args, **kwargs): # -> float:
        ...
    
    def qrvs(self, *args, **kwargs): # -> ArrayLike:
        ...
    


