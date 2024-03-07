
import unidecode  # Importa la biblioteca unidecode para manipulación de texto

# Función para realizar operaciones aritméticas básicas con dos números
def operaciones(a,b):
    suma = a+b  # Calcula la suma de a y b
    resta = a-b  # Calcula la diferencia entre a y b
    multiplicacion= a*b  # Calcula el producto de a y b
    division = a/b  # Calcula la división de a entre b
    return suma, resta, multiplicacion, division  # Devuelve los resultados de las operaciones

n1 = int(input("ingrese el primer número: "))  # Obtiene el primer número del usuario
n2 = int(input("ingrese el segundo número: "))  # Obtiene el segundo número del usuario

# Realiza operaciones aritméticas en los números de entrada y almacena los resultados
suma, resta, multiplicacion, division = operaciones(n1, n2)

# Imprime los resultados de las operaciones aritméticas
print("La suma es:", suma)
print("La resta es:", resta)
print("La multiplicación es:", multiplicacion)
print("La división es:", division)

# Función para determinar si un número es par o impar
def par_impar(N):
    if N%2==0:
        return print(f"{N} es par")  # Imprime si N es par
    else:
        print(f"{N} es impar")  # Imprime si N es impar

n = int(input("ingrese un numero: "))  # Obtiene un número del usuario
print(par_impar(n))  # Verifica si el número es par o impar

# Función para calcular el área de un triángulo
def area(b,h):
    A=(b*h)*1/2  # Calcula el área del triángulo
    return A  # Devuelve el área

B= int(input("introduzca la base del triangulo: "))  # Obtiene la base del triángulo del usuario
H= int(input("introduzca la altura del triangulo: "))  # Obtiene la altura del triángulo del usuario
print(f"el area del triangulo es {area(B,H)}")  # Imprime el área del triángulo

# Función para calcular el factorial de un número
def factorial(N):
    fac=1
    if N==0:
        return 1  # Devuelve 1 si N es 0
    else:
        for i in range(1,N+1):
            fac *= i  # Calcula el factorial de N
    return fac  # Devuelve el factorial

num= int(input("ingrese un numero: "))  # Obtiene un número del usuario
print(f"el factorial del numero {num} es {factorial(num)}")  # Imprime el factorial del número

# Función para verificar si un número es primo
def es_primo(n):
    if n <= 1:
        return False  # Devuelve Falso si n es menor o igual a 1
    for i in range(2, n):
        if n % i == 0:
            return False  # Devuelve Falso si n es divisible por algún número en el rango
    return True  # Devuelve Verdadero si n es primo

numero = int(input("Ingresa un número para verificar si es primo: "))  # Obtiene un número del usuario
if es_primo(numero):
    print(f"{numero} es un número primo.")  # Imprime si el número es primo
else:
    print(f"{numero} no es un número primo.")  # Imprime si el número no es primo

texto = input("ingrese una cadena de texto: ")  # Obtiene una entrada de texto del usuario
nuevo_texto= texto[::-1]  # Invierte el texto de entrada
print(nuevo_texto)  # Imprime el texto invertido

print("CUANTOS DATOS INGRESARA")
print("_______________________")
N = int(input(": "))  # Obtiene el número de datos de entrada del usuario
ls = []
for i in range(1,N+1):
    valor = int(input(f"{i}) "))  # Obtiene cada dato de entrada del usuario
    ls.append(valor)  # Agrega la entrada a la lista
ls.sort()  # Ordena la lista en orden ascendente
print("\n"
      f"sus datos de forma ordenada es {ls}")  # Imprime los datos ordenados

s = "cadena"
s2 =  "".join([ s[i] for i in range(len(s)-1, -1, -1) ])  # Invierte la cadena 'cadena'
print(f"la forma invertida de {s} es {s2}")  # Imprime la cadena invertida

N = int(input("ingrese un numero: "))  # Obtiene un número del usuario
pares = sum([i for i in range(N+1) if i%2==0])  # Calcula la suma de los números pares hasta N
print(f"la suma de los numeros pares en los {N} primeros numeros es {pares}")  # Imprime la suma de los números pares

cuadrados = [i**2 for i in range(11)]  # Calcula los cuadrados de los números del 0 al 10
print(cuadrados)  # Imprime la lista de cuadrados

# Función para contar el número de vocales en un texto
def vocal(texto):
    vocales= 'aeiou'
    cont = 0
    for i in texto:
        if i in vocales:
            cont += 1
    return cont

cadena_texto = input("ingrese una cadena de texto: ")  # Obtiene una entrada de texto del usuario
print(f"hay {vocal(cadena_texto)} vocales en el texto que ingreso")  # Imprime el número de vocales en el texto de entrada

# Inicializa la lista de Fibonacci con los dos primeros números
fibonacci = [0, 1]  

# Itera hasta que la lista de Fibonacci tenga 10 números
while len(fibonacci) < 10: 
    # Obtiene los dos últimos números de la lista
    a, b = fibonacci[-2], fibonacci[-1]  
    # Calcula el siguiente número de la serie Fibonacci
    c = a + b  
    # Agrega el nuevo número a la lista
    fibonacci.append(c)  

# Imprime un mensaje y la lista de los primeros 10 números de la serie Fibonacci
print("Los primeros 10 números de la serie Fibonacci son:")
print(fibonacci)


# Función para verificar si una palabra es un palíndromo
def es_palindromo(palabra):
    palabra = unidecode.unidecode(palabra.lower())  # Normaliza la palabra para la comparación
    palabra = palabra.replace(' ', '')  # Elimina los espacios de la palabra
    return palabra == palabra[::-1]  # Verifica si la palabra es un palíndromo

palabra = input("Ingresa una palabra: ")  # Obtiene una palabra del usuario
if es_palindromo(palabra):
    print(f"'{palabra}' es un palíndromo.")  # Imprime si la palabra es un palíndromo
else:
    print(f"'{palabra}' no es un palíndromo.")  # Imprime si la palabra no es un palíndromo

N = int(input("ingrese un numero de la tabla\n"
              "de multiplicar que desea: "))  # Obtiene un número para la tabla de multiplicar del usuario
for i in range(13):
    print(f"{i} x {N} = {i*N}")  # Imprime la tabla de multiplicar

import math

# Función para calcular el área de un círculo
def area_circulo(radio):
    area = math.pi * radio**2  # Calcula el área del círculo
    return area  # Devuelve el área

radio_circulo = float(input("Ingresa el radio del círculo: "))  # Obtiene el radio del círculo del usuario
area_resultante = area_circulo(radio_circulo)  # Calcula el área del círculo
print(f"El área del círculo con radio {radio_circulo} es: {area_resultante}")  # Imprime el área del círculo

N = int(input("ingresa un numero preferentemente \n"
              "con 2 digitos : "))  # Obtiene un número del usuario
sum_dig = sum([int(i) for i in str(N)])  # Calcula la suma de los dígitos en el número
print(f"la suma de los digitos del numero es {sum_dig}")  # Imprime la suma de los dígitos en el número
