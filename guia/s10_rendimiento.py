from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="rendimiento",
    nombre="Caché y rendimiento",
    icono="⚡",
    intro=r"""
Como el script se re‑ejecuta con cada interacción, es clave **no repetir trabajo costoso**:

| Herramienta | Úsala para |
|---|---|
| `@st.cache_data` | Datos serializables: DataFrames, listas, resultados de consultas/API |
| `@st.cache_resource` | Recursos globales: conexiones a BD, modelos de ML |
| `@st.fragment` | Re‑ejecutar solo una parte de la página |
""",
    ejemplos=[
        Ejemplo(
            titulo="@st.cache_data",
            desc="La primera vez tarda 1.5 s; con el mismo argumento después es instantáneo. `ttl` define cuánto dura la caché.",
            codigo=r"""
import time
import pandas as pd
import streamlit as st

@st.cache_data(ttl=300, show_spinner="Cargando datos...")
def cargar_datos(n):
    time.sleep(1.5)  # simula una consulta lenta
    return pd.DataFrame({"n": range(n), "cuadrado": [i ** 2 for i in range(n)]})

n = st.slider("Filas", 5, 50, 10, key="cd_filas")
inicio = time.time()
df = cargar_datos(n)
st.caption(f"Tardó {time.time() - inicio:.2f} s (pruébalo de nuevo con el mismo valor)")
st.dataframe(df, height=200)

if st.button("Limpiar caché de esta función", key="cd_limpiar"):
    cargar_datos.clear()
    st.toast("Caché limpiada")
""",
        ),
        Ejemplo(
            titulo="@st.cache_resource",
            desc="Crea el recurso **una sola vez** y lo comparte entre todas las sesiones y reruns (ideal para conexiones y modelos).",
            codigo=r"""
import sqlite3
import pandas as pd
import streamlit as st

@st.cache_resource
def obtener_conexion():
    conn = sqlite3.connect(":memory:", check_same_thread=False)
    conn.execute("CREATE TABLE personas (id INTEGER, nombre TEXT)")
    conn.executemany("INSERT INTO personas VALUES (?, ?)", [(1, "Ana"), (2, "Luis"), (3, "Marta")])
    return conn

conn = obtener_conexion()
st.dataframe(pd.read_sql("SELECT * FROM personas", conn), hide_index=True)
""",
        ),
        Ejemplo(
            titulo="@st.fragment — rerun parcial",
            desc="Al interactuar con widgets dentro del fragmento, **solo se re‑ejecuta el fragmento**, no toda la página.",
            codigo=r"""
import datetime
import streamlit as st

st.write("Hora de la página completa:", datetime.datetime.now().strftime("%H:%M:%S"))

@st.fragment
def zona_interactiva():
    st.write("Hora del fragmento:", datetime.datetime.now().strftime("%H:%M:%S"))
    if "frag_n" not in st.session_state:
        st.session_state.frag_n = 0
    if st.button("Sumar (solo re-ejecuta el fragmento)", key="frag_btn"):
        st.session_state.frag_n += 1
    st.write("Clics:", st.session_state.frag_n)

zona_interactiva()
""",
        ),
        Ejemplo(
            titulo="Fragmento que se actualiza solo (run_every)",
            desc="Con `run_every` el fragmento se refresca periódicamente: ideal para métricas «en vivo». (No se ejecuta aquí para no refrescar esta página sin parar.)",
            ejecutar=False,
            codigo=r"""
import datetime
import streamlit as st

@st.fragment(run_every="2s")
def reloj():
    st.metric("Hora actual", datetime.datetime.now().strftime("%H:%M:%S"))

reloj()
""",
        ),
        Ejemplo(
            titulo="st.rerun y st.stop",
            desc=(
                "`st.rerun()` relanza el script de inmediato. `st.stop()` detiene la ejecución en ese punto "
                "(útil para exigir login o campos obligatorios). No se ejecutan aquí porque interrumpirían esta página."
            ),
            ejecutar=False,
            codigo=r"""
import streamlit as st

nombre = st.text_input("Nombre (obligatorio)")
if not nombre:
    st.warning("Escribe tu nombre para continuar.")
    st.stop()          # ← nada de lo que sigue se ejecuta

st.success(f"Hola {nombre}")

if st.button("Aplicar cambios"):
    st.session_state["guardado"] = True
    st.rerun()         # ← vuelve a ejecutar el script desde arriba
""",
        ),
    ],
)
