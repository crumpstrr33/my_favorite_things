from importlib.metadata import version

from .colors import fader, multifader
from .ddicts import format_ddict, nested_ddict
from .plot import bar_count, cumulative_bins, histbar, log_bins
from .save import save

__all__ = [
    "save",
    "nested_ddict",
    "format_ddict",
    "cumulative_bins",
    "log_bins",
    "bar_count",
    "histbar",
    "fader",
    "multifader",
]
__version__ = version("my-favorite-things")
