import os
from dataclasses import dataclass

from manim import *

from src.anims.fractal import make_n_iters
from src.funcs import get_direction, make_connecting_line


@dataclass
class EntryData:
    all_objects: VGroup
    rays: int


def get_rays_anims(entry_data: EntryData, central_circle: Circle, ) -> list:
    anims = []
    for i in range(entry_data.rays):
        print(f'iter {i}')
        (x, y, z) = get_direction(i, entry_data.rays)
        pnt = Dot(point=[x * 2.5, y * 2.5, 0], color=PURPLE)
        cl = make_connecting_line(pnt, central_circle)
        entry_data.all_objects.add(cl)
        anims.append(Create(cl))
    return anims


class CircleWithNRays(Scene):
    def construct(self):
        iterations = int(os.environ.get('ITERATIONS', 5))
        rays = int(os.environ.get('RAYS', 5))
        entry_data = EntryData(VGroup(), rays)

        make_n_iters(
            iterations,
            self.make_1_iteration,
            entry_data,
        )

    def make_1_iteration(self, entry_data: EntryData) -> EntryData:
        central_circle = Circle()

        entry_data.all_objects.add(central_circle)
        self.play(Create(central_circle))

        anims = get_rays_anims(entry_data, central_circle)

        self.play(*anims)

        self.play(
            entry_data.all_objects.animate.scale(0.25, about_point=(0, 0, 0)),
            run_time=1
        )
        return EntryData(entry_data.all_objects, entry_data.rays)
