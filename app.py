"""Guía interactiva de Streamlit — cada componente con demo en vivo y código.

Ejecutar localmente:   streamlit run app.py
"""
import streamlit as st

from guia import SECCIONES, buscar
from guia.runner import render_seccion

st.set_page_config(
    page_title="Guía interactiva de Streamlit",
    page_icon="📘",
    layout="wide",
    initial_sidebar_state="expanded",
)

POR_CLAVE = {s.clave: s for s in SECCIONES}
CLAVES = [s.clave for s in SECCIONES]


def etiqueta(clave: str) -> str:
    s = POR_CLAVE[clave]
    return f"{s.icono} {s.nombre}"


def ir_a(clave: str) -> None:
    """Callback: navega a una sección y limpia el buscador."""
    st.session_state.seccion_actual = clave
    st.session_state.buscador = ""


# ---------------------------------------------------------------- Barra lateral
with st.sidebar:
    st.markdown("## 📘 Guía de Streamlit")
    st.text_input("🔎 Buscar componente", key="buscador", placeholder="ej: slider, cache, form…")
    st.radio(
        "Categorías",
        CLAVES,
        format_func=etiqueta,
        key="seccion_actual",
        label_visibility="collapsed",
    )
    st.divider()
    st.radio(
        "Disposición de los ejemplos",
        ["Apilado", "Lado a lado"],
        key="layout_modo",
        help="«Lado a lado» muestra el código a la izquierda y el resultado a la derecha (mejor en pantallas anchas).",
    )
    st.caption(f"Streamlit {st.__version__}")

layout = st.session_state.get("layout_modo", "Apilado")
consulta = st.session_state.get("buscador", "").strip()

# ---------------------------------------------------------------- Contenido
if consulta:
    resultados = buscar(consulta)
    st.title(f"🔎 Resultados para «{consulta}»")
    if not resultados:
        st.info("No hay coincidencias. Prueba con otra palabra (por ejemplo: `button`, `chart`, `session_state`).")
    else:
        st.caption(f"{len(resultados)} ejemplo(s) encontrados. Pulsa uno para abrirlo en su categoría.")
        for i, (sec, ej) in enumerate(resultados):
            st.button(
                f"{sec.icono} {sec.nombre}  ›  {ej.titulo}",
                key=f"res_{i}",
                on_click=ir_a,
                args=(sec.clave,),
                width="stretch",
            )
else:
    seccion = POR_CLAVE[st.session_state.seccion_actual]
    render_seccion(seccion, layout)

    if seccion.clave == "inicio":
        st.divider()
        st.subheader("🗺️ Índice de categorías")
        columnas = st.columns(3)
        for i, s in enumerate(SECCIONES[1:], start=0):
            with columnas[i % 3]:
                with st.container(border=True):
                    st.markdown(f"**{s.icono} {s.nombre}**")
                    st.caption(f"{len(s.ejemplos)} ejemplos")
                    st.button("Abrir", key=f"idx_{s.clave}", on_click=ir_a, args=(s.clave,))
