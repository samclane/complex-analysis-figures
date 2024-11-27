from manim import *

class ComplexAdditionWithLine(Scene):
    def construct(self):
        # Create the complex plane
        plane = ComplexPlane(
            x_range=[-2, 4, 1],
            y_range=[-2, 4, 1],
            background_line_style={"stroke_opacity": 0.4},
        )
        plane.add_coordinates()

        # Define the vectors
        z = complex(2, 1)  # Z = 2 + i
        w = complex(1, 2)  # W = 1 + 2i
        z_plus_w = z + w

        # Arrows for the vectors
        arrow_z = Arrow(plane.c2p(0, 0), plane.c2p(z.real, z.imag), color=BLUE, buff=0)
        arrow_w = Arrow(plane.c2p(0, 0), plane.c2p(w.real, w.imag), color=GREEN, buff=0)
        arrow_z_plus_w = Arrow(
            plane.c2p(z.real, z.imag),
            plane.c2p(z_plus_w.real, z_plus_w.imag),
            color=RED,
            buff=0,
        )

        # Line from origin to z + w
        line_origin_to_z_plus_w = Arrow(
            plane.c2p(0, 0), plane.c2p(z_plus_w.real, z_plus_w.imag), color=YELLOW
        )

        # Labels for the vectors
        label_z = MathTex("z").next_to(arrow_z, RIGHT, buff=0.2)
        label_w = MathTex("w").next_to(arrow_w, UP, buff=0.2)
        label_z_plus_w = MathTex("z + w").next_to(
            arrow_z_plus_w, UP + RIGHT, buff=0.2
        )

        # Add everything to the scene
        scale = min(self.camera.frame_height / 8, self.camera.frame_width / 8)
        vgroup = VGroup(
            plane,
            arrow_z,
            arrow_w,
            arrow_z_plus_w,
            line_origin_to_z_plus_w,
            label_z,
            label_w,
            label_z_plus_w,
        ).scale(scale)
        self.add(vgroup)
