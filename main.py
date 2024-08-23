num = int(input("Ingrese un numero: "))

if num % 2 == 0:
    print("El numero es par")
else:
    print("El numero es impar")
    
cant = int(input("Cuantos datos va a ingresar: "))

numeros = []

for i in range(0, cant):
    numeros.append(int(input("Digite un numero: ")))

suma = sum(numeros)

print(f"La suma total de los numeros es de: {suma}")

matriz = []

for fila in range(3):
    filas = []
    for columna in range(3):
        filas.append(int(input(f"Digite el valor de la fila {fila+1}: ")))
    matriz.append(filas)

for filas in matriz:
    print(filas)