"""
This type stub file was generated by pyright.
"""

def check_arguments(fun, y0, support_complex): # -> tuple[(t: Unknown, y: Unknown) -> NDArray[Any], NDArray[Any]]:
    """Helper function for checking arguments common to all solvers."""
    ...

class OdeSolver:
    """Base class for ODE solvers.

    In order to implement a new solver you need to follow the guidelines:

        1. A constructor must accept parameters presented in the base class
           (listed below) along with any other parameters specific to a solver.
        2. A constructor must accept arbitrary extraneous arguments
           ``**extraneous``, but warn that these arguments are irrelevant
           using `common.warn_extraneous` function. Do not pass these
           arguments to the base class.
        3. A solver must implement a private method `_step_impl(self)` which
           propagates a solver one step further. It must return tuple
           ``(success, message)``, where ``success`` is a boolean indicating
           whether a step was successful, and ``message`` is a string
           containing description of a failure if a step failed or None
           otherwise.
        4. A solver must implement a private method `_dense_output_impl(self)`,
           which returns a `DenseOutput` object covering the last successful
           step.
        5. A solver must have attributes listed below in Attributes section.
           Note that ``t_old`` and ``step_size`` are updated automatically.
        6. Use `fun(self, t, y)` method for the system rhs evaluation, this
           way the number of function evaluations (`nfev`) will be tracked
           automatically.
        7. For convenience, a base class provides `fun_single(self, t, y)` and
           `fun_vectorized(self, t, y)` for evaluating the rhs in
           non-vectorized and vectorized fashions respectively (regardless of
           how `fun` from the constructor is implemented). These calls don't
           increment `nfev`.
        8. If a solver uses a Jacobian matrix and LU decompositions, it should
           track the number of Jacobian evaluations (`njev`) and the number of
           LU decompositions (`nlu`).
        9. By convention, the function evaluations used to compute a finite
           difference approximation of the Jacobian should not be counted in
           `nfev`, thus use `fun_single(self, t, y)` or
           `fun_vectorized(self, t, y)` when computing a finite difference
           approximation of the Jacobian.

    Parameters
    ----------
    fun : callable
        Right-hand side of the system. The calling signature is ``fun(t, y)``.
        Here ``t`` is a scalar and there are two options for ndarray ``y``.
        It can either have shape (n,), then ``fun`` must return array_like with
        shape (n,). Or, alternatively, it can have shape (n, n_points), then
        ``fun`` must return array_like with shape (n, n_points) (each column
        corresponds to a single column in ``y``). The choice between the two
        options is determined by `vectorized` argument (see below).
    t0 : float
        Initial time.
    y0 : array_like, shape (n,)
        Initial state.
    t_bound : float
        Boundary time --- the integration won't continue beyond it. It also
        determines the direction of the integration.
    vectorized : bool
        Whether `fun` is implemented in a vectorized fashion.
    support_complex : bool, optional
        Whether integration in a complex domain should be supported.
        Generally determined by a derived solver class capabilities.
        Default is False.

    Attributes
    ----------
    n : int
        Number of equations.
    status : string
        Current status of the solver: 'running', 'finished' or 'failed'.
    t_bound : float
        Boundary time.
    direction : float
        Integration direction: +1 or -1.
    t : float
        Current time.
    y : ndarray
        Current state.
    t_old : float
        Previous time. None if no steps were made yet.
    step_size : float
        Size of the last successful step. None if no steps were made yet.
    nfev : int
        Number of the system's rhs evaluations.
    njev : int
        Number of the Jacobian evaluations.
    nlu : int
        Number of LU decompositions.
    """
    TOO_SMALL_STEP = ...
    def __init__(self, fun, t0, y0, t_bound, vectorized, support_complex=...) -> None:
        ...
    
    @property
    def step_size(self): # -> Any | None:
        ...
    
    def step(self): # -> None:
        """Perform one integration step.

        Returns
        -------
        message : string or None
            Report from the solver. Typically a reason for a failure if
            `self.status` is 'failed' after the step was taken or None
            otherwise.
        """
        ...
    
    def dense_output(self): # -> ConstantDenseOutput:
        """Compute a local interpolant over the last successful step.

        Returns
        -------
        sol : `DenseOutput`
            Local interpolant over the last successful step.
        """
        ...
    


class DenseOutput:
    """Base class for local interpolant over step made by an ODE solver.

    It interpolates between `t_min` and `t_max` (see Attributes below).
    Evaluation outside this interval is not forbidden, but the accuracy is not
    guaranteed.

    Attributes
    ----------
    t_min, t_max : float
        Time range of the interpolation.
    """
    def __init__(self, t_old, t) -> None:
        ...
    
    def __call__(self, t):
        """Evaluate the interpolant.

        Parameters
        ----------
        t : float or array_like with shape (n_points,)
            Points to evaluate the solution at.

        Returns
        -------
        y : ndarray, shape (n,) or (n, n_points)
            Computed values. Shape depends on whether `t` was a scalar or a
            1-D array.
        """
        ...
    


class ConstantDenseOutput(DenseOutput):
    """Constant value interpolator.

    This class used for degenerate integration cases: equal integration limits
    or a system with 0 equations.
    """
    def __init__(self, t_old, t, value) -> None:
        ...
    


