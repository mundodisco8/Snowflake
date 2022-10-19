"""
This type stub file was generated by pyright.
"""

"""
Generic test utilities.

"""
__all__ = ['PytestTester', 'check_free_memory', '_TestPythranFunc']
class FPUModeChangeWarning(RuntimeWarning):
    """Warning about FPU mode change"""
    ...


class PytestTester:
    """
    Pytest test runner entry point.
    """
    def __init__(self, module_name) -> None:
        ...
    
    def __call__(self, label=..., verbose=..., extra_argv=..., doctests=..., coverage=..., tests=..., parallel=...): # -> bool:
        ...
    


class _TestPythranFunc:
    '''
    These are situations that can be tested in our pythran tests:
    - A function with multiple array arguments and then
      other positional and keyword arguments.
    - A function with array-like keywords (e.g. `def somefunc(x0, x1=None)`.
    Note: list/tuple input is not yet tested!

    `self.arguments`: A dictionary which key is the index of the argument,
                      value is tuple(array value, all supported dtypes)
    `self.partialfunc`: A function used to freeze some non-array argument
                        that of no interests in the original function
    '''
    ALL_INTEGER = ...
    ALL_FLOAT = ...
    ALL_COMPLEX = ...
    def setup_method(self): # -> None:
        ...
    
    def get_optional_args(self, func): # -> dict[Unknown, Unknown]:
        ...
    
    def get_max_dtype_list_length(self): # -> int:
        ...
    
    def get_dtype(self, dtype_list, dtype_idx):
        ...
    
    def test_all_dtypes(self): # -> None:
        ...
    
    def test_views(self): # -> None:
        ...
    
    def test_strided(self): # -> None:
        ...
    


def check_free_memory(free_mb): # -> None:
    """
    Check *free_mb* of memory is available, otherwise do pytest.skip
    """
    ...

