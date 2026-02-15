
# trying manim


uv run manim -pql main.py StartingFromTheLeftCircle

uv run manim -pql nrays.py StartingFromTheLeftCircle



ls -la $(uv run python -c "import site; print(site.getsitepackages()[0])") | grep -E "(manim-fractal|manim_fractal)"