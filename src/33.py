from manim import *


class UnitCircleComplexZoomed(Scene):
    def construct(self):
        # Draw the axes with scaling
        axes = NumberPlane(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1},
        )

        # Draw the unit circle
        unit_circle = Circle(radius=1, color=WHITE)  # Scale up the circle

        # Define the angle t
        angle = ValueTracker(PI / 4)  # Adjust the angle value as desired

        # Create the point y(t) = c(t) + i*s(t)
        point = always_redraw(
            lambda: Dot(
                point=axes.coords_to_point(
                    np.cos(angle.get_value()), np.sin(angle.get_value())
                ),
                color=YELLOW,
            )
        )

        # Add the angle arc
        angle_arc = always_redraw(
            lambda: Arc(
                radius=0.6,  # Larger radius for better visibility
                start_angle=0,
                angle=angle.get_value(),
                color=GREEN,
            )  # Scale up the arc
        )

        # Add the line connecting the origin to y(t)
        radius_line = always_redraw(
            lambda: Line(
                start=axes.coords_to_point(0, 0), end=point.get_center(), color=RED
            )
        )

        # Label the point
        point_label = always_redraw(
            lambda: MathTex("y(t) = c(t) + i s(t)")
            .next_to(point, UR, buff=0.3)
        )

        # Label the angle t
        angle_label = always_redraw(
            lambda: MathTex(r"t")
            
            .move_to(
                Arc(
                    radius=0.8,
                    start_angle=0,
                    angle=angle.get_value(),
                )
                
                .point_from_proportion(0.5)
            )
        )

        i_point = Dot(axes.coords_to_point(0, 1), color=WHITE)
        one_point = Dot(axes.coords_to_point(1, 0), color=WHITE)
        i_label = MathTex(r"i").next_to(i_point, UR)
        one_label = MathTex(r"1").next_to(one_point, DR)

        # Add elements to the scene
        vgroup = VGroup(
            axes,
            unit_circle,
            point,
            angle_arc,
            radius_line,
            point_label,
            angle_label,
            i_point,
            one_point,
            i_label,
            one_label,
        )
        self.add(vgroup.scale(2).move_to(LEFT - 0.5*LEFT))
