"""Renderiza ejemplos: muestra el código y lo ejecuta en vivo.

El código que se muestra es EXACTAMENTE el que se ejecuta (via exec), por lo que
lo que ves en pantalla siempre coincide con el resultado.
"""
import linecache
import re
import textwrap

import streamlit as st


def _slug(texto: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", texto.lower()).strip("-")


def ejecutar_codigo(codigo: str, clave: str) -> None:
    """Ejecuta un snippet registrando su fuente en linecache.

    Registrar la fuente permite que st.cache_data / st.fragment / st.echo
    puedan inspeccionar el código de funciones definidas dentro del snippet.
    """
    nombre_archivo = f"<ejemplo:{clave}>"
    linecache.cache[nombre_archivo] = (
        len(codigo),
        None,
        codigo.splitlines(True),
        nombre_archivo,
    )
    espacio = {"__name__": "__ejemplo__"}
    try:
        exec(compile(codigo, nombre_archivo, "exec"), espacio)
    except Exception as e:  # noqa: BLE001
        # Las excepciones de control de Streamlit (st.rerun / st.stop) deben propagarse.
        if type(e).__module__.startswith("streamlit.runtime.scriptrunner"):
            raise
        st.exception(e)


def render_ejemplo(ej, seccion_clave: str, layout: str = "Apilado") -> None:
    codigo = textwrap.dedent(ej.codigo).strip("\n")
    clave = f"{seccion_clave}-{_slug(ej.titulo)}"

    st.markdown(f"#### {ej.titulo}")
    if ej.desc:
        st.markdown(ej.desc)

    if not ej.ejecutar:
        st.code(codigo, language=ej.lenguaje)
        return

    if layout == "Lado a lado":
        col_codigo, col_resultado = st.columns(2, gap="medium")
        with col_codigo:
            st.caption("Código")
            st.code(codigo, language=ej.lenguaje, wrap_lines=True)
        with col_resultado:
            st.caption("Resultado en vivo")
            with st.container(border=True):
                ejecutar_codigo(codigo, clave)
    else:
        st.code(codigo, language=ej.lenguaje)
        st.caption("▼ Resultado en vivo")
        with st.container(border=True):
            ejecutar_codigo(codigo, clave)


def render_seccion(seccion, layout: str = "Apilado") -> None:
    st.title(f"{seccion.icono} {seccion.nombre}")
    if seccion.intro:
        st.markdown(textwrap.dedent(seccion.intro).strip())
    for i, ej in enumerate(seccion.ejemplos):
        st.divider()
        render_ejemplo(ej, seccion.clave, layout)
