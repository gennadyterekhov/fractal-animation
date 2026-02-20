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
    starting_circle: Union[Circle, None]
    rays: int
    current_iteration: int
    text_blocks: List[Text]


class CircleWithNRays(Scene):
    def construct(self):
        iterations = int(os.environ.get('ITERATIONS', 5))
        rays = int(os.environ.get('RAYS', 5))
        entry_data = EntryData(VGroup(), None, rays, 1, [])

        make_n_iters(
            iterations,
            self.make_1_iteration,
            entry_data,
        )

    def make_1_iteration(self, entry_data: EntryData) -> EntryData:
        print('[make_1_iteration]', entry_data.current_iteration)
        existing_text = None
        if len(entry_data.text_blocks):
            existing_text = entry_data.text_blocks[0]
        else:
            entry_data.text_blocks.append(Text(''))
            existing_text = entry_data.text_blocks[0]
        entry_data.text_blocks[0] = write_on_screen(
            self,
            f'Iteration: {entry_data.current_iteration}',
            existing_text,
        )
        if entry_data.starting_circle is None:
            entry_data.starting_circle = make_filled_circle()
            entry_data.all_objects.add(entry_data.starting_circle)
            self.play(Create(entry_data.starting_circle), )
            self.wait(0.1)

        _start_crcl_center = Dot(point=entry_data.starting_circle.get_center(), color=PURPLE)
        self.add(_start_crcl_center)
        entry_data.all_objects.add(_start_crcl_center)

        central_point = Dot(point=[0, 0, 0], color=BLUE)
        # entry_data.all_objects.add(central_point)

        print(f'will have {entry_data.rays} circles')
        anims = []
        for i in range(entry_data.rays):
            print(f'iter {i}')
            (x, y, z) = get_direction(i, entry_data.rays)
            pnt = Dot(point=[x * 2.5, y * 2.5, 0], color=PURPLE)
            virtual_circle_w_centers = Circle(
                radius=2.5,
                color=BLUE,
                stroke_width=2
            )
            # self.add(pnt)
            # self.add(virtual_circle_w_centers)
            crcl = Circle(
                radius=1,
                color=WHITE,
                stroke_width=2,
            ).move_to(pnt.get_center())
            crcl.set_fill(GREEN, opacity=0.8)
            cl = make_connecting_line(crcl, entry_data.starting_circle)

            # entry_data.all_objects.add(virtual_circle_w_centers)
            # entry_data.all_objects.add(pnt)
            # entry_data.all_objects.add(crcl)
            entry_data.all_objects.add(cl)

            # anims.append(Create(crcl))
            anims.append(Create(cl))

        self.play(*anims)

        next_level_left = Circle(
            color=WHITE,
            radius=entry_data.all_objects.width / 2 + 0.5
        )
        next_level_left.move_to(central_point.get_center())
        self.play(Create(next_level_left))

        entry_data.all_objects.add(next_level_left)
        self.wait(0.1)
        # меняет ли это координаты?
        self.play(
            entry_data.all_objects.animate.scale(0.25),
            run_time=1
        )
        self.wait(0.1)
        res_data = EntryData(
            entry_data.all_objects,
            next_level_left,
            entry_data.rays,
            entry_data.current_iteration + 1,
            entry_data.text_blocks,
        )
        return res_data
