from manim import *
from math import *
import numpy as np
# manim -pql main.py CreateCircle
class CreateCircle(Scene):
    def construct(self):
        circle = Circle()
        circle.set_fill(PINK, opacity=0.5)
        self.play(Create(circle))


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, UP, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(Transform(square, circle))  # transform the square into a circle
        self.play(
            square.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()


class TwoTransforms(Scene):
    def transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(Transform(a, b))
        self.play(Transform(a, c))
        self.play(FadeOut(a))

    def replacement_transform(self):
        a = Circle()
        b = Square()
        c = Triangle()
        self.play(ReplacementTransform(a, b))
        self.play(ReplacementTransform(b, c))
        self.play(FadeOut(c))

    def construct(self):
        self.transform()
        self.wait(0.5)  # wait for 0.5 seconds
        self.replacement_transform()


class TransformCycle(Scene):
    def construct(self):
        a = Circle()
        t1 = Square()
        t2 = Triangle()
        self.add(a)
        self.wait()
        for t in [t1,t2]:
            self.play(Transform(a,t))


def fourier_sin(n, x):
    f = 0
    for i in range(1, n+1):
        f += 2*(-1)**(i+1)/i * np.sin(i*x)
    return f


def fourier_cos(n, x):
    f = np.pi/2
    for i in range(1, n+1):
        f += 2*((-1)**i-1)/(i**2*np.pi)*np.cos(i*x)
    return f


class sinseries(Scene):
    def construct(self):
        # Create Axes with specified x and y ranges and equal axis lengths
        ax = Axes(
            x_range = [-3*PI, 3*PI, PI/2],
            y_range = [-PI, PI, PI/2],
            tips = False,
            axis_config={"include_numbers": False},
            x_length = 9,
            y_length = 3
        )
        ax.x_axis.set_color(RED)
        ax.y_axis.set_color(RED)
        base_graph = ax.plot(lambda x: x, x_range=[0, np.pi], color = BLUE, use_smoothing=False)
        sin_1 = ax.plot(lambda x: fourier_sin(1, x), x_range=[-3*np.pi, 3*np.pi], color = GREEN)
        self.play(Create(ax))
        self.wait(1)
        self.play(Create(base_graph))
        self.wait(1)
        self.play(Create(sin_1))
        temp = sin_1
        for i in range(1, 25):
            graph = ax.plot(lambda x: fourier_sin(i+1, x), x_range=[-3*np.pi, 3*np.pi], color = GREEN)
            self.play(ReplacementTransform(temp, graph), run_time = float(0.25))
            temp = graph
        

class cosineseries(Scene):
    def construct(self):
        # Create Axes with specified x and y ranges and equal axis lengths
        ax = Axes(
            x_range = [-3*PI, 3*PI, PI/2],
            y_range = [-3*PI, 3*PI, PI/2],
            tips = False,
            axis_config={"include_numbers": False},
            x_length = 8,
            y_length = 8
        )
        ax.x_axis.set_color(RED)
        ax.y_axis.set_color(RED)
        base_graph = ax.plot(lambda x: x, x_range=[0, np.pi], color = BLUE, use_smoothing=False)
        cos_1 = ax.plot(lambda x: fourier_cos(0, x), x_range=[-3*np.pi, 3*np.pi], color = GREEN)
        self.play(Create(ax))
        self.wait(1)
        self.play(Create(base_graph))
        self.wait(1)
        self.play(Create(cos_1))
        temp = cos_1
        for i in range(1, 25):
            graph = ax.plot(lambda x: fourier_cos(i, x), x_range=[-3*np.pi, 3*np.pi], color = GREEN)
            self.play(ReplacementTransform(temp, graph), run_time = float(0.2))
            temp = graph


class bolzano(MovingCameraScene):
    def construct(self):
        ax = Axes(
            x_range = [-1, 1, 0.5],
            y_range = [-1, 1, 0.5],
            tips = False,
            axis_config={"include_numbers": False},
            x_length = 6,
            y_length = 6
        )
        ax.x_axis.set_color(BLUE_C)
        ax.y_axis.set_color(BLUE_C)
        # Generate 100 red dots within the axes' range
        num_dots = 100000
        points = [
            ax.coords_to_point(
                np.random.uniform(-1, 1),  # Random x-coordinate in range [-1, 1]
                np.random.uniform(-1, 1)   # Random y-coordinate in range [-1, 1]
            )
            for _ in range(num_dots)
        ]
        dots = VGroup(*[Dot(point, color=RED, radius=0.005) for point in points])
        outer_box = Rectangle(
            width=6,
            height=6,
            color=RED
        ).move_to(ax.get_center())
        # Add Axes and outer box to the scene
        self.play(Create(ax), run_time=1)
        # Animate the creation of all dots quickly
        self.play(FadeIn(dots), run_time=2)
        self.wait(1)
        self.wait(1)
        self.play(Create(outer_box))
        center = [0, 0]
        for z in range(1,5):
            box1 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(-1/(2**z) + center[0], 1/(2**z) + center[1]))
            box2 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(1/(2**z) + center[0], 1/(2**z) + center[1]))
            box3 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(-1/(2**z) + center[0], -1/(2**z) + center[1]))
            box4 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(1/(2**z) + center[0], -1/(2**z) + center[1]))
            self.play(Create(box1))
            self.play(Create(box2))
            self.play(Create(box3))
            self.play(Create(box4))
            self.wait(1)
            s = [box1, box2, box3, box4]
            t = np.random.choice([0, 1, 2, 3])
            self.play(
                self.camera.frame.animate.move_to(s[t].get_center()).set(width=box1.width * 1.8),  # Use *1.5 to provide a margin
                run_time = 2
            )
            centers = [[-1/(2**z) + center[0], 1/(2**z) + center[1]], [1/(2**z) + center[0], 1/(2**z) + center[1]], [-1/(2**z) + center[0], -1/(2**z) + center[1]], [1/(2**z) + center[0], -1/(2**z) + center[1]]]
            center = [centers[t][0], centers[t][1]]
        self.wait(2)


class bolzano2(Scene): # manim -pqk --renderer=OpenGL main.py bolzano2 --disable_caching --write_to_movie
    def construct(self):
        ax = Axes(
            x_range = [-1, 1, 0.5],
            y_range = [-1, 1, 0.5],
            tips = False,
            axis_config={"include_numbers": False},
            x_length = 6,
            y_length = 6
        )
        ax.x_axis.set_color(BLUE_C)
        ax.y_axis.set_color(BLUE_C)
        # Generate 100 red dots within the axes' range
        # Number of dots
        num_dots = 1000000

        # Generate random coordinates in [-1, 1] x [-1, 1]
        x_coords = np.random.uniform(-1, 1, num_dots)
        y_coords = np.random.uniform(-1, 1, num_dots)

        # Convert to Manim points
        points = [ax.coords_to_point(x, y) for x, y in zip(x_coords, y_coords)]

        # Group all dots
        dots = VGroup(*[Dot(point, radius=0.005, color=RED) for point in points[:20000]])
        outer_box = Rectangle(
            width=6,
            height=6,
            color=RED
        ).move_to(ax.get_center())
        # Add Axes and outer box to the scene
        self.play(Create(ax), run_time=1)
        # Animate the creation of all dots quickly
        self.play(FadeIn(dots), run_time=2)
        self.wait(1)
        self.play(Create(outer_box))
        center = [0, 0]
        for z in range(1,6):
            box1 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(-1/(2**z) + center[0], 1/(2**z) + center[1]))
            box2 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(1/(2**z) + center[0], 1/(2**z) + center[1]))
            box3 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(-1/(2**z) + center[0], -1/(2**z) + center[1]))
            box4 = Rectangle(
                width = 6/(2**z),
                height = 6/(2**z),
                color = GREEN,
                stroke_width = 2**(3-z)
            ).move_to(ax.coords_to_point(1/(2**z) + center[0], -1/(2**z) + center[1]))
            self.play(Create(box1))
            self.play(Create(box2))
            self.play(Create(box3))
            self.play(Create(box4))
            self.wait(1)
            s = [box1, box2, box3, box4]
            t = np.random.choice([0, 1, 2, 3])
            self.play(
                self.camera.animate.move_to(s[t].get_center()).set(width=box1.width * 1.8),  # Use *1.5 to provide a margin
                run_time = 2
            )
            centers = [[-1/(2**z) + center[0], 1/(2**z) + center[1]], [1/(2**z) + center[0], 1/(2**z) + center[1]], [-1/(2**z) + center[0], -1/(2**z) + center[1]], [1/(2**z) + center[0], -1/(2**z) + center[1]]]
            center = [centers[t][0], centers[t][1]]
        self.wait(2)


def fourier_sin_cos(n, x):
    f = 0
    for i in range(1, n + 1):  # Sum up to n terms
        f += (8 * i) / (np.pi * (4 * i**2 - 1)) * np.sin(2 * i * x)
    return f


class CosineApproximation(Scene):
    def construct(self):
        # Create axes with the range from -3pi to 3pi for the cosine graph
        ax = Axes(
            x_range=[-3*PI, 3*PI, 1],
            y_range=[-2, 2, 1],
            tips=False,
            axis_config={"include_numbers": False},
            x_length=12,
            y_length=4
        )
        self.add(ax)

        # Create the original cosine graph on the range [-3π, 3π]
        cos_graph = ax.plot(lambda x: np.cos(x), x_range=[-3*PI, 3*PI], color=BLUE, use_smoothing=True)

        # Create the label for the cosine graph
        cos_label = MathTex("f(x) = \\cos(x)").next_to(ax, UP, buff=0.3)

        # Animate the cosine graph creation
        self.play(Create(cos_graph), Write(cos_label))

        sin_graph = ax.plot(lambda x: fourier_sin_cos(1, x), x_range=[-3*PI, 3*PI], color=YELLOW)
        sin_label = MathTex(r"f(x) \approx \sum_{n=1}^{1} \frac{8n}{\pi(4n^2-1)} \sin(2nx)").next_to(ax, UP, buff=0.3)

        # Animate the first Fourier series term
        self.play(Create(sin_graph), ReplacementTransform(cos_label, sin_label), run_time = 3)
        
        temp = sin_graph
        old_label = sin_label
        for i in range(2, 200):  # Adding terms one by one up to the 10th term
            new_graph = ax.plot(lambda x: fourier_sin_cos(i, x), x_range=[-3*PI, 3*PI], color=YELLOW)
            new_label = MathTex(
                f"f(x) \\approx \\sum_{{n=1}}^{{{i}}} \\frac{{8n}}{{\\pi(4n^2-1)}} \\sin(2nx)"
            ).next_to(ax, UP, buff=0.3)

            # Smooth transition from the previous graph to the new one
            self.play(ReplacementTransform(temp, new_graph), ReplacementTransform(old_label, new_label), run_time=(1/(1.1+floor(log10(i)))**4))

            # Update the temp variable for the next iteration
            temp = new_graph
            old_label = new_label


class CauchyText(MovingCameraScene):
    def construct(self):
        # Define the full sentence with Text and MathTex combined
        original_position = self.camera.frame.get_center()
        definition = Tex(
            'A sequence ', r'$(x_n)$', ' is a Cauchy sequence if for every ', r'$\varepsilon > 0$', '\\\\',  # Line break
            'there exists an ', r'$N$', r'$\in\:$',  r'$\mathbb{N}$', ' such that for all integers ', r'$m, n\:$', r'$ \geq$', '$N$', '\\\\',  # Line break
            r'$|$', '$x_n$', ' $-$ ', '$x_m$', r'$|$', r' $<\varepsilon$.'
        )
        
        # Set color for specific parts
        definition.set_color_by_tex("x_n", YELLOW)         # x_n in the sequence and inequality
        definition.set_color_by_tex("x_m", YELLOW)          # x_m in the inequality
        definition.set_color_by_tex("m, n", YELLOW)
        definition.set_color_by_tex("N", BLUE)             # N for natural numbers
        definition.set_color_by_tex(r"\varepsilon", RED)   # Epsilon
        definition.set_color_by_tex("-", WHITE)            # Optional: color the minus sign
        definition.set_color_by_tex("|", DARK_BLUE)           # Optional: color the absolute value symbols
        definition.set_color_by_tex(r"\mathbb{N}", GREEN)
        ax = NumberLine(
            x_range = [0, 1, 1/16],
            length = 10,
            include_numbers = False
        )
        label_edges = [
            Dot(ax.n2p(0), color=RED).to_edge(DOWN).shift(UP),
            Dot(ax.n2p(1), color=RED).to_edge(DOWN).shift(UP)
        ]
        label_edges_text = [
            MathTex("0").next_to(label_edges[0], DOWN),
            MathTex("1").next_to(label_edges[1], DOWN),
        ]
        ax.to_edge(DOWN).shift(UP)
        sequence_intro_text = Tex(
            'Consider the sequence ', r'$($','$a_n$', r'$\; \mid \;$', r'$a_n\;$', r'$=$', r'$1 - 2^{-n}$', r'$, \; n \in\;$', r'$\mathbb{N}$',r'$)$' 
        )
        sequence_intro_text.set_color_by_tex("a_n", YELLOW)
        sequence_intro_text.set_color_by_tex(r"1 - 2^{-n}", RED) 
        sequence_intro_text.set_color_by_tex(r"\mid", DARK_BLUE)
        sequence_intro_text.set_color_by_tex(r"\mathbb{N}", GREEN)
        sequence_intro_text.to_edge(UP)
        points = []
        for i in range(1, 30):
            points += Dot(ax.n2p(1 - 2**(-i)), color = YELLOW, radius = 0.15*1.3**(-i))
        # Animate the definition
        self.play(Write(definition), run_time=6)
        self.wait(1.5)
        self.play(Transform(definition, VGroup(ax, label_edges_text[0], label_edges_text[1])), run_time = 2)
        self.play(Write(sequence_intro_text), run_time = 3)
        self.wait(0.5)
        self.play(*[Create(point) for point in points])
        self.wait(0.25)  # Wait for a while before finishing the scene
        self.play(self.camera.frame.animate.move_to(points[1].get_center()).set(width=6), FadeOut(VGroup(label_edges[0], label_edges[1])), run_time = 2)
        sequence_note_text = Tex(
            'Notice that the distance between each consecutive point decreases', '\\\\', 'by a factor of', ' 2 ', 'as the sequence continues'
        ).next_to(points[1], UP, buff = 0.2)
        sequence_note_text.set_color_by_tex("2", BLUE).scale(0.4)
        self.play(Write(sequence_note_text), run_time = 2)
        self.wait(1.5)
        temp_line = []
        for i in range(0, 5):
            line = Line(points[i].get_center(), points[i+1].get_center(), color = YELLOW)
            distance = 2**(-i) - 2**(-i-1)
            print(distance)
            distance_text = Tex(f"{distance:.4f}", color = BLUE)
            distance_text.next_to(line, DOWN, buff = 0.0).scale(0.5/(i+1))
            if i == 0:
                self.play(Create(line), Write(distance_text), run_time = 2)
                temp_line.append(line)
                temp_line.append(distance_text)
            else:
                self.play(Transform(temp_line[0], line), Transform(temp_line[1], distance_text), FadeOut(points[i - 1]), run_time = 1.5)
        self.wait(1)
        cauchy_question = Tex('Is this sequence a', ' Cauchy',' sequence? ',  'Why', '?')
        cauchy_question.set_color_by_tex("Cauchy", YELLOW)
        cauchy_question.set_color_by_tex("Why", RED).next_to(points[1], UP, buff = 0.2).scale(0.5)
        self.play(Transform(sequence_note_text, cauchy_question), FadeOut(temp_line[1]), run_time = 2)
        self.wait(4)
        # self.play(
        #     *[FadeOut(mob)for mob in self.mobjects]
        #     # All mobjects in the screen are saved in self.mobjects
        # , run_time = 1)
        # self.wait(0.1)
        # self.play(self.camera.frame.animate.move_to(original_position).set(width = 10), run_time = 0.1)
        

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


class characteristicsTests(ThreeDScene):
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
        tex_4 = Tex(r'$\cos(x - y)\;$', r'$+\;$', r'$-\cos(x - y)\;$', r'$=\;$', '$0$').to_edge(UP)
        tex_4.set_color_by_tex_to_color_map(
            {
                'cos': YELLOW,
                '0': BLUE
            }
        )
        tex_5 = Tex(r'$0$', r'$=$', r'$0$').to_edge(UP)
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
        
        
        
        
        # self.stop_ambient_camera_rotation()
        # self.move_camera(phi=90*DEGREES, theta = 225*DEGREES, run_time = 4)
        # self.wait(1)
        # axes_2d = Axes(
        #     x_range=[-4, 4, 4],
        #     y_range=[-2, 2, 2],
        #     axis_config={"color": WHITE}
        # )

        # sine_curve = axes_2d.plot(lambda x: (1/np.sqrt(2)+0.05)*np.sin(1.93*x), x_range=[-PI/1.93, PI/1.93], color=RED, stroke_width = 9)
        # self.camera.add_fixed_in_frame_mobjects(axes_2d, sine_curve)e
        # self.play(Create(sine_curve), run_time = 3)
        # self.wait(1)
        # self.play(FadeOut(sine_curve), run_time = 1)
        # self.begin_ambient_camera_rotation(rate = 3*DEGREES)
        # self.move_camera(phi=60 * DEGREES, theta=225 * DEGREES, run_time = 3)


class Napkin(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes(
            x_range=[-4, 4, 4],
            y_range=[-4, 4, 4],
            z_range=[-4, 4, 4],
            x_length=8,
            y_length=8,
            z_length=8,
            
        )
        axes.set_color(BLUE)
        self.add(axes)
        # Create a sphere
        sphere = Sphere(radius=2, resolution=32)
        sphere.set_fill_by_checkerboard(BLACK, WHITE)
        
        # Add objects to the scene
        self.set_camera_orientation(phi=65 * DEGREES, theta=0 * DEGREES)
        self.begin_ambient_camera_rotation(rate = 10*DEGREES)
        self.play(Create(sphere), run_time = 6)
        
        # Set camera position for 3D effect

        
        # Render the scene
        self.wait(20)

