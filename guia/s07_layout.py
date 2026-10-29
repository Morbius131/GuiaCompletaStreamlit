from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="layout",
    nombre="Layout y contenedores",
    icono="🧱",
    intro=r"""
Organiza la página con barra lateral, columnas, pestañas, expanders, contenedores, popovers, diálogos y formularios.
Los contenedores se usan con `with` (o llamando métodos sobre el objeto devuelto).
""",
    ejemplos=[
        Ejemplo(
            titulo="st.sidebar — barra lateral",
            desc="Cualquier elemento dentro de `with st.sidebar:` (o `st.sidebar.xxx`) aparece en la barra lateral. **Mira la barra lateral de esta página 👈**: se añade un bloque al final.",
            codigo=r"""
import streamlit as st

with st.sidebar:
    st.divider()
    st.subheader("Demo de sidebar")
    opcion = st.selectbox("Filtro de ejemplo", ["Todos", "Activos", "Inactivos"], key="sb_filtro")
    st.caption("Contenido dentro de st.sidebar")

st.write("Filtro elegido en la barra lateral:", opcion)
""",
        ),
        Ejemplo(
            titulo="st.columns — columnas",
            desc="Reparte el ancho. Pasa un entero o proporciones (`[3, 1]`). Opciones: `gap`, `vertical_alignment`, `border`.",
            codigo=r"""
import streamlit as st

col1, col2, col3 = st.columns([2, 1, 1], gap="medium", border=True)

with col1:
    st.subheader("Columna ancha")
    st.write("Ocupa el doble de espacio.")
col2.metric("Ventas", "1.200", "+5%")
col3.button("Acción", key="col_btn")
""",
        ),
        Ejemplo(
            titulo="st.tabs — pestañas",
            desc="Agrupa contenido en pestañas. Todo el contenido se ejecuta, aunque no sea visible.",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

tab_grafico, tab_datos, tab_info = st.tabs(["📈 Gráfico", "🗃️ Datos", "ℹ️ Info"])

df = pd.DataFrame(np.random.default_rng(0).standard_normal((20, 2)), columns=["a", "b"])
with tab_grafico:
    st.line_chart(df)
with tab_datos:
    st.dataframe(df)
with tab_info:
    st.write("Información adicional aquí.")
""",
        ),
        Ejemplo(
            titulo="st.expander",
            desc="Sección plegable. Ideal para detalles opcionales.",
            codigo=r"""
import streamlit as st

with st.expander("Ver más detalles"):
    st.write("Este contenido está oculto hasta que se expande.")
    st.code("print('hola')")

with st.expander("Abierto por defecto", expanded=True, icon=":material/info:"):
    st.write("Este expander inicia abierto.")
""",
        ),
        Ejemplo(
            titulo="st.container",
            desc="Agrupa elementos y permite insertarlos en desorden. Soporta `border=True` y `height` (con scroll).",
            codigo=r"""
import streamlit as st

caja = st.container(border=True)
st.write("Esto se escribe fuera del contenedor, aunque lo creé primero.")
caja.write("Esto va dentro del contenedor (añadido después).")

with st.container(height=120, border=True):
    for i in range(1, 11):
        st.write(f"Línea {i} dentro de un contenedor con scroll")
""",
        ),
        Ejemplo(
            titulo="st.empty — marcador reemplazable",
            desc="Un «hueco» de un solo elemento que puedes reescribir: perfecto para contadores y animaciones.",
            codigo=r"""
import time
import streamlit as st

if st.button("Iniciar cuenta regresiva", key="empty_btn"):
    hueco = st.empty()
    for i in range(5, 0, -1):
        hueco.metric("Cuenta regresiva", i)
        time.sleep(0.4)
    hueco.success("¡Despegue! 🚀")
""",
        ),
        Ejemplo(
            titulo="st.popover — menú emergente",
            desc="Un botón que abre una pequeña ventana flotante con widgets.",
            codigo=r"""
import streamlit as st

with st.popover("Opciones de visualización"):
    st.checkbox("Mostrar cuadrícula", True, key="pop_grid")
    st.checkbox("Mostrar leyenda", key="pop_leyenda")
    st.slider("Opacidad", 0, 100, 80, key="pop_opacidad")
""",
        ),
        Ejemplo(
            titulo="st.dialog — ventana modal",
            desc="Decora una función con `@st.dialog` y llámala para abrir un modal. Usa `st.rerun()` para cerrarlo.",
            codigo=r"""
import streamlit as st

@st.dialog("Confirmar acción")
def confirmar():
    st.write("¿Seguro que deseas continuar?")
    if st.button("Sí, continuar", key="dlg_si"):
        st.session_state["dlg_confirmado"] = True
        st.rerun()

if st.button("Abrir diálogo", key="dlg_abrir"):
    confirmar()

if st.session_state.get("dlg_confirmado"):
    st.success("Acción confirmada ✅")
""",
        ),
        Ejemplo(
            titulo="st.form — agrupar widgets y enviar juntos",
            desc="Dentro de un formulario, la app **no se re‑ejecuta** hasta pulsar el botón de envío. Evita reruns innecesarios.",
            codigo=r"""
import streamlit as st

with st.form("form_contacto"):
    nombre = st.text_input("Tu nombre", key="form_nombre")
    edad = st.number_input("Tu edad", 0, 120, 30, key="form_edad")
    acepta = st.checkbox("Acepto recibir correos", key="form_acepta")
    enviado = st.form_submit_button("Enviar", type="primary")

if enviado:
    st.success(f"Gracias {nombre or '(sin nombre)'}, edad {edad}, correos: {acepta}")
""",
        ),
    ],
)
