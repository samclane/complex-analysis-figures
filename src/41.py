from manim import *

class GraphWithAsymptotes(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-2, 2, 1],
            y_range=[-2, 2, 1],
            axis_config={"include_numbers": False}
        )

        # Add labels for the axes
        x_label = axes.get_x_axis_label("x")
        self.add(axes, x_label)

        # Define the function g(x)
        def g(x):
            return 1 / x

        # Plot the function
        graph = axes.plot(g, x_range=[-2, -0.2], color=BLUE)
        graph_right = axes.plot(g, x_range=[0.2, 2], color=BLUE)

        
        # Add labels for x = -1 and x = 1
        label_minus_1 = MathTex("-1").next_to(axes.c2p(-1, 0), DOWN)
        label_1 = MathTex("1").next_to(axes.c2p(1, 0), DOWN)

        # Add all elements to the scene
        self.add(graph, graph_right, label_minus_1, label_1)

        # Add the g(x) label near the curve
        graph_label = MathTex("g(x)").next_to(axes.c2p(1.5, g(1.5)), UR)
        self.add(graph_label)
