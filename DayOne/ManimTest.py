from manimlib.scene.scene import Scene
from manimlib.mobject.geometry import Square
from manimlib.animation.creation import *
from manimlib.constants import *

class Pith(Scene):
    def construct(self):

        sq = Square(
            side_length = 5, stroke_color = GREEN, fill_color= BLUE, fill_opacity=0.75
            )
        self.play(ShowCreation(sq), runtime=3)
        self.wait()