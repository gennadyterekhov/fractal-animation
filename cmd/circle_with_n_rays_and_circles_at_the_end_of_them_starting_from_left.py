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
    radius: float


def get_rays_anims(entry_data: EntryData, central_circle: Circle) -> list:
    anims = []
    for i in range(entry_data.rays):
        (x, y, z) = get_direction(i, entry_data.rays)
        crcl = Circle(
            radius=entry_data.radius,
            color=WHITE,
            stroke_width=2,
        ).move_to([x * 2.5, y * 2.5, 0])
        crcl.set_fill(GREEN, opacity=0.8)
        cl = make_connecting_line(crcl, central_circle)
        entry_data.all_objects.add(cl)
        entry_data.all_objects.add(crcl)
        anims.append(Create(cl))
        anims.append(Create(crcl))

    return anims


def get_radius(rays: int) -> float:
    """we need to pick the value and then check manually"""
    return 1 / (1 * rays) + 0.09


class StartingFromTheLeftCircleWithVariableRadius(Scene):
    def construct(self):
        iterations = int(os.environ.get('ITERATIONS', 5))
        rays = int(os.environ.get('RAYS', 5))
        radius = get_radius(rays)
        entry_data = EntryData(VGroup(), rays, radius)
        make_n_iters(
            iterations,
            self.make_1_iteration_old,
            entry_data,
        )

    def make_1_iteration(self, entry_data: EntryData) -> EntryData:
        # main circle is always the same size
        central_circle = Circle(radius=1)
        entry_data.all_objects.add(central_circle)
        self.play(Create(central_circle))
        anims = get_rays_anims(entry_data, central_circle)
        self.play(*anims)
        self.play(entry_data.all_objects.animate.scale(0.25, about_point=(0, 0, 0)))
        return EntryData(entry_data.all_objects, entry_data.rays, entry_data.radius)

    def make_1_iteration_old(self, entry_data: EntryData) -> EntryData:

        starting_circle = Circle(
            radius=entry_data.radius,
            color=WHITE,
            stroke_width=2,
        )
        starting_circle.set_fill(GREEN, opacity=0.8)
        entry_data.all_objects.add(starting_circle)

        self.play(Create(starting_circle), )
        self.play(
            entry_data.all_objects.animate.shift(LEFT * 2.5),
            run_time=2
        )

        # first ray is always left, so central has direction=right
        central_circle = Circle(color=WHITE, stroke_width=2, radius=1, )
        # central_circle.next_to(starting_circle, RIGHT, buff=0.5)
        central_circle.move_to((0,0,0))
        entry_data.all_objects.add(central_circle)
        self.play(Create(central_circle))

        _start_crcl_center = Dot(
            point=starting_circle.get_center(), color=PURPLE)
        self.add(_start_crcl_center)
        entry_data.all_objects.add(_start_crcl_center)

        connecting_line = make_connecting_line(
            starting_circle,
            central_circle,
        )
        entry_data.all_objects.add(connecting_line)
        self.play(Create(connecting_line))

        central_point = Dot(point=[0, 0, 0], color=BLUE)
        # entry_data.all_objects.add(central_point)

        anims = get_rays_anims(entry_data, central_circle)
        self.play(*anims)
        self.play(
            entry_data.all_objects.animate.scale(0.25),
            run_time=1
        )
        return EntryData(
            entry_data.all_objects,
            entry_data.rays,
            entry_data.radius,
        )
        next_level_left = Circle(
            color=WHITE,
            radius=entry_data.all_objects.width / 2 + 0.5
        )
        next_level_left.move_to(central_point.get_center())
        self.play(Create(next_level_left))

        entry_data.all_objects.add(next_level_left)
        # меняет ли это координаты?
        return EntryData(
            entry_data.all_objects,
            entry_data.rays,
            entry_data.radius,
        )
