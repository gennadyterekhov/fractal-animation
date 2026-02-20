# trying manim

# simplest example of fractal animation

    ITERATIONS=3 uv run manim -pql ./cmd/circle.py ConcentricCircles

# examples

## circle with N rays beaming from it

    ITERATIONS=2 RAYS=4 uv run manim -pql ./cmd/circle_with_n_rays.py CircleWithNRays

## circle with n rays and circles at the end of them

    ITERATIONS=2 RAYS=4 uv run manim -pql ./cmd/circle_with_n_rays_and_circles_at_the_end_of_them.py StartingFromTheCenter

## circle with n rays and circles at the end of them with variable radius

    ITERATIONS=2 RAYS=8 uv run manim -pql ./cmd/circle_with_n_rays_and_circles_at_the_end_of_them_with_variable_radius.py StartingFromTheCenterWithVariableRadius


## starting from left circle

    ITERATIONS=2 RAYS=8 uv run manim -pql ./cmd/circle_with_n_rays_and_circles_at_the_end_of_them_starting_from_left.py StartingFromTheLeftCircleWithVariableRadius

# tests

    uv run manim -pql ./cmd/example.py NRaysTest

    uv run manim -pql ./cmd/example.py PointExample

    uv run manim -pql ./cmd/example.py HalfCircle





