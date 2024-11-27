from manim import *


class RectangleWithArrows(Scene):
    def construct(self):
        # Create a rectangle for R_dz
        rect_color = BLUE
        rectangle = Rectangle(width=6, height=4, color=rect_color)
        rectangle_label = MathTex("R_{\\alpha z}").move_to(rectangle.get_center())

        # Add rectangle to the scene
        self.add(rectangle, rectangle_label)

        # # Define the corners of the rectangle
        bottom_left = rectangle.get_corner(DL)
        bottom_right = rectangle.get_corner(DR)
        top_left = rectangle.get_corner(UL)
        top_right = rectangle.get_corner(UR)

        # Add points at corners a+ib and x+iy
        point_color = rect_color
        point_a_ib = Dot(bottom_left, color=point_color)
        point_x_iy = Dot(top_right, color=point_color)
        self.add(point_a_ib, point_x_iy)

        # # Label the corners
        label_a_ib = MathTex("a+ib").next_to(bottom_left, LEFT)
        label_x_iy = MathTex("x+iy").next_to(top_right, RIGHT)
        label_sigma_xz = MathTex("\\sigma_{\\alpha z}").next_to(bottom_right, RIGHT, buff=0.7)
        label_gamma_xz = MathTex("\\gamma_{\\alpha z}").next_to(top_left, LEFT, buff=0.7)

        self.add(label_a_ib, label_x_iy, label_sigma_xz, label_gamma_xz)

        # Draw arrows from sigma and gamma to the nearest sides
        arrow_sigma_1 = CurvedArrow(
            start_point=label_sigma_xz.get_right() + 0.1 * RIGHT,
            end_point=rectangle.get_right(),
            color=YELLOW,
        )
        arrow_sigma_2 = CurvedArrow(
            start_point=label_sigma_xz.get_left() + 0.1 * LEFT,
            end_point=rectangle.get_bottom(),
            color=YELLOW,
        )
        arrow_gamma_1 = CurvedArrow(
            start_point=label_gamma_xz.get_left() + 0.1 * LEFT,
            end_point=rectangle.get_left(),
            color=YELLOW,
        )
        arrow_gamma_2 = CurvedArrow(
            start_point=label_gamma_xz.get_right() + 0.1 * RIGHT,
            end_point=rectangle.get_top(),
            color=YELLOW,
        )
        # flip arrow sigma2 and gamma2 arc center Ys so they go outside the rectangle
        arrow_sigma_2.rotate(PI, about_point=arrow_sigma_2.get_center()).shift(DOWN).flip()
        arrow_gamma_2.rotate(PI, about_point=arrow_gamma_2.get_center()).shift(UP).flip()
        self.add(arrow_sigma_1, arrow_sigma_2, arrow_gamma_1, arrow_gamma_2)

        # add arrowheads to show the direction of Rdz
        arrowhead_color = rect_color
        arrowhead_bottom = Arrow(
            start=bottom_right,
            end=rectangle.get_bottom() + LEFT,
            buff=0,
            color=arrowhead_color,
            max_stroke_width_to_length_ratio=0,
        )
        arrowhead_top = Arrow(
            start=top_left,
            end=rectangle.get_top() + RIGHT,
            buff=0,
            color=arrowhead_color,
            max_stroke_width_to_length_ratio=0,
        )
        arrowhead_left = Arrow(
            start=bottom_left,
            end=rectangle.get_left() + UP,
            buff=0,
            color=arrowhead_color,
            max_stroke_width_to_length_ratio=0,
        )
        arrowhead_right = Arrow(
            start=top_right,
            end=rectangle.get_right() + DOWN,
            buff=0,
            color=arrowhead_color,
            max_stroke_width_to_length_ratio=0,
        )
        self.add(arrowhead_bottom, arrowhead_top, arrowhead_left, arrowhead_right)
