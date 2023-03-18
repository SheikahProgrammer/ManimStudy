from manim import *

class Damn(Scene):
    def construct(self):
        name = Text("Avinash")
        tri = Triangle().scale(0.6)
        self.play(Create(tri), runtime=3)
        self.play(Write(name))
        self.wait()
 
