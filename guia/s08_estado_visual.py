from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="mensajes",
    nombre="Mensajes y progreso",
    icono="💬",
    intro=r"""
Comunica el estado de la app al usuario: mensajes de éxito/aviso/error, barras de progreso, spinners y notificaciones.
""",
    ejemplos=[
        Ejemplo(
            titulo="st.success / info / warning / error",
            desc="Cuadros de mensaje de color. Aceptan Markdown e `icon`.",
            codigo=r"""
import streamlit as st

st.success("Operación completada correctamente.", icon="✅")
st.info("Información útil para el usuario.")
st.warning("Cuidado: esta acción no se puede deshacer.")
st.error("Algo salió mal. Intenta de nuevo.")
""",
        ),
        Ejemplo(
            titulo="st.exception",
            desc="Muestra una excepción con su traza (útil dentro de `try/except`).",
            codigo=r"""
import streamlit as st

try:
    1 / 0
except ZeroDivisionError as e:
    st.exception(e)
""",
        ),
        Ejemplo(
            titulo="st.progress — barra de progreso",
            desc="Valor de 0 a 100 (o 0.0 a 1.0). Actualízala dentro de un bucle.",
            codigo=r"""
import time
import streamlit as st

if st.button("Iniciar proceso", key="prog_btn"):
    barra = st.progress(0, text="Procesando...")
    for i in range(100):
        time.sleep(0.01)
        barra.progress(i + 1, text=f"Procesando... {i + 1}%")
    barra.empty()
    st.success("¡Proceso terminado!")
""",
        ),
        Ejemplo(
            titulo="st.spinner",
            desc="Indicador de «cargando» mientras se ejecuta el bloque `with`.",
            codigo=r"""
import time
import streamlit as st

if st.button("Calcular algo pesado", key="spin_btn"):
    with st.spinner("Calculando..."):
        time.sleep(1.5)
    st.success("¡Listo!")
""",
        ),
        Ejemplo(
            titulo="st.status — contenedor de estado",
            desc="Muestra pasos de un proceso largo y cambia su estado final (`running`, `complete`, `error`).",
            codigo=r"""
import time
import streamlit as st

if st.button("Ejecutar pipeline", key="status_btn"):
    with st.status("Ejecutando pipeline...", expanded=True) as estado:
        st.write("📥 Descargando datos...")
        time.sleep(0.6)
        st.write("🧹 Limpiando...")
        time.sleep(0.6)
        st.write("🧠 Entrenando modelo...")
        time.sleep(0.6)
        estado.update(label="Pipeline completado", state="complete", expanded=False)
""",
        ),
        Ejemplo(
            titulo="st.toast",
            desc="Notificación emergente temporal en la esquina de la pantalla.",
            codigo=r"""
import streamlit as st

if st.button("Mostrar toast", key="toast_btn"):
    st.toast("Cambios guardados", icon="💾")
""",
        ),
        Ejemplo(
            titulo="st.balloons / st.snow",
            desc="Animaciones de celebración 🎈❄️.",
            codigo=r"""
import streamlit as st

c1, c2 = st.columns(2)
if c1.button("🎈 Globos", key="fx_balloons"):
    st.balloons()
if c2.button("❄️ Nieve", key="fx_snow"):
    st.snow()
""",
        ),
    ],
)
