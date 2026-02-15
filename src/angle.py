import math


def get_angle(iter: int, rays: int) -> float:
    print()
    part = 360/rays
    print('360/rays', part)
    print('part*iter', part*iter)
    angle = 180-part*iter
    return angle


def to_rads(angle_in_degrees: float) -> float:
    return math.pi/180 * angle_in_degrees


def main():
    ang = get_angle(0, 4)
    assert (ang == 180)

    ang = get_angle(1, 4)
    print('ang',ang)
    assert (ang == 90)

    ang = get_angle(2, 4)
    assert (ang == 0)

    ang = get_angle(3, 4)
    assert (ang == -90)


if __name__ == '__main__':
    main()
