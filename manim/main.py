# generar fibonacci
def fibonacci_gen(num):
    fn = [0, 1]
    while fn[-1] <= num:
        fn.append(fn[-1] + fn[-2])
    if fn[-1] > num:
        fn.pop()
    # for valor in fn:
    #     print(valor)
    return fn

# Ejemplo de uso:
numlimit = int(input("ingrese el numero al que quiera ir hasta foibonacci: "))  # Puedes cambiar este valor según desees
fib = fibonacci_gen(numlimit) #
print(f"Secuencia de Fibonacci hasta el número {numlimit}:")
print(fib)