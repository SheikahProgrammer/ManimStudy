from manimlib.scene.scene import *     
from manimlib.mobject.geometry import *
from manimlib.animation.creation import *
from manimlib.constants import *
from manimlib import *

class Testing(Scene):
    def construct(self):
        name = Text("Avinash")
        sq = Square(side_length = 5)
        tri = Triangle().scale(0.6)
        self.play(ShowCreation(sq), runtime=3)
        self.wait()