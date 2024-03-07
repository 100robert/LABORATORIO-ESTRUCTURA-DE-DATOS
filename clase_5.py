# Importamos la librería audioop pero no se utiliza en el código, por lo que se podría eliminar.
from audioop import reverse
# Importamos la función sort de numpy pero no se utiliza en el código, por lo que se podría eliminar.
from numpy import sort
# Importamos unidecode para normalizar cadenas quitando acentos y caracteres especiales.
import unidecode

# 1) Función para obtener números primos de un conjunto de números.
def es_primo(n):
    # Un número primo es mayor que 1 y solo divisible por 1 y por sí mismo.
    if n < 2:
        return False
    # Iteramos desde 2 hasta la raíz cuadrada de n + 1.
    for i in range(2, int(n**0.5) + 1):
        # Si n es divisible por cualquier número en ese rango, no es primo.
        if n % i == 0:
            return False
    # Si pasa el bucle sin encontrar divisores, es primo.
    return True

# Función para filtrar números primos de un conjunto.
def obtener_primos(numeros):
    primos = set()
    # Iteramos sobre el conjunto de números.
    for num in numeros:
        # Si el número es primo, lo añadimos al conjunto de primos.
        if es_primo(num):
            primos.add(num)
    # Devolvemos el conjunto de números primos.
    return primos
# Ejemplo de uso de la función obtener_primos.
numeros = {10, 15, 23, 25, 29}
print(obtener_primos(numeros))

# 2) Función para obtener palabras que comienzan con una letra determinada.
def conjun_palabras(texto, z):
    # Comprensión de conjunto para filtrar palabras que comienzan con la letra z.
    new_conj = {palabra for palabra in texto if palabra[0]==z}
    # Imprimimos el conjunto resultante.
    return print(new_conj)
# Ejemplo de uso de la función conjun_palabras.
palabras = {'hola', 'apa', 'banana', 'laboratirio', 'arona', 'agora'}
char = 'a'
conjun_palabras(palabras, char)


#3) Escriba una función que reciba un conjunto de números y 
#devuelva un conjunto con los números que son divisibles por un número determinado.
# 3) Definición de la función que recibe un conjunto de números (x) y un número (y).
# Devuelve un conjunto con los números de x que son divisibles por y.
def num_divisibles(x,y):
    # Comprensión de conjunto que itera sobre x y selecciona los números divisibles por y.
    divisibles={numero for numero in x if numero%y==0}
    # Imprime el conjunto de números divisibles.
    return print(divisibles)
# Ejemplo de uso de la función num_divisibles con un conjunto de números y el divisor 3.
numeros = {12, 34, 67, 9, 6, 18, 135, 9, 6}
num_divisibles(numeros, 3)

# 4) Definición de la función que recibe dos conjuntos de números y devuelve su intersección.
def conj_interseccion(conj1, conj2):
    # Utiliza el método intersection para encontrar los elementos comunes entre conj1 y conj2.
    return conj1.intersection(conj2)
# Ejemplo de uso de la función conj_interseccion con dos conjuntos de números.
set1= {1,2,3,4,5,6,78,3,6,8}
set2 = {2,7,9,55,60,88,0,63,4}
print(conj_interseccion(set1,set2))

# 5) Definición de la función que recibe dos conjuntos de números y devuelve la diferencia simétrica.
def dif_simetrica(conj1,conj2):
    # Utiliza el método symmetric_difference para encontrar los elementos que están en conj1 o conj2 pero no en ambos.
    return conj1.symmetric_difference(conj2)
# Ejemplo de uso de la función dif_simetrica con dos conjuntos de números.
set1 = {1,5,6,8,0,2,4,7}
set2 = {0,11,4,12,5,78,6,7}
print(dif_simetrica(set1,set2))

# 6) Definición de la función que recibe dos conjuntos de números y devuelve la diferencia simétrica, enfocada en el segundo conjunto.
def dif_simetrica(conj1,conj2):
    # Utiliza el método symmetric_difference pero invirtiendo el orden de los conjuntos para enfocarse en el segundo.
    return conj2.symmetric_difference(conj1)
# Ejemplo de uso de la función dif_simetrica con dos conjuntos de números, enfocándose en el segundo conjunto.
set1 = {1,5,6,8,0,2,4,7}
set2 = {0,11,4,12,5,78,6,7}
print(dif_simetrica(set1,set2))

# 7) Definición de la función que recibe un conjunto de palabras y devuelve un conjunto con los anagramas encontrados.
def encontrar_anagramas(palabras):
    # Inicializa un conjunto vacío para almacenar los anagramas.
    anagramas = set()
    # Primer bucle que itera sobre cada palabra en el conjunto de palabras.
    for palabra in palabras:
        # Segundo bucle que itera sobre las palabras para comparar con cada palabra del primer bucle.
        for otra_palabra in palabras:
            # Comprueba si las palabras son diferentes y si, al ordenarlas, son iguales (condición de anagrama).
            if palabra != otra_palabra and sorted(palabra) == sorted(otra_palabra):
                # Añade ambas palabras al conjunto de anagramas.
                anagramas.add(palabra)
                anagramas.add(otra_palabra)
    # Devuelve el conjunto de anagramas.
    return anagramas
# Ejemplo de uso de la función encontrar_anagramas con un conjunto de palabras.
palabras = {'amor', 'roma', 'casa', 'saca', 'perro', 'gato', 'ballena', 'llenaba', 'taza', 'zata'}
print(encontrar_anagramas(palabras))

# 8) Definición de la función que verifica si una palabra es palíndromo y devuelve un conjunto con los palíndromos encontrados.
def son_palindromo(palabra):
    # Inicializa un conjunto vacío para almacenar los palíndromos.
    set1 = set()
    # Itera sobre cada palabra en el conjunto de entrada.
    for pal in palabra:
        # Normaliza la palabra eliminando acentos, convirtiéndola a minúsculas y eliminando espacios.
        pal = unidecode.unidecode(pal.lower())
        pal = pal.replace(' ', '')
        # Comprueba si la palabra es igual a su inversa (condición de palíndromo).
        if pal == pal[::-1]:
            # Añade la palabra al conjunto de palíndromos.
            set1.add(pal)
    # Devuelve el conjunto de palíndromos.
    return print(set1)
# Ejemplo de uso de la función son_palindromo con un conjunto de palabras.
palab = {'aná', 'reconoser', 'menem', 'hola', 'anita', 'radar'}
son_palindromo(palab)

# 9) Definición de la función que recibe un conjunto de palabras y un número n. Devuelve un conjunto con las palabras de longitud n.
def len_palabra(palbras, n):
    # Comprensión de conjunto que selecciona las palabras de longitud n.
    new_set = {palbra for palbra in palbras if len(palbra)==n }     
    # Devuelve el conjunto de palabras seleccionadas.
    return print(new_set)
# Ejemplo de uso de la función len_palabra con un conjunto de palabras y una longitud específica.
palabras={'hecho', 'carro', 'funcion', 'foco', 'pera', 'perro', 'cuartro'}
len_palabra(palabras,5)

# 10) Definición de la función que recibe un conjunto de palabras y una letra. Devuelve un conjunto con las palabras que contienen esa letra.
def palab_letra_determinada(palabras,letra):
    # Comprensión de conjunto que selecciona las palabras que contienen la letra especificada.
    conjunto_nuevo = {palabra for palabra in palabras if letra in palabra}
    # Devuelve el conjunto de palabras seleccionadas.
    return print(conjunto_nuevo)
# Ejemplo de uso de la función palab_letra_determinada con un conjunto de palabras y una letra específica.
palbras = {'conjuro', 'axioma', 'neon', 'carro', 'transmición'}
palab_letra_determinada(palbras,'u')

# 11) Definición de la función que recibe un conjunto de números y devuelve un conjunto con los números ordenados de menor a mayor.
def ordenado(numeros):
    # Ordena el conjunto de números y lo convierte en un conjunto antes de imprimirlo.
    return print(set(sorted(numeros)))
# Ejemplo de uso de la función ordenado con un conjunto de números.
num = {6,7,8,3,5,1,11,88,6,14,50}
ordenado(num)

# 12) Definición de la función que recibe un conjunto de números y devuelve una lista con los números ordenados de mayor a menor.
def ordenado(numeros):
    # Ordena el conjunto de números de mayor a menor y devuelve la lista resultante.
    return sorted(numeros, reverse=True)
# Ejemplo de uso de la función ordenado con un conjunto de números, ordenados de mayor a menor.
num = {6,7,8,3,5,1,11,88,6,14,50}
print(ordenado(num))

# 13) Definición de la función que recibe un conjunto de números y devuelve un conjunto con los números duplicados.
def encontrar_duplicados(numeros):
    # Inicializa dos conjuntos vacíos para almacenar los números únicos y duplicados.
    duplicados = set()
    unicos = set()
    # Itera sobre cada número en el conjunto de entrada.
    for num in numeros:
        # Comprueba si el número ya está en el conjunto de únicos.
        if num in unicos:
            # Si es así, lo añade al conjunto de duplicados.
            duplicados.add(num)
        else:
            # Si no, lo añade al conjunto de únicos.
            unicos.add(num)
    # Devuelve el conjunto de números duplicados.
    return duplicados
# Ejemplo de uso de la función encontrar_duplicados con una lista de números.
numeros = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]
print(encontrar_duplicados(numeros))

# 14) Definición de la función que recibe un conjunto de números y devuelve un conjunto con los números únicos (no duplicados).
def numeros_unicos(datos):
    # Inicializa dos conjuntos vacíos para almacenar los números únicos y repetidos.
    num_unicos=set()
    num_repetidos=set()
    # Itera sobre cada número en el conjunto de entrada.
    for i in datos:
        # Comprueba si el número ya está en el conjunto de únicos.
        if i in num_unicos:
            # Si es así, lo añade al conjunto de repetidos.
            num_repetidos.add(i)
        else:
            # Si no, lo añade al conjunto de únicos.
            num_unicos.add(i)
    # Devuelve el conjunto de números únicos.
    return print(num_unicos)
# Ejemplo de uso de la función numeros_unicos con una lista de números.
numeros = [1, 2, 3, 2, 1, 5, 6, 5, 5, 5]
numeros_unicos(numeros)

# 15) Definición de la función que recibe un conjunto de números y devuelve un conjunto con los números primos ordenados de menor a mayor.
def primos_ordenados(dato): 
    # Definición de la función interna es_primo para verificar si un número es primo.
    def es_primo(n):
        # Un número primo es mayor que 1 y solo divisible por 1 y por sí mismo.
        if n <= 1:
            return False
        # Itera desde 2 hasta n-1 para comprobar si n es divisible por algún número en ese rango.
        for i in range(2, n):
            if n % i == 0:
                return False
        # Si no encuentra divisores, devuelve True indicando que el número es primo.
        return True
    # Comprensión de conjunto que selecciona los números primos del conjunto de entrada.
    primos = {numero for numero in numeros if es_primo(numero)}
    # Ordena el conjunto de números primos y devuelve la lista resultante.
    return sorted(primos)
# Ejemplo de uso de la función primos_ordenados con un conjunto de números.
numeros = {1, 45, 63, 2, 8, 9, 7, 15, 75, 30, 11, 4, 3}
resultado = primos_ordenados(numeros)
print(resultado)

# 16) Definición de la función que recibe un conjunto de palabras y devuelve un conjunto con los palíndromos ordenados de menor a mayor.
def palindromo_ordenado(palabras):
    # Definición de la función interna es_palindromo para verificar si una palabra es palíndromo.
    def es_palindromo(palabra):
        # Normaliza la palabra eliminando acentos, convirtiéndola a minúsculas y eliminando espacios.
        palabra = unidecode.unidecode(palabra.lower())
        palabra = palabra.replace(' ', '')
        # Comprueba si la palabra es igual a su inversa (condición de palíndromo).
        return palabra == palabra[::-1]
    # Comprensión de conjunto que selecciona los palíndromos del conjunto de entrada.
    palindromos = {palabra for palabra in palabras if es_palindromo(palabra)}
    # Ordena el conjunto de palíndromos y devuelve la lista resultante.
    palindromos_ordenados = sorted(palindromos)
    return sorted(palindromos_ordenados)
# Ejemplo de uso de la función palindromo_ordenado con un conjunto de palabras.
palabras = {'aná', 'pedro',  "Radar", "oso", "reconocer", 'anana'}
resultado=set(palindromo_ordenado(palabras))
print(resultado)

# 17) Definición de la función que recibe un conjunto de palabras, verifica si son palíndromos, tienen una longitud determinada y las ordena de menor a mayor.
def palindromos_ordenados_len(palabras,n):
    # Comprensión de conjunto que selecciona las palabras que son palíndromos y tienen longitud n.
    palabras_con_longitud = {palabra for palabra in palabras if len(palabra) == n and son_palindromo(palabra)}
    # Ordena el conjunto de palabras seleccionadas y devuelve la lista resultante.
    palindromos_ordenado=sorted(palabras_con_longitud)
    return print(palindromos_ordenado)
# Ejemplo de uso de la función palindromos_ordenados_len con un conjunto de palabras y una longitud específica.
conjunto_palabras = {'ana', 'pedro',  "radar", "oso", "reconocer", 'anana'}
palindromos_ordenados_len(conjunto_palabras,3)

# 18) Definición de la función que recibe un conjunto de palabras y una letra. Devuelve un conjunto con las palabras que contienen esa letra y están ordenadas de mayor a menor.
def palabras_ordenar(palabras, letra):
    # Comprensión de conjunto que selecciona las palabras que contienen la letra especificada.
    palabras_con_letra = {palabra for palabra in palabras if letra in palabra}
    # Ordena el conjunto de palabras seleccionadas por longitud de manera descendente y devuelve la lista resultante.
    palabras_ordenadas = sorted(palabras_con_letra, key=len, reverse=True)
    return palabras_ordenadas
# Ejemplo de uso de la función palabras_ordenar con un conjunto de palabras y una letra específica.
palabras = {"hola", "mundo", "python", "programación"}
print(palabras_ordenar(palabras, 'o'))

# 19) Definición de la función que recibe un conjunto de números, elimina los duplicados y los ordena de menor a mayor.
def numeros_ordenados(dato):
    # Elimina los duplicados convirtiendo el conjunto de entrada en un conjunto.
    numeros_unicos=set(dato)
    # Ordena el conjunto de números únicos y devuelve la lista resultante.
    unicos_ordenados=sorted(numeros_unicos)
    return print(unicos_ordenados)
# Ejemplo de uso de la función numeros_ordenados con una lista de números.
numeros = [1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 7, 8, 9, 10]
numeros_ordenados(numeros)

# 20) Definición de la función que recibe un conjunto de palabras, verifica si son palíndromos, tienen una longitud determinada y las ordena de menor a mayor.
def es_palindromo(palabra):
    # Normaliza la palabra eliminando acentos, convirtiéndola a minúsculas y eliminando espacios.
    palabra = unidecode.unidecode(palabra.lower())
    palabra = palabra.replace(' ', '')
    # Comprueba si la palabra es igual a su inversa (condición de palíndromo).
    return palabra == palabra[::-1]
def palindromos_ordenado_len(palabras, longitud):
    # Comprensión de conjunto que selecciona los palíndromos del conjunto de entrada con longitud especificada.
    palindromos_longitud = {palabra for palabra in palabras if es_palindromo(palabra) and len(palabra) == longitud}
    # Ordena el conjunto de palíndromos seleccionados y devuelve la lista resultante.
    palin_ordenados = sorted(palindromos_longitud)
    return print(palin_ordenados)
# Ejemplo de uso de la función palindromos_ordenado_len con un conjunto de palabras y una longitud específica.
palabras = {"radar", "mundo", "reconocer", "rotor", "python", "rever"}
palindromos_ordenado_len(palabras,5)