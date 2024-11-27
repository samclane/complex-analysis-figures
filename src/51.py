from manim import *


class NestedRegion(Scene):
    def construct(self):
        # Draw the outermost shape (O), a rounded rectangle
        outer_shape = RoundedRectangle(
            width=6,
            height=6,
            corner_radius=1.7,
            fill_color=BLUE,
            fill_opacity=0.2,
            stroke_width=0,
        )
        outer_shape_label = MathTex("\mathcal{O}").next_to(outer_shape, UP)
        self.add(outer_shape, outer_shape_label)

        # Inner Square R(jk)
        inner_square = Square(side_length=4, color=RED, fill_opacity=0.2)
        inner_square_label = MathTex("R_{jk}").next_to(inner_square, UP)
        self.add(inner_square, inner_square_label)

        # Divide the inner square into 9 equal squares
        squares = VGroup()
        for i in range(3):
            for j in range(3):
                square = Square(side_length=4 / 3, color=WHITE, fill_opacity=0.0)
                square.move_to(
                    inner_square.get_center() + np.array([i - 1, j - 1, 0]) * 4 / 3
                )
                squares.add(square)
        self.add(squares)

        # Innermost square Omega(jk)
        innermost_square = RoundedRectangle(
            width=3.5, height=3.5, color=GREEN, fill_opacity=0.2
        )
        # cut out a center square
        innermost_cutout = RoundedRectangle(
            width=2, height=2, corner_radius=0.6, color=BLACK, fill_opacity=1
        )
        innermost_cutout.move_to(innermost_square.get_center())
        innermost_cutout = Cutout(innermost_cutout, innermost_square, fill_opacity=0.7)

        innermost_square_label = MathTex("\Omega_{jk}").next_to(
            innermost_square, RIGHT, buff=0.5
        )
        overall_square_label = MathTex("\Omega").next_to(innermost_square_label, UP)
        self.add(
            innermost_square,
            innermost_square_label,
            overall_square_label,
            innermost_cutout,
        )

        innermost_circle = Circle(radius=0.4, color=ORANGE, fill_opacity=0.2)
        self.add(innermost_circle)
