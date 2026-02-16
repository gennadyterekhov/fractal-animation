# trying manim

# simplest example of fractal animation
ITERATIONS=3 uv run manim -pql circle.py ConcentricCircles

# examples 
uv run manim -pql nrays.py StartingFromTheLeftCircle


uv run manim -pql main.py StartingFromTheLeftCircle


ITERATIONS=3 RAYS=4 uv run manim -pql varradnrays.py StartingFromTheLeftCircle

# tests
uv run manim -pql nrays.py NRaysTest

uv run manim -pql nrays.py PointExample

uv run manim -pql nrays.py HalfCircle





