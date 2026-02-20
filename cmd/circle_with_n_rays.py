from dataclasses import dataclass
from manim import *
from src.angle import get_angle, to_rads
from src.anims.fractal import make_n_iters
from src.debug.logger import write_on_screen
from src.funcs import get_circle_radius, get_direction, make_connecting_line, make_filled_circle
import os
from typing import Union, List
import math


@dataclass
class EntryData:
    all_objects: VGroup
    rays: int
    current_iteration: int
    text_blocks: List[Text]


class CircleWithNRays(Scene):
    def construct(self):
        iterations = int(os.environ.get('ITERATIONS', 5))
        rays = int(os.environ.get('RAYS', 5))
        entry_data = EntryData(VGroup(), rays, 1, [])

        make_n_iters(
            iterations,
            self.make_1_iteration,
            entry_data,
        )

    def make_1_iteration(self, entry_data: EntryData) -> EntryData:
        print('[make_1_iteration]', entry_data.current_iteration)

        central_circle = Circle()

        entry_data.all_objects.add(central_circle)
        self.play(Create(central_circle))
        self.wait(0.1)

        print(f'will have {entry_data.rays} rays')
        anims = []
        for i in range(entry_data.rays):
            print(f'iter {i}')
            (x, y, z) = get_direction(i, entry_data.rays)
            _cntr_pnt = Dot(point=[0,0,0], color=RED)
            pnt = Dot(point=[x * 2.5, y * 2.5, 0], color=PURPLE)
            virtual_circle_w_centers = Circle(
                radius=2.5,
                color=BLUE,
                stroke_width=2
            )
            # self.add(_cntr_pnt)
            # self.add(pnt)
            # self.add(virtual_circle_w_centers)
            crcl = Circle(
                radius=1,
                color=WHITE,
                stroke_width=2,
            ).move_to(pnt.get_center())
            crcl.set_fill(GREEN, opacity=0.8)
            cl = make_connecting_line(pnt, central_circle)

            # entry_data.all_objects.add(virtual_circle_w_centers)
            # entry_data.all_objects.add(pnt)
            # entry_data.all_objects.add(crcl)
            entry_data.all_objects.add(cl)

            # anims.append(Create(crcl))
            anims.append(Create(cl))

        self.play(*anims)

        self.play(
            entry_data.all_objects.animate.scale(0.25, about_point=(0,0,0)),
            run_time=1
        )
        self.wait(0.1)
        res_data = EntryData(
            entry_data.all_objects,
            entry_data.rays,
            entry_data.current_iteration + 1,
            entry_data.text_blocks,
        )
        return res_data
