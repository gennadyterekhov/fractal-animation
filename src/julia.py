from manim import *

from src.project import get_project_dir, read_json_file, write_json_file


def get_julia_points():
    path = f'{get_project_dir()}/src/pre_computed_data/julia_points.json'
    points = read_json_file(path)
    mobjects = []
    for coords in points:
        mobjects.append(Dot(
            point=[coords['x'], coords['y'], 0],
            radius=0.002,
            color=get_color_by_iteration(coords['n'], coords['max_iter'])
        ))
    return mobjects


def get_color_by_iteration(n, max_iter):
    """Map iteration count to a color."""
    if n == max_iter:
        # Points in the set (didn't escape)
        return WHITE
    else:
        # Points outside the set - color based on escape speed
        t = n / max_iter
        # Use a color gradient (blue to red)
        return interpolate_color(BLUE, RED, t)


def pre_compute_julia_set():
    c_real = -0.743643887037151
    c_imag = 0.131825904205330
    c = complex(c_real, c_imag)

    # Julia set parameters
    max_iter = 100  # Maximum iterations for the fractal calculation
    power = 2  # Using z = z^2 + c

    # Create the Julia set as a custom mobject
    julia = create_julia_set(c, max_iter, power)
    path = f'{get_project_dir()}/src/pre_computed_data/julia_points.json'

    write_json_file(path, julia)


def create_julia_set(c, max_iter, power=2) -> list[dict]:
    scale = 4
    x_center = -0.5
    y_center = 0
    width = 3.5 * scale
    height = 3.5 * scale

    # Resolution for the fractal (higher = better quality but slower)
    resolution = 400

    # Create a grid of points
    x_coords = np.linspace(x_center - width / 2, x_center + width / 2, resolution)
    y_coords = np.linspace(y_center - height / 2, y_center + height / 2, resolution)

    # Create a VMobject to hold all the points
    julia_set = []

    # Calculate the fractal
    for i, x in enumerate(x_coords):
        for j, y in enumerate(y_coords):
            z = complex(x, y)
            n = 0

            # Iterate to check if point escapes
            while n < max_iter and abs(z) <= 2:
                z = z ** power + c
                n += 1

            # If point didn't escape, it's in the Julia set
            if n == max_iter:
                point = {
                    'x': x,
                    'y': y,
                    'n': n,
                    'max_iter': max_iter,
                }
                julia_set.append(point)

    return julia_set


def create_julia_set_of_mobjects( c, max_iter, power=2):
    """Create the Julia set as a VMobject."""
    # Set up the coordinate system
    # Center on the interesting region for this specific c value
    scale = 4
    x_center = -0.5
    y_center = 0
    width = 3.5 * scale
    height = 3.5 * scale

    # Resolution for the fractal (higher = better quality but slower)
    resolution = 400

    # Create a grid of points
    x_coords = np.linspace(x_center - width / 2, x_center + width / 2, resolution)
    y_coords = np.linspace(y_center - height / 2, y_center + height / 2, resolution)

    # Create a VMobject to hold all the points
    julia_set = VGroup()

    # Calculate the fractal
    for i, x in enumerate(x_coords):
        for j, y in enumerate(y_coords):
            z = complex(x, y)
            n = 0

            # Iterate to check if point escapes
            while n < max_iter and abs(z) <= 2:
                z = z ** power + c
                n += 1

            # If point didn't escape, it's in the Julia set
            if n == max_iter:
                point = Dot(
                    point=[x, y, 0],
                    radius=0.002,
                    color=get_color_by_iteration(n, max_iter)
                )
                julia_set.add(point)

    return julia_set
