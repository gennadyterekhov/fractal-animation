import os
from dataclasses import dataclass

from manim import *

from src.anims.fractal import make_n_iters
from src.funcs import get_direction, make_connecting_line


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

        central_circle = Circle(color=WHITE, stroke_width=2, radius=1, )
        central_circle.move_to((0, 0, 0))
        entry_data.all_objects.add(central_circle)
        self.play(Create(central_circle))

        connecting_line = make_connecting_line(
            starting_circle,
            central_circle,
        )
        entry_data.all_objects.add(connecting_line)
        self.play(Create(connecting_line))

        anims = get_rays_anims(entry_data, central_circle)
        self.play(*anims)
        self.play(
            entry_data.all_objects.animate.scale(0.25 * entry_data.radius),
            run_time=1
        )
        return EntryData(
            entry_data.all_objects,
            entry_data.rays,
            entry_data.radius,
        )
