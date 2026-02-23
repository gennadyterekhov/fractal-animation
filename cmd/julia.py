import numpy as np
from manim import *

from src.julia import get_julia_points, get_color_by_iteration


class JuliaIsland(Scene):
    def construct(self):
        # Hardcoded parameters for Re(c) = -0.743643887037151, Im(c) = 0.131825904205330
        c_real = -0.743643887037151
        c_imag = 0.131825904205330
        c = complex(c_real, c_imag)

        # Julia set parameters
        max_iter = 100  # Maximum iterations for the fractal calculation
        power = 2  # Using z = z^2 + c

        # Create the Julia set as a custom mobject
        # julia = self.create_julia_set(c, max_iter, power)
        julia = self.load_pre_computed_julia_set(c, max_iter, power)

        # Add the Julia set to the scene
        self.add(julia)

        # Optional: Add a title with the parameters
        title = Text(
            f"Julia Island\nRe(c) = {c_real:.15f}\nIm(c) = {c_imag:.15f}",
            font_size=24,
            color=YELLOW
        ).to_corner(UL)
        self.add(title)
        # self.play(julia.animate.scale(4, about_point=(0, 0, 0)))

    # Optional: Add a slow reveal animation
    # self.wait(2)


    def load_pre_computed_julia_set(self, c, max_iter, power=2):
        julia_set = VGroup()
        dots = get_julia_points()
        julia_set.add(dots)
        return julia_set


class AnimatedJuliaIsland(JuliaIsland):
    """An animated version that shows the Julia set being built."""

    def construct(self):
        c_real = -0.743643887037151
        c_imag = 0.131825904205330
        c = complex(c_real, c_imag)

        # Parameters
        max_iter = 100
        power = 2

        # Create the Julia set with animation
        julia = self.animate_julia_set(c, max_iter, power)

        # Add title
        title = Text(
            f"Julia Island\nRe(c) = {c_real:.15f}\nIm(c) = {c_imag:.15f}",
            font_size=24,
            color=YELLOW
        ).to_corner(UL)
        self.add(title)

        self.wait(2)

    def animate_julia_set(self, c, max_iter, power=2):
        """Create the Julia set with animation showing points appearing."""
        # Set up the coordinate system
        x_center = -0.5
        y_center = 0
        width = 3.5
        height = 3.5

        # Lower resolution for animation to keep it smooth
        resolution = 200

        x_coords = np.linspace(x_center - width / 2, x_center + width / 2, resolution)
        y_coords = np.linspace(y_center - height / 2, y_center + height / 2, resolution)

        # Create the Julia set gradually
        julia_set = VGroup()

        for i, x in enumerate(x_coords):
            # Create a vertical strip of points
            strip = VGroup()

            for j, y in enumerate(y_coords):
                z = complex(x, y)
                n = 0

                while n < max_iter and abs(z) <= 2:
                    z = z ** power + c
                    n += 1

                if n == max_iter:
                    point = Dot(
                        point=[x, y, 0],
                        radius=0.002,
                        color=self.get_color_by_iteration(n, max_iter)
                    )
                    strip.add(point)

            # Add the strip to the scene with animation
            if len(strip) > 0:
                self.play(
                    Create(strip),
                    run_time=0.05,
                    rate_func=linear
                )
                julia_set.add(strip)

        return julia_set


class ZoomIntoJuliaIsland(JuliaIsland):
    """A zoom animation into the Julia island."""

    def construct(self):
        c_real = -0.743643887037151
        c_imag = 0.131825904205330
        c = complex(c_real, c_imag)

        # Parameters
        max_iter = 150  # Higher iterations for deeper zoom
        power = 2

        # Create the initial wide view
        initial_julia = self.create_julia_set_with_params(
            c, max_iter, power,
            x_center=-0.5, y_center=0,
            width=4, height=4,
            resolution=300
        )

        # Create the zoomed view
        zoomed_julia = self.create_julia_set_with_params(
            c, max_iter, power,
            x_center=-0.75, y_center=0.15,
            width=0.5, height=0.5,
            resolution=400
        )

        # Add the initial view
        self.add(initial_julia)

        # Title
        title = Text(
            f"Julia Island Zoom\nRe(c) = {c_real:.15f}\nIm(c) = {c_imag:.15f}",
            font_size=24,
            color=YELLOW
        ).to_corner(UL)
        self.add(title)

        self.wait(1)

        # Zoom animation
        self.play(
            Transform(initial_julia, zoomed_julia),
            run_time=3,
            rate_func=smooth
        )

        self.wait(2)

    def create_julia_set_with_params(self, c, max_iter, power,
                                     x_center, y_center, width, height,
                                     resolution=300):
        """Helper method to create a Julia set with specific view parameters."""
        x_coords = np.linspace(x_center - width / 2, x_center + width / 2, resolution)
        y_coords = np.linspace(y_center - height / 2, y_center + height / 2, resolution)

        julia_set = VGroup()

        for x in x_coords:
            for y in y_coords:
                z = complex(x, y)
                n = 0

                while n < max_iter and abs(z) <= 2:
                    z = z ** power + c
                    n += 1

                if n == max_iter:
                    point = Dot(
                        point=[x, y, 0],
                        radius=0.001,
                        color=self.get_color_by_iteration(n, max_iter)
                    )
                    julia_set.add(point)

        return julia_set
