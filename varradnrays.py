from manim import *
from numpy import ndarray
from dataclasses import dataclass
from typing import Union
import math
from src.angle import get_angle, to_rads
from src.anims.fractal import make_n_iters
from src.funcs import get_circle_radius, make_connecting_line, make_filled_circle_w_rays
import os


@dataclass
class EntryData:
    all_objects: VGroup
    starting_circle: Union[Circle, None]
    rays: int


class StartingFromTheLeftCircle(Scene):
    def construct(self):
        iterations = int(os.environ.get('ITERATIONS', 5))
        rays = int(os.environ.get('RAYS', 5))
        entry_data = EntryData(VGroup(), None, rays)

        make_n_iters(
            iterations,
            self.make_1_iteration,
            entry_data,
        )

    def make_the_first_iteration_and_return_starting_circle(self, rays: int = 4) -> dict:
        left_circle = make_filled_circle_w_rays(rays)
        all_objects = VGroup()
        all_objects.add(left_circle)
        self.play(Create(left_circle),)
        self.wait(0.1)
        return self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(left_circle, all_objects, rays)

    def make_1_iteration(self, entry_data: EntryData) -> EntryData:
        ''' dont add virtual objects to all_objects so that they dont accidentally appear in animations
        '''
        
        if entry_data.starting_circle is None:
            entry_data.starting_circle = make_filled_circle_w_rays(entry_data.rays)
            all_objects = VGroup()
            all_objects.add(entry_data.starting_circle)
            self.play(Create(entry_data.starting_circle),)
            self.wait(0.1)
        
        central_circle = Circle(
            color=WHITE, radius=get_circle_radius(entry_data.rays))
        # first ray is always left, so central has direction=right
        central_circle.next_to(entry_data.starting_circle, RIGHT, buff=0.5)

        self.play(
            entry_data.all_objects.animate.shift(
                LEFT * (1/get_circle_radius(entry_data.rays))),
            run_time=2
        )
        entry_data.all_objects.add(central_circle)
        self.play(Create(central_circle))

        connecting_line = make_connecting_line(
            entry_data.starting_circle,
            central_circle,
        )
        entry_data.all_objects.add(connecting_line)
        self.play(Create(connecting_line))

        central_point = Dot(point=[0, 0, 0], color=BLUE)
        # entry_data.all_objects.add(central_point)

        print(f'will have {entry_data.rays} circles')
        anims = []
        for i in range(1, entry_data.rays):
            print(f'iter {i}')

            angle = get_angle(i, entry_data.rays)
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
                radius=get_circle_radius(entry_data.rays),
                color=WHITE,
                stroke_width=2,
            ).move_to(pnt.get_center())
            crcl.set_fill(GREEN, opacity=0.8)
            cl = make_connecting_line(crcl, central_circle)

            # entry_data.all_objects.add(virtual_circle_w_centers)
            # entry_data.all_objects.add(pnt)
            entry_data.all_objects.add(crcl)
            entry_data.all_objects.add(cl)

            anims.append(Create(crcl))
            anims.append(Create(cl))

        self.play(*anims)

        next_level_left = Circle(
            color=WHITE,
            radius=entry_data.all_objects.width/2 + 0.5
        )
        next_level_left.move_to(central_point.get_center())
        self.play(Create(next_level_left))

        entry_data.all_objects.add(next_level_left)
        self.wait(0.1)
        self.play(
            entry_data.all_objects.animate.scale(0.25),
            run_time=1
        )
        self.wait(0.1)
        res_data = EntryData(
            entry_data.all_objects,
            next_level_left,
            entry_data.rays,
        )
        return res_data
