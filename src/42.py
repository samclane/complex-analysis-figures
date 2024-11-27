from manim import *

class ComplexPlaneTransformations(Scene):
    def construct(self):
        self.subplots = [VGroup() for _ in range(4)]
        # 1st plot is vertical band between -pi/2 and pi/2
        self.subplots[0] = self.get_vertical_band()
        # 2nd plot is entire positive half-plane
        self.subplots[1] = self.get_positive_half_plane()
        # 3rd plot is entire plane, with axis i and -i
        self.subplots[2] = self.get_full_plane()
        # 4th plot is entire plane, with axis 0 to -1 drawn
        self.subplots[3] = self.get_full_plane_with_axis()
        # Add all subplots to the scene
        for subplot in self.subplots:
            self.add(subplot.scale(0.75))
        # create an arrow between 1st and 2nd plot
        arrow_1 = Arrow(self.subplots[0].get_right(), self.subplots[1].get_left(), buff=0.1)
        text_1 = MathTex(r"{e} ^ {it}").next_to(arrow_1, UP)
        self.add(arrow_1, text_1)
        # create an arrow between 2nd and 3rd plot
        arrow_2 = Arrow(self.subplots[1].get_bottom(), self.subplots[3].get_top(), buff=0.1)
        text_2 = MathTex(r"{z} ^ {2}").next_to(arrow_2, RIGHT)
        self.add(arrow_2, text_2)
        # create an arrow between 3rd and 4th plot
        arrow_3 = Arrow(self.subplots[3].get_left(), self.subplots[2].get_right(), buff=0.1)
        text_3 = MathTex(r"i\frac{1 - z}{1 + z}").next_to(arrow_3, UP)
        self.add(arrow_3, text_3)
        # create an arrow between 1st and 4th plot
        arrow_4 = Arrow(self.subplots[0].get_bottom(), self.subplots[2].get_top(), buff=0.1)
        text_4 = MathTex(r"\text{tan} z").next_to(arrow_4, LEFT)
        self.add(arrow_4, text_4)
        
    def get_vertical_band(self):
        # Create the complex plane
        plane = ComplexPlane(
            x_range=[-2, 2, 1],  # X-axis range
            y_range=[-2, 2, 1],  # Y-axis range
            background_line_style={"stroke_opacity": 0.0},
            axis_config={"stroke_opacity": 0.4},
            
        )
        plane.move_to(2*UL + LEFT)
        # Shade the vertical band between -pi/2 and pi/2
        band = Rectangle(width=PI, height=4, fill_opacity=0.2, fill_color=BLUE)
        band.move_to(plane)
        # add vertical lines at -pi/2 and pi/2
        line_left = Line(plane.c2p(-PI/2, -2), plane.c2p(-PI/2, 2), color=RED)
        line_right = Line(plane.c2p(PI/2, -2), plane.c2p(PI/2, 2), color=RED)
        # add labels for -pi/2 and pi/2
        label_left = MathTex(r"-\frac{\pi}{2}").next_to(plane.c2p(-PI/2, 0), DL)
        label_right = MathTex(r"\frac{\pi}{2}").next_to(plane.c2p(PI/2, 0), DR)
        return VGroup(plane, band, line_left, line_right, label_left, label_right)
    
    def get_positive_half_plane(self):
        # Create the complex plane
        plane = ComplexPlane(
            x_range=[-0.5, 2, 1],  # X-axis range
            y_range=[-2, 2, 1],  # Y-axis range
            background_line_style={"stroke_opacity": 0.0},
        )
        plane.move_to(2*UR + RIGHT)
        # Shade the positive half-plane
        half_plane = Rectangle(width=2, height=4, fill_opacity=0.2, fill_color=BLUE)
        # move to the positive half-plane
        half_plane.move_to(plane)
        # label origin as 0
        label_0 = MathTex("0").next_to(plane.c2p(0, 0), DL, buff=0.5)
        return VGroup(plane, half_plane, label_0)
    
    def get_full_plane(self):
        # create a blank complex plane
        plane = ComplexPlane(
            x_range=[-2, 2, 1],  # X-axis range
            y_range=[-2, 2, 1],  # Y-axis range
            background_line_style={"stroke_opacity": 0.0},
            axis_config={"stroke_opacity": 0.0},
        )
        plane.move_to(2*DL + LEFT)
        # Add labels for i and -i
        label_i = MathTex("i").next_to(plane.c2p(0, 1), RIGHT, buff=0.2)
        label_minus_i = MathTex("-i").next_to(plane.c2p(0, -1), RIGHT, buff=0.2)
        # Create lines from origin to +i and -i
        line_to_i = Line(plane.c2p(0, 0.1), plane.c2p(0, 2), color=BLUE)
        line_to_minus_i = Line(plane.c2p(0, -0.1), plane.c2p(0, -2), color=BLUE)
        # color rect to highlight plane
        rect = Rectangle(width=4, height=4, fill_opacity=0.2, fill_color=BLUE)
        rect.move_to(plane)
        return VGroup(plane, label_i, label_minus_i, line_to_i, line_to_minus_i, rect)
    
    def get_full_plane_with_axis(self):
        # create a blank complex plane
        plane = ComplexPlane(
            x_range=[-2, 2, 1],  # X-axis range
            y_range=[-2, 2, 1],  # Y-axis range
            background_line_style={"stroke_opacity": 0.0},
            axis_config={"stroke_opacity": 0.0},
        )
        plane.move_to(2*DR + RIGHT)
        # Add a point
        point = Dot(plane.c2p(0, 0), color=YELLOW)
        # Add labels for 0
        label_0 = MathTex("0").next_to(plane.c2p(0, 0), RIGHT, buff=0.2)
        # Create lines from origin to +i and -i
        line_to_minus_one = Line(plane.c2p(0, 0), plane.c2p(-2, 0), color=BLUE)
        # color rect to highlight plane
        rect = Rectangle(width=4, height=4, fill_opacity=0.2, fill_color=BLUE)
        rect.move_to(plane)
        return VGroup(plane, label_0, line_to_minus_one, rect, point)