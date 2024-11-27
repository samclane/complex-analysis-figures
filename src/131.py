from manim import *


class PrTheta(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3, 3],
            y_range=[-0.1, 10],
            axis_config={"color": BLUE},
        )
        axes.add_coordinates(range(-3, 4), range(0, 10, 2))

        def pr_theta(r, theta):
            return (1 / 2 * PI) * ((1 - r**2) / (1 - 2 * r * np.cos(theta) + r**2))

        graph = axes.plot(lambda t: pr_theta(0.7, t), x_range=[-PI, PI], color=YELLOW)
        graph_label = MathTex("p(r, \\theta)").next_to(axes.get_y(), UR, buff=1)
        theta_label = MathTex("\\theta").next_to(axes, DR, buff=0.1)
        vgroup = VGroup(axes, graph, graph_label, theta_label)
        self.add(vgroup)
