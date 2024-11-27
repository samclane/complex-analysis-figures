from manim import *

class logx(Scene):
    def construct(self):
        axes = Axes( 
            x_range=[-0.1, 2, 2], 
            y_range=[-4, 2, 2], 
            x_length=4, 
            y_length=4, 
            axis_config={'include_numbers': True, 'numbers_to_exclude': [0]}, 
            x_axis_config={'color': ORANGE}, 
            y_axis_config={'color': ORANGE}, 
        ) 
        axes_label = axes.get_axis_labels(x_label='x', y_label='t') 
        graph = axes.plot(lambda x: np.log(x), x_range=[0.01, 3], color=YELLOW)
        # intercept
        intercept = Dot(axes.coords_to_point(1, 0), color=YELLOW)
        intercept_label = MathTex("1").next_to(intercept, DOWN, buff=0.2)
        graph_label = MathTex("t = log(x)").next_to(graph, UP, buff=0.2) 
        vgroup = VGroup(axes, graph, graph_label, axes_label, intercept, intercept_label)
        self.add(vgroup.scale(1.5))