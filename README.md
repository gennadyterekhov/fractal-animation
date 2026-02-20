# trying manim

# simplest example of fractal animation
ITERATIONS=3 uv run manim -pql ./cmd/circle.py ConcentricCircles

# examples 

## circle with N rays beaming from it
ITERATIONS=2 RAYS=4 uv run manim -pql ./cmd/circle_with_n_rays.py CircleWithNRays

## circle with n rays and circles at the end of them
ITERATIONS=2 RAYS=4 uv run manim -pql ./cmd/circle_with_n_rays_and_circles_at_the_end_of_them.py StartingFromTheCenter


uv run manim -pql ./cmd/main.py StartingFromTheLeftCircle


ITERATIONS=3 RAYS=4 uv run manim -pql ./cmd/varradnrays.py StartingFromTheLeftCircle

# tests
uv run manim -pql ./cmd/nrays.py NRaysTest

uv run manim -pql ./cmd/nrays.py PointExample

uv run manim -pql ./cmd/nrays.py HalfCircle





