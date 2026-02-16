from manim import *
from numpy import ndarray
from src.angle import get_angle, to_rads
import math


def get_direction(iter: int, rays: int) -> ndarray:
    '''
    UP: Vector3D = np.array((0.0, 1.0, 0.0))
    """One unit step in the positive Y direction."""

    DOWN: Vector3D = np.array((0.0, -1.0, 0.0))
    """One unit step in the negative Y direction."""

    RIGHT: Vector3D = np.array((1.0, 0.0, 0.0))
    """One unit step in the positive X direction."""

    LEFT: Vector3D = np.array((-1.0, 0.0, 0.0))
    """One unit step in the negative X direction."""

    '''
    print()
    print('get_direction', iter)
    angle = get_angle(iter, rays)
    angle_in_rads = to_rads(angle)
    x = math.cos(angle_in_rads)
    y = math.sin(angle_in_rads)
    print('angle', angle)
    print('angle_in_rads', angle_in_rads)
    print('x', x)
    print('y', y)
    return np.array((x, y, 0.0))


def get_circle_radius(rays: int) -> float:
    if rays < 8:
        return 1
    if rays < 13:
        return 0.5
    return 0.25


def make_connecting_line(obj1: Circle, obj2: Circle):
    direction = (obj2.get_center() - obj1.get_center())
    direction = normalize(direction)

    start_point = obj1.get_center() + direction*obj1.radius

    end_point = obj2.get_center() - direction*obj2.radius
    connecting_line = Line(start_point, end_point,
                           color=WHITE, stroke_width=3)
    return connecting_line


def make_filled_circle():
    circle = Circle(color=WHITE)
    circle.set_fill(GREEN, opacity=0.8)
    return circle
def make_filled_circle_w_rays(rays:int):
    circle = Circle(color=WHITE,radius=get_circle_radius(rays))
    circle.set_fill(GREEN, opacity=0.8)
    return circle