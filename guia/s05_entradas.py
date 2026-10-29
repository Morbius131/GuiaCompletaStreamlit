from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="entradas",
    nombre="Widgets de entrada",
    icono="🎛️",
    intro=r"""
Los **widgets** devuelven el valor que el usuario elige y provocan un *rerun* al cambiar.
Parámetros comunes a casi todos: `key` (identificador único), `help` (ayuda emergente), `disabled`,
`on_change` (callback) y `label_visibility`.
""",
    ejemplos=[
        Ejemplo(
            titulo="st.button",
            desc="Devuelve `True` **solo en la ejecución** posterior al clic. Variantes con `type='primary'|'secondary'|'tertiary'` e iconos.",
            codigo=r"""
import streamlit as st

if st.button("Haz clic aquí", key="btn_basico"):
    st.write("¡Botón presionado! 🎉")

st.button("Botón primario", type="primary", icon=":material/rocket_launch:", key="btn_primario")
st.button("Deshabilitado", disabled=True, key="btn_deshab")
""",
        ),
        Ejemplo(
            titulo="st.checkbox y st.toggle",
            desc="Valores booleanos. `toggle` es un interruptor.",
            codigo=r"""
import streamlit as st

acepto = st.checkbox("Acepto los términos", key="chk_terminos")
modo = st.toggle("Activar modo avanzado", key="tgl_avanzado")

st.write("Términos aceptados:", acepto)
st.write("Modo avanzado:", modo)
""",
        ),
        Ejemplo(
            titulo="st.radio",
            desc="Una opción entre varias. `horizontal=True` las pone en fila; `index=None` deja sin selección inicial.",
            codigo=r"""
import streamlit as st

genero = st.radio("Película favorita", ["Comedia", "Drama", "Documental"], horizontal=True, key="radio_peli")
st.write("Elegiste:", genero)

sin_defecto = st.radio("Sin valor inicial", ["Sí", "No"], index=None, key="radio_sin_defecto")
st.write("Elegiste:", sin_defecto)
""",
        ),
        Ejemplo(
            titulo="st.selectbox",
            desc="Lista desplegable con búsqueda. `index=None` + `placeholder` para empezar vacío.",
            codigo=r"""
import streamlit as st

opcion = st.selectbox(
    "¿Cómo prefieres que te contacten?",
    ["Email", "Teléfono", "WhatsApp"],
    index=None,
    placeholder="Selecciona una opción...",
    key="sel_contacto",
)
st.write("Elegiste:", opcion)
""",
        ),
        Ejemplo(
            titulo="st.multiselect",
            desc="Varias opciones. Devuelve una lista. `max_selections` limita la cantidad.",
            codigo=r"""
import streamlit as st

colores = st.multiselect(
    "Elige hasta 3 colores",
    ["Rojo", "Verde", "Azul", "Amarillo", "Negro"],
    default=["Verde"],
    max_selections=3,
    key="multi_colores",
)
st.write("Elegiste:", colores)
""",
        ),
        Ejemplo(
            titulo="st.slider y st.select_slider",
            desc="Un valor, un rango (tupla), fechas… `select_slider` elige entre valores discretos.",
            codigo=r"""
import datetime
import streamlit as st

edad = st.slider("Edad", 0, 100, 25, key="sl_edad")
rango = st.slider("Rango", 0.0, 100.0, (25.0, 75.0), key="sl_rango")
fecha = st.slider("Fecha", datetime.date(2026, 1, 1), datetime.date(2026, 12, 31),
                  datetime.date(2026, 6, 15), key="sl_fecha")
talla = st.select_slider("Talla", options=["XS", "S", "M", "L", "XL"], value="M", key="sl_talla")

st.write(edad, rango, fecha, talla)
""",
        ),
        Ejemplo(
            titulo="st.text_input y st.text_area",
            desc="Texto de una línea o multilínea. `type='password'` oculta los caracteres; `max_chars`, `placeholder`.",
            codigo=r"""
import streamlit as st

nombre = st.text_input("Nombre completo", placeholder="Ej: Ana Pérez", max_chars=40, key="ti_nombre")
clave = st.text_input("Contraseña", type="password", key="ti_clave")
mensaje = st.text_area("Mensaje", height=100, key="ta_mensaje")

st.write("Nombre:", nombre, "| Largo de la clave:", len(clave), "| Palabras:", len(mensaje.split()))
""",
        ),
        Ejemplo(
            titulo="st.number_input",
            desc="Número entero o decimal con límites y paso.",
            codigo=r"""
import streamlit as st

n = st.number_input("Cantidad", min_value=0, max_value=100, value=5, step=1, key="ni_cantidad")
precio = st.number_input("Precio", min_value=0.0, value=9.99, step=0.5, format="%.2f", key="ni_precio")
st.write("Total:", n * precio)
""",
        ),
        Ejemplo(
            titulo="st.date_input y st.time_input",
            desc="Fecha (una o un rango) y hora.",
            codigo=r"""
import datetime
import streamlit as st

d = st.date_input("Fecha de inicio", datetime.date(2026, 10, 29), key="di_inicio")
rango = st.date_input("Rango de fechas",
                      (datetime.date(2026, 1, 1), datetime.date(2026, 1, 31)), key="di_rango")
h = st.time_input("Hora", datetime.time(8, 30), key="ti_hora")

st.write(d, rango, h)
""",
        ),
        Ejemplo(
            titulo="st.color_picker",
            desc="Selector de color; devuelve un string hexadecimal.",
            codigo=r"""
import streamlit as st

color = st.color_picker("Elige un color", "#E4572E", key="cp_color")
st.markdown(f"<div style='height:40px;border-radius:6px;background:{color}'></div>", unsafe_allow_html=True)
st.write("Hex:", color)
""",
        ),
        Ejemplo(
            titulo="st.pills y st.segmented_control",
            desc="Selectores en forma de «píldoras» o control segmentado. `selection_mode='multi'` permite varias.",
            codigo=r"""
import streamlit as st

temas = st.pills("Temas de interés", ["Datos", "IA", "Web", "VR"], selection_mode="multi", key="pills_temas")
vista = st.segmented_control("Vista", ["Lista", "Tarjetas", "Tabla"], default="Lista", key="seg_vista")

st.write("Temas:", temas)
st.write("Vista:", vista)
""",
        ),
        Ejemplo(
            titulo="st.feedback — valoración",
            desc="Estrellas, pulgares o caritas. Devuelve un índice (0..n-1) o `None`.",
            codigo=r"""
import streamlit as st

estrellas = st.feedback("stars", key="fb_estrellas")
pulgares = st.feedback("thumbs", key="fb_pulgares")
st.write("Estrellas (0‑4):", estrellas, "| Pulgares (0=👎, 1=👍):", pulgares)
""",
        ),
        Ejemplo(
            titulo="st.download_button",
            desc="Descarga datos generados por tu app (CSV, JSON, imágenes, PDF…).",
            codigo=r"""
import pandas as pd
import streamlit as st

df = pd.DataFrame({"a": [1, 2, 3], "b": ["x", "y", "z"]})
csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    "Descargar CSV",
    data=csv,
    file_name="datos.csv",
    mime="text/csv",
    icon=":material/download:",
    key="dl_csv",
)
""",
        ),
        Ejemplo(
            titulo="st.link_button",
            desc="Botón que abre una URL en una pestaña nueva.",
            codigo=r"""
import streamlit as st

st.link_button("Ir a la documentación", "https://docs.streamlit.io", icon=":material/menu_book:")
""",
        ),
    ],
)
