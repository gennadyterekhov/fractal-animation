import math

from manim import *

from src.angle import get_angle, to_rads


class NRaysTest(Scene):
    # works
    def construct(self) -> dict:
        central_circle = Circle(color=WHITE)
        all_objects = VGroup()
        all_objects.add(central_circle)
        points = [

        ]
        # self.play(Create(central_circle),)
        self.add(central_circle)
        rays = 7
        print(f'will have {rays} circles')
        for i in range(0, rays + 1):
            print(f'iter {i}')

            angle = get_angle(i, rays)
            angle_in_rads = to_rads(angle)
            x = math.cos(angle_in_rads)
            y = math.sin(angle_in_rads)

            print('angle', angle)
            print('angle_in_rads', angle_in_rads)
            print('x', x)
            print('y', y)

            # dir = get_direction(i, rays)

            pnt = Dot(point=[x, y, 0])
            circle = Circle(
                radius=0.5,
                color=RED,
                stroke_width=2
            ).move_to(pnt.get_center())
            radius = Line((x, y, 0), (0, 0, 0),
                          color=WHITE, stroke_width=3)
            self.add(pnt)
            self.add(circle)
            self.add(radius)
        self.wait()


class PointExample(Scene):
    def construct(self):
        # Create a dot at specific coordinates (default radius=0.08)
        point = Dot(point=[2, 1, 0])  # [x, y, z] coordinates
        points = [
            # Dot(point=[0, 0, 0]),
            # Dot(point=[2, 1, 0]),
        ]
        labels = []

        for x in range(-1, 2):
            for y in range(-1, 2):
                points.append(Dot(point=[x, y, 0]))
                # labels.append(MathTex(f"({x}, {y})", color=WHITE).next_to(point, UP))
        # label = MathTex("P", color=WHITE).next_to(point, UP)
        # Add to scene
        self.add(*points)
        self.add(*labels)
        self.wait()


class HalfCircle(Scene):
    def construct(self):
        # Create a dot at specific coordinates (default radius=0.08)
        point = Dot(point=[2, 1, 0])  # [x, y, z] coordinates
        points = [
            # Dot(point=[0, 0, 0]),
            # Dot(point=[2, 1, 0]),
        ]
        labels = []
        step = 0.1
        # Create a range from 0 to 2.0 with a step of 0.5 (multiply bounds by 1/step)
        float_list = [i * step for i in range(int(0 / step), int(2.5 / step))]

        # range(0,4,0.1)

        for rad in float_list:
            points.append(Dot(point=[math.cos(rad), math.sin(rad), 0]))
            # labels.append(MathTex(f"({x}, {y})", color=WHITE).next_to(point, UP))
        # label = MathTex("P", color=WHITE).next_to(point, UP)
        # Add to scene
        self.add(*points)
        self.add(*labels)
        self.wait()
