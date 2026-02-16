from manim import *
from numpy import ndarray
import math
from src.angle import get_angle, to_rads
from src.funcs import get_circle_radius, make_connecting_line, make_filled_circle


class StartingFromTheLeftCircle(Scene):
    def construct(self):
        self.make_n_iters(1, 12)

    def make_n_iters(self, n: int = 2, rays: int = 4):

        res_dct = self.make_the_first_iteration_and_return_starting_circle(
            rays)
        for i in range(n):
            res_dct = self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(
                res_dct['starting_circle'],
                res_dct['all_objects'],
                rays,
            )

    def make_the_first_iteration_and_return_starting_circle(self, rays: int = 4) -> dict:
        left_circle = make_filled_circle(rays)
        all_objects = VGroup()
        all_objects.add(left_circle)
        self.play(Create(left_circle),)
        self.wait(0.1)
        return self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(left_circle, all_objects, rays)

    def make_1_iteration_and_return_starting_circle_and_all_prev_objs(self, starting_circle, all_objects: VGroup, rays: int = 4) -> dict:
        ''' dont add virtual objects to all_objects so that they dont accidentally appear in animations
        '''
        central_circle = Circle(color=WHITE, radius=get_circle_radius(rays))

        self.play(
            all_objects.animate.shift(LEFT * (1/get_circle_radius(rays))),
            run_time=2
        )
        # first ray is always left, so central has direction=right
        # central_circle.next_to(starting_circle, RIGHT, buff=0.5)
        all_objects.add(central_circle)
        self.play(Create(central_circle))

        connecting_line = make_connecting_line(
            starting_circle,
            central_circle,
        )
        all_objects.add(connecting_line)
        self.play(Create(connecting_line))

        central_point = Dot(point=[0, 0, 0], color=BLUE)
        # all_objects.add(central_point)

        print(f'will have {rays} circles')
        anims = []
        for i in range(1, rays):
            print(f'iter {i}')

            angle = get_angle(i, rays)
            angle_in_rads = to_rads(angle)
            x = math.cos(angle_in_rads)
            y = math.sin(angle_in_rads)

            pnt = Dot(point=[x*2.5, y*2.5, 0], color=PURPLE)
            virtual_circle_w_centers = Circle(
                radius=2.5,
                color=BLUE,
                stroke_width=2
            )
            # self.add(pnt)
            # self.add(virtual_circle_w_centers)
            crcl = Circle(
                radius=get_circle_radius(rays),
                color=WHITE,
                stroke_width=2,
            ).move_to(pnt.get_center())
            crcl.set_fill(GREEN, opacity=0.8)
            cl = make_connecting_line(crcl, central_circle)

            # all_objects.add(virtual_circle_w_centers)
            # all_objects.add(pnt)
            all_objects.add(crcl)
            all_objects.add(cl)

            anims.append(Create(crcl))
            anims.append(Create(cl))

        self.play(*anims)

        next_level_left = Circle(
            color=WHITE,
            radius=all_objects.width/2 + 0.5
        )
        next_level_left.move_to(central_point.get_center())
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
