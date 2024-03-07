"""Ejercicio parte 01  Colas:"""
"""Verificar si una palabra es palíndroma
1.
Implementa una función que determine si una palabra es palíndroma o 
no. Utiliza una cola para comparar los caracteres de la palabra en
orden original y reverso.
"""

class Cola:
    # Inicializa la cola
    def __init__(self):
        self.items = []  # Lista para almacenar los elementos de la cola

    # Verifica si la cola está vacía
    def esta_vacia(self):
        return not bool(self.items)  # Devuelve True si la lista de items está vacía, False de lo contrario

    # Agrega un dato a la cola
    def encolar(self, dato):
        self.items.append(dato)  # Agrega el dato al final de la lista de items

    # Elimina y devuelve el primer elemento de la cola
    def desencolar(self):
        if self.esta_vacia():  # Verifica si la cola está vacía
            return None  # Devuelve None si la cola está vacía
        else:
            return self.items.pop(0)  # Elimina y devuelve el primer elemento de la lista de items

    # Verifica si una palabra es palíndroma
    def es_palindroma(palabra):
        # Crear una cola y una pila
        cola = Cola()  # Inicializa una nueva cola
        pila = []  # Inicializa una nueva pila

        # Agregar los caracteres de la palabra a la cola y a la pila
        for caracter in palabra:
            cola.encolar(caracter)  # Agrega el caracter a la cola
            pila.append(caracter)  # Agrega el caracter a la pila

        # Comparar los caracteres en orden original y reverso
        while not cola.esta_vacia():  # Mientras la cola no esté vacía
            if cola.desencolar() != pila.pop():  # Compara los elementos de la cola y la pila
                return False  # Devuelve False si no son iguales

        return True  # Devuelve True si la palabra es palíndroma

# Prueba del método estático
palabra = "radar"
print(f"¿'{palabra}' es palíndroma? {Cola.es_palindroma(palabra)}")


"""2.
Diseño de un sistema de gestión de pedidos
Crea un sistema de gestión de pedidos que utilice una cola para procesar 
los pedidos en el orden en que fueron recibidos. Implementa funciones para 
agregar pedidos, procesar pedidos y mostrar el estado actual de la cola.
"""
class Cola:
    # Inicializa la cola
    def __init__(self):
        self.items = []  # Inicializa la lista de items en la cola

    # Verifica si la cola está vacía
    def esta_vacia(self):
        return not bool(self.items)  # Devuelve True si la lista de items está vacía, False de lo contrario

    # Agrega un dato a la cola
    def encolar(self, dato):
        self.items.append(dato)  # Agrega el dato al final de la lista de items

    # Elimina y devuelve el primer elemento de la cola
    def desencolar(self):
        if self.esta_vacia():  # Verifica si la cola está vacía
            return None  # Devuelve None si la cola está vacía
        else:
            return self.items.pop(0)  # Elimina y devuelve el primer elemento de la lista de items

    # Devuelve el estado actual de la cola
    def ver_estado(self):
        return self.items  # Devuelve la lista de items actual en la cola

class SistemaPedidos:
    # Inicializa el sistema de gestión de pedidos
    def __init__(self):
        self.cola_pedidos = Cola()  # Crea una cola para almacenar los pedidos

    # Agrega un pedido a la cola de pedidos
    def agregar_pedido(self, pedido):
        self.cola_pedidos.encolar(pedido)  # Agrega el pedido a la cola de pedidos

    # Procesa el primer pedido en la cola
    def procesar_pedido(self):
        if self.cola_pedidos.esta_vacia():  # Verifica si no hay pedidos en la cola
            print("No hay pedidos para procesar.")  # Imprime un mensaje indicando que no hay pedidos para procesar
        else:
            pedido_procesado = self.cola_pedidos.desencolar()  # Obtiene y elimina el primer pedido de la cola
            print(f"El pedido '{pedido_procesado}' ha sido procesado.")  # Imprime el pedido procesado

    # Muestra los pedidos actuales en la cola
    def ver_pedidos(self):
        pedidos = self.cola_pedidos.ver_estado()  # Obtiene la lista de pedidos en la cola
        if not pedidos:  # Verifica si no hay pedidos en la cola
            print("No hay pedidos en la cola.")  # Imprime un mensaje indicando que no hay pedidos en la cola
        else:
            print("Pedidos en la cola: ", end="")  # Imprime el mensaje inicial
            for pedido in pedidos:  # Itera sobre cada pedido en la lista de pedidos
                print(pedido, end=" ")  # Imprime cada pedido separado por un espacio
            print()  # Imprime un salto de línea al final

# Prueba del sistema de gestión de pedidos
sistema = SistemaPedidos()  # Crea una instancia del sistema de gestión de pedidos
sistema.agregar_pedido("Pedido 1")  # Agrega un pedido a la cola
sistema.agregar_pedido("Pedido 2")  # Agrega otro pedido a la cola
sistema.ver_pedidos()  # Muestra los pedidos en la cola
sistema.procesar_pedido()  # Procesa el primer pedido en la cola
sistema.ver_pedidos()  # Muestra los pedidos actualizados en la cola

"""""3.
Búsqueda de rutas en un laberinto
Desarrolla un programa que encuentre el camino más corto a través de un laberinto. 
Utiliza una cola para realizar un recorrido en anchura (BFS) desde el punto de 
inicio hasta el punto de destino.
"""""

class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return not bool(self.items)

    def encolar(self, dato):
        self.items.append(dato)

    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop(0)

# Definimos el laberinto como una lista de listas
laberinto = [
    ['.', '.', '#', '#', '.', '.', '.', '.'],
    ['.', '#', '.', '.', '.', '#', '#', '.'],
    ['.', '#', '#', '#', '.', '.', '#', '.'],
    ['.', '.', '.', '.', '#', '#', '#', '.'],
    ['#', '#', '#', '.', '#', '.', '.', '.'],
    ['.', '#', '#', '#', '#', '#', '#', '.'],
    ['.', '#', '.', '.', '.', '.', '#', '.'],
    ['.', '#', '#', '#', '#', '#', '.', '.']
]

# Definimos el punto de inicio y el punto de destino
inicio = (0, 0)
destino = (7, 7)

# Creamos una cola para almacenar los nodos por visitar
cola = [inicio]

# Creamos un diccionario para almacenar los nodos visitados y sus predecesores
predecesores = {inicio: None}

# Mientras la cola no esté vacía
while cola:
    # Sacamos el primer nodo de la cola
    nodo = cola.pop(0)

    # Si hemos llegado al destino
    if nodo == destino:
        # Reconstruimos el camino y terminamos
        camino = []
        while nodo is not None:
            camino.append(nodo)
            nodo = predecesores[nodo]
        camino.reverse()
        print("El camino más corto es:", camino)
        break

    # Para cada vecino del nodo
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        vecino = (nodo[0] + dx, nodo[1] + dy)

        # Si el vecino está dentro del laberinto y no es una pared
        if (0 <= vecino[0] < len(laberinto) and 0 <= vecino[1] < len(laberinto[0]) and
                laberinto[vecino[0]][vecino[1]] != '#' and vecino not in predecesores):
            # Agregamos el vecino a la cola y lo marcamos como visitado
            cola.append(vecino)
            predecesores[vecino] = nodo


"""4.
Diseño de un sistema de gestión de tareas (Avanzado)
Implementa un sistema de gestión de tareas que permita agregar tareas, 
marcar tareas como completadas y mostrar la próxima tarea pendiente."""

# Definimos la clase Cola
class Cola:
    # El método __init__ se llama cuando creamos un nuevo objeto Cola
    def __init__(self):
        # Inicializamos la cola como una lista vacía
        self.items = []

    # Este método devuelve True si la cola está vacía y False si no lo está
    def esta_vacia(self):
        return not bool(self.items)

    # Este método agrega un nuevo elemento al final de la cola
    def encolar(self, tarea):
        self.items.append(tarea)

    # Este método elimina y devuelve el primer elemento de la cola
    def desencolar(self):
        if self.esta_vacia():
            return None
        else:
            return self.items.pop(0)

# Definimos la clase SistemaTareas
class SistemaTareas:
    # El método __init__ se llama cuando creamos un nuevo objeto SistemaTareas
    def __init__(self):
        # Creamos una nueva cola para almacenar las tareas
        self.cola_tareas = Cola()

    # Este método agrega una nueva tarea a la cola de tareas
    def agregar_tarea(self, tarea):
        self.cola_tareas.encolar(tarea)
        print(f"La tarea '{tarea}' ha sido agregada.")

    # Este método marca la próxima tarea en la cola como completada
    def completar_tarea(self):
        if self.cola_tareas.esta_vacia():
            print("No hay tareas pendientes.")
        else:
            tarea_completada = self.cola_tareas.desencolar()
            print(f"La tarea '{tarea_completada}' ha sido completada.")

    # Este método muestra la próxima tarea en la cola
    def ver_proxima_tarea(self):
        if self.cola_tareas.esta_vacia():
            print("No hay tareas pendientes.")
        else:
            print(f"La próxima tarea pendiente es '{self.cola_tareas.items[0]}'.")

# Creamos un nuevo objeto SistemaTareas
sistema = SistemaTareas()

# Agregamos algunas tareas al sistema
sistema.agregar_tarea("Hacer la compra")
sistema.agregar_tarea("Estudiar para el examen")

# Mostramos la próxima tarea pendiente
sistema.ver_proxima_tarea()

# Completamos una tarea
sistema.completar_tarea()

# Mostramos la próxima tarea pendiente
sistema.ver_proxima_tarea()

'''Contar nodos:'''
'''5.
Implementar una función que cuente la 
cantidad de nodos en el árbol.'''
# Definición de la clase Arbol: representa la estructura general de un árbol.
class Arbol:
    def __init__(self):
        pass

# Definición de la clase Nodo: representa un nodo individual en el árbol con un dato y referencias a nodos izquierdo y derecho.
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

# Definición de la clase ArbolBinario: representa un árbol binario con métodos para insertar datos, recorrer en orden y contar nodos.
class ArbolBinario:
    def __init__(self):
        self.raiz = None

    # Método para insertar un dato en el árbol
    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    # Método auxiliar para insertar un dato en el árbol de forma ordenada
    def _insertar(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar(dato, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar(dato, nodo.derecha)

    # Método para recorrer el árbol en orden
    def inorden(self):
        if self.raiz is not None:
            self._inorden(self.raiz)

    # Método auxiliar para recorrer el árbol en orden y mostrar los datos
    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(str(nodo.dato) + ", ", end="")
            self._inorden(nodo.derecha)

    # Método para contar los nodos en el árbol
    def contar_nodos(self):
        return self._contar_nodos(self.raiz)

    # Método auxiliar para contar los nodos en el árbol de forma recursiva
    def _contar_nodos(self, nodo):
        if nodo is None:
            return 0
        else:
            return 1 + self._contar_nodos(nodo.izquierda) + self._contar_nodos(nodo.derecha)

# Crear un objeto de la clase ArbolBinario
arbol = ArbolBinario()

# Insertar algunos nodos en el árbol
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)

# Contar los nodos en el árbol
cantidad_nodos = arbol.contar_nodos()

print("La cantidad de nodos en el árbol es:", cantidad_nodos)

'''8.
Implementar una función que calcule la altura del 
árbol (la longitud del camino más largo desde la raíz hasta una hoja).'''
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class arbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar(dato, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar(dato, nodo.derecha)

    def inorden(self):
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(str(nodo.dato) + ", ", end="")
            self._inorden(nodo.derecha)

    # Definición de la función para calcular la altura del árbol
    def altura(self):
        return self._altura(self.raiz)

    # Función interna para calcular la altura de un nodo
    def _altura(self, nodo):
        if nodo is None:
            return 0
        else:
            altura_izquierda = self._altura(nodo.izquierda)
            altura_derecha = self._altura(nodo.derecha)
            return 1 + max(altura_izquierda, altura_derecha)

# Crear un objeto de la clase ArbolBinario
mi_arbol = arbolBinario()

# Insertar algunos nodos en el árbol
mi_arbol.insertar(10)
mi_arbol.insertar(5)
mi_arbol.insertar(15)
mi_arbol.insertar(2)
mi_arbol.insertar(7)
mi_arbol.insertar(3)
mi_arbol.insertar(17)

# Calcular la altura del árbol
altura = mi_arbol.altura()

# Imprimir la altura del árbol
print("La altura del árbol es:", altura)



'''9.
Implementar una función que calcule la profundidad de un 
nodo (la longitud del camino desde la raíz hasta el nodo).'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar(dato, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar(dato, nodo.derecha)

    def inorden(self):
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(str(nodo.dato) + ", ", end="")
            self._inorden(nodo.derecha)
    
    # Función para calcular la profundidad de un nodo en el árbol
    def profundidad(self, dato):
        # Llama a la función interna _profundidad con el dato, la raíz del árbol y una profundidad inicial de 0
        return self._profundidad(dato, self.raiz, 0)

    # Función interna para calcular la profundidad de un nodo en el árbol
    def _profundidad(self, dato, nodo, profundidad_actual):
        # Si el nodo actual es nulo, devuelve -1
        if nodo is None:
            return -1
        # Si el dato del nodo actual es igual al dato buscado, devuelve la profundidad actual
        if nodo.dato == dato:
            return profundidad_actual
        # Calcula la profundidad del nodo en el subárbol izquierdo
        profundidad_izquierda = self._profundidad(dato, nodo.izquierda, profundidad_actual + 1)
        # Si se encuentra la profundidad en el subárbol izquierdo, la devuelve
        if profundidad_izquierda != -1:
            return profundidad_izquierda
        # Si no se encuentra en el subárbol izquierdo, busca en el subárbol derecho
        else:
            return self._profundidad(dato, nodo.derecha, profundidad_actual + 1)

# Crear un objeto de la clase Arbol
arbol = Arbol()

# Insertar algunos nodos en el árbol
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(3)
arbol.insertar(17)

# Calcular la profundidad del nodo con dato 7
profundidad = arbol.profundidad(7)

# Imprimir la profundidad calculada
print("La profundidad del nodo con dato 7 es:", profundidad)

'''"""Buscar el mínimo y el máximo:"""
10.
Implementar una función que encuentre el nodo con el valor mínimo en el árbol.'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar(dato, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar(dato, nodo.derecha)

    def inorden(self):
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(str(nodo.dato) + ", ", end="")
            self._inorden(nodo.derecha)

    def minimo(self):
        # Verificar si la raíz del árbol es nula
        if self.raiz is None:
            # Devolver None si el árbol está vacío
            return None
        else:
            return self._minimo(self.raiz)

    def _minimo(self, nodo):
        # Verificar si el nodo actual no tiene hijo izquierdo
        if nodo.izquierda is None:
            # Devolver el dato del nodo actual si no tiene hijo izquierdo
            return nodo.dato
        else:
            # Llamar recursivamente a la función con el hijo izquierdo
            return self._minimo(nodo.izquierda)

# Crear un objeto de la clase ArbolBinario
arbol = arbol()

# Insertar algunos nodos
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(3)
arbol.insertar(17)

# Encontrar el valor mínimo
minimo = arbol.minimo()

print("El valor mínimo en el árbol es:", minimo)


'''11.
Implementar una función que encuentre el nodo con el valor máximo en el árbol.'''

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.izquierda = None
        self.derecha = None

class Arbolbinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, dato):
        if self.raiz is None:
            self.raiz = Nodo(dato)
        else:
            self._insertar(dato, self.raiz)

    def _insertar(self, dato, nodo):
        if dato < nodo.dato:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(dato)
            else:
                self._insertar(dato, nodo.izquierda)
        else:
            if nodo.derecha is None:
                nodo.derecha = Nodo(dato)
            else:
                self._insertar(dato, nodo.derecha)

    def inorden(self):
        if self.raiz is not None:
            self._inorden(self.raiz)

    def _inorden(self, nodo):
        if nodo is not None:
            self._inorden(nodo.izquierda)
            print(str(nodo.dato) + ", ", end="")
            self._inorden(nodo.derecha)

    # Definir una función para encontrar el valor máximo en el árbol
    def maximo(self):
        # Verificar si la raíz del árbol es nula
        if self.raiz is None:
            # Devolver None si el árbol está vacío
            return None
        else:
            # Llamar a la función recursiva para encontrar el valor máximo
            return self._maximo(self.raiz)

    # Función recursiva para encontrar el valor máximo en el árbol
    def _maximo(self, nodo):
        # Verificar si el nodo actual no tiene un hijo derecho
        if nodo.derecha is None:
            # Devolver el dato del nodo actual si no tiene hijo derecho
            return nodo.dato
        else:
            # Llamar recursivamente al hijo derecho para encontrar el valor máximo
            return self._maximo(nodo.derecha)
   
# Crear un objeto de la clase ArbolBinario
arbol = Arbolbinario()

# Insertar algunos nodos en el árbol
arbol.insertar(10)
arbol.insertar(5)
arbol.insertar(15)
arbol.insertar(2)
arbol.insertar(7)
arbol.insertar(3)
arbol.insertar(17)

# Encontrar y almacenar el valor máximo del árbol
maximo = arbol.maximo()

# Imprimir el valor máximo encontrado en el árbol
print("El valor máximo en el árbol es:", maximo)
