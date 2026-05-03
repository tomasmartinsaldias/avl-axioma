import streamlit as st
from motor import MotorAxioma
from generador import creador_ejercicios, creador_diccionario

DICCIONARIO_CONCEPTOS, DICCIONARIO_INVERSO = creador_diccionario()

# --- INICIALIZACIÓN ---
if 'motor' not in st.session_state:
    st.session_state.motor = MotorAxioma()
    # Población inicial
    creador_ejercicios(st.session_state.motor.arbol, 3000)

if 'filtros' not in st.session_state:
    st.session_state.filtros = None

if 'resultados' not in st.session_state:
    st.session_state.resultados = []

if st.sidebar.button("Reiniciar y Repoblar Árbol"):
    # Borramos el motor de la sesión para que se vuelva a inicializar con los nuevos valores
    if 'motor' in st.session_state:
        del st.session_state.motor
    st.rerun()

def fetch_resultados():
    if st.session_state.filtros:
        f = st.session_state.filtros
        st.session_state.resultados = st.session_state.motor.obtener_ejercicios(
            f['id_concepto'], 
            bloom=f['bloom'], 
            dificultad=f['dificultad']
        )

st.title("Axioma: Gestión de Ejercicios AVL")

# --- BARRA LATERAL (FILTROS) ---
st.sidebar.header("Filtros de Búsqueda")
# Usamos el diccionario inverso para obtener el ID a partir del nombre
nombre_seleccionado = st.sidebar.selectbox("Concepto", list(DICCIONARIO_CONCEPTOS.values()))
id_concepto = DICCIONARIO_INVERSO[nombre_seleccionado]

bloom = st.sidebar.slider("Nivel Bloom (Opcional)", 0, 6, 0)
bloom_val = bloom if bloom > 0 else None

dificultad = st.sidebar.slider("Dificultad (Opcional)", 0, 99, 0)
dificultad_val = dificultad if dificultad > 0 else None

if st.sidebar.button("Buscar Ejercicios"):
    st.session_state.filtros = {
        'id_concepto': id_concepto,
        'bloom': bloom_val,
        'dificultad': dificultad_val
    }
    fetch_resultados()

# --- CUERPO PRINCIPAL ---
if st.session_state.filtros is not None:
    if st.session_state.resultados:
        st.write(f"Se encontraron {len(st.session_state.resultados)} ejercicios.")
        
        # Preparamos una lista de strings para el selector de selección única
        opciones = {f"Score: {ej.score} | Bloom: {ej.bloom} | Dif: {ej.dificultad}": ej 
                    for ej in st.session_state.resultados}
        
        seleccion = st.selectbox("Selecciona un ejercicio para operar:", list(opciones.keys()))
        ejercicio_actual = opciones[seleccion]

        col1, col2 = st.columns(2)

        with col1:
            st.subheader("Actualizar")
            nueva_dif = st.number_input("Nueva Dificultad", 1, 99, value=ejercicio_actual.dificultad)
            if st.button("Aplicar Cambio"):
                st.session_state.motor.actualizar_dificultad(ejercicio_actual, nueva_dif)
                st.success("Dificultad actualizada y árbol rebalanceado.")
                fetch_resultados() # Refrescamos los resultados para evitar inconsistencias
                st.rerun()

        with col2:
            st.subheader("Eliminar")
            if st.button("Eliminar Ejercicio", type="primary"):
                st.session_state.motor.arbol.delete(ejercicio_actual.score)
                st.warning("Ejercicio eliminado.")
                fetch_resultados() # Refrescamos los resultados para sacar el eliminado de la lista
                st.rerun()
    else:
        st.warning("No se encontraron ejercicios con esos parámetros.")
else:
    st.info("Usa los filtros laterales para buscar ejercicios en el árbol AVL.")