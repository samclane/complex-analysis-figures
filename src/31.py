from manim import *

class et(Scene):
    def construct(self):
        axes = Axes( 
            x_range=[-2, 4, 2], 
            y_range=[-0.5, 4, 2], 
            x_length=4, 
            y_length=4, 
            axis_config={'include_numbers': True, 'numbers_to_exclude': [0]}, 
            x_axis_config={'color': ORANGE}, 
            y_axis_config={'color': ORANGE}, 
        ) 
        axes_label = axes.get_axis_labels(x_label='t', y_label='x') 
        graph = axes.plot(lambda x: np.e ** (x), x_range=[-2,1.5], color=YELLOW)
        # intercept
        intercept = Dot(axes.coords_to_point(0, 1), color=YELLOW)
        intercept_label = MathTex("1").next_to(intercept, LEFT, buff=0.2)
        graph_label = axes.get_graph_label(graph, label='e^t', color=YELLOW, x_val=1,dot=False) 
        vgroup = VGroup(axes, graph, graph_label, axes_label, intercept, intercept_label)
        self.add(vgroup.scale(1.5))