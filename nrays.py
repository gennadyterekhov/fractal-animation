from manim import *
from numpy import ndarray
import math
from src.angle import get_angle, to_rads


class StartingFromTheLeftCircle(Scene):
    def construct(self):
        self.make_n_iters(1, 7)

    def make_n_iters(self, n: int = 2, rays: int = 4):

        res_dct = self.make_the_first_iteration_and_return_starting_circle(
            rays)
        for i in range(n):
            res_dct = self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(
                res_dct['starting_circle'],
                res_dct['all_objects'],
                rays,
            )

    def make_the_first_iteration_and_return_starting_circle(self, rays: int = 4) -> dict:
        left_circle = make_filled_circle()
        all_objects = VGroup()
        all_objects.add(left_circle)
        self.play(Create(left_circle),)
        self.wait(0.1)
        return self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(left_circle, all_objects, rays)

    def make_1_iteration_and_return_starting_circle_and_all_prev_objs(self, starting_circle, all_objects: VGroup, rays: int = 4) -> dict:
        ''' dont add virtual objects to all_objects so that they dont accidentally appear in animations
        '''
        central_circle = Circle(color=WHITE)

        # first ray is always left, so central has direction=right
        central_circle.next_to(starting_circle, RIGHT, buff=0.5)
        all_objects.add(central_circle)
        self.play(Create(central_circle))

        connecting_line = make_connecting_line(
            starting_circle,
            central_circle,
        )
        all_objects.add(connecting_line)
        self.play(Create(connecting_line))

        self.play(
            all_objects.animate.shift(LEFT * 2.5),
            run_time=2
        )

        central_point = Dot(point=[0, 0, 0], color=BLUE)
        # all_objects.add(central_point)
        
        print(f'will have {rays} circles')
        anims = []
        for i in range(1, rays):
            print(f'iter {i}')
            

            angle = get_angle(i, rays)
            angle_in_rads = to_rads(angle)
            x = math.cos(angle_in_rads)
            y = math.sin(angle_in_rads)

            
            
            pnt = Dot(point=[x*2.5, y*2.5, 0],color=PURPLE)
            virtual_circle_w_centers = Circle(
                radius=2.5,
                color=BLUE,
                stroke_width=2
            )
            # self.add(pnt)
            # self.add(virtual_circle_w_centers)
            crcl = Circle(
                radius=1,
                color=WHITE,
                stroke_width=2,
            ).move_to(pnt.get_center())
            crcl.set_fill(GREEN, opacity=0.8)
            cl = make_connecting_line(crcl, central_circle)
            
            # all_objects.add(virtual_circle_w_centers)
            # all_objects.add(pnt)
            all_objects.add(crcl)
            all_objects.add(cl)

            anims.append(Create(crcl))
            anims.append(Create(cl))

        self.play(*anims)

        next_level_left = Circle(
            color=WHITE,
            radius=all_objects.width/2 + 0.5
        )
        next_level_left.move_to(central_point.get_center())
        self.play(Create(next_level_left))

        all_objects.add(next_level_left)
        self.wait(0.1)
        self.play(
            all_objects.animate.scale(0.25),
            run_time=1
        )
        self.wait(0.1)
        return {
            'starting_circle': next_level_left,
            'all_objects': all_objects,
        }


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
        for i in range(0, rays+1):
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


def get_direction(iter: int, rays: int) -> ndarray:
    '''
    UP: Vector3D = np.array((0.0, 1.0, 0.0))
    """One unit step in the positive Y direction."""

    DOWN: Vector3D = np.array((0.0, -1.0, 0.0))
    """One unit step in the negative Y direction."""

    RIGHT: Vector3D = np.array((1.0, 0.0, 0.0))
    """One unit step in the positive X direction."""

    LEFT: Vector3D = np.array((-1.0, 0.0, 0.0))
    """One unit step in the negative X direction."""

    '''
    print()
    print('get_direction', iter)
    angle = get_angle(iter, rays)
    angle_in_rads = to_rads(angle)
    x = math.cos(angle_in_rads)
    y = math.sin(angle_in_rads)
    print('angle', angle)
    print('angle_in_rads', angle_in_rads)
    print('x', x)
    print('y', y)
    return np.array((x, y, 0.0))


def make_connecting_line(obj1: Circle, obj2: Circle):
    direction = (obj2.get_center() - obj1.get_center())
    direction = normalize(direction)

    start_point = obj1.get_center() + direction

    end_point = obj2.get_center() - direction
    connecting_line = Line(start_point, end_point,
                           color=WHITE, stroke_width=3)
    return connecting_line


def make_filled_circle():
    circle = Circle(color=WHITE)
    circle.set_fill(GREEN, opacity=0.8)
    return circle
