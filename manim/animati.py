from manim import *

class TresCuadrados(Scene):
    def construct(self):
        # Crear los primeros dos cuadrados con tamaño 1
        cuadro1 = Square(side_length=1).set_color(BLUE)
        cuadro2 = Square(side_length=1).set_color(RED)

        # Posicionar el segundo cuadrado debajo del primero
        cuadro1.next_to(cuadro2, UP)

        # Crear el tercer cuadrado con tamaño 2
        cuadro3 = Square(side_length=2).set_color(GREEN)

        # Posicionar el tercer cuadrado a la derecha del cuadro1
        cuadro3.next_to(cuadro1, RIGHT, buff=1)

        # Añadir los cuadrados a la escena
        self.play(Create(cuadro1), Create(cuadro2), Create(cuadro3))
        self.wait(2)

# Para renderizar, usa el siguiente comando en la terminal:
# manim -pql nombre_del_archivo.py TresCuadrados
