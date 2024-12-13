from manim import *
import numpy as np
from scipy import integrate
# import time # Uncomment this line if you want to use the time.sleep function

class FourierSeries(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[0, 1.5, 0.01],
            y_range=[0, 1.5, 0.01],
            x_length=6,
            y_length=6,
            axis_config={"include_ticks": False}
        )
        self.add(axes)

        # Set this function to whatever you want - as long as its bounded and continuous on (0, 1)
        def f(x):
            return np.sqrt(1 - x**2)
        
        def calculate_coeffients(n_terms):
            coefficients = np.zeros(n_terms)
    
            # First, we calculate the A_0 coefficient
            coefficients[0] = 2 * integrate.quad(f, 0, 1)[0]
            
            # Next, we calculate the A_n coefficients
            for n in range(1, n_terms):
                integrand = lambda x: f(x) * np.cos(n * np.pi * x)
                coefficients[n] = 2 * integrate.quad(integrand, 0, 1)[0]

            return coefficients
        
        def fourier_approximation(x, n_terms, coefficients):
            result = coefficients[0] / 2  # First term should be a0/2
            
            for n in range(1, n_terms):
                result += coefficients[n] * np.cos(n * np.pi * x)
            return result
        
        # Calculate all coefficients once
        n_terms = 60 # set this number to whatever you want within reason
        all_coefficients = calculate_coeffients(n_terms)
        
        # Plot original function
        original = axes.plot(f, x_range=[0, 1], color=BLUE)
        
        # Plot initial Fourier approximation
        approximation = axes.plot(
            lambda x: fourier_approximation(x, 1, all_coefficients),
            x_range=[0, 1],
            color=RED
        )

        self.play(Create(original))
        self.wait(1)
        self.play(Create(approximation), run_time=1)

        # Animate adding terms
        for n in range(2, n_terms + 1):
            new_approximation = axes.plot(
                lambda x: fourier_approximation(x, n, all_coefficients),
                x_range=[0, 1],
                color=RED
            )
            self.play(Transform(approximation, new_approximation), run_time=0.02)