from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="sesion",
    nombre="Estado de sesión y callbacks",
    icono="🧠",
    intro=r"""
`st.session_state` es un diccionario que **persiste entre ejecuciones** dentro de la misma sesión del navegador.
Es la herramienta para contadores, carritos, historiales, pasos de un asistente, etc.

> Regla de oro: no puedes modificar `st.session_state[key]` de un widget **después** de crearlo en la misma ejecución;
> hazlo dentro de un **callback** (`on_click` / `on_change`).
""",
    ejemplos=[
        Ejemplo(
            titulo="Contador básico",
            desc="Inicializa la clave una vez y modifícala al pulsar botones.",
            codigo=r"""
import streamlit as st

if "contador" not in st.session_state:
    st.session_state.contador = 0

c1, c2, c3 = st.columns(3)
if c1.button("➕ Sumar", key="ss_sumar"):
    st.session_state.contador += 1
if c2.button("➖ Restar", key="ss_restar"):
    st.session_state.contador -= 1
if c3.button("🔄 Reiniciar", key="ss_reset"):
    st.session_state.contador = 0

st.metric("Contador", st.session_state.contador)
""",
        ),
        Ejemplo(
            titulo="Callbacks con on_click y args",
            desc="Los callbacks se ejecutan **antes** del rerun, así que pueden cambiar el estado de widgets sin errores.",
            codigo=r"""
import streamlit as st

if "cb_total" not in st.session_state:
    st.session_state.cb_total = 0

def sumar(cantidad):
    st.session_state.cb_total += cantidad

st.button("+1", on_click=sumar, args=(1,), key="cb_1")
st.button("+10", on_click=sumar, kwargs={"cantidad": 10}, key="cb_10")
st.write("Total:", st.session_state.cb_total)
""",
        ),
        Ejemplo(
            titulo="Widgets enlazados con key",
            desc="Al dar `key` a un widget, su valor vive en `st.session_state[key]`. Puedes leerlo en cualquier parte y resetearlo con un callback.",
            codigo=r"""
import streamlit as st

# Valores iniciales en session_state (así el widget no necesita un "value" por defecto)
st.session_state.setdefault("ss_nombre", "")
st.session_state.setdefault("ss_nivel", 5)

st.text_input("Tu nombre", key="ss_nombre")
st.slider("Tu nivel", 0, 10, key="ss_nivel")

def limpiar():
    st.session_state.ss_nombre = ""
    st.session_state.ss_nivel = 5

st.button("Limpiar campos", on_click=limpiar, key="ss_limpiar")
st.write(f"Hola, {st.session_state.ss_nombre or 'desconocido'} — nivel {st.session_state.ss_nivel}")
""",
        ),
        Ejemplo(
            titulo="Lista de tareas (persistir una lista)",
            desc="Un patrón muy común: guardar una lista en `session_state` y añadir elementos con `on_change`.",
            codigo=r"""
import streamlit as st

if "tareas" not in st.session_state:
    st.session_state.tareas = ["Aprender Streamlit"]

def agregar():
    texto = st.session_state.nueva_tarea.strip()
    if texto:
        st.session_state.tareas.append(texto)
    st.session_state.nueva_tarea = ""

st.text_input("Nueva tarea (Enter para añadir)", key="nueva_tarea", on_change=agregar)

for i, t in enumerate(st.session_state.tareas, start=1):
    st.write(f"{i}. {t}")

if st.button("Vaciar lista", key="vaciar_tareas"):
    st.session_state.tareas = []
    st.rerun()
""",
        ),
        Ejemplo(
            titulo="Asistente por pasos (wizard)",
            desc="Guarda en qué paso va el usuario y muestra contenido distinto según el paso.",
            codigo=r"""
import streamlit as st

if "paso" not in st.session_state:
    st.session_state.paso = 1

def ir(n):
    st.session_state.paso = n

paso = st.session_state.paso
st.progress(paso / 3, text=f"Paso {paso} de 3")

if paso == 1:
    st.write("👋 Bienvenido al asistente.")
    st.button("Siguiente →", on_click=ir, args=(2,), key="wz_s1")
elif paso == 2:
    st.text_input("Escribe tu correo", key="wz_correo")
    st.button("← Atrás", on_click=ir, args=(1,), key="wz_a2")
    st.button("Siguiente →", on_click=ir, args=(3,), key="wz_s2")
else:
    st.success(f"¡Listo! Correo registrado: {st.session_state.get('wz_correo', '')}")
    st.button("Reiniciar", on_click=ir, args=(1,), key="wz_r3")
""",
        ),
        Ejemplo(
            titulo="Inspeccionar el estado",
            desc="`st.session_state` se puede mostrar como cualquier diccionario (útil para depurar).",
            codigo=r"""
import streamlit as st

st.session_state.setdefault("depuracion", "valor inicial")
st.write(dict(st.session_state))
""",
        ),
    ],
)
