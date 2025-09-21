import streamlit as st

st.title("Test de Selección – Entrenador Comercial ArchViz")

# Preguntas y respuestas correctas (V=Verdadero, F=Falso)
preguntas = [
    ("El trabajo en ventas B2B siempre puede comenzar sin anticipo.", "F"),
    ("La trazabilidad debe quedar siempre en email.", "V"),
    ("En ArchViz es correcto aplicar uplift por una sola imagen.", "V"),
    ("Un Change Order se aplica si hay nuevas vistas post-blockout.", "V"),
    ("El feedback consolidado en =5 días evita retrasos.", "V"),
    ("Una animación de 30s se cobra por segundo + modelado.", "V"),
    ("Enseñar sin práctica es suficiente para un equipo pequeño.", "F"),
    ("Un capacitador debe adaptar a distintos estilos de aprendizaje.", "V"),
    ("Flujo estándar: Blockout 1 ronda, Color 2 rondas, finales 5K.", "V"),
    ("Si el cliente pide rondas extra sin pagar, se cierra con la última versión aprobada.", "V")
]

# Estado del candidato
if "indice" not in st.session_state:
    st.session_state.indice = 0
if "activo" not in st.session_state:
    st.session_state.activo = True

nombre = st.text_input("Ingresá tu nombre antes de comenzar:")

if nombre and st.session_state.activo:
    pregunta, respuesta_correcta = preguntas[st.session_state.indice]
    st.write(f"**Pregunta {st.session_state.indice+1}:** {pregunta}")

    opcion = st.radio("Elegí una opción:", ["V", "F"])

    if st.button("Responder"):
        if opcion == respuesta_correcta:
            st.success("¡Correcto! Pasás a la siguiente.")
            st.session_state.indice += 1
            if st.session_state.indice == len(preguntas):
                st.balloons()
                st.success(f"¡Felicitaciones {nombre}, completaste el test!")
                st.session_state.activo = False
        else:
            st.error("Respuesta incorrecta. El test finalizó.")
            st.session_state.activo = False
