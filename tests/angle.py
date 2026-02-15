from src.angle import get_angle, to_rads
import math


def test_angle():
    ang = get_angle(0, 4)
    assert (ang == 180)

    ang = get_angle(1, 4)
    assert (ang == 90)

    ang = get_angle(2, 4)
    assert (ang == 0)

    ang = get_angle(3, 4)
    assert (ang == -90)

    ang = get_angle(0, 5)
    assert (ang == 180)

    ang = get_angle(1, 5)
    print('ang', ang)
    assert (ang == 108)

    ang = get_angle(2, 5)
    assert (ang == 36)

    ang = get_angle(3, 5)
    assert (ang == -36)

    ang = get_angle(4, 5)
    assert (ang == -108)


def test_rads():
    rads = to_rads(0)
    assert (assert_floats(rads, 0))

    rads = to_rads(30)
    assert (assert_floats(rads, 0.523))

    rads = to_rads(45)
    assert (assert_floats(rads, 0.785))

    rads = to_rads(60)
    assert (assert_floats(rads, 1.047))

    rads = to_rads(180)
    print('rads', rads)
    assert (assert_floats(rads, 3.141))


def assert_floats(a, b) -> bool:
    epsilon = 0.001

    aok = in_region(a, b-epsilon, b+epsilon)
    bok = in_region(b, a-epsilon, a+epsilon)
    return aok and bok


def in_region(point, a, b) -> bool:
    return point >= a and point <= b


def main():
    test_angle()
    test_rads()


if __name__ == '__main__':
    main()
