
from manim import *


class StartingFromTheLeftCircle(Scene):
    def make_1_iteration_and_return_starting_circle_and_all_prev_objs(self, starting_circle, all_objects: VGroup) -> dict:
        all_circles = VGroup()
        all_lines = VGroup()

        central_circle = Circle(color=WHITE)
        central_circle.next_to(
            starting_circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(central_circle))

        connecting_line = self.make_connecting_line(
            starting_circle,
            central_circle,
        )

        self.play(Create(connecting_line))

        up_circle = self.make_filled_circle()
        down_circle = self.make_filled_circle()
        right_circle = self.make_filled_circle()

        all_circles.add(up_circle, down_circle, right_circle,
                        starting_circle, central_circle)
        all_objects.add(*all_circles)

        up_circle.next_to(central_circle, UP, buff=0.5)
        down_circle.next_to(central_circle, DOWN, buff=0.5)
        right_circle.next_to(central_circle, RIGHT, buff=0.5)

        connecting_line2 = self.make_connecting_line(up_circle, central_circle)
        connecting_line3 = self.make_connecting_line(
            down_circle, central_circle)
        connecting_line4 = self.make_connecting_line(
            right_circle, central_circle)

        all_lines.add(connecting_line, connecting_line2,
                      connecting_line3, connecting_line4)
        all_objects.add(*all_lines)

        self.play(
            Create(up_circle),
            Create(down_circle),
            Create(right_circle),
            Create(connecting_line2),
            Create(connecting_line3),
            Create(connecting_line4),
        )

        # all_objects = VGroup(up_circle, down_circle, right_circle, central_circle, starting_circle,
        #  connecting_line, connecting_line2, connecting_line3, connecting_line4)
        self.play(
            all_objects.animate.shift(LEFT * 2.5),
            run_time=2
        )

        next_level_left = Circle(
            color=WHITE,
            radius=all_objects.width/2 + 0.5  # Add padding
        )
        next_level_left.move_to(all_objects.get_center())
        self.play(Create(next_level_left))

        all_objects.add(next_level_left)
        all_plus_next_level_left = VGroup(up_circle, down_circle, right_circle, central_circle, starting_circle,
                                          connecting_line, connecting_line2, connecting_line3, connecting_line4, next_level_left)
        self.wait(0.1)
        self.play(
            all_objects.animate.scale(
                0.25),  # Scale factor < 1 makes smaller
            run_time=1
        )
        self.wait(0.1)
        # return next_level_left
        return {
            'starting_circle': next_level_left,
            'all_objects': all_objects,
        }

    def make_the_first_iteration_and_return_starting_circle(self) -> dict:
        left_circle = self.make_filled_circle()

        central_circle = Circle(color=WHITE)
        central_circle.next_to(
            left_circle, RIGHT, buff=0.5)  # set the position
        all_object = VGroup()
        all_object.add(left_circle, central_circle)
        # show the shapes on screen
        self.play(Create(left_circle),)
        self.wait(0.1)
        return self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(left_circle, all_object)

    def construct(self):

        res_dct = self.make_the_first_iteration_and_return_starting_circle()
        res_dct = self.make_1_iteration_and_return_starting_circle_and_all_prev_objs(
            res_dct['starting_circle'],
            res_dct['all_objects'],
        )
        res_dct['starting_circle']
        res_dct['all_objects']

    def make_connecting_line(self, obj1, obj2):
        # Calculate points on the circles' boundaries
        direction = (obj2.get_center() - obj1.get_center())
        direction = normalize(direction)  # Manim's normalize function

        # Start point: obj1 center + radius1 * direction (towards obj2)
        start_point = obj1.get_center() + direction * obj1.radius

        # End point: obj2 center - radius2 * direction (from obj2 towards obj1)
        end_point = obj2.get_center() - direction * obj2.radius
        print(f'start_point', start_point)
        print(f'end_point', end_point)
        print(f'obj1.radius', obj1.radius)
        print(f'obj2.radius', obj2.radius)
        print()
        # print(f'start_point', start_point)
        # Draw the line
        connecting_line = Line(start_point, end_point,
                               color=WHITE, stroke_width=3)
        return connecting_line

    def make_filled_circle(self):
        circle = Circle(color=WHITE)  # create a circle
        circle.set_fill(GREEN, opacity=0.8)  # set the color and transparency

        return circle
