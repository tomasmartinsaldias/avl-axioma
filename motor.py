from clase_arbol import BinarySearchTree, TreeNode

class Ejercicio:
    def __init__(self, id_concepto:int, bloom:int, dificultad:int, id_ejercicio:int):
        self.id_concepto = id_concepto
        self.bloom = bloom
        self.dificultad = dificultad
        self.id_ejercicio = id_ejercicio
    
    @property #hace que se pueda llamar sin el paréntesis
    def score(self):
        return self.id_concepto*10**5 + self.bloom*10**4 + self.dificultad*10**2 + self.id_ejercicio
    
class MotorAxioma:
    def __init__(self):
        self.arbol = BinarySearchTree()
    def actualizar_dificultad(self, ejercicio, dificultad_nueva):
        self.arbol.delete(ejercicio.score)
        ejercicio.dificultad = dificultad_nueva
        self.arbol.put(ejercicio.score, ejercicio)

    def rango_min(self, id_concepto, bloom=1, dificultad=0):
        return id_concepto*10**5 + bloom*10**4 + dificultad*10**2

    def rango_max(self, id_concepto, bloom=6, dificultad=99):
        return id_concepto*10**5 + bloom*10**4 + dificultad*10**2 + 99

    def busqueda_rango(self, nodo_actual, min, max, resultados=None):
        if resultados is None:
            resultados = []
        if min > max: 
            return None
        if nodo_actual is None: 
            return resultados
        if nodo_actual.key >= min and nodo_actual.key <= max:
            resultados.append(nodo_actual.payload)
        if nodo_actual.hasLeftChild() and nodo_actual.key >= min:
            self.busqueda_rango(nodo_actual.leftChild, min, max, resultados)
        if nodo_actual.hasRightChild() and nodo_actual.key <= max:
                self.busqueda_rango(nodo_actual.rightChild, min, max, resultados)
        return resultados

    def obtener_ejercicios(self, id_concepto, bloom=None, dificultad=None):
        
        # CASO 1: El usuario solo pasó el concepto (Ej: "Dame todo el Tema 15")
        if bloom is None:
            min_score = self.rango_min(id_concepto)
            max_score = self.rango_max(id_concepto)
            
        # CASO 2: El usuario pasó concepto y Bloom (Ej: "Dame el Tema 15, nivel Bloom 3")
        elif dificultad is None:
            min_score = self.rango_min(id_concepto, bloom=bloom)
            max_score = self.rango_max(id_concepto, bloom=bloom)
            
        # CASO 3: El usuario pasó todo (Ej: "Dame ejercicios súper específicos")
        else:
            min_score = self.rango_min(id_concepto, bloom, dificultad)
            max_score = self.rango_max(id_concepto, bloom, dificultad)

        ejercicios = self.busqueda_rango(self.arbol.root, min_score, max_score)
        return ejercicios

  