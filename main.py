from motor import MotorAxioma
from generador import creador_ejercicios, creador_diccionario

diccionario, dict_inverso = creador_diccionario()

def imprimir_resultados(resultados, id_c):
    if resultados:
        print(f"Se encontraron {len(resultados)} ejercicios para el Concepto {diccionario[id_c]}.")
        print("El recorrido Inorder debería mostrarlos ordenados por Bloom y Dificultad:")
        print("-" * 50)
        for ej in resultados:
            print(f"Score: {ej.score} | Bloom: {ej.bloom} | Dificultad: {ej.dificultad} | ID Local: {ej.id_ejercicio}")
    else:
        print(f"No se generaron ejercicios aleatorios con los requisitos buscados.")

# 1. Inicializamos el motor
motor = MotorAxioma()

# 2. Generamos 10,000 ejercicios aleatorios
# (Usamos un número grande para garantizar que haya varios del mismo concepto)
print("Generando 10,000 ejercicios sintéticos...")
creador_ejercicios(motor.arbol, 10000)
print(f"Total de nodos en el AVL: {motor.arbol.size}")

# 3. Probamos la búsqueda para un concepto
def return_resultados():
    id_c = int(input("Ingrese el ID del concepto a buscar: "))
    id_b = input("Ingrese el nivel de Bloom a buscar (o deje vacío para omitir): ")
    if id_b:
        id_d = input("Ingrese el nivel de dificultad a buscar (o deje vacío para omitir): ")
    if not id_b:
        resultados = motor.obtener_ejercicios(id_concepto=id_c)
    elif not id_d:
        resultados = motor.obtener_ejercicios(id_concepto=id_c, bloom=int(id_b))
    else: resultados = motor.obtener_ejercicios(id_concepto=id_c, bloom=int(id_b), dificultad=int(id_d))
    return resultados, id_c
    
resultados, id_concepto = return_resultados()
imprimir_resultados(resultados, id_concepto)

