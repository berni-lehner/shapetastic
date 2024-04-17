import numpy as np

import matplotlib.pyplot as plt
import matplotlib.colors as mcolors

def create_canvas(width_pixels: int, height_pixels: int, background_color: str ='white', dpi: int=100) -> tuple:
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



def save_canvas(fig: plt.Figure, file_name: str, pad_inches: float=0, dpi: int=100) -> None:
    """
    Saves the canvas to a file.

    Args:
        fig (matplotlib.figure.Figure): The matplotlib figure object to save.
        file_name (str): The name of the file to save the figure to.
        pad_inches (float, optional): Padding around the saved figure, in inches. Defaults to 0.
        dpi (int, optional): Dots per inch (resolution) of the saved figure. Defaults to 100.
    """
    fig.savefig(file_name, bbox_inches='tight', pad_inches=pad_inches, dpi=dpi)


