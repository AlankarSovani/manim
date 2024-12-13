from manim import *
from math import *
import numpy as np


class CauchyText(MovingCameraScene):
    def construct(self):
        # Define the full sentence with Text and MathTex combined
        original_position = self.camera.frame.get_center()
        original_width = self.camera.frame_width
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
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        , run_time = 1)
        self.wait(0.1)
        self.play(self.camera.frame.animate.move_to(original_position).set(width = original_width), run_time = 0.1)
        first_question_ans = Tex('Without going into the detail, ', '\\\\', 'we can see that every element becomes', ' closer ', 'to the next one ', '\\\\', 'as the index ',  'increases.').scale(0.8)
        first_question_ans.set_color_by_tex_to_color_map(
            {
            "closer": RED,
            "increases": BLUE
            }
        )
        self.play(Write(first_question_ans), run_time = 7)
        first_question_ans_2 = Tex('Therefore, this sequence is ', 'Cauchy').scale(0.9).next_to(first_question_ans, DOWN)
        first_question_ans_2.set_color_by_tex_to_color_map(
            {
                "Cauchy": YELLOW
            }
        )
        self.play(Write(first_question_ans_2), run_time = 3)
        big_idea_1 = Tex('The Big Idea: ').scale(1.3)
        big_idea_2 = Tex(r'A sequence is Cauchy', r'$\iff$', 'The sequence converges to a real number').next_to(big_idea_1, DOWN).scale(0.6)
        self.play(ReplacementTransform(VGroup(first_question_ans, first_question_ans_2), big_idea_1), run_time = 4)
        self.play(Write(big_idea_2), run_time = 5)
        self.wait(6) # talking time
        self.play(FadeOut(VGroup(big_idea_1, big_idea_2)), run_time = 3)
        number_line = NumberLine(
            x_range = [0, 4, 1],
            length = 10,
            include_numbers = True,
            label_direction = DOWN
        ).to_edge(DOWN)
        pi_label = MathTex(r"\pi").next_to(number_line.n2p(3.14159), UP).set_color(YELLOW)
        seq1_points = [number_line.n2p(3 + 1 / n) for n in range(1, 6)]
        seq2_points = [number_line.n2p(3.2 - 1 / (2 * n)) for n in range(1, 6)]
        seq1_dots = [Dot(point, color=BLUE) for point in seq1_points]
        seq2_dots = [Dot(point, color=RED) for point in seq2_points]
        self.play(Create(number_line), run_time = 3)
        text_rational = Tex(r"You might think that this fact isn't special, but it is.").to_edge(UP)
        text_rational_2 = Tex(r"For instance, not all rational sequences", "\\\\", "converge to a rational number.").next_to(text_rational, DOWN)
        self.play(Write(text_rational), run_time = 4)
        self.wait(1)
        self.play(Write(text_rational_2), run_time = 6)
        self.wait(1)
        self.play(FadeOut(VGroup(text_rational, text_rational_2)))
        self.wait(1)
        seq1_tex = Tex(r'$p_n$').scale(2)
        seq2_tex = Tex(r'$q_n$').next_to(seq1_tex, DOWN).scale(2)
        seq1_tex.set_color(BLUE)
        seq2_tex.set_color(RED)
        self.play(FadeIn(seq1_tex, seq2_tex))
        for dot in seq1_dots:
            self.play(Create(dot), run_time = 0.5)
            self.wait(0.5)
        self.wait(1)
        for dot in seq2_dots:
            self.play(Create(dot), run_time = 0.5)
            self.wait(0.5)
        self.wait(1)
        self.play(Create(pi_label))
        self.play(FadeOut(seq1_tex, seq2_tex))
        # Introduce the new definition of equivalence
        seq_tex = Tex('As you can see, both of these sequences converge to ', r'$\pi$.', '\\\\', 
                      'We will say that ', r'$a_n$', r'$\sim$', r'$b_n$', ' if ', r'$\lim (b_n - a_n) = 0$')
        seq_tex.set_color_by_tex_to_color_map(
            {
                "pi": YELLOW,
                "a_n": BLUE,
                "b_n": RED,
                "~": YELLOW,
                "lim": GREEN
            }
        )
        self.play(Write(seq_tex), run_time=6)
        self.wait(1)
        self.play(
            *[FadeOut(mob) for mob in self.mobjects], run_time=3
        )
        

class CauchyTextIntro(MovingCameraScene):
    def construct(self):
        # Initial camera settings
        original_position = self.camera.frame.get_center()
        original_width = self.camera.frame_width

        

class CauchyTextFinal(MovingCameraScene):
    def construct(self):
        # Define the full sentence with Text and MathTex combined
        original_position = self.camera.frame.get_center()
        original_width = self.camera.frame_width
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
        for i in range(1, 10):
            points += Dot(ax.n2p(1 - 2**(-i)), color = YELLOW, radius = 0.15*1.3**(-i))
        # Animate the definition
        self.play(Write(definition), run_time=6)
        self.wait(10)
        self.play(Transform(definition, VGroup(ax, label_edges_text[0], label_edges_text[1])), run_time = 2)
        self.play(Write(sequence_intro_text), run_time = 3)
        self.wait(2)
        for point in points:
            self.play(Create(point), run_time = 0.5)
        self.wait(0.25)  # Wait for a while before finishing the scene
        self.play(self.camera.frame.animate.move_to(points[1].get_center()).set(width=6), FadeOut(VGroup(label_edges[0], label_edges[1])), run_time = 5)
        sequence_note_text = Tex(
            'Notice that the distance between each consecutive point decreases', '\\\\', 'by a factor of', ' 2 ', 'as the sequence continues'
        ).next_to(points[1], UP, buff = 0.2)
        sequence_note_text.set_color_by_tex("2", BLUE).scale(0.4)
        self.play(Write(sequence_note_text), run_time = 4)
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
                self.play(Transform(temp_line[0], line), Transform(temp_line[1], distance_text), FadeOut(points[i - 1]), run_time = 2)
        self.wait(1)
        cauchy_question = Tex('Is this sequence a', ' Cauchy',' sequence? ',  'Why', '?')
        cauchy_question.set_color_by_tex("Cauchy", YELLOW)
        cauchy_question.set_color_by_tex("Why", RED).next_to(points[1], UP, buff = 0.2).scale(0.5)
        self.play(Transform(sequence_note_text, cauchy_question), FadeOut(temp_line[1]), run_time = 2)
        self.wait(4)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        , run_time = 3)
        self.wait(0.1)
        self.play(self.camera.frame.animate.move_to(original_position).set(width = original_width), run_time = 0.1)
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
        definition.to_edge(UP)
        self.play(Write(definition), run_time = 5)
        proof1_1 = Tex('From the triangle inequality: ', r'$|$', '$x_n$', ' $-$ ', '$x_m$', r'$|$', r'$\leq$', r'$|$', '$x_n - L$', r'$|$', ' $+$ ', r'$|$', '$x_m - L$', r'$|$', '\\\\',
                       'so if ', r'$|x_n - L|$', ' and ', r'$|x_m - L|$', ' are both less than ', r'$\frac{\varepsilon}{2}$', ',', '\\\\',
                       'our sequence is Cauchy. (L is the limit of our sequence)')
        proof1_1.set_color_by_tex_to_color_map({
            "x_n": YELLOW,
            "x_m": YELLOW,
            r"\varepsilon": RED,
            "-": WHITE
        })
        self.play(Write(proof1_1), run_time = 4)
        self.wait(3)
        self.play(FadeOut(proof1_1, definition))
        proof1_2 = Tex('We look for an ', r'$N$', r'$\in\:$',  r'$\mathbb{N}$', ' such that ', '\\\\', '$|x_N - L| <$', r'$\frac{\varepsilon}{2}$').to_edge(UP)
        proof1_2.set_color_by_tex_to_color_map({
            "x_n": YELLOW,
            "x_m": YELLOW,
            r"\varepsilon": RED,
            "|": DARK_BLUE,
            "-": WHITE
        })
        self.play(Write(proof1_2), run_time = 5)
        self.wait(3)
        proof1_3 = Tex(r'$1 + \frac{1}{2^N} - 1 < \frac{\varepsilon}{2}$').scale(2)
        proof1_4 = Tex(r'$2^{-N} < \frac{\varepsilon}{2}$').scale(2)
        proof1_5 = Tex(r'$N > \log_2(\frac{2}{\varepsilon})$').scale(2)
        self.play(Write(proof1_3), run_time = 3)
        self.wait(2)
        self.play(ReplacementTransform(proof1_3, proof1_4), run_time = 3)
        self.wait(2)
        self.play(ReplacementTransform(proof1_4, proof1_5), run_time = 3)
        self.wait(6)
        self.play(FadeOut(proof1_5, proof1_2))
        # Step 1: Introduce the sequence
        text_intro = Tex("Let's examine the sequence approximating ", r"$\sqrt{2}$.")
        text_intro.set_color_by_tex(r"$\sqrt{2}$", YELLOW)
        self.play(Write(text_intro), run_time=3)
        self.wait(3)

        # Step 2: Create the number line
        number_line = NumberLine(
            x_range=[1, 2, 0.1], length=10, include_numbers=True, include_tip=True
        ).shift(DOWN)
        self.play(Create(number_line), run_time=3)

        # Step 3: Plot the rational approximations
        points = [1, 1.5, 1.4, 1.4167]  # Approximate values: 1/1, 3/2, 7/5, 17/12
        dots = VGroup(*[Dot(number_line.n2p(x), color=BLUE) for x in points])
        self.play(FadeIn(dots), run_time=3)
        self.wait(1)

        text_cauchy = Tex(
            r"This sequence is Cauchy: $\left|a_n - a_m\right|$ can be made arbitrarily small."
        ).scale(0.8)
        self.play(ReplacementTransform(text_intro, text_cauchy), run_time=3)
        self.wait(2)

        # Step 5: Highlight the irrational limit
        sqrt2_dot = Dot(number_line.n2p(1.414213), color=YELLOW)
        sqrt2_label = MathTex(r"\sqrt{2}", color=YELLOW).scale(0.8).next_to(sqrt2_dot, DOWN)

        self.play(FadeIn(sqrt2_dot), run_time=2)
        self.wait(2)
        text_irrational = Tex(
            r"The sequence converges to ", r"$\sqrt{2}$", ", which is irrational!"
        )
        text_irrational.set_color_by_tex(r"$\sqrt{2}$", YELLOW)
        self.play(ReplacementTransform(text_cauchy, text_irrational), self.camera.frame.animate.move_to(original_position).set_width(original_width),  run_time=3)
        self.wait(3)
        # Step 6: Conclude
        conclusion = Tex("Thus, the sequence is Cauchy but does not converge in ", r"$\mathbb{Q}$.")
        conclusion.set_color_by_tex(r"$\mathbb{Q}$", GREEN)
        self.play(ReplacementTransform(text_irrational, conclusion), run_time=3)
        self.wait(3)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
            # All mobjects in the screen are saved in self.mobjects
        , run_time = 3)
        question_1 = Tex('This leads to the thought that there is a way to \\\\construct the set of real numbers from the set of rationals!')
        self.play(Write(question_1), run_time = 8)
        self.wait(5)
        self.play(FadeOut(question_1))
        
        
        # EQUIVALENCE
        equi_tex = Tex("Let $a_n$, $b_n$, be Cauchy sequences.\\\\Define ", r"$a_n\sim b_n \iff \lim(b_n - a_n) = 0$","\\\\", "Let us prove that ", r"$\sim$", " is an equivalence relation!")
        equi_tex.set_color_by_tex_to_color_map({r"$\sim$": YELLOW})
        self.play(Write(equi_tex), run_time=10)
        self.wait(3)

        # Reflexivity
        reflexive_tex = Tex("Reflexivity").to_edge(UP).scale(1.5)
        self.play(ReplacementTransform(equi_tex, reflexive_tex), run_time=3)
        reflexive_proof = Tex(
            "Take a Cauchy sequence ", r"$a_n$", ".", "\\\\",
            r"$\lim (a_n - a_n) = \lim (0) = 0$, ", "so ", r"$a_n \sim a_n$."
        )
        reflexive_proof.set_color_by_tex_to_color_map({r"$a_n$": BLUE})
        self.play(Write(reflexive_proof), run_time=8)
        self.wait(3)

        # Transition to symmetry
        symm_tex = Tex("Symmetry").to_edge(UP).scale(1.5)
        self.play(ReplacementTransform(VGroup(reflexive_tex, reflexive_proof), symm_tex), run_time=3)
        symm_proof = Tex(
            "Take sequences ", r"$a_n$", " and ", r"$b_n$", " such that ", r"$a_n \sim b_n$", ".\\\\",
            r"$\lim (b_n - a_n) = \lim (a_n - b_n)$ ", "by properties of limits,\\\\",
            "and since the left-hand side is zero,\\\\ the right-hand side is also zero.\\\\",
            "Thus, ", r"$b_n \sim a_n$."
        )
        symm_proof.set_color_by_tex_to_color_map({r"$a_n$": BLUE, r"$b_n$": ORANGE})
        self.play(Write(symm_proof), run_time=20)
        self.wait(3)

        # Transition to transitivity
        trans_tex = Tex("Transitivity").to_edge(UP).scale(1.5)
        self.play(ReplacementTransform(VGroup(symm_tex, symm_proof), trans_tex), run_time=3)
        trans_proof = Tex(
            "Take sequences ", r"$a_n$", ", ", r"$b_n$", ", and ", r"$c_n$", " such that\\\\",
            r"$a_n \sim b_n$ ", "and ", r"$b_n \sim c_n$", ".\\\\",
            r"$\lim (b_n - a_n) = 0$ and $\lim (c_n - b_n) = 0$.", '\\\\',
            "By the triangle inequality: ", r"$|c_n - a_n| \leq |c_n - b_n| + |b_n - a_n|$.",  '\\\\',
            "Taking the limit: ", r"$\lim |c_n - a_n| \leq \lim |c_n - b_n| + \lim |b_n - a_n|$.",  '\\\\',
            "Since both terms on the right-hand side are zero, \\\\", r"$\lim |c_n - a_n| = 0$.",  '\\\\',
            "Thus, ", r"$a_n \sim c_n$."
        )
        trans_proof.set_color_by_tex_to_color_map({
            r"$a_n$": BLUE, r"$b_n$": ORANGE, r"$c_n$": PURPLE
        })
        self.play(Write(trans_proof), run_time=30)
        self.wait(4)

        # Conclusion
        conclusion = Tex("Thus, ", r"$\sim$", " is an equivalence relation!")
        conclusion.set_color_by_tex_to_color_map({r"$\sim$": YELLOW})
        self.play(ReplacementTransform(VGroup(trans_tex, trans_proof), conclusion), run_time=3)
        self.wait(4)
        self.play(FadeOut(conclusion), run_time=2)
        # Step 1: Introduction
        completeness_1 = Tex(r"But what are the consequences of $\sim$'s properties?")
        self.play(Write(completeness_1), run_time=3)
        self.wait(3)
        self.play(FadeOut(completeness_1), run_time=2)

        # Step 2: Equivalence classes in terms of rational sequences
        completeness_2 = Tex(
            "Every representative of an equivalence class\\\\"
            "is a sequence of rational numbers."
        )
        self.play(Write(completeness_2), run_time=3)
        self.wait(4)
        self.play(FadeOut(completeness_2), run_time=2)

        # Step 3: Properties of \( \mathbb{Q} \) as a field
        completeness_3 = Tex(r"Properties of $\mathbb{Q}$ as a field:")
        completeness_3.to_edge(UP)
        self.play(Write(completeness_3), run_time=3)

        field_properties = VGroup(
            Tex(r"1. Closure under addition and multiplication:"),
            Tex(r"$a, b \in \mathbb{Q} \implies a + b, a \cdot b \in \mathbb{Q}$."),
            Tex(r"2. Associativity of addition and multiplication:"),
            Tex(r"$(a + b) + c = a + (b + c)$, $(a \cdot b) \cdot c = a \cdot (b \cdot c)$."),
            Tex(r"3. Commutativity of addition and multiplication:"),
            Tex(r"$a + b = b + a$, $a \cdot b = b \cdot a$."),
            Tex(r"4. Existence of additive and multiplicative identities:"),
            Tex(r"$a + 0 = a$, $a \cdot 1 = a$."),
            Tex(r"5. Existence of additive and multiplicative inverses:"),
            Tex(r"For all $a \neq 0$, $a \cdot a^{-1} = 1$."),
            Tex(r"6. Distributive property:"),
            Tex(r"$a \cdot (b + c) = a \cdot b + a \cdot c$."),
        ).arrange(DOWN, aligned_edge=LEFT).next_to(completeness_3, DOWN).scale(0.6)
        self.play(Write(field_properties, shift=UP), run_time=20)
        self.wait(3)

        # Step 4: Transition to the implications of \( \sim \)
        completeness_4 = Tex(
            r"However, $\mathbb{Q}$ is not complete as a field."
        )
        self.play(FadeOut(field_properties), ReplacementTransform(completeness_3, completeness_4), run_time=3)
        self.wait(2)

        completeness_5 = Tex(
            r"The equivalence relation $\sim$ allows us to construct a complete field", "\\\\",
            r"by defining limits of Cauchy sequences as equivalence classes.",
        )
        completeness_5.scale(0.8).to_edge(UP)
        self.play(ReplacementTransform(completeness_4, completeness_5), run_time=4)
        self.wait(3)

        # Step 5: Conclusion
        conclusion = Tex(
            r"We construct $\mathbb{R}$ as the set of all equivalence classes of $\sim$", "\\\\"
            r"Since the equivalence classes of $\sim$ inherit the properties of $\mathbb{Q}$,", "\\\\",
            r"$\mathbb{R}$ is an ordered field.",
        )
        conclusion.scale(0.9).to_edge(UP)
        self.play(ReplacementTransform(completeness_5, conclusion), run_time=4)
        self.wait(5)
        self.play(FadeOut(conclusion), run_time=2)
        final_r_complete = Tex(r'What makes $\mathbb{R}$ complete?', '\\\\'
                               'PAUSE VIDEO HERE').scale(1.3)
        self.play(Write(final_r_complete), run_time = 3)
        self.wait(3)
        