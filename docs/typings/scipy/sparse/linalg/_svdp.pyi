"""
This type stub file was generated by pyright.
"""

"""
Python wrapper for PROPACK
--------------------------

PROPACK is a collection of Fortran routines for iterative computation
of partial SVDs of large matrices or linear operators.

Based on BSD licensed pypropack project:
  http://github.com/jakevdp/pypropack
  Author: Jake Vanderplas <vanderplas@astro.washington.edu>

PROPACK source is BSD licensed, and available at
  http://soi.stanford.edu/~rmunk/PROPACK/
"""
__all__ = ['_svdp']
_lansvd_dict = ...
_lansvd_irl_dict = ...
_which_converter = ...
class _AProd:
    """
    Wrapper class for linear operator

    The call signature of the __call__ method matches the callback of
    the PROPACK routines.
    """
    def __init__(self, A) -> None:
        ...
    
    def __call__(self, transa, m, n, x, y, sparm, iparm): # -> None:
        ...
    
    @property
    def shape(self): # -> tuple[Unknown, ...]:
        ...
    
    @property
    def dtype(self): # -> dtype[Unknown]:
        ...
    


