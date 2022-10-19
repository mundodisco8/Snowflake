"""
This type stub file was generated by pyright.
"""

__all__ = ['LinAlgError', 'LinAlgWarning', 'norm']
class LinAlgWarning(RuntimeWarning):
    """
    The warning emitted when a linear algebra related operation is close
    to fail conditions of the algorithm or loss of accuracy is expected.
    """
    ...


def norm(a, ord=..., axis=..., keepdims=..., check_finite=...): # -> floating[Any]:
    """
    Matrix or vector norm.

    This function is able to return one of eight different matrix norms,
    or one of an infinite number of vector norms (described below), depending
    on the value of the ``ord`` parameter. For tensors with rank different from
    1 or 2, only `ord=None` is supported.

    Parameters
    ----------
    a : array_like
        Input array. If `axis` is None, `a` must be 1-D or 2-D, unless `ord`
        is None. If both `axis` and `ord` are None, the 2-norm of
        ``a.ravel`` will be returned.
    ord : {int, inf, -inf, 'fro', 'nuc', None}, optional
        Order of the norm (see table under ``Notes``). inf means NumPy's
        `inf` object.
    axis : {int, 2-tuple of ints, None}, optional
        If `axis` is an integer, it specifies the axis of `a` along which to
        compute the vector norms. If `axis` is a 2-tuple, it specifies the
        axes that hold 2-D matrices, and the matrix norms of these matrices
        are computed. If `axis` is None then either a vector norm (when `a`
        is 1-D) or a matrix norm (when `a` is 2-D) is returned.
    keepdims : bool, optional
        If this is set to True, the axes which are normed over are left in the
        result as dimensions with size one. With this option the result will
        broadcast correctly against the original `a`.
    check_finite : bool, optional
        Whether to check that the input matrix contains only finite numbers.
        Disabling may give a performance gain, but may result in problems
        (crashes, non-termination) if the inputs do contain infinities or NaNs.

    Returns
    -------
    n : float or ndarray
        Norm of the matrix or vector(s).

    Notes
    -----
    For values of ``ord <= 0``, the result is, strictly speaking, not a
    mathematical 'norm', but it may still be useful for various numerical
    purposes.

    The following norms can be calculated:

    =====  ============================  ==========================
    ord    norm for matrices             norm for vectors
    =====  ============================  ==========================
    None   Frobenius norm                2-norm
    'fro'  Frobenius norm                --
    'nuc'  nuclear norm                  --
    inf    max(sum(abs(a), axis=1))      max(abs(a))
    -inf   min(sum(abs(a), axis=1))      min(abs(a))
    0      --                            sum(a != 0)
    1      max(sum(abs(a), axis=0))      as below
    -1     min(sum(abs(a), axis=0))      as below
    2      2-norm (largest sing. value)  as below
    -2     smallest singular value       as below
    other  --                            sum(abs(a)**ord)**(1./ord)
    =====  ============================  ==========================

    The Frobenius norm is given by [1]_:

        :math:`||A||_F = [\\sum_{i,j} abs(a_{i,j})^2]^{1/2}`

    The nuclear norm is the sum of the singular values.

    Both the Frobenius and nuclear norm orders are only defined for
    matrices.

    References
    ----------
    .. [1] G. H. Golub and C. F. Van Loan, *Matrix Computations*,
           Baltimore, MD, Johns Hopkins University Press, 1985, pg. 15

    Examples
    --------
    >>> from scipy.linalg import norm
    >>> a = np.arange(9) - 4.0
    >>> a
    array([-4., -3., -2., -1.,  0.,  1.,  2.,  3.,  4.])
    >>> b = a.reshape((3, 3))
    >>> b
    array([[-4., -3., -2.],
           [-1.,  0.,  1.],
           [ 2.,  3.,  4.]])

    >>> norm(a)
    7.745966692414834
    >>> norm(b)
    7.745966692414834
    >>> norm(b, 'fro')
    7.745966692414834
    >>> norm(a, np.inf)
    4
    >>> norm(b, np.inf)
    9
    >>> norm(a, -np.inf)
    0
    >>> norm(b, -np.inf)
    2

    >>> norm(a, 1)
    20
    >>> norm(b, 1)
    7
    >>> norm(a, -1)
    -4.6566128774142013e-010
    >>> norm(b, -1)
    6
    >>> norm(a, 2)
    7.745966692414834
    >>> norm(b, 2)
    7.3484692283495345

    >>> norm(a, -2)
    0
    >>> norm(b, -2)
    1.8570331885190563e-016
    >>> norm(a, 3)
    5.8480354764257312
    >>> norm(a, -3)
    0

    """
    ...

