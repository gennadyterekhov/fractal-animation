import math


def get_angle(iter: int, rays: int) -> float:
    one_ray_degree = 360/rays
    angle = 180-one_ray_degree*iter
    return angle


def to_rads(angle_in_degrees: float) -> float:
    return math.pi/180 * angle_in_degrees
