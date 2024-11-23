from manim import *
import numpy as np

class squareToCircle(Scene):
    def construct(self):
        square = Square().set_fill(color=GREEN_B, opacity=0.5).set_stroke(color=GREEN_B)
        circle = Circle().set_fill(color=RED, opacity=0.5).set_stroke(color=RED)
        
        self.play(FadeIn(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)
        self.play(FadeOut(circle))
        self.wait(1)

class helloWorld(Scene):
    def construct(self):
        text = Text('Hello world!', font="arial").scale(3)
        
        self.play(FadeIn(text))
        self.wait(1)
        self.play(FadeOut(text))
        self.wait(1)

class SineWaveToText(Scene):
    def construct(self):
        # Sine wave parameters
        amplitude = 1
        frequency = 1
        wave_speed = 1

        # Create a sine wave using ParametricFunction
        sine_wave = ParametricFunction(
            lambda t: np.array([t, amplitude * np.sin(2 * PI * frequency * t), 0]),
            t_range=[-3.5, 3.5, 0.01],
            color=BLUE
        ).shift(UP)  # Shift wave upwards
        
        # Updater function to create the "moving wave" effect
        def update_wave(mob, dt):
            mob.become(
                ParametricFunction(
                    lambda t: np.array([t, amplitude * np.sin(2 * PI * frequency * (t - wave_speed * self.time)), 0]),
                    t_range=[-3.5, 3.5, 0.01],
                    color=BLUE
                ).shift(UP)
            )
            self.time += dt
        
        # Initialize time tracker
        self.time = 0
        sine_wave.add_updater(update_wave)
        
        # Create the text object
        text = Text("Hello, World!", font="Arial", font_size=72).move_to(ORIGIN)
        
        # Add the sine wave and let it oscillate for a few seconds
        self.add(sine_wave)
        self.wait(3)  # Oscillating sine wave
        
        # Stop the oscillation and morph into the text
        sine_wave.remove_updater(update_wave)
        self.play(Transform(sine_wave, text), run_time=3)
        
        # Hold the final text for a moment
        self.wait(2)

class CircleAndItsRadius(Scene):
    def construct(self):
        circle = Circle(radius=2.0, color=WHITE)
        dot = Dot(point=ORIGIN, color=BLUE, radius=0.05)
        movingDot = Dot(point=[2, 0, 0], color = YELLOW)
        line = always_redraw(lambda: Line(start=ORIGIN, end=movingDot.get_center(), color = GREEN_B))

        self.play(FadeIn(circle))
        self.play(Create(dot))
        self.play(Create(movingDot))
        self.play(Create(line))

        self.play(MoveAlongPath(movingDot, circle), run_time=2, rate_func=linear)

        self.play(FadeOut(movingDot))

        self.wait(3)

# class Draft(Scene):
    # def construct(self):
        