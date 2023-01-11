"""
This type stub file was generated by pyright.
"""

"""Functions to construct sparse matrices
"""
__docformat__ = ...
__all__ = ['spdiags', 'eye', 'identity', 'kron', 'kronsum', 'hstack', 'vstack', 'bmat', 'rand', 'random', 'diags', 'block_diag']
def spdiags(data, diags, m=..., n=..., format=...): # -> dia_matrix | Any:
    """
    Return a sparse matrix from diagonals.

    Parameters
    ----------
    data : array_like
        Matrix diagonals stored row-wise
    diags : sequence of int or an int
        Diagonals to set:

        * k = 0  the main diagonal
        * k > 0  the kth upper diagonal
        * k < 0  the kth lower diagonal
    m, n : int, tuple, optional
        Shape of the result. If `n` is None and `m` is a given tuple,
        the shape is this tuple. If omitted, the matrix is square and
        its shape is len(data[0]).
    format : str, optional
        Format of the result. By default (format=None) an appropriate sparse
        matrix format is returned. This choice is subject to change.

    See Also
    --------
    diags : more convenient form of this function
    dia_matrix : the sparse DIAgonal format.

    Examples
    --------
    >>> from scipy.sparse import spdiags
    >>> data = np.array([[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]])
    >>> diags = np.array([0, -1, 2])
    >>> spdiags(data, diags, 4, 4).toarray()
    array([[1, 0, 3, 0],
           [1, 2, 0, 4],
           [0, 2, 3, 0],
           [0, 0, 3, 4]])

    """
    ...

def diags(diagonals, offsets=..., shape=..., format=..., dtype=...): # -> dia_matrix | Any:
    """
    Construct a sparse matrix from diagonals.

    Parameters
    ----------
    diagonals : sequence of array_like
        Sequence of arrays containing the matrix diagonals,
        corresponding to `offsets`.
    offsets : sequence of int or an int, optional
        Diagonals to set:
          - k = 0  the main diagonal (default)
          - k > 0  the kth upper diagonal
          - k < 0  the kth lower diagonal
    shape : tuple of int, optional
        Shape of the result. If omitted, a square matrix large enough
        to contain the diagonals is returned.
    format : {"dia", "csr", "csc", "lil", ...}, optional
        Matrix format of the result. By default (format=None) an
        appropriate sparse matrix format is returned. This choice is
        subject to change.
    dtype : dtype, optional
        Data type of the matrix.

    See Also
    --------
    spdiags : construct matrix from diagonals

    Notes
    -----
    This function differs from `spdiags` in the way it handles
    off-diagonals.

    The result from `diags` is the sparse equivalent of::

        np.diag(diagonals[0], offsets[0])
        + ...
        + np.diag(diagonals[k], offsets[k])

    Repeated diagonal offsets are disallowed.

    .. versionadded:: 0.11

    Examples
    --------
    >>> from scipy.sparse import diags
    >>> diagonals = [[1, 2, 3, 4], [1, 2, 3], [1, 2]]
    >>> diags(diagonals, [0, -1, 2]).toarray()
    array([[1, 0, 1, 0],
           [1, 2, 0, 2],
           [0, 2, 3, 0],
           [0, 0, 3, 4]])

    Broadcasting of scalars is supported (but shape needs to be
    specified):

    >>> diags([1, -2, 1], [-1, 0, 1], shape=(4, 4)).toarray()
    array([[-2.,  1.,  0.,  0.],
           [ 1., -2.,  1.,  0.],
           [ 0.,  1., -2.,  1.],
           [ 0.,  0.,  1., -2.]])


    If only one diagonal is wanted (as in `numpy.diag`), the following
    works as well:

    >>> diags([1, 2, 3], 1).toarray()
    array([[ 0.,  1.,  0.,  0.],
           [ 0.,  0.,  2.,  0.],
           [ 0.,  0.,  0.,  3.],
           [ 0.,  0.,  0.,  0.]])
    """
    ...

def identity(n, dtype=..., format=...): # -> csr_matrix | csc_matrix | coo_matrix | dia_matrix | Any:
    """Identity matrix in sparse format

    Returns an identity matrix with shape (n,n) using a given
    sparse format and dtype.

    Parameters
    ----------
    n : int
        Shape of the identity matrix.
    dtype : dtype, optional
        Data type of the matrix
    format : str, optional
        Sparse format of the result, e.g., format="csr", etc.

    Examples
    --------
    >>> from scipy.sparse import identity
    >>> identity(3).toarray()
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])
    >>> identity(3, dtype='int8', format='dia')
    <3x3 sparse matrix of type '<class 'numpy.int8'>'
            with 3 stored elements (1 diagonals) in DIAgonal format>

    """
    ...

def eye(m, n=..., k=..., dtype=..., format=...): # -> csr_matrix | csc_matrix | coo_matrix | dia_matrix | Any:
    """Sparse matrix with ones on diagonal

    Returns a sparse (m x n) matrix where the kth diagonal
    is all ones and everything else is zeros.

    Parameters
    ----------
    m : int
        Number of rows in the matrix.
    n : int, optional
        Number of columns. Default: `m`.
    k : int, optional
        Diagonal to place ones on. Default: 0 (main diagonal).
    dtype : dtype, optional
        Data type of the matrix.
    format : str, optional
        Sparse format of the result, e.g., format="csr", etc.

    Examples
    --------
    >>> from scipy import sparse
    >>> sparse.eye(3).toarray()
    array([[ 1.,  0.,  0.],
           [ 0.,  1.,  0.],
           [ 0.,  0.,  1.]])
    >>> sparse.eye(3, dtype=np.int8)
    <3x3 sparse matrix of type '<class 'numpy.int8'>'
        with 3 stored elements (1 diagonals) in DIAgonal format>

    """
    ...

def kron(A, B, format=...): # -> coo_matrix | Any | bsr_matrix:
    """kronecker product of sparse matrices A and B

    Parameters
    ----------
    A : sparse or dense matrix
        first matrix of the product
    B : sparse or dense matrix
        second matrix of the product
    format : str, optional
        format of the result (e.g. "csr")

    Returns
    -------
    kronecker product in a sparse matrix format


    Examples
    --------
    >>> from scipy import sparse
    >>> A = sparse.csr_matrix(np.array([[0, 2], [5, 0]]))
    >>> B = sparse.csr_matrix(np.array([[1, 2], [3, 4]]))
    >>> sparse.kron(A, B).toarray()
    array([[ 0,  0,  2,  4],
           [ 0,  0,  6,  8],
           [ 5, 10,  0,  0],
           [15, 20,  0,  0]])

    >>> sparse.kron(A, [[1, 2], [3, 4]]).toarray()
    array([[ 0,  0,  2,  4],
           [ 0,  0,  6,  8],
           [ 5, 10,  0,  0],
           [15, 20,  0,  0]])

    """
    ...

def kronsum(A, B, format=...): # -> coo_matrix | Any | bsr_matrix:
    """kronecker sum of sparse matrices A and B

    Kronecker sum of two sparse matrices is a sum of two Kronecker
    products kron(I_n,A) + kron(B,I_m) where A has shape (m,m)
    and B has shape (n,n) and I_m and I_n are identity matrices
    of shape (m,m) and (n,n), respectively.

    Parameters
    ----------
    A
        square matrix
    B
        square matrix
    format : str
        format of the result (e.g. "csr")

    Returns
    -------
    kronecker sum in a sparse matrix format

    Examples
    --------


    """
    ...

def hstack(blocks, format=..., dtype=...): # -> Self@_data_matrix | csr_matrix | csc_matrix | coo_matrix | Any:
    """
    Stack sparse matrices horizontally (column wise)

    Parameters
    ----------
    blocks
        sequence of sparse matrices with compatible shapes
    format : str
        sparse format of the result (e.g., "csr")
        by default an appropriate sparse matrix format is returned.
        This choice is subject to change.
    dtype : dtype, optional
        The data-type of the output matrix. If not given, the dtype is
        determined from that of `blocks`.

    See Also
    --------
    vstack : stack sparse matrices vertically (row wise)

    Examples
    --------
    >>> from scipy.sparse import coo_matrix, hstack
    >>> A = coo_matrix([[1, 2], [3, 4]])
    >>> B = coo_matrix([[5], [6]])
    >>> hstack([A,B]).toarray()
    array([[1, 2, 5],
           [3, 4, 6]])

    """
    ...

def vstack(blocks, format=..., dtype=...): # -> Self@_data_matrix | csr_matrix | csc_matrix | coo_matrix | Any:
    """
    Stack sparse matrices vertically (row wise)

    Parameters
    ----------
    blocks
        sequence of sparse matrices with compatible shapes
    format : str, optional
        sparse format of the result (e.g., "csr")
        by default an appropriate sparse matrix format is returned.
        This choice is subject to change.
    dtype : dtype, optional
        The data-type of the output matrix. If not given, the dtype is
        determined from that of `blocks`.

    See Also
    --------
    hstack : stack sparse matrices horizontally (column wise)

    Examples
    --------
    >>> from scipy.sparse import coo_matrix, vstack
    >>> A = coo_matrix([[1, 2], [3, 4]])
    >>> B = coo_matrix([[5, 6]])
    >>> vstack([A, B]).toarray()
    array([[1, 2],
           [3, 4],
           [5, 6]])

    """
    ...

def bmat(blocks, format=..., dtype=...): # -> Self@_data_matrix | csr_matrix | csc_matrix | coo_matrix | Any:
    """
    Build a sparse matrix from sparse sub-blocks

    Parameters
    ----------
    blocks : array_like
        Grid of sparse matrices with compatible shapes.
        An entry of None implies an all-zero matrix.
    format : {'bsr', 'coo', 'csc', 'csr', 'dia', 'dok', 'lil'}, optional
        The sparse format of the result (e.g. "csr"). By default an
        appropriate sparse matrix format is returned.
        This choice is subject to change.
    dtype : dtype, optional
        The data-type of the output matrix. If not given, the dtype is
        determined from that of `blocks`.

    Returns
    -------
    bmat : sparse matrix

    See Also
    --------
    block_diag, diags

    Examples
    --------
    >>> from scipy.sparse import coo_matrix, bmat
    >>> A = coo_matrix([[1, 2], [3, 4]])
    >>> B = coo_matrix([[5], [6]])
    >>> C = coo_matrix([[7]])
    >>> bmat([[A, B], [None, C]]).toarray()
    array([[1, 2, 5],
           [3, 4, 6],
           [0, 0, 7]])

    >>> bmat([[A, None], [None, C]]).toarray()
    array([[1, 2, 0],
           [3, 4, 0],
           [0, 0, 7]])

    """
    ...

def block_diag(mats, format=..., dtype=...): # -> coo_matrix | Any:
    """
    Build a block diagonal sparse matrix from provided matrices.

    Parameters
    ----------
    mats : sequence of matrices
        Input matrices.
    format : str, optional
        The sparse format of the result (e.g., "csr"). If not given, the matrix
        is returned in "coo" format.
    dtype : dtype specifier, optional
        The data-type of the output matrix. If not given, the dtype is
        determined from that of `blocks`.

    Returns
    -------
    res : sparse matrix

    Notes
    -----

    .. versionadded:: 0.11.0

    See Also
    --------
    bmat, diags

    Examples
    --------
    >>> from scipy.sparse import coo_matrix, block_diag
    >>> A = coo_matrix([[1, 2], [3, 4]])
    >>> B = coo_matrix([[5], [6]])
    >>> C = coo_matrix([[7]])
    >>> block_diag((A, B, C)).toarray()
    array([[1, 2, 0, 0],
           [3, 4, 0, 0],
           [0, 0, 5, 0],
           [0, 0, 6, 0],
           [0, 0, 0, 7]])

    """
    ...

def random(m, n, density=..., format=..., dtype=..., random_state=..., data_rvs=...): # -> coo_matrix | Any:
    """Generate a sparse matrix of the given shape and density with randomly
    distributed values.

    Parameters
    ----------
    m, n : int
        shape of the matrix
    density : real, optional
        density of the generated matrix: density equal to one means a full
        matrix, density of 0 means a matrix with no non-zero items.
    format : str, optional
        sparse matrix format.
    dtype : dtype, optional
        type of the returned matrix values.
    random_state : {None, int, `numpy.random.Generator`,
                    `numpy.random.RandomState`}, optional

        If `seed` is None (or `np.random`), the `numpy.random.RandomState`
        singleton is used.
        If `seed` is an int, a new ``RandomState`` instance is used,
        seeded with `seed`.
        If `seed` is already a ``Generator`` or ``RandomState`` instance then
        that instance is used.
        This random state will be used
        for sampling the sparsity structure, but not necessarily for sampling
        the values of the structurally nonzero entries of the matrix.
    data_rvs : callable, optional
        Samples a requested number of random values.
        This function should take a single argument specifying the length
        of the ndarray that it will return. The structurally nonzero entries
        of the sparse random matrix will be taken from the array sampled
        by this function. By default, uniform [0, 1) random values will be
        sampled using the same random state as is used for sampling
        the sparsity structure.

    Returns
    -------
    res : sparse matrix

    Notes
    -----
    Only float types are supported for now.

    Examples
    --------
    >>> from scipy.sparse import random
    >>> from scipy import stats
    >>> from numpy.random import default_rng
    >>> rng = default_rng()
    >>> rvs = stats.poisson(25, loc=10).rvs
    >>> S = random(3, 4, density=0.25, random_state=rng, data_rvs=rvs)
    >>> S.A
    array([[ 36.,   0.,  33.,   0.],   # random
           [  0.,   0.,   0.,   0.],
           [  0.,   0.,  36.,   0.]])

    >>> from scipy.sparse import random
    >>> from scipy.stats import rv_continuous
    >>> class CustomDistribution(rv_continuous):
    ...     def _rvs(self,  size=None, random_state=None):
    ...         return random_state.standard_normal(size)
    >>> X = CustomDistribution(seed=rng)
    >>> Y = X()  # get a frozen version of the distribution
    >>> S = random(3, 4, density=0.25, random_state=rng, data_rvs=Y.rvs)
    >>> S.A
    array([[ 0.        ,  0.        ,  0.        ,  0.        ],   # random
           [ 0.13569738,  1.9467163 , -0.81205367,  0.        ],
           [ 0.        ,  0.        ,  0.        ,  0.        ]])

    """
    ...

def rand(m, n, density=..., format=..., dtype=..., random_state=...): # -> coo_matrix | Any:
    """Generate a sparse matrix of the given shape and density with uniformly
    distributed values.

    Parameters
    ----------
    m, n : int
        shape of the matrix
    density : real, optional
        density of the generated matrix: density equal to one means a full
        matrix, density of 0 means a matrix with no non-zero items.
    format : str, optional
        sparse matrix format.
    dtype : dtype, optional
        type of the returned matrix values.
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
    res : sparse matrix

    Notes
    -----
    Only float types are supported for now.

    See Also
    --------
    scipy.sparse.random : Similar function that allows a user-specified random
        data source.

    Examples
    --------
    >>> from scipy.sparse import rand
    >>> matrix = rand(3, 4, density=0.25, format="csr", random_state=42)
    >>> matrix
    <3x4 sparse matrix of type '<class 'numpy.float64'>'
       with 3 stored elements in Compressed Sparse Row format>
    >>> matrix.toarray()
    array([[0.05641158, 0.        , 0.        , 0.65088847],
           [0.        , 0.        , 0.        , 0.14286682],
           [0.        , 0.        , 0.        , 0.        ]])

    """
    ...
