from src.angle import get_angle

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
