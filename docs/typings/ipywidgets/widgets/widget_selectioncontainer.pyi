"""
This type stub file was generated by pyright.
"""

from .widget_box import Box
from .widget import register
from .widget_core import CoreWidget

"""SelectionContainer class.

Represents a multipage container that can be used to group other widgets into
pages.
"""
def pad(iterable, padding=..., length=...): # -> islice[Unknown | None]:
    """Returns the sequence elements and then returns None up to the given size (or indefinitely if size is None)."""
    ...

class _SelectionContainer(Box, CoreWidget):
    """Base class used to display multiple child widgets."""
    titles = ...
    selected_index = ...
    def set_title(self, index, title): # -> None:
        """Sets the title of a container page.
        Parameters
        ----------
        index : int
            Index of the container page
        title : unicode
            New title
        """
        ...
    
    def get_title(self, index): # -> Any:
        """Gets the title of a container page.
        Parameters
        ----------
        index : int
            Index of the container page
        """
        ...
    


@register
class Accordion(_SelectionContainer):
    """Displays children each on a separate accordion page."""
    _view_name = ...
    _model_name = ...


@register
class Tab(_SelectionContainer):
    """Displays children each on a separate accordion tab."""
    _view_name = ...
    _model_name = ...
    def __init__(self, children=..., **kwargs) -> None:
        ...
    


@register
class Stack(_SelectionContainer):
    """Displays only the selected child."""
    _view_name = ...
    _model_name = ...


