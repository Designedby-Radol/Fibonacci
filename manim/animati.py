from manim import *

class ArcExample(Scene):
    def construct(self):
      #cuadr 1 //////////////////////////////////////////////////////////////////
        sre1 = Square().scale(1)
        arc1 = Arc(
        angle=PI/2).rotate(PI, about_point=ORIGIN).shift(
        sre1.get_center()+0.5).scale(2)
        
        py_1= VGroup(sre1, arc1)
        py_1.shift(DOWN,LEFT*2)
        self.add(py_1)
      #cuadr 2 //////////////////////////////////////////////////////////////////
        sre11 = Square().scale(1)
        arc11 = Arc(
        radius=1, angle=PI/2).rotate(
        PI/2, about_point=ORIGIN).scale(2).shift(
        sre11.get_center()+0.5,DOWN)
        
        py_11= VGroup(sre11, arc11)
        py_11.shift(UP,LEFT*2)
        self.add(py_11)
      #cuadr 3 //////////////////////////////////////////////////////////////////
        sre2 = Square().scale(2)
        arc2 =Arc(angle=PI/2).shift(sre2.get_center()-0.5).scale(4)
        self.add(NumberPlane())
        py_2= VGroup(sre2, arc2)
        py_2.shift(RIGHT)
        self.add(py_2)
        
# don't remove below command for run button to work
