from manim import *


class ComplexPlaneFigure(Scene):
    def construct(self):
        # create a point
        point = Dot(point=ORIGIN, color=YELLOW)
        # label the point
        label = MathTex("a+ib").next_to(point, RIGHT, buff=0.2)
        # add the point and label to the scene
        # add a vertical line above the point
        line = Line(start=point.get_center(), end=point.get_center() + UP, color=YELLOW)
        # add the line to the scene
        # add a horizontal line to the right of that line
        line2 = Line(start=line.get_end(), end=line.get_end() + RIGHT, color=YELLOW)
        # add the line to the scene
        # add a point at the end of the horizontal line
        point2 = Dot(point=line2.get_end(), color=YELLOW)
        # label the point
        label2 = MathTex("x+iy").next_to(point2, RIGHT, buff=0.2)
        # draw a kidney-bean shape around the points
        kidney_bean = ParametricFunction(
            lambda t: np.array(
                [
                    (
                        (2 * np.cos(t) - np.cos(2 * t) + 2) * np.cos(-PI / 4)
                        - (2 * np.sin(t) - np.sin(2 * t)) * np.sin(-PI / 4)
                    )
                    / 1,
                    (
                        (2 * np.cos(t) - np.cos(2 * t) + 2) * np.sin(-PI / 4)
                        + (2 * np.sin(t) - np.sin(2 * t)) * np.cos(-PI / 4)
                        + 1
                    )
                    / 2
                    + 0.5,  # Shifted up by 1 unit
                    0,
                ]
            ),
            t_range=[-PI, PI],
            color=YELLOW,
            use_smoothing=True,  # Enable smoothing
        )
        vgroup = VGroup(point, label, line, line2, point2, label2, kidney_bean)
        scale = min(self.camera.frame_height / 8, self.camera.frame_width / 8)
        self.add(vgroup.scale(scale))