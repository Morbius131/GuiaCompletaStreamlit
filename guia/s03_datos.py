from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="datos",
    nombre="Datos y tablas",
    icono="📊",
    intro=r"""
Muestra y edita datos tabulares con `st.dataframe`, `st.data_editor` y `st.table`, o resalta cifras clave con `st.metric`.
La configuración de columnas (`st.column_config`) permite barras de progreso, enlaces, mini‑gráficos y más.
""",
    ejemplos=[
        Ejemplo(
            titulo="st.dataframe — tabla interactiva",
            desc="Ordenable, con búsqueda y descarga. Acepta DataFrames de pandas (incluidos `Styler`), listas, dicts, Polars, etc.",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

rng = np.random.default_rng(0)
df = pd.DataFrame(rng.standard_normal((8, 4)), columns=["A", "B", "C", "D"])

st.dataframe(df, width="stretch")
st.caption("Con estilos de pandas (resaltar máximos):")
st.dataframe(df.style.highlight_max(axis=0).format("{:.2f}"), width="stretch")
""",
        ),
        Ejemplo(
            titulo="st.dataframe — selección de filas",
            desc="Con `on_select='rerun'` obtienes las filas que el usuario selecciona.",
            codigo=r"""
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "Ciudad": ["Bogotá", "Medellín", "Cali", "Villavicencio", "Barranquilla"],
    "Habitantes (miles)": [7900, 2570, 2280, 560, 1280],
})

evento = st.dataframe(
    df,
    hide_index=True,
    on_select="rerun",
    selection_mode="multi-row",
    key="datos_sel_filas",
)
filas = evento.selection.rows
st.write("Filas seleccionadas:", filas)
if filas:
    st.write(df.iloc[filas])
""",
        ),
        Ejemplo(
            titulo="st.column_config — columnas con formato",
            desc="Barras de progreso, enlaces, casillas, mini‑gráficos de línea y formatos numéricos.",
            codigo=r"""
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "Proyecto": ["Alpha", "Beta", "Gamma"],
    "Avance": [80, 55, 95],
    "Sitio": ["https://streamlit.io", "https://docs.streamlit.io", "https://python.org"],
    "Tendencia": [[1, 3, 2, 5, 4], [2, 2, 3, 3, 5], [5, 4, 4, 6, 7]],
    "Activo": [True, True, False],
    "Presupuesto": [1_200_000, 800_000, 450_000],
})

st.dataframe(
    df,
    hide_index=True,
    width="stretch",
    column_config={
        "Avance": st.column_config.ProgressColumn("Avance", min_value=0, max_value=100, format="%d%%"),
        "Sitio": st.column_config.LinkColumn("Sitio web"),
        "Tendencia": st.column_config.LineChartColumn("Tendencia"),
        "Activo": st.column_config.CheckboxColumn("¿Activo?"),
        "Presupuesto": st.column_config.NumberColumn("Presupuesto", format="$%d"),
    },
)
""",
        ),
        Ejemplo(
            titulo="st.data_editor — tabla editable",
            desc="El usuario edita celdas, añade o borra filas (`num_rows='dynamic'`). Devuelve el DataFrame editado.",
            codigo=r"""
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "Tarea": ["Diseñar", "Programar", "Probar"],
    "Estado": ["Hecho", "En curso", "Pendiente"],
    "Horas": [4, 10, 3],
})

editado = st.data_editor(
    df,
    num_rows="dynamic",
    hide_index=True,
    width="stretch",
    key="datos_editor",
    column_config={
        "Estado": st.column_config.SelectboxColumn("Estado", options=["Pendiente", "En curso", "Hecho"]),
        "Horas": st.column_config.NumberColumn("Horas", min_value=0, step=1),
    },
)
st.metric("Total de horas", int(editado["Horas"].sum()))
""",
        ),
        Ejemplo(
            titulo="st.table — tabla estática",
            desc="Sin interactividad: muestra todo el contenido. Útil para tablas pequeñas.",
            codigo=r"""
import pandas as pd
import streamlit as st

st.table(pd.DataFrame({"Plan": ["Básico", "Pro"], "Precio": ["$0", "$20"], "Usuarios": [1, 10]}))
""",
        ),
        Ejemplo(
            titulo="st.metric — indicadores (KPI)",
            desc="Valor grande con variación (`delta`). Úsalo con `st.columns` para tableros.",
            codigo=r"""
import streamlit as st

c1, c2, c3 = st.columns(3)
c1.metric("Temperatura", "24 °C", "1.2 °C")
c2.metric("Ventas", "$ 12.4 M", "-8%")
c3.metric("Usuarios", "1.250", "+120", delta_color="off")
st.metric("Con borde", "98 %", "2 %", border=True)
""",
        ),
        Ejemplo(
            titulo="st.json — objetos JSON",
            desc="Visualizador expandible/colapsable de JSON. Ideal para respuestas de APIs.",
            codigo=r"""
import streamlit as st

st.json({
    "proyecto": "demo",
    "version": 1.2,
    "autores": ["Ana", "Luis"],
    "config": {"debug": False, "puerto": 8501},
}, expanded=2)
""",
        ),
    ],
)
