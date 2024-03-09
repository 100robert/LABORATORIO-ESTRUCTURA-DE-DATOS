import numpy as np
# Recursividad:
'''# 1) Ejercicio 1: Escribe una función recursiva que imprima los números pares del 1 al 100.'''
def numeros_pares(n):
    # Verifica si el número n es menor o igual a 100
    if n <= 100:
        # Verifica si el número n es par
        if n % 2 == 0:
            # Imprime el número par n
            print(n)
        # Llama recursivamente a la función con el siguiente número
        numeros_pares(n + 1)
        
# Llama a la función numeros_pares con el número inicial 1
numeros_pares(1)


'''# 2) Ejercicio 2: Escribe una función recursiva que imprima la suma de los números del 1 al n.'''
def suma_numeros(n):
    # Verifica si n es igual a 1
    if n == 1:
        return n
    else:
        # Retorna la suma de n y la llamada recursiva con n-1
        return n + suma_numeros(n - 1)
print(suma_numeros(7))

'''# 3) Ejercicio 3: Escribe una función recursiva que imprima la pirámide de números del 1 al n.'''
def imprimir_piramide(n, i=1):
    # Verifica si el índice i es mayor que el número n
    if i > n:
        return
    else:
        # Calcula la cantidad de espacios necesarios
        espacios = ' ' * (n - i)
        # Crea una cadena de números para la fila actual
        numeros = str(i) * (2 * i - 1)
        # Imprime la fila de la pirámide con los espacios y números correspondientes
        print(espacios + numeros)
        # Llama recursivamente a la función con el siguiente índice
        imprimir_piramide(n, i + 1)

# Llama a la función imprimir_piramide con n=5 para imprimir la pirámide
imprimir_piramide(5)

'''# 4) Ejercicio 4: Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n.'''
def imprimir_piramide_invertida(n, i=None):
    # Verifica si i es None y lo iguala a n si es así
    if i is None:
        i = n
    
    # Verifica si i es igual a 0 y retorna en ese caso
    if i == 0:
        return
    else:
        # Calcula la cantidad de espacios necesarios
        espacios = ' ' * (n - i)
        # Crea una cadena de números para la fila actual
        numeros = str(i) * (2 * i - 1)
        # Imprime la fila de la pirámide con los espacios y números correspondientes
        print(espacios + numeros)
        # Llama recursivamente a la función con el siguiente índice
        imprimir_piramide_invertida(n, i - 1)

imprimir_piramide_invertida(5)

'''# 5) Ejercicio 2: Escribe una función recursiva que imprima la tabla de multiplicar del n.'''
def tabla_multiplicar(n, i=0):
    # Verifica si i es mayor o igual a 13
    if i >= 13:
        return
    else:
        # Imprime la multiplicación de i por n
        print(f"{i} x {n} = {i * n}")
    # Llama recursivamente a la función con el siguiente índice
    tabla_multiplicar(n, i + 1)
tabla_multiplicar(8)

'''#MATRICES
# 6) Crea una matriz de números reales.'''
# Crea una matriz de números enteros
matriz = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
# Imprime la matriz creada
print(matriz)
'''# 7) Crea una matriz de números complejos.'''
# Crea una matriz de números complejos
matriz_compleja = np.array([
    [2j, 3j, 5j],  # Primera fila de la matriz con números complejos
    [8j, 9.10j, 2j],  # Segunda fila de la matriz con números complejos
    [1.4j, 6j, 17]  # Tercera fila de la matriz con números complejos
])
print(matriz_compleja)  # Imprime la matriz de números complejos

'''# 8) Crea una matriz de matrices.'''

# Crea una matriz de matrices con números enteros
matriz_de_matrices = np.array([
    [[1, 2], [31, 45], [1, 24], [14, 235]], 
    [[52, 6], [27, 8], [12, 22], [31, 42]],  
    [[15, 22], [32, 42], [52, 6], [21, 2]],
    [[14, 2], [73, 4], [71, 22], [81, 62]],
])
print(matriz_de_matrices)  # Imprime la matriz de matrices creada

'''''# 9) Accede al elemento central de una matriz.'''''


# Crea una matriz de 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Obtiene el número de filas y columnas de la matriz
filas, columnas = matriz.shape
# Verifica si tanto el número de filas como el número de columnas son impares
if filas % 2 == 1 and columnas % 2 == 1:
    # Calcula el elemento central de la matriz
    elemento_central = matriz[filas // 2, columnas // 2]
    # Imprime el elemento central
    print(elemento_central)
else:
    # Imprime un mensaje indicando que la matriz no tiene un único elemento central
    print("La matriz no tiene un único elemento central.")

'''# 10) Suma dos matrices de diferentes tamaños.'''

# Crea dos matrices de 2x2
matriz1 = np.array([[1, 2], [3, 4]])
matriz2 = np.array([[5, 6], [7, 8]])
# Realiza la suma de las dos matrices
suma = np.add(matriz1, matriz2)
# Imprime la matriz resultante de la suma
print(suma)

'''# 11) Multiplica una matriz por un número.'''
# Crea una matriz de 2x2
matriz = np.array([[1, 2], [3, 4]])
# Define el número por el cual se multiplicará la matriz
numero = 3
# Realiza la multiplicación de la matriz por el número
resultado = np.multiply(matriz, numero)
# Imprime el resultado de la multiplicación
print(resultado)

'''# 12) Calcula la media de los elementos de una matriz.'''

# Crea una matriz de 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Calcula la media de los elementos de la matriz
media = np.mean(matriz)
# Imprime la media calculada
print(media)
'''# Ejercicio parte 01:
# Ejercicio 1:
# Crea una matriz de números aleatorios de tamaño 100x100.'''

# Crea una matriz de números aleatorios de tamaño 100x100
matriz = np.random.rand(100, 100)
# Imprime la matriz generada
print(matriz)

'''# Ejercicio 2:
# Calcula la media, la mediana y la desviación estándar de los elementos de una matriz.'''

# Crea una matriz de 3x3
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# Calcula la media de los elementos de la matriz
media = np.mean(matriz)
# Calcula la mediana de los elementos de la matriz
mediana = np.median(matriz)
# Calcula la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz)
# Imprime la media calculada
print("Media:", media)
# Imprime la mediana calculada
print("Mediana:", mediana)
# Imprime la desviación estándar calculada
print("Desviación estándar:", desviacion_estandar)

'''# Ejercicio 3:
# Escribe una función que encuentre el elemento máximo de una matriz.'''

# Definición de la función para encontrar el máximo de una matriz
def maximo_matriz(matriz):
    maximo = np.max(matriz)  # Encuentra el valor máximo en la matriz
    return maximo  # Retorna el valor máximo encontrado

# Matriz de ejemplo
matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Imprime el máximo de la matriz utilizando la función definida
print("El máximo de la matriz es:", maximo_matriz(matriz))

'''# Ejercicio 4:
# Escribe una función que encuentre la submatriz de mayor suma de una matriz.
'''
# Función para encontrar la submatriz de mayor suma en una matriz
def max_sum_submatrix(matriz):
    # Si la matriz está vacía, retorna 0
    if not matriz:
        return 0
    
    # Inicializa la suma máxima como negativa infinita
    max_sum = float('-inf')
    # Obtiene el número de filas y columnas de la matriz
    filas, columnas = len(matriz), len(matriz[0])

    # Itera sobre las columnas izquierdas
    for left in range(columnas):
        # Inicializa un arreglo temporal de suma para cada fila
        temp = [0]*filas
        # Itera sobre las columnas derechas
        for right in range(left, columnas):
            # Actualiza la suma temporal para cada fila
            for i in range(filas):
                temp[i] += matriz[i][right]

            # Calcula la suma máxima de la submatriz actual
            sum_actual = max_sum_subarray(temp)
            # Actualiza la suma máxima global
            max_sum = max(max_sum, sum_actual)

    return max_sum

# Función para encontrar la subsecuencia de suma máxima en un arreglo
def max_sum_subarray(arr):
    # Inicializa la suma máxima como negativa infinita
    max_sum = float('-inf')
    sum_actual = 0
    # Itera sobre los elementos del arreglo
    for num in arr:
        # Calcula la suma actual considerando el elemento actual
        sum_actual = max(num, sum_actual + num)
        # Actualiza la suma máxima global
        max_sum = max(max_sum, sum_actual)
    return max_sum

'''# Ejercicio 5:
# Escribe una función que encuentre la matriz de covarianza de dos matrices.'''
# Función para calcular la matriz de covarianza de una matriz
def matriz_covarianza(matriz):
    # Calcula la matriz de covarianza utilizando la función np.cov
    covarianza = np.cov(matriz, rowvar=False)
    return covarianza

matriz = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Imprime la matriz de covarianza calculada
print("La matriz de covarianza es:\n", matriz_covarianza(matriz))

