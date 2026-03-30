"""
Formatting options for Numpy and Matplotlib. For the former, the print options
are edited to make output clearer in Jupyter notebook. For the latter, matplotlib
plots are formatted as I like it :)
"""

from functools import wraps

import matplotlib.pyplot as plt
import numpy as np
from matplotlib import rcParams
from matplotlib.ticker import NullLocator

rcparams = {
    "figure.figsize": (8, 8),
    "axes.grid": True,
    "axes.axisbelow": True,
    "axes.labelsize": "xx-large",
    # Linestyle
    "lines.linewidth": 2,
    # Ticks
    "xtick.labelsize": "x-large",
    "xtick.top": True,
    "xtick.labeltop": False,
    "xtick.bottom": True,
    "ytick.labelsize": "x-large",
    "ytick.right": True,
    "ytick.labelright": False,
    "ytick.left": True,
    # Histograms
    "hist.bins": 50,
}


def format_plots():
    """
    Formats matplotlib plots, just run `format_plots`. Because we are changing
    minor and major grid lines differently, we need to use a wrapper such that
    when the figure/subplot is called, the formatting is applied. For global
    changes, rcParams is used.
    """
    # Global parameters
    rcParams.update(rcparams)
    # Styling for the major tick grid
    major_grid = {"ls": "solid", "alpha": 0.7}
    # Styling for the minor tick grid
    minor_grid = {"ls": "dotted", "alpha": 1.0}

    # Preserve original functions to add wrappers to
    _original_figure = plt.figure
    _original_subplots = plt.subplots

    # Wrapper for `plt.figure`
    @wraps(_original_figure)
    def _styled_figure(*args, **kwargs):
        fig = _original_figure(*args, **kwargs)

        def _apply_grid():
            # Loop through axes to apply changes
            for ax in fig.axes:
                # Don't do anything if axis can't support a grid
                if hasattr(ax, "grid"):
                    # Only reset minor ticks if they aren't already formatted
                    x_is_null = isinstance(ax.xaxis.get_minor_locator(), NullLocator)
                    y_is_null = isinstance(ax.yaxis.get_minor_locator(), NullLocator)
                    if x_is_null or y_is_null:
                        ax.minorticks_on()
                    ax.grid(which="major", **major_grid)
                    ax.grid(which="minor", **minor_grid)

        # Apply grid change
        _apply_grid()
        fig.canvas.mpl_connect("draw_event", lambda evt: _apply_grid())
        return fig

    # Wrapper for `plt.subplots`
    @wraps(_original_subplots)
    def _styled_subplots(*args, **kwargs):
        fig, axes = _original_subplots(*args, **kwargs)

        # Turn `axes` into a flattened numpy array`
        all_axes = axes.flatten() if isinstance(axes, np.ndarray) else [axes]

        # Loop through all axes
        for ax in all_axes:
            if ax is not None:
                # Only reset minor ticks if they aren't already formatted
                x_is_null = isinstance(ax.xaxis.get_minor_locator(), NullLocator)
                y_is_null = isinstance(ax.yaxis.get_minor_locator(), NullLocator)
                if x_is_null or y_is_null:
                    ax.minorticks_on()
                ax.grid(which="major", **major_grid)
                ax.grid(which="minor", **minor_grid)

        return fig, axes

    # Apply the wrappers
    plt.figure = _styled_figure
    plt.subplots = _styled_subplots


def format_numpy(precision: int = 6, linewidth: int = 1000, sign: str = " "):
    """
    Sets numpy print options to chosen values. These are just values I have
    chosen that work well for me in Jupyter notebooks.
    """
    np.set_printoptions(precision=precision, linewidth=linewidth, sign=sign)
