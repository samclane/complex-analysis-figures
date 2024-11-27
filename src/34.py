from manim import *


class InscribedTriangles(Scene):
    def construct(self):
        # vgroup
        vgroup = VGroup()
        # Draw the axes
        axes = NumberPlane(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            background_line_style={"stroke_color": BLUE_E, "stroke_width": 1},
        )
        axes.add_coordinates(range(-1, 2), [])
        vgroup.add(axes)

        # Draw the unit circle
        unit_circle = Circle(radius=1, color=WHITE)
        vgroup.add(unit_circle)

        # inscribe a hexagon
        hexagon = RegularPolygon(n=6, color=YELLOW).scale(1)
        vgroup.add(hexagon)

        # Label the midpoint on the x-axis
        midpoint_label = (
            MathTex(r"\frac{1}{2}").next_to([0.5, 0, 0], DOWN, buff=-0.1).scale(0.55)
        )
        midpoint_dot = Dot(point=[0.5, 0, 0], color=RED)
        vgroup.add(midpoint_label, midpoint_dot)

        # Draw a line from the midpoint to the top of the hexagon
        line = Line(start=[0.5, 0, 0], end=[0.5, np.sqrt(3) / 2, 0], color=RED)
        vgroup.add(line)

        # Add an upside down triangle touching 60 and 120 degrees
        triangle = Polygon(
            [-0.5, np.sqrt(3) / 2, 0], [0.5, np.sqrt(3) / 2, 0], [0, 0, 0], color=YELLOW
        )
        vgroup.add(triangle)

        # Add x and y labels
        x_label = MathTex("x").next_to(axes.coords_to_point(1.2, 0), RIGHT)
        y_label = MathTex("y").next_to(axes.coords_to_point(0, 1.2), UP)
        vgroup.add(x_label, y_label)

        # Zoom in
        vgroup.scale(2)

        self.add(vgroup)
