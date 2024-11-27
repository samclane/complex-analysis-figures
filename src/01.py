from manim import *

class ComplexPlanePlot(Scene):
    def construct(self):
        vgroup = VGroup()
        # Create the complex plane
        plane = ComplexPlane(
            x_range=[-2, 2, 1],  # X-axis range
            y_range=[-2, 2, 1],  # Y-axis range
            background_line_style={"stroke_opacity": 0.4},
        )
        plane.add_coordinates()  # Add numbers to axes

        # Define points on the plane
        point_1 = Dot(plane.coords_to_point(1, 0), color=YELLOW)
        point_i = Dot(plane.coords_to_point(0, 1), color=YELLOW)

        # Labels for the points
        label_1 = MathTex("1").next_to(point_1, RIGHT, buff=0.2)
        label_i = MathTex("i").next_to(point_i, UP, buff=0.2)

        # Add everything to the scene
        vgroup.add(plane, point_1, point_i, label_1, label_i)
        vgroup.scale(2)
        self.add(vgroup)