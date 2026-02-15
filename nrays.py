from manim import *
from numpy import ndarray
import math


class StartingFromTheLeftCircle(Scene):
    def construct(self):
        self.make_n_iters(1)

    def make_n_iters(self, n: int = 2, rays: int = 5):

        res_dct = self.make_the_first_iteration_and_return_starting_circle(
            rays)
        for i in range(n):
            res_dct = self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(
                res_dct['starting_circle'],
                res_dct['all_objects'],
                rays,
            )

    def make_the_first_iteration_and_return_starting_circle(self, rays: int = 4) -> dict:
        left_circle = self.make_filled_circle()

        central_circle = Circle(color=WHITE)

        # first ray is always left, so central has direction=right
        central_circle.next_to(
            left_circle, RIGHT, buff=0.5)
        all_object = VGroup()
        all_object.add(left_circle, central_circle)
        self.play(Create(left_circle),)
        self.wait(0.1)
        return self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(left_circle, all_object, rays)

    def make_1_iteration_and_return_starting_circle_and_all_prev_objs(self, starting_circle, all_objects: VGroup, rays: int = 4) -> dict:
        central_circle = Circle(color=WHITE)

        # first ray is always left, so central has direction=right
        central_circle.next_to(starting_circle, RIGHT, buff=0.5)
        self.play(Create(central_circle))

        connecting_line = self.make_connecting_line(
            starting_circle,
            central_circle,
        )

        self.play(Create(connecting_line))

        # will have n circles
        anims = []
        for i in range(1, rays+1):
            # res_crcl = self.create_nth_circle(i)
            crcl = self.make_filled_circle()
            crcl.next_to(
                central_circle, self.get_direction(i, rays), buff=0.5)
            cl = self.make_connecting_line(crcl, central_circle)
            all_objects.add(crcl)
            all_objects.add(cl)

            anims.append(Create(crcl))
            anims.append(Create(cl))

        self.play(*anims)
        self.play(
            all_objects.animate.shift(LEFT * 2.5),
            run_time=2
        )

        next_level_left = Circle(
            color=WHITE,
            radius=all_objects.width/2 + 0.5
        )
        next_level_left.move_to(all_objects.get_center())
        self.play(Create(next_level_left))

        all_objects.add(next_level_left)
        self.wait(0.1)
        self.play(
            all_objects.animate.scale(0.25),
            run_time=1
        )
        self.wait(0.1)
        return {
            'starting_circle': next_level_left,
            'all_objects': all_objects,
        }

    def create_nth_circle(self, iter: int, rays: int) -> dict:
        crcl = self.make_filled_circle()
        return {
            'circle': crcl,
            'direction': self.get_direction(iter, rays),
        }

    def get_direction(self, iter: int, rays: int) -> ndarray:
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
        if iter == 0:
            return RIGHT
        angle = self.get_angle(iter, rays)
        angle_in_rads = self.to_rads(angle)
        x = math.cos(angle_in_rads)
        y = math.sin(angle_in_rads)
        print('angle', angle)
        print('x', x)
        print('y', y)
        return np.array((x*0.5, y*0.5, 0.0))

    def get_angle(self, iter: int, rays: int) -> float:
        part = 360/rays
        print('360/rays', part)
        print('part*iter', part*iter)
        angle = 180-part*iter
        return angle

    def to_rads(self, angle_in_degrees: float) -> float:
        return math.pi/180 * angle_in_degrees

    def make_connecting_line(self, obj1: Circle, obj2: Circle):
        direction = (obj2.get_center() - obj1.get_center())
        direction = normalize(direction)

        start_point = obj1.get_center() + direction

        end_point = obj2.get_center() - direction
        connecting_line = Line(start_point, end_point,
                               color=WHITE, stroke_width=3)
        return connecting_line

    def make_filled_circle(self):
        circle = Circle(color=WHITE)
        circle.set_fill(GREEN, opacity=0.8)
        return circle
