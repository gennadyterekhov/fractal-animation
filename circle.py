from dataclasses import dataclass
from manim import *
from src.angle import get_angle, to_rads
from src.anims.fractal import make_n_iters
from src.funcs import get_circle_radius, make_connecting_line, make_filled_circle


@dataclass
class EntryData:
    all_objects: VGroup


class ConcentricCircles(Scene):
    def construct(self):
        entry_data = EntryData(VGroup())
        make_n_iters(
            4,
            self.make_1_iteration,
            entry_data,
        )

    def make_1_iteration(self, entry_data: EntryData) -> dict:
        central_circle = Circle()

        entry_data.all_objects.add(central_circle)
        self.play(Create(central_circle))
        self.wait(0.1)
        self.play(
            entry_data.all_objects.animate.scale(0.25),
            run_time=1
        )
        self.wait(0.1)
        return EntryData(entry_data.all_objects)
