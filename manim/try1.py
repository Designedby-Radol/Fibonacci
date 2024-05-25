# def fibonacci_hasta(num):
#     fib_sequence = [0, 1]  
#     while fib_sequence[-1] <= num:
#         fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])  
#     # Eliminar el último número que excede num
#     fib_sequence.pop()
#     return fib_sequence  
#     # Ejemplo de uso:
#     numero_limite = 50    
#     # Cambia este valor según desees
#     fib = fibonacci_hasta(numero_limite)
#     print(f"Secuencia de Fibonacci hasta el número{numero_limite}:")
#     print(fib)

# generar fibonacci
class fibonacci_gen:
    num = int (input ("ingrese el numero de veces que quiere imprimir fiboinacci"))
    fn = [0, 1]
    i = 0
    while i <= num:
        fn(fn[-1]+fn[-2])
        i= i + i

    for valor in matriz_lineal:
        print(valor)
    fn.pop()
    fn0 = fibonacci_gen(i)
    


# class crear_matriz():
#     matriz_lineal = [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     # Imprimir los valores de la matriz usando un bucle
#     for valor in matriz_lineal:
#         print(valor)
