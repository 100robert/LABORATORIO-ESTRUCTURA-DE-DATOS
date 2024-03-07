"""primera parte"""

# 1. Validar la edad de un usuario.

# Definición de la función para validar la edad del usuario.
def validacion_edad(edad):
    # Asegura que la edad sea un número entero.
    assert isinstance(edad, int), "La edad debe ser un número entero"
    # Asegura que la edad esté en el rango de 0 a 100.
    assert 0 <= edad <= 100, "La edad debe osilar de 0 entre 100"
    # Imprime un mensaje si la edad es válida.
    print("La edad es válida.")
# Bloque try-except para manejar posibles errores al validar la edad.
try:
    validacion_edad(5)  # Llamada a la función con un ejemplo.
except ValueError:
    print("Error: Ingrese un número entero para la edad.")

# 2. Verificar el tipo de dato de una variable.

# Definición de la función para verificar el tipo de dato de una variable.
def tipo_dato(variable):
    # Serie de condiciones para determinar el tipo de dato de la variable.
    if isinstance(variable, int):
        print(f"La variable es de tipo Entero.")
    elif isinstance(variable, float):
        print(f"La variable es de tipo Flotante.")
    elif isinstance(variable, str):
        print(f"La variable es de tipo Cadena de texto.")
    elif isinstance(variable, list):
        print(f"La variable es de tipo Lista.")
    elif isinstance(variable, dict):
        print(f"La variable es de tipo Diccionario.")
    elif isinstance(variable, tuple):
        print(f"La variable es de tipo Tupla.")
    elif isinstance(variable, bool):
        print(f"La variable es de tipo Booleano.")
    else:
        print(f"La variable es de un tipo no identificado.")
tipo_dato(2)  # Llamada a la función con un ejemplo.

# 3. Validar el rango de una calificación.

# Definición de la función para validar el rango de una calificación.
def validacion_rango_calificacion(calificación):
    # Asegura que la calificación sea un número entero.
    assert isinstance(calificación,int), "la calificacion debe ser un entro"
    # Asegura que la calificación esté en el rango de 0 a 20.
    assert 0<=calificación<=20, "la calificacion debe osilar entre 0 y 20"
    # Imprime un mensaje si la calificación es válida.
    print("La calificacion es válida.")
# Bloque try-except para manejar posibles errores al validar la calificación.
try:
    validacion_rango_calificacion('a')  # Llamada a la función con un ejemplo incorrecto.
except AssertionError as e:
    print(f"Error: {e}")

# 4. Asegurar que una lista no esté vacía.

# Definición de la función para verificar que una lista no esté vacía.
def verificar_lista(lista):
    # Asegura que la longitud de la lista sea mayor a 0.
    assert len(lista) > 0, "La lista está vacía"
    # Imprime un mensaje si la lista no está vacía.
    return print("La lista no está vacía.")
# Bloque try-except para manejar posibles errores al verificar la lista.
try:
    mi_lista = [3]  # Ejemplo de lista no vacía.
    verificar_lista(mi_lista)  # Llamada a la función.
except AssertionError as e:
    print(f"Error: {e}")

# 5. Validar la igualdad de dos objetos.

# Definición de la función para validar la igualdad de dos objetos.
def validar_igualdad(obj1, obj2):
    # Asegura que los dos objetos sean iguales.
    assert obj1 == obj2, "los valores de los objetos son diferentes"
    # Imprime un mensaje si los objetos son iguales.
    return print("los 2 objetos son iguales") 
# Bloque try-except para manejar posibles errores al validar la igualdad.
try: 
    validar_igualdad(3,'d')  # Llamada a la función con ejemplos diferentes.
except AssertionError as e:
    print(f"Error: {e}")

# 6. Asegurar que un ciclo while se ejecute al menos una vez.

# Definición de la función para asegurar la ejecución de un ciclo while al menos una vez.
def ejecuto_while_mas_una_vez(n):
    contador = 0  # Inicialización del contador.
    while contador<n:  # Ciclo while que se ejecuta mientras el contador sea menor que n.
        contador += 1  # Incremento del contador.
    # Asegura que el contador sea al menos 1, indicando que el ciclo se ejecutó al menos una vez.
    assert contador>=1, "el ciclo while no se ejecuto al menos una vez"
    # Imprime un mensaje si el ciclo se ejecutó al menos una vez.
    print("si se ejecuto al menos una vez")
# Bloque try-except para manejar posibles errores al asegurar la ejecución del ciclo.
try:
    ejecuto_while_mas_una_vez(0)  # Llamada a la función con un ejemplo.
except AssertionError as e:
    print(f"Error: {e}")

# 7. Asegurar que una función retorna un valor específico.

# Definición de la función que retorna el doble del valor ingresado.
def mi_funcion(valor):
    resultado = valor * 2  # Cálculo del resultado.
    # Asegura que el resultado sea 44.
    assert resultado == 44, "La función debería retornar 44"
    return resultado  # Retorna el resultado.
# Bloque try-except para manejar posibles errores al asegurar el retorno de la función.
try:
    resultado_funcion = mi_funcion(27)  # Llamada a la función con un ejemplo incorrecto.
    print(f"El resultado de la función es: {resultado_funcion}")
except AssertionError as e:
    print(f"Error: {e}")

# 8. Validar el estado de una variable después de una operación.

# Definición de la función para validar el estado de una variable después de una operación.
def estado_variable(n, opccion):
    valor = 3  # Valor base para las operaciones.
    n = int(n)  # Conversión de n a entero.
    # Asegura que n sea 0 y que sea igual a '4', lo cual es un error lógico.
    assert n==0 and n=='4', "en munero deve ser mayor a 0 para poder vividir"
    # Serie de condiciones para realizar operaciones matemáticas según la opción elegida.
    if opccion == '1':
        estado = valor+n  # Suma.
        print(f"el numero {n} se sumo y su estado actual es {estado}")
    elif opccion == '2':
        estado = valor-n  # Resta.
        print(f"el numero {n} se resto y su estado actual es {estado}")
    elif opccion == '3':
        estado = valor*n  # Multiplicación.
        print(f"el numero {n} se multiplico y su estado actual es {estado}")
    elif opccion == '4':
        estado = valor/n  # División.
        print(f"el numero {n} se dividio y su estado actual es {estado}")
# Bloque try-except para manejar posibles errores al validar el estado de la variable.
try:
    estado_variable(0,'1')  # Llamada a la función con un ejemplo.
except AssertionError as e:
    print(f"Error: {e}")

# 9. Asegurar que un módulo se ha importado correctamente.

# Bloque try-except para manejar la importación del módulo 'unidecode'.
try:
    import unidecode  # Intento de importar el módulo 'unidecode'.
    print("El módulo 'unidecode' se ha importado correctamente.")  # Mensaje de éxito.
except ImportError:  # Manejo del error si la importación falla.
    print("Error al importar el módulo 'unidecode'. Asegúrese de que esté instalado.")

""""segunda parte"""
# 10. Desarrollar el código de buscar nodo en la lista enlazada simple.

# Definición de la clase Nodo, que representa un nodo en la lista enlazada.
class Nodo:
    def __init__(self, dato):
        self.dato=dato  # Valor del nodo.
        self.siguiente = None  # Referencia al siguiente nodo, inicialmente None.
# Definición de la clase ListaEnlazadaSimple, que representa una lista enlazada simple.
class ListaEnlazadaSimple:
    def __init__(self):
        self.primero=None  # Inicialización del primer nodo de la lista como None.

    # Método para agregar un nuevo nodo al final de la lista.
    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)  # Creación de un nuevo nodo.
        if self.primero is None:  # Si la lista está vacía, el nuevo nodo se convierte en el primero.
            self.primero = nuevo_nodo
        else:  # Si la lista no está vacía, se recorre hasta encontrar el último nodo y se agrega el nuevo.
            actual = self.primero
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    # Método para imprimir todos los nodos de la lista.
    def imprimir(self):
        actual=self.primero  # Comienza desde el primer nodo.
        while actual:  # Mientras haya nodos en la lista.
            print(actual.dato, end=' -> ')  # Imprime el valor del nodo actual.
            actual=actual.siguiente  # Avanza al siguiente nodo.

    # Método para buscar un valor específico en la lista.
    def BuscarNodo(self,valor):
        actual = self.primero  # Comienza desde el primer nodo.
        while actual:  # Mientras haya nodos en la lista.
            if actual.dato==valor:  # Si el valor del nodo actual coincide con el buscado.
                return True  # Retorna True indicando que se encontró el valor.
            actual=actual.siguiente  # Avanza al siguiente nodo.
        return False  # Retorna False si no se encontró el valor en la lista.
    '''Suma de Nodos'''
    # 11. Implementa una función que sume todos los nodos de una lista enlazada simple.
    def sumarNodos(self):
        suma = 0  # Inicialización de la suma.
        actual = self.primero  # Comienza desde el primer nodo.
        while actual is not None:  # Mientras haya nodos en la lista.
            suma += actual.dato  # Suma el valor del nodo actual a la suma total.
            actual = actual.siguiente  # Avanza al siguiente nodo.
        return suma  # Retorna la suma total de los valores de los nodos.
    '''Longitud de la Lista'''
    # 12. Crea una función que devuelva la longitud de una lista enlazada simple.
    def LongitudLista(self):
        longitud = 0  # Inicialización de la longitud.
        actual = self.primero  # Comienza desde el primer nodo.
        while actual is not None:  # Mientras haya nodos en la lista.
            longitud += 1  # Incrementa la longitud por cada nodo encontrado.
            actual = actual.siguiente  # Avanza al siguiente nodo.
        return longitud  # Retorna la longitud total de la lista.
    '''''''""""Concatenar Listas""""'''''''
# 13. Implementa una función que concatene dos listas enlazadas simples.
    def concatenar_listas(self,segundalista):
        if self.primero is None:  # Si la primera lista está vacía.
            self.primero = segundalista.primero  # La primera lista toma los nodos de la segunda.
        else:  # Si la primera lista no está vacía.
            actual = self.primero  # Comienza desde el primer nodo de la primera lista.
            while actual.siguiente is not None:  # Recorre hasta encontrar el último nodo.
                actual = actual.siguiente
            actual.siguiente = segundalista.primero  # Conecta el último nodo de la primera lista con el primero de la segunda.

    '''Eliminar Duplicados'''
# 14. Crea una función que elimine los nodos duplicados de una lista enlazada simple.
    def eliminar_duplicados(self):
        if self.primero is None:  # Si la lista está vacía, no hay nada que hacer.
            return
        nodo_actual = self.primero  # Comienza desde el primer nodo.
        while nodo_actual is not None:  # Mientras haya nodos en la lista.
            anterior = nodo_actual  # Guarda el nodo actual como anterior.
            siguiente = nodo_actual.siguiente  # Avanza al siguiente nodo.
            while siguiente is not None:  # Mientras haya nodos siguientes.
                if siguiente.dato == nodo_actual.dato:  # Si el valor del nodo siguiente es igual al nodo actual.
                    anterior.siguiente = siguiente.siguiente  # Elimina el nodo duplicado conectando el nodo anterior con el siguiente del duplicado.
                else:
                    anterior = siguiente  # Si no son iguales, avanza el nodo anterior al siguiente.
                siguiente = siguiente.siguiente  # Avanza al siguiente nodo.
            nodo_actual = nodo_actual.siguiente  # Avanza al siguiente nodo actual.

    '''Invertir Lista'''
# 15. Implementa una función que invierta el orden de una lista enlazada simple.
    def invertir(self):
        nodo_anterior = None  # Inicializa el nodo anterior como None.
        nodo_actual = self.primero  # Comienza desde el primer nodo.
        while nodo_actual is not None:  # Mientras haya nodos en la lista.
            nodo_siguiente = nodo_actual.siguiente  # Guarda el nodo siguiente.
            nodo_actual.siguiente = nodo_anterior  # Cambia el enlace del nodo actual al nodo anterior, invirtiendo la dirección.
            nodo_anterior = nodo_actual  # El nodo actual se convierte en el nodo anterior para el siguiente ciclo.
            nodo_actual = nodo_siguiente  # Avanza al siguiente nodo.
        self.primero = nodo_anterior  # El último nodo se convierte en el primero de la lista invertida.

mi_lista=ListaEnlazadaSimple()  # Crea una instancia de la lista enlazada simple.
mi_lista.agregar(1)  # Agrega el valor 1 a la lista.
mi_lista.agregar(2)  # Agrega el valor 2 a la lista.
mi_lista.agregar(2)  # Agrega otro valor 2 a la lista, para demostrar la eliminación de duplicados.
mi_lista.imprimir()  # Imprime la lista.
print("\n")
lista2 = ListaEnlazadaSimple()  # Crea otra instancia de la lista enlazada simple.
lista2.agregar(4)  # Agrega el valor 4 a la segunda lista.
lista2.agregar(4)  # Agrega otro valor 4 a la segunda lista, para demostrar la eliminación de duplicados.
lista2.agregar(6)  # Agrega el valor 6 a la segunda lista.
print(mi_lista.BuscarNodo(8))  # Busca el valor 8 en la primera lista y imprime el resultado.
print(mi_lista.sumarNodos())  # Suma los nodos de la primera lista e imprime el resultado.
print(mi_lista.LongitudLista())  # Imprime la longitud de la primera lista.

print("estos son los elementos de la segunda lista son \n",lista2.imprimir())  # Imprime los elementos de la segunda lista.
print("\n")
print(lista2.eliminar_duplicados())  # Elimina los nodos duplicados de la segunda lista.
print("la nueva lista creada es:")
mi_lista.concatenar_listas(lista2)  # Concatena la primera y la segunda lista.
print(mi_lista.imprimir())  # Imprime la lista resultante después de la concatenación.
print(lista2.invertir())  # Invierte la segunda lista.


