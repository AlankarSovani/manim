from manim import *
import numpy as np

class MethodOfCharacteristics(ThreeDScene):
    def construct(self):
        # Set up the 3D axes
        axes = ThreeDAxes(
            x_range=[-4, 4, 4],
            y_range=[-4, 4, 4],
            z_range=[-2, 2, 2],
            x_length=8,
            y_length=8,
            z_length=4
        )
        axes.set_color(BLUE)

        # Define the solution surface
        surface = Surface(
            lambda u, v: np.array([u, v, 2*np.sin((u - v))*0.5]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(20, 20),
        )
        surface.set_color(RED)
        surface.set_style(fill_opacity=1, stroke_color=BLACK, stroke_width=0)
        method_intro_tex = Tex('Consider the equation ', r'$u_x\;$', r'$+\;$', r'$u_y\;$', r'$=\;$', '$0$').shift(UP/4).scale(1.5)
        method_intro_tex.set_color_by_tex_to_color_map(
            {
                'u_x': YELLOW,
                'u_y': YELLOW,
                '0': BLUE
            }
        )
        question_intro_tex = Tex(r'How would we find all possible functions ', '\\\\',  r'$ u \;$', r'$=\;$', r'$f(x, y)$',  r' that satisfy this equation?').next_to(method_intro_tex, DOWN)
        question_intro_tex.set_color_by_tex_to_color_map(
            {
                r' u ': YELLOW,
                r'f(x, y)': RED
            }
        )
        general_question_intro_tex = Tex(r'Or more generally, how would we find the solutions to').shift(UP/4)
        general_equation_tex = Tex(r'$f(x, y)$', r'$u_x\;$', r'$+\;$', r'$g(x, y)$', r'$u_y\;$', r'$=\;$', r'$h(x, y)$', r'?').next_to(general_question_intro_tex, DOWN)
        general_equation_tex.set_color_by_tex_to_color_map(
            {
                r"f(x, y)": RED,
                r"u_x": YELLOW,
                r"g(x, y)": BLUE,
                r"u_y": YELLOW,
                r"h(x, y)": PINK        
            }
        )
        title_tex = Tex(r'Method of', '\\\\', 'Characteristics').scale(2.5).shift(UP/4)
        title_tex.set_color_by_tex_to_color_map(
            {
                "Method": BLUE,
                "Characteristics": PINK
            }
        )
        self.camera.add_fixed_in_frame_mobjects(title_tex)
        # clarification_x = Tex(r'$u_x = \frac{\partial u(x, y)}{\partial x}$').scale(1.5)
        # clarification_y = Tex(r'$u_y = \frac{\partial u(x, y)}{\partial y}$').next_to(clarification_x, DOWN).scale(1.5)
        self.play(Write(method_intro_tex), run_time = 2)
        self.wait(1)
        self.play(Write(question_intro_tex), run_time = 4)
        self.wait(1.5)
        self.play(ReplacementTransform(VGroup(method_intro_tex, question_intro_tex), general_question_intro_tex), run_time = 2)
        self.wait(0.5)
        self.play(Write(general_equation_tex), run_time = 3)
        self.wait(2)
        self.play(ReplacementTransform(VGroup(general_question_intro_tex, general_equation_tex), title_tex), run_time = 5)
        self.wait(2)
        # self.play(Write(clarification_x), Write(clarification_y), run_time = 3)
        self.set_camera_orientation(phi=60 * DEGREES, theta=0 * DEGREES)
        self.begin_ambient_camera_rotation(rate=3*DEGREES)
        self.play(FadeOut(title_tex), run_time = 1)
        self.play(Create(VGroup(axes, surface)), run_time = 3)
        # self.play(self.camera.frame.animate.move_to([0, 0, 0]), run_time=3)  # Move the camera frame
        self.wait(1)
        tex_1 = Tex('Sometimes when dealing with a problem, ', 'it helps to analyze the', '\\\\', ' properties ', 'of the question itself').to_edge(UP)
        tex_1.set_color_by_gradient(RED, BLUE, PURPLE)
        tex_2 = Tex(r"Let's start with the original equation: ", "\\\\", r'$u_x\;$', r'$+\;$', r'$u_y\;$', r'$=\;$', '$0$').to_edge(UP)
        tex_2.set_color_by_tex_to_color_map(
            {
                'u_x': YELLOW,
                'u_y': YELLOW,
                '0': BLUE
            }
        )
        tex_3 = Tex('The function you are seeing on screen is ', r'$f(x, y)\;$', r'$=\;$', r'$\sin(x - y)$', '\\\\', 'Let us check that it satisfies our equation.').to_edge(UP)
        tex_3.set_color_by_tex_to_color_map(
            {
                "sin": RED,
                "f(x, y)": YELLOW
            }
        )
        self.camera.add_fixed_in_frame_mobjects(tex_1, tex_2, tex_3)
        self.play(Write(tex_1), run_time = 4)
        self.wait(3)
        self.play(FadeOut(tex_1), run_time = 2)
        self.play(FadeIn(tex_2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(tex_2), run_time = 1)
        self.play(FadeIn(tex_3), run_time = 2)
        self.wait(4)
        self.play(FadeOut(tex_3), run_time = 3)
        self.stop_ambient_camera_rotation()
        self.move_camera(phi=90*DEGREES, theta = 45*DEGREES, run_time = 2)
        surface.set_style(fill_opacity=1, stroke_color=BLACK, stroke_width=0)
        self.wait(2)
        
class test(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 4],
            y_range=[-4, 4, 4],
            z_range=[-2, 2, 2],
            x_length=8,
            y_length=8,
            z_length=4
        )
        axes.set_color(BLUE)

        # Define the solution surface
        surface = Surface(
            lambda u, v: np.array([u, v, 2*np.sin((u - v))*0.5]),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(20, 20),
        )
        surface.set_color(RED)
        surface.set_style(fill_opacity=1, stroke_color=BLACK, stroke_width=3)
        self.set_camera_orientation(phi=60 * DEGREES, theta=0 * DEGREES)
        self.begin_ambient_camera_rotation(rate=1*DEGREES)
        self.wait(1)
        self.play(Create(VGroup(axes, surface)), run_time = 3)
        self.wait(1)
        tex_1 = Tex('Sometimes when dealing with a problem, ', 'it helps to analyze the', '\\\\', ' properties ', 'of the question itself').to_edge(UP)
        tex_2 = Tex(r"Let's start with the original equation: ", "\\\\", r'$u_x\;$', r'$+\;$', r'$u_y\;$', r'$=\;$', '$0$').to_edge(UP)
        tex_2.set_color_by_tex_to_color_map(
            {
                'u_x': YELLOW,
                'u_y': YELLOW,
                '0': BLUE
            }
        )
        tex_3 = Tex('The function you are seeing on screen is ', r'$f(x, y)\;$', r'$=\;$', r'$\sin(x - y)$', '\\\\', 'Let us check that it satisfies our equation.').to_edge(UP)
        tex_3.set_color_by_tex_to_color_map(
            {
                "sin": RED,
                "f(x, y)": YELLOW
            }
        )
        tex_4 = Tex(r'$\cos(x - y)\;$', r'$+\;$', r'$-\cos(x - y)\;$', r'$=\;$', '$0$').to_edge(UP)
        tex_4.set_color_by_tex_to_color_map(
            {
                'cos': YELLOW,
                '0': BLUE
            }
        )
        tex_5 = Tex(r'$0\;$', r'$=\;$', r'$0$').to_edge(UP)
        tex_5.set_color_by_tex_to_color_map(
            {
                '0': BLUE
            }
        )
        self.camera.add_fixed_in_frame_mobjects(tex_1, tex_2, tex_3, tex_4, tex_5)
        self.play(Write(tex_1), run_time = 4)
        self.wait(3)
        self.play(FadeOut(tex_1), run_time = 2)
        self.play(Write(tex_2), run_time = 2)
        self.wait(2)
        self.play(FadeOut(tex_2), run_time = 1)
        self.play(Write(tex_3), run_time = 2)
        self.wait(4)
        self.play(FadeOut(tex_3), run_time = 3)
        self.play(Write(tex_2), run_time = 2)
        self.wait(1)
        self.play(ReplacementTransform(tex_2, tex_4), run_time = 2)
        self.wait(2)
        self.play(ReplacementTransform(tex_4, tex_5), run_time = 2)
        