from manim import *

class AutoArrangeSquares(Scene):
    def construct(self):
        # Llama a la función para crear y organizar cuadros
        self.arrange_squares(5, side_length=1, gap=0.5)
    
    def arrange_squares(self, num_squares, side_length=1, gap=0.5):
        squares = VGroup()  # Agrupa todos los cuadros

        for i in range(num_squares):
            square = Square(side_length=side_length)
            # Coloca el cuadro en su posición adecuada
            square.shift(RIGHT * (side_length + gap) * i)
            squares.add(square)
        
        # Añade todos los cuadros a la escena
        self.play(Create(squares))
        self.wait(2)
