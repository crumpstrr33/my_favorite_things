from importlib.metadata import version

from .colors import fader, multifader
from .ddicts import format_ddict, nested_ddict, pprint_nested_dict
from .equations import cubic_equation
from .plot import bar_count, cumulative_bins, histbar, log_bins
from .save import save

__all__ = [
    "bar_count",
    "cubic_equation",
    "cumulative_bins",
    "fader",
    "format_ddict",
    "histbar",
    "log_bins",
    "multifader",
    "nested_ddict",
    "pprint_nested_dict",
    "save",
]
__version__ = version("my-favorite-things")
