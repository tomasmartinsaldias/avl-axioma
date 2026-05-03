from motor import Ejercicio
import random
    
def creador_diccionario():
    DICCIONARIO_CONCEPTOS = {}
    dict_inverso = {}
    contador = 1
    conceptos = "Notación Big O (O), Análisis del peor caso, Análisis del mejor caso, Análisis del caso promedio, Pilas (Stacks), Colas (Queues), Doble colas (Deques), Listas enlazadas simples, Listas doblemente enlazadas, Listas circulares enlazadas, Evaluación de expresiones (Postfijas y Prefijas), Representación en memoria contigua vs. enlazada, Búsqueda secuencial, Búsqueda binaria, Ordenamiento de burbuja (Bubble Sort), Ordenamiento por selección (Selection Sort), Ordenamiento por inserción (Insertion Sort), Ordenamiento de Shell (Shell Sort), Ordenamiento por mezcla (Merge Sort), Ordenamiento rápido (Quick Sort), Estabilidad de ordenamiento, Ordenamiento in-place, Recorrido en preorden, Recorrido en inorden, Recorrido en postorden, Recorrido por niveles (BFS), Árbol de análisis sintáctico, Evaluación de expresiones aritméticas, Inserción y eliminación en BST, Sucesor y predecesor inorden, Árbol AVL (Rotaciones), Montículos binarios (Min-heap y Max-heap), Operación Heapify (up y down)"
    lista_conceptos = conceptos.split(",")
    for c in lista_conceptos:
        c = c.strip()    
        DICCIONARIO_CONCEPTOS[contador] = c
        dict_inverso[c] = contador
        contador += 1
    return DICCIONARIO_CONCEPTOS, dict_inverso

def creador_ejercicios(arbol, n_ejercicios):
    diccionario_conceptos, diccionario_inverso = creador_diccionario()
    contadores_locales = {}
    for n in range(n_ejercicios):
        concepto = random.randint(1, len(diccionario_conceptos)) #Podría ser hasta 999
        bloom = random.randint(1,6)
        dificultad = random.randint(1,99)
        clave = (concepto, bloom, dificultad)
        if clave in contadores_locales:
            contadores_locales[clave] += 1
        else:
            contadores_locales[clave] = 0
        id_ejercicio = contadores_locales[clave]
        if id_ejercicio < 100:
            ejercicio = Ejercicio(concepto, bloom, dificultad, id_ejercicio)
            arbol.put(ejercicio.score, ejercicio)

