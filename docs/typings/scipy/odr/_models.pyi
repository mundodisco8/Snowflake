"""
This type stub file was generated by pyright.
"""

from scipy.odr._odrpack import Model

""" Collection of Model instances for use with the odrpack fitting package.
"""
__all__ = ['Model', 'exponential', 'multilinear', 'unilinear', 'quadratic', 'polynomial']
class _MultilinearModel(Model):
    r"""
    Arbitrary-dimensional linear model

    This model is defined by :math:`y=\beta_0 + \sum_{i=1}^m \beta_i x_i`

    Examples
    --------
    We can calculate orthogonal distance regression with an arbitrary
    dimensional linear model:

    >>> from scipy import odr
    >>> x = np.linspace(0.0, 5.0)
    >>> y = 10.0 + 5.0 * x
    >>> data = odr.Data(x, y)
    >>> odr_obj = odr.ODR(data, odr.multilinear)
    >>> output = odr_obj.run()
    >>> print(output.beta)
    [10.  5.]

    """
    def __init__(self) -> None:
        ...
    


multilinear = ...
def polynomial(order): # -> Model:
    """
    Factory function for a general polynomial model.

    Parameters
    ----------
    order : int or sequence
        If an integer, it becomes the order of the polynomial to fit. If
        a sequence of numbers, then these are the explicit powers in the
        polynomial.
        A constant term (power 0) is always included, so don't include 0.
        Thus, polynomial(n) is equivalent to polynomial(range(1, n+1)).

    Returns
    -------
    polynomial : Model instance
        Model instance.

    Examples
    --------
    We can fit an input data using orthogonal distance regression (ODR) with
    a polynomial model:

    >>> import matplotlib.pyplot as plt
    >>> from scipy import odr
    >>> x = np.linspace(0.0, 5.0)
    >>> y = np.sin(x)
    >>> poly_model = odr.polynomial(3)  # using third order polynomial model
    >>> data = odr.Data(x, y)
    >>> odr_obj = odr.ODR(data, poly_model)
    >>> output = odr_obj.run()  # running ODR fitting
    >>> poly = np.poly1d(output.beta[::-1])
    >>> poly_y = poly(x)
    >>> plt.plot(x, y, label="input data")
    >>> plt.plot(x, poly_y, label="polynomial ODR")
    >>> plt.legend()
    >>> plt.show()

    """
    ...

class _ExponentialModel(Model):
    r"""
    Exponential model

    This model is defined by :math:`y=\beta_0 + e^{\beta_1 x}`

    Examples
    --------
    We can calculate orthogonal distance regression with an exponential model:

    >>> from scipy import odr
    >>> x = np.linspace(0.0, 5.0)
    >>> y = -10.0 + np.exp(0.5*x)
    >>> data = odr.Data(x, y)
    >>> odr_obj = odr.ODR(data, odr.exponential)
    >>> output = odr_obj.run()
    >>> print(output.beta)
    [-10.    0.5]

    """
    def __init__(self) -> None:
        ...
    


exponential = ...
class _UnilinearModel(Model):
    r"""
    Univariate linear model

    This model is defined by :math:`y = \beta_0 x + \beta_1`

    Examples
    --------
    We can calculate orthogonal distance regression with an unilinear model:

    >>> from scipy import odr
    >>> x = np.linspace(0.0, 5.0)
    >>> y = 1.0 * x + 2.0
    >>> data = odr.Data(x, y)
    >>> odr_obj = odr.ODR(data, odr.unilinear)
    >>> output = odr_obj.run()
    >>> print(output.beta)
    [1. 2.]

    """
    def __init__(self) -> None:
        ...
    


unilinear = ...
class _QuadraticModel(Model):
    r"""
    Quadratic model

    This model is defined by :math:`y = \beta_0 x^2 + \beta_1 x + \beta_2`

    Examples
    --------
    We can calculate orthogonal distance regression with a quadratic model:

    >>> from scipy import odr
    >>> x = np.linspace(0.0, 5.0)
    >>> y = 1.0 * x ** 2 + 2.0 * x + 3.0
    >>> data = odr.Data(x, y)
    >>> odr_obj = odr.ODR(data, odr.quadratic)
    >>> output = odr_obj.run()
    >>> print(output.beta)
    [1. 2. 3.]

    """
    def __init__(self) -> None:
        ...
    


quadratic = ...