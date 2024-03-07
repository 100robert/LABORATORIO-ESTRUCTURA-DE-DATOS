from unidecode import unidecode

"""Ejercicio parte 01  Listas Enlazadas Dobles:
Duplicar Nodos:"""
"""1.
Crea una lista con al menos 4 nodos, duplica cada nodo de la lista e imprime 
la lista original y la lista duplicada hacia adelante y hacia atrás.
"""
# Definición de la clase Nodo para representar un nodo en una lista doblemente enlazada
class Nodo:
    # Constructor de la clase Nodo
    def __init__(self, dato):
        self.dato = dato  # Almacena el dato en el nodo
        self.siguiente = None  # Inicializa el puntero al siguiente nodo como None
        self.anterior = None  # Inicializa el puntero al nodo anterior como None

# Definición de la clase ListaDoblementeEnlazada para representar una lista doblemente enlazada
class ListaDoblementeEnlazada:
    # Constructor de la clase ListaDoblementeEnlazada
    def __init__(self):
        self.primero = None  # Inicializa el primer nodo de la lista como None

    # Método para añadir un nuevo nodo al final de la lista
    def anexar(self, dato):
        if not self.primero:  # Verifica si la lista está vacía
            self.primero = Nodo(dato)  # Crea un nuevo nodo con el dato y lo asigna como primero
        else:
            actual = self.primero
            while actual.siguiente:  # Recorre la lista hasta el último nodo
                actual = actual.siguiente
            nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato
            actual.siguiente = nuevo_nodo  # Establece el nuevo nodo como siguiente del último nodo
            nuevo_nodo.anterior = actual  # Establece el nodo actual como anterior del nuevo nodo

    # Método para imprimir la lista en orden normal o inverso
    def imprimir(self, reversa=False):
        if reversa:  # Si se desea imprimir en orden inverso
            actual = self.primero
            while actual.siguiente:  # Avanza hasta el último nodo
                actual = actual.siguiente
            while actual:  # Imprime los nodos en orden inverso
                print(actual.dato, end=" ")
                actual = actual.anterior
        else:  # Si se desea imprimir en orden normal
            actual = self.primero
            while actual:  # Imprime los nodos en orden normal
                print(actual.dato, end=" ")
                actual = actual.siguiente
        print()  # Imprime un salto de línea al final

    # Método para duplicar cada nodo de la lista
    def duplicar_nodos(self):
        actual = self.primero
        while actual:  # Recorre la lista
            nuevo_nodo = Nodo(actual.dato)  # Crea un nuevo nodo con el mismo dato
            nuevo_nodo.siguiente = actual.siguiente  # Establece el siguiente del nuevo nodo
            if actual.siguiente:  # Verifica si hay un nodo siguiente
                actual.siguiente.anterior = nuevo_nodo  # Establece el nuevo nodo como anterior del siguiente
            actual.siguiente = nuevo_nodo  # Establece el nuevo nodo como siguiente del nodo actual
            nuevo_nodo.anterior = actual  # Establece el nodo actual como anterior del nuevo nodo
            actual = nuevo_nodo.siguiente  # Avanza al siguiente nodo en la lista

# Creación de una instancia de ListaDoblementeEnlazada
mi_lista = ListaDoblementeEnlazada()
for i in [1, 2, 3, 4]:  # Añade los números 1, 2, 3, 4 a la lista
    mi_lista.anexar(i)

print("Lista Original:")
mi_lista.imprimir()  # Imprime la lista en orden normal
mi_lista.imprimir(reversa=True)  # Imprime la lista en orden inverso

# Llamada al método para duplicar los nodos de la lista
mi_lista.duplicar_nodos()

print("Lista Duplicada:")
mi_lista.imprimir()  # Imprime la lista duplicada en orden normal
mi_lista.imprimir(reversa=True)  # Imprime la lista duplicada en orden inverso

"""2.
Contar Nodos Pares e Impares:
Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos 
tienen un dato impar e imprime la lista hacia adelante y hacia atrás.
"""

class Nodo:
    # Inicializa un nodo con un dato y referencias al siguiente y anterior
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None  # Referencia al siguiente nodo
        self.anterior = None  # Referencia al nodo anterior

class ListaDoble:
    # Inicializa una lista doblemente enlazada con referencias al primero y último nodo
    def __init__(self):
        self.primero = None  # Referencia al primer nodo
        self.ultimo = None  # Referencia al último nodo

    # Agrega un nuevo nodo con un dato a la lista
    def agregar(self, dato):
        if self.primero is None:
            self.primero = self.ultimo = Nodo(dato)  # Crea el primer nodo si la lista está vacía
        else:
            aux = self.ultimo
            self.ultimo = aux.siguiente = Nodo(dato)  # Crea un nuevo nodo y lo enlaza al último nodo
            self.ultimo.anterior = aux  # Establece el nodo anterior del nuevo nodo

    # Muestra los datos de los nodos en la lista desde inicio hasta fin
    def mostrar(self, inicio, fin):
        valores = []
        while inicio:
            valores.append(inicio.dato)  # Agrega el dato del nodo a la lista de valores
            inicio = inicio.siguiente  # Avanza al siguiente nodo
        return valores  # Devuelve la lista de valores

    # Cuenta la cantidad de nodos pares e impares en la lista
    def contar_pares_impares(self):
        pares = impares = 0
        aux = self.primero
        while aux:
            if aux.dato % 2 == 0:
                pares += 1  # Incrementa el contador de pares si el dato es par
            else:
                impares += 1  # Incrementa el contador de impares si el dato es impar
            aux = aux.siguiente  # Avanza al siguiente nodo
        return pares, impares  # Devuelve la cantidad de pares e impares

lista = ListaDoble()
for i in range(1, 10):
    lista.agregar(i)  # Agrega números del 1 al 9 a la lista

pares, impares = lista.contar_pares_impares()  # Obtiene la cantidad de pares e impares
print(f"Números pares: {pares}")  # Imprime la cantidad de números pares
print(f"Números impares: {impares}")  # Imprime la cantidad de números impares
print("Lista de adelante hacia atrás: ", lista.mostrar(lista.primero, lista.ultimo))  # Muestra la lista de inicio a fin
print("Lista de atrás hacia adelante: ", lista.mostrar(lista.ultimo, lista.primero)[::-1])  # Muestra la lista de fin a inicio


"""3.
Insertar Nodo en Posición Específica:
Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en 
la posición 3 e imprime la lista hacia adelante y hacia atrás.
"""

class Nodo:
    # Clase que representa un nodo en una lista doblemente enlazada
    def __init__(self, dato=None):
        self.dato = dato  # Inicializa el dato del nodo
        self.siguiente = None  # Inicializa el siguiente nodo como None
        self.anterior = None  # Inicializa el nodo anterior como None

class ListaDoblementeEnlazada:
    # Clase que representa una lista doblemente enlazada
    def __init__(self):
        self.primero = None  # Inicializa el primer nodo como None
        self.ultimo = None  # Inicializa el último nodo como None

    def anexar(self, dato):
        # Método para agregar un nuevo nodo al final de la lista
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def insertar_en_posicion(self, dato, posicion):
        # Método para insertar un nuevo nodo en una posición específica de la lista
        nuevo_nodo = Nodo(dato)  # Crea un nuevo nodo con el dato proporcionado
        actual = self.primero
        # Recorre la lista hasta la posición deseada
        for _ in range(posicion - 1):
            if actual is not None:
                actual = actual.siguiente  # Avanza al siguiente nodo
        # Verifica si la posición es válida
        if actual is None:
            print("La posición es mayor que la longitud de la lista.")
        else:
            siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo  # Inserta el nuevo nodo en la posición deseada
            # Establece el nodo anterior del nuevo nodo como el nodo actual
            nuevo_nodo.anterior = actual
            # Establece el nodo siguiente del nuevo nodo como el nodo siguiente
            nuevo_nodo.siguiente = siguiente
            # Verifica si el nodo siguiente no es None
            if siguiente is not None:
                # Establece el nodo anterior del nodo siguiente como el nuevo nodo
                siguiente.anterior = nuevo_nodo

    def imprimir(self, reversa=False):
        # Método para imprimir los datos de la lista en orden o en reversa
        if reversa:
            actual = self.ultimo
            while actual:
                print(actual.dato, end=" ")  # Imprime el dato del nodo actual
                actual = actual.anterior  # Avanza al nodo anterior
        else:
            actual = self.primero
            while actual:
                print(actual.dato, end=" ")  # Imprime el dato del nodo actual
                actual = actual.siguiente  # Avanza al nodo siguiente
        print()  # Imprime un salto de línea al final
# Crear lista con al menos 5 nodos
mi_lista = ListaDoblementeEnlazada()
for i in range(1, 6):
    mi_lista.anexar(i)

# Insertar un nuevo nodo con el dato 15 en la posición 3
mi_lista.insertar_en_posicion(15, 3)

# Imprimir la lista hacia adelante y hacia atrás
print("Lista hacia adelante:")
mi_lista.imprimir()
print("Lista hacia atrás:")
mi_lista.imprimir(reversa=True)




"""4.
Eliminar Nodos Duplicados:
Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, 
dejando solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás.
"""

class Nodo:
    def __init__(self, dato=None):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def anexar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.primero is None:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.ultimo.siguiente = nuevo_nodo
            nuevo_nodo.anterior = self.ultimo
            self.ultimo = nuevo_nodo

    def imprimir(self, reversa=False):
        if reversa:
            actual = self.ultimo
            while actual:
                print(actual.dato, end=" ")
                actual = actual.anterior
        else:
            actual = self.primero
            while actual:
                print(actual.dato, end=" ")
                actual = actual.siguiente
        print()

    def eliminar_duplicados(self):
        # Conjunto para almacenar los datos vistos
        datos_vistos = set()
        # Iniciar desde el primer nodo
        actual = self.primero
        # Recorrer la lista
        while actual:
            # Verificar si el dato actual ya ha sido visto
            if actual.dato in datos_vistos:
                siguiente = actual.siguiente
                # Actualizar los enlaces para eliminar el nodo duplicado
                if actual.anterior:
                    actual.anterior.siguiente = actual.siguiente
                if actual.siguiente:
                    actual.siguiente.anterior = actual.anterior
                # Actualizar el primer y último nodo si es necesario
                if actual == self.primero:
                    self.primero = actual.siguiente
                if actual == self.ultimo:
                    self.ultimo = actual.anterior
                actual = siguiente
            else:
                # Agregar el dato actual al conjunto de datos vistos
                datos_vistos.add(actual.dato)
                actual = actual.siguiente

    def invertir_lista(self):
        actual = self.primero
        while actual:
            siguiente = actual.siguiente
            actual.siguiente = actual.anterior
            actual.anterior = siguiente
            actual = siguiente
        self.primero, self.ultimo = self.ultimo, self.primero

# Crear lista con datos duplicados y operaciones
mi_lista_duplicados = ListaDoblementeEnlazada()
for i in [5, 8, 11, 8, 14, 17, 5, 11]:
    mi_lista_duplicados.anexar(i)

# Eliminar duplicados
mi_lista_duplicados.eliminar_duplicados()

# Imprimir lista hacia adelante y hacia atrás después de eliminar duplicados
print("Lista hacia adelante después de eliminar duplicados:")
mi_lista_duplicados.imprimir()
print("Lista hacia atrás después de eliminar duplicados:")
mi_lista_duplicados.imprimir(reversa=True)

# Invertir la lista
mi_lista_duplicados.invertir_lista()

# Imprimir lista hacia adelante y hacia atrás después de invertir
print("Lista hacia adelante después de invertir:")
mi_lista_duplicados.imprimir()
print("Lista hacia atrás después de invertir:")
mi_lista_duplicados.imprimir(reversa=True)



"""5.
Invertir la Lista:
Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento 
se convierte en el primero y viceversa) e imprime la lista hacia adelante y hacia atrás."""
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaDoblementeEnlazada:
    def __init__(self):
        self.primero = None
        self.ultimo = None

    def agregar_al_final(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.ultimo is not None:
            nuevo_nodo.anterior = self.ultimo
            self.ultimo.siguiente = nuevo_nodo
            self.ultimo = nuevo_nodo
        else:
            self.primero = nuevo_nodo
            self.ultimo = nuevo_nodo

    def imprimir_adelante(self):
        # Itera a través de la lista desde el primer nodo hasta el último nodo
        nodo_actual = self.primero
        while nodo_actual is not None:
            # Imprime el dato del nodo actual sin saltar de línea
            print(nodo_actual.dato, end=' ')
            # Avanza al siguiente nodo en la lista
            nodo_actual = nodo_actual.siguiente
        # Imprime un salto de línea al final
        print()

    def imprimir_atras(self):
        # Itera a través de la lista desde el último nodo hasta el primer nodo
        nodo_actual = self.ultimo
        while nodo_actual is not None:
            # Imprime el dato del nodo actual sin saltar de línea
            print(nodo_actual.dato, end=' ')
            # Retrocede al nodo anterior en la lista
            nodo_actual = nodo_actual.anterior
        # Imprime un salto de línea al final
        print()

    def invertir(self):
        """
  Invierte el orden de los nodos en la lista.

  Recorre la lista desde el primer nodo (`nodo_actual`).

  Mientras `nodo_actual` no sea `None`:
    Se intercambian los punteros `siguiente` y `anterior` del nodo actual.
    Se actualiza el puntero `nodo_actual` al nodo anterior.

  Finalmente, se intercambian los punteros `primero` y `ultimo` de la lista.
  """
        nodo_actual = self.primero
        while nodo_actual is not None:
            nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior, nodo_actual.siguiente
            nodo_actual = nodo_actual.anterior
        self.primero, self.ultimo = self.ultimo, self.primero

# Crear una lista doblemente enlazada
mi_lista = ListaDoblementeEnlazada()

# Agregar elementos a la lista
for i in range(1, 7):
    mi_lista.agregar_al_final(i)

# Imprimir la lista hacia adelante y hacia atrás
mi_lista.imprimir_adelante()
mi_lista.imprimir_atras()

# Invertir la lista
mi_lista.invertir()

# Imprimir la lista invertida hacia adelante y hacia atrás
mi_lista.imprimir_adelante()
mi_lista.imprimir_atras()


'''Ejercicios parte 02:
Invertir una cadena:
6.
Utilizar una pila para invertir el orden de los caracteres de una cadena.
'''

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not bool(self.items)

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

# Función para invertir una cadena utilizando una pila
def invertir_cadena(cadena):
    pila = Pila()  # Se crea una instancia de la clase Pila

    for caracter in cadena:  # Se recorre cada caracter de la cadena
        pila.apilar(caracter)  # Se apila el caracter en la pila

    cadena_invertida = ""  # Se inicializa una cadena vacía para almacenar la cadena invertida
    while not pila.esta_vacia():  # Mientras la pila no esté vacía
        cadena_invertida += pila.desapilar()  # Se desapila un caracter y se agrega a la cadena invertida

    return cadena_invertida  # Se devuelve la cadena invertida

cadena = "Hola Mundo"
print(f"Cadena original: {cadena}")
print(f"Cadena invertida: {invertir_cadena(cadena)}")


'''7.
Convertir número decimal a binario:
Implementar un programa que convierta un número decimal a su representación en sistema binario utilizando una pila.
'''

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not bool(self.items)

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()

def decimal_a_binario(num):
    pila = Pila()

    while num > 0:
        residuo = num % 2
        pila.apilar(residuo)
        num = num // 2

    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())

    return binario

num = 42
print(f"El número decimal {num} en binario es {decimal_a_binario(num)}")


'''8.
Evaluar expresión posfija:
Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila.
'''

# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la pila como una lista vacía

    def esta_vacia(self):
        return not bool(self.items)  # Verifica si la pila está vacía

    def apilar(self, dato):
        self.items.append(dato)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento de la parte superior de la pila

# Función para evaluar una expresión en notación posfija
def evaluar_posfija(expresion):
    pila = Pila()  # Creación de una instancia de la clase Pila
    for caracter in expresion.split():
        if caracter.isdigit():
            pila.apilar(int(caracter))  # Si es un número, se apila en la pila
        else:
            num2 = pila.desapilar()
            num1 = pila.desapilar()
            resultado = eval(f"{num1} {caracter} {num2}")  # Evalúa la operación y apila el resultado
            pila.apilar(resultado)
    return pila.desapilar()  # El resultado final está en la parte superior de la pila

# Ejemplo de uso para evaluar una expresión en notación posfija
expresion = "2 3 1 * + 9 -"
print(f"El resultado de la expresión {expresion} en notación posfija es {evaluar_posfija(expresion)}")



'''9.
Validar operadores anidados:
Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una pila.
'''

# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la pila como una lista vacía

    def esta_vacia(self):
        return not bool(self.items)  # Verifica si la pila está vacía

    def apilar(self, dato):
        self.items.append(dato)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento de la parte superior de la pila

# Función para verificar si los paréntesis, corchetes y llaves están correctamente anidados
def verificar_anidamiento(expresion):
    pila = Pila()  # Creación de una instancia de la clase Pila
    for caracter in expresion:
        if caracter in "([{":
            pila.apilar(caracter)  # Si es un paréntesis de apertura, corchete o llave, se apila en la pila
        elif caracter in ")]}":
            if pila.esta_vacia():
                return False  # Si se encuentra un cierre sin su correspondiente apertura, la expresión no está bien anidada
            if not corresponde(pila.desapilar(), caracter):
                return False  # Si la apertura y el cierre no corresponden, la expresión no está bien anidada
    return pila.esta_vacia()  # La expresión está bien anidada si la pila está vacía al final

# Función para verificar si una apertura y un cierre corresponden
def corresponde(apertura, cierre):
    parejas = {"(": ")", "[": "]", "{": "}"}
    return parejas[apertura] == cierre

# Ejemplo de uso para verificar el anidamiento de una expresión
expresion = "{2 + [3 * (4 + 5)]}"
if verificar_anidamiento(expresion):
    print(f"La expresión {expresion} está correctamente anidada")
else:
    print(f"La expresión {expresion} no está correctamente anidada")


'''10.
Ordenar una pila:
Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales.
'''

# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la pila como una lista vacía

    def esta_vacia(self):
        return not bool(self.items)  # Verifica si la pila está vacía

    def apilar(self, dato):
        self.items.append(dato)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento de la parte superior de la pila

    def cima(self):
        if not self.esta_vacia():
            return self.items[-1]  # Devuelve el elemento en la parte superior de la pila

# Función para ordenar una pila de manera ascendente
def ordenar_pila(pila_original):
    pila_auxiliar = Pila()  # Creación de una pila auxiliar para el proceso de ordenamiento
    while not pila_original.esta_vacia():
        temp = pila_original.desapilar()  # Tomar un elemento de la pila original
        while not pila_auxiliar.esta_vacia() and pila_auxiliar.cima() > temp:
            # Mientras haya elementos en la pila auxiliar mayores que el temporal,
            # se apilan de nuevo en la pila original
            pila_original.apilar(pila_auxiliar.desapilar())
        pila_auxiliar.apilar(temp)  # Se apila el elemento temporal en la pila auxiliar
    return pila_auxiliar

# Creación de una instancia de la clase Pila
pila = Pila()
# Apilar elementos en la pila original
ls = [5, 1, 3, 2, 4]
for i in ls:
    pila.apilar(i)

# Ordenar la pila y mostrar los resultados
pila_ordenada = ordenar_pila(pila)
print("Pila original: ", [5, 1, 3, 2, 4])
print("Pila ordenada: ", [pila_ordenada.desapilar() for _ in range(5)])


'''11.
Eliminar duplicados:
Eliminar los elementos duplicados de una pila.
'''

# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la pila como una lista vacía

    def esta_vacia(self):
        return not bool(self.items)  # Verifica si la pila está vacía

    def apilar(self, dato):
        self.items.append(dato)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento de la parte superior de la pila

# Función para eliminar duplicados de una pila
def eliminar_duplicados(pila_original):
    pila_auxiliar = Pila()  # Creación de una pila auxiliar
    elementos_vistos = set()  # Conjunto para almacenar elementos ya vistos
    while not pila_original.esta_vacia():
        elemento = pila_original.desapilar()
        if elemento not in elementos_vistos:
            elementos_vistos.add(elemento)
            pila_auxiliar.apilar(elemento)  # Apila elementos no duplicados en la pila auxiliar
    return pila_auxiliar

# Creación de una instancia de la clase Pila e inserción de elementos duplicados
pila = Pila()
for i in [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]:
    pila.apilar(i)

# Eliminación de duplicados y obtención de la pila resultante
pila_sin_duplicados = eliminar_duplicados(pila)

# Impresión de los resultados
print("Pila original: ", [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])
print("Pila sin duplicados: ", [pila_sin_duplicados.desapilar() for _ in range(4)])



'''12.
Implementar una calculadora sencilla:
Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar expresiones.
'''
# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la pila como una lista vacía

    def esta_vacia(self):
        return not bool(self.items)  # Verifica si la pila está vacía

    def apilar(self, dato):
        self.items.append(dato)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento de la parte superior de la pila

# Función para evaluar una expresión en notación posfija
def evaluar_expresion(expresion):
    pila = Pila()  # Creación de una instancia de la clase Pila
    for caracter in expresion.split():
        if caracter.isdigit():
            pila.apilar(int(caracter))  # Si es un número, se apila en la pila
        else:
            num2 = pila.desapilar()
            num1 = pila.desapilar()
            resultado = eval(f"{num1} {caracter} {num2}")  # Evalúa la operación y apila el resultado
            pila.apilar(resultado)
    return pila.desapilar()  # El resultado final está en la parte superior de la pila

# Ejemplo de uso para evaluar una expresión en notación posfija
expresion = "2 3 1 * + 9 -"
print(f"El resultado de la expresión {expresion} en notación posfija es {evaluar_expresion(expresion)}")


'''13.
Comprobar palíndromos:
Utilizar una pila para comprobar si una palabra o frase es un palíndromo.
'''

# Definición de la clase Pila
class Pila:
    def __init__(self):
        self.items = []  # Inicialización de la pila como una lista vacía

    def esta_vacia(self):
        return not bool(self.items)  # Verifica si la pila está vacía

    def apilar(self, dato):
        self.items.append(dato)  # Agrega un elemento a la parte superior de la pila

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()  # Elimina y devuelve el elemento de la parte superior de la pila

# Función para determinar si una palabra o frase es un palíndromo
def es_palindromo(palabra):
    pila = Pila()  # Creación de una instancia de la clase Pila
    palabra = unidecode(palabra.lower().replace(" ", ""))  # Normaliza y elimina espacios de la palabra
    for caracter in palabra:
        pila.apilar(caracter)  # Apila cada caracter de la palabra

    palabra_invertida = ""
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()  # Desapila y construye la palabra invertida

    return palabra == palabra_invertida  # Compara la palabra original con la invertida

# Ejemplo de uso para verificar si la frase es un palíndromo
palabra = "Anita lava la tina"
if es_palindromo(palabra):
    print(f"La frase '{palabra}' es un palíndromo")
else:
    print(f"La frase '{palabra}' no es un palíndromo")


'''14.
Simular el proceso de deshacer (undo):
Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los deshaceres.'''

class Pila:
  """
  Clase que define una pila con las operaciones básicas:
    - Inicializar
    - Verificar si está vacía
    - Apilar un elemento
    - Desapilar un elemento
  """

  def __init__(self):
    """
    Inicializa la pila con una lista vacía.
    """
    # Inicializa la pila con una lista vacía
    self.items = []

  def esta_vacia(self):
    """
    Verifica si la pila está vacía.
    """
    # Retorna True si la lista está vacía, False en caso contrario
    return not bool(self.items)

  def apilar(self, dato):
    """
    Agrega un elemento a la pila.
    """
    # Agrega el elemento al final de la lista
    self.items.append(dato)

  def desapilar(self):
    """
    Saca y devuelve el elemento superior de la pila.
    """
    # Si la pila no está vacía, retorna el último elemento y lo elimina de la lista
    if not self.esta_vacia():
      return self.items.pop()

class SistemaDeshacer:

    def __init__(self):
        # Inicializa el sistema de deshacer con dos pilas vacías
        self.pila_acciones = Pila()  # Inicializa una pila para almacenar acciones
        self.pila_deshacer = Pila()  # Inicializa una pila para almacenar acciones deshechas

    def ejecutar_accion(self, accion):
        # Agrega una acción a la pila de acciones y muestra un mensaje
        self.pila_acciones.apilar(accion)  # Agrega la acción a la pila de acciones
        print(f"Ejecutando acción: {accion}")  # Imprime un mensaje indicando la acción ejecutada

    def deshacer_accion(self):
        if not self.pila_acciones.esta_vacia():
            # Deshace la última acción realizada
            accion_deshacer = self.pila_acciones.desapilar()  # Obtiene la última acción realizada
            self.pila_deshacer.apilar(accion_deshacer)  # Agrega la acción a la pila de acciones deshechas
            print(f"Deshaciendo acción: {accion_deshacer}")  # Imprime un mensaje indicando la acción deshecha

    def rehacer_accion(self):
        if not self.pila_deshacer.esta_vacia():
            # Rehace la última acción deshecha
            accion_rehacer = self.pila_deshacer.desapilar()  # Obtiene la última acción deshecha
            self.pila_acciones.apilar(accion_rehacer)  # Agrega la acción de rehacer a la pila de acciones
            print(f"Rehaciendo acción: {accion_rehacer}")  # Imprime un mensaje indicando la acción rehacer
sistema = SistemaDeshacer()
sistema.ejecutar_accion("Abrir documento")
sistema.ejecutar_accion("Editar documento")
sistema.deshacer_accion()
sistema.rehacer_accion()

