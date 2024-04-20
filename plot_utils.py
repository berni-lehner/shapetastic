import numpy as np
from pathlib import Path

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

from typing import Callable, Any

def create_canvas(width_pixels: int,
    height_pixels: int,
    background_color: str ='white',
    dpi: int=100) -> tuple:
    """
    Creates a blank canvas for plotting.

    Args:
        width_pixels (int): Width of the canvas in pixels.
        height_pixels (int): Height of the canvas in pixels.
        background_color (str, optional): Background color of the canvas. Defaults to 'white'.
        dpi (int, optional): Dots per inch (resolution) of the canvas. Defaults to 100.

    Returns:
        tuple: A tuple containing the matplotlib figure and axis objects.
    """
    # Calculate the dimensions of the plot in inches
    width_inches = width_pixels/dpi
    height_inches = height_pixels/dpi

    fig, ax = plt.subplots(figsize=(width_inches, height_inches), dpi=dpi)

    # Set figure background color
    fig.patch.set_facecolor(background_color)
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.axis('off')

    # Adjust the subplot parameters to prevent clipping of the saved plot
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1, wspace=0, hspace=0)

    return fig, ax


def save_canvas(fig: plt.Figure,
    file_name: str,
    pad_inches: float=0,
    dpi: int=100) -> None:
    """
    Saves the canvas to a file.

    Args:
        fig (matplotlib.figure.Figure): The matplotlib figure object to save.
        file_name (str): The name of the file to save the figure to.
        pad_inches (float, optional): Padding around the saved figure, in inches. Defaults to 0.
        dpi (int, optional): Dots per inch (resolution) of the saved figure. Defaults to 100.
    """
    # Create parent folder if necessary
    resultpath = Path(file_name).parent
    if not resultpath.exists():
        resultpath.mkdir(parents=True)

    fig.savefig(file_name, bbox_inches='tight', pad_inches=pad_inches, dpi=dpi)


def create_sample(
    canvas_width_px: int,
    canvas_height_px: int,
    background_color: str = 'white',
    dpi: int = 100,
    file_name: str | None = None,
    plot_function: Callable[[Any], None] | None = None,
    **plot_kwargs: Any) -> None:
    """
    Creates a pixel accurate sample plotted with a given function and saves it to a file.

    Args:
        canvas_width_px: The width of the canvas in pixels.
        canvas_height_px: The height of the canvas in pixels.
        background_color: The background color of the canvas. Defaults to 'white'.
        dpi: The resolution of the canvas in dots per inch. Defaults to 100.
        file_name: The file name to save the plot to. If None, the plot will not be saved.
        plot_function: The function to plot. Must take a dictionary of keyword arguments.
        **plot_kwargs: Additional keyword arguments to pass to the plot function.

    Raises:
        ValueError: If plot_function is None.
    """
    if plot_function is None:
        raise ValueError(f"Invalid value for plot_function: {plot_function}")

    fig, ax = create_canvas(
        width_pixels=canvas_width_px,
        height_pixels=canvas_height_px,
        background_color=background_color,
        dpi=dpi
    )
    # Add ax to key word args list
    plot_kwargs['ax'] = ax

    plot_function(**plot_kwargs)

    if file_name is not None:
        save_canvas(fig, file_name)
