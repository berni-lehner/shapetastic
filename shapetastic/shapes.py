import numpy as np

import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

from .color_utils import interpolate_color

def draw_polygon(ax: plt.Axes, x: float, y: float, radius: float, n_points: int, color: str, rotation_angle: float = 0, outline: str = None, linewidth: float = 1) -> None:
    """
    Draw a polygon with specified parameters.

    Parameters:
        ax (plt.Axes): The Axes object to draw the polygon on.
        x (float): x-coordinate of the center of the polygon.
        y (float): y-coordinate of the center of the polygon.
        radius (float): Radius of the polygon (distance from center to vertices).
        n_points (int): Number of points/vertices of the polygon.
        color (str): Color of the polygon.
        rotation_angle (float, optional): Rotation angle of the polygon in degree. Defaults to 0.
        outline (str, optional): Color of the outline. Defaults to None.
        linewidth (float, optional): Width of the outline. If None, no outline will be drawn. Defaults to 1.

    Returns:
        None
    """
    # Draw figure
    angles = np.linspace(0, 2 * np.pi, n_points, endpoint=False) + np.deg2rad(rotation_angle)
    vertices = np.column_stack([x + radius * np.cos(angles), y + radius * np.sin(angles)])
    polygon = Polygon(vertices, closed=True, edgecolor=color, facecolor=color)

    ax.add_patch(polygon)

    # Compute interpolated color value for outline
    if outline == "interpolate":
        background_color = ax.get_figure().get_facecolor()
        outline = interpolate_color(background_color, color)
        
    # Draw outline
    if outline is not None and linewidth is not None:
        polygon.set_linewidth(linewidth)
        polygon.set_edgecolor(outline)
    
    plt.plot()


from matplotlib.patches import Ellipse

def draw_ellipse(ax: plt.Axes, x: float, y: float, width: float, height: float, color: str, rotation_angle: float = 0, outline: str = None, linewidth: float = 1) -> None:
    """
    Draw an ellipse with specified parameters.

    Parameters:
        ax (plt.Axes): The Axes object to draw the ellipse on.
        x (float): x-coordinate of the center of the ellipse.
        y (float): y-coordinate of the center of the ellipse.
        width (float): Width of the ellipse.
        height (float): Height of the ellipse.
        color (str): Color of the ellipse.
        rotation_angle (float, optional): Rotation angle of the ellipse in degree. Defaults to 0.
        outline (str, optional): Color of the outline. Defaults to None.
        linewidth (float, optional): Width of the outline. If None, no outline will be drawn. Defaults to 1.

    Returns:
        None
    """
    # Draw figure
    ellipse = Ellipse((x, y), width, height, angle=rotation_angle, edgecolor=color, facecolor=color, linewidth=linewidth)
    ax.add_patch(ellipse)

    # Compute interpolated color value for outline
    if outline == "interpolate":
        background_color = ax.get_figure().get_facecolor()
        outline = interpolate_color(background_color, color)
        
    # Draw outline
    if outline is not None and linewidth is not None:
        ellipse.set_linewidth(linewidth)
        ellipse.set_edgecolor(outline)

    plt.plot()    


from matplotlib.patches import Rectangle


def draw_rectangle(ax: plt.Axes, x: float, y: float, width: float, height: float, color: str, rotation_angle: float = 0, outline: str = None, linewidth: float = 1) -> None:
    """
    Draw a rectangle with specified parameters.

    Parameters:
        ax (plt.Axes): The Axes object to draw the rectangle on.
        x (float): x-coordinate of the center of the rectangle.
        y (float): y-coordinate of the center of the rectangle.
        width (float): Width of the rectangle.
        height (float): Height of the rectangle.
        color (str): Color of the rectangle.
        rotation_angle (float, optional): Rotation angle of the ellipse in degree. Defaults to 0.
        outline (str, optional): Color of the outline. Defaults to None.
        linewidth (float, optional): Width of the outline. If None, no outline will be drawn. Defaults to 1.

    Returns:
        None
    """
    # Draw figure 
    rectangle = Rectangle((x - width/2, y - height/2), width, height, angle=rotation_angle, rotation_point='center', edgecolor=color, facecolor=color, linewidth=linewidth)
    ax.add_patch(rectangle)

    # Compute interpolated color value for outline
    if outline == "interpolate":
        background_color = ax.get_figure().get_facecolor()
        outline = interpolate_color(background_color, color)
        
    # Draw outline
    if outline is not None and linewidth is not None:
        rectangle.set_linewidth(linewidth)
        rectangle.set_edgecolor(outline)

    plt.plot()


from matplotlib.patches import Polygon
from matplotlib.transforms import Affine2D


def draw_parallelogram(ax: plt.Axes, x: float, y: float, width: float, height: float, color: str, skew: float = 0, rotation_angle: float = 0, outline: str = None, linewidth: float = 1) -> None:
    """
    Draw a parallelogram with specified parameters.

    Parameters:
        ax (plt.Axes): The Axes object to draw the parallelogram on.
        x (float): x-coordinate of the center of the parallelogram.
        y (float): y-coordinate of the center of the parallelogram.
        width (float): Width of the parallelogram.
        height (float): Height of the parallelogram.
        color (str): Color of the parallelogram.
        skew (float, optional): Skew factor of the parallelogram in degrees. Defaults to 0.
        rotation_angle (float, optional): Rotation angle of the parallelogram in degrees. Defaults to 0.
        outline (str, optional): Color of the outline. Defaults to None.
        linewidth (float, optional): Width of the outline. If None, no outline will be drawn. Defaults to 1.

    Returns:
        None
    """
    # TODO: workaround to ensure proper correspondence to rotation_angle and skew
    tmp = width
    width = height
    height = tmp
    rotation_angle = (rotation_angle+90) % 360

    # Compensate for skew
    rotation_angle = rotation_angle+skew

    # Calculate translation for skew along x-axis
    tx = height * np.tan(np.deg2rad(skew))

    # Calculate vertices of the parallelogram at origin
    vertices = np.array([
        [- width / 2 - tx, - height / 2],
        [width / 2 - tx, - height / 2],
        [width / 2, height / 2],
        [- width / 2, height / 2]
    ])

    # Calculate center of the parallelogram at origin
    center_x = np.mean(vertices[:, 0])
    center_y = np.mean(vertices[:, 1])

    # Apply rotation around the center of the parallelogram
    rotation_transform = Affine2D().translate(-center_x, -center_y).rotate_deg(rotation_angle).translate(x, y)
    transformed_vertices = rotation_transform.transform(vertices)

    # Create parallelogram
    parallelogram = Polygon(transformed_vertices, edgecolor=color, facecolor=color, linewidth=linewidth)

    # Add parallelogram to the axes
    ax.add_patch(parallelogram)

    # Compute interpolated color value for outline
    if outline == "interpolate":
        background_color = ax.get_figure().get_facecolor()
        outline = interpolate_color(background_color, color)
        
    # Draw outline
    if outline is not None and linewidth is not None:
        parallelogram.set_linewidth(linewidth)
        parallelogram.set_edgecolor(outline)

    plt.plot()


def draw_star(ax: plt.Axes, x: float, y: float, outer_radius: float, inner_radius: float, num_peaks: int, color: str, rotation_angle: float = 0, outline: str = None, linewidth: float = 1) -> None:
    """
    Draw a star shape with specified parameters.

    Parameters:
        ax (plt.Axes): The Axes object to draw the star on.
        x (float): x-coordinate of the center of the star.
        y (float): y-coordinate of the center of the star.
        outer_radius (float): Outer radius of the star (distance from center to outer points).
        inner_radius (float): Inner radius of the star (distance from center to inner points).
        color (str): Color of the star.
        rotation_angle (float): Rotation angle of the star in degree. Defaults to 0.
        num_peaks (int): Number of peaks of the star.
        outline (str, optional): Color of the outline. Defaults to None.
        linewidth (float, optional): Width of the outline. If None, no outline will be drawn. Defaults to 1.

    Returns:
        None
    """
    angles = np.linspace(0, 2 * np.pi, 2 * num_peaks, endpoint=False) + np.deg2rad(rotation_angle)
    vertices = []
    for i in range(2 * num_peaks):
        radius = outer_radius if i % 2 == 0 else inner_radius
        vertices.append((x + radius * np.cos(angles[i]), y + radius * np.sin(angles[i])))
    polygon = Polygon(vertices, closed=True, edgecolor=color, facecolor=color)
    ax.add_patch(polygon)

    # Compute interpolated color value for outline
    if outline == "interpolate":
        background_color = ax.get_figure().get_facecolor()
        outline = interpolate_color(background_color, color)
        
    # Draw outline
    if outline is not None and linewidth is not None:
        polygon.set_linewidth(linewidth)
        polygon.set_edgecolor(outline)

    plt.plot()
