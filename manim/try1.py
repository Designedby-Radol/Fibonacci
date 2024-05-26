# generar fibonacci
# def fibonacci_gen(num):
#     fn = [0, 1]
#     while fn[-1] <= num:
#         fn.append(fn[-1] + fn[-2])
#     if fn[-1] > num:
#         fn.pop()
#     # for valor in fn:
#     #     print(valor)
#     return fn

# # Ejemplo de uso:
# numlimit = int(input("ingrese el numero al que quiera ir hasta foibonacci: "))  # Puedes cambiar este valor según desees
# fib = fibonacci_gen(numlimit) #
# print(f"Secuencia de Fibonacci hasta el número {numlimit}:")
# print(fib)


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 30)
persona1.saludar()  # Salida: Hola, mi nombre es Ana y tengo 30 años.

def saludar(nombre):
    print(f"Hola, {nombre}!")

saludar("Carlos")  # Salida: Hola, Carlos!

class Animal:
    def __init__(self, nombre, especie):
        self.nombre = nombre
        self.especie = especie

    def hacer_sonido(self):
        print(f"{self.nombre} hace un sonido.")

perro = Animal("Fido", "Perro")
perro.hacer_sonido()  # Salida: Fido hace un sonido.

