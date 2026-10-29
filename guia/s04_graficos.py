from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="graficos",
    nombre="Gráficos y mapas",
    icono="📈",
    intro=r"""
Streamlit incluye gráficos nativos rápidos de usar (`line_chart`, `bar_chart`, …) y soporta las librerías más conocidas:
**Matplotlib**, **Altair**, **Plotly**, **Vega‑Lite**, entre otras.
""",
    ejemplos=[
        Ejemplo(
            titulo="st.line_chart y st.area_chart",
            desc="Gráficos de líneas/áreas con una sola línea de código. Cada columna del DataFrame es una serie.",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

rng = np.random.default_rng(42)
df = pd.DataFrame(rng.standard_normal((30, 3)).cumsum(axis=0), columns=["a", "b", "c"])

st.line_chart(df)
st.area_chart(df, stack=False)
""",
        ),
        Ejemplo(
            titulo="st.bar_chart",
            desc="Barras verticales u horizontales (`horizontal=True`), apiladas o agrupadas (`stack=False`).",
            codigo=r"""
import pandas as pd
import streamlit as st

df = pd.DataFrame({
    "Mes": ["Ene", "Feb", "Mar", "Abr"],
    "Ventas": [120, 150, 90, 180],
    "Costos": [80, 95, 70, 110],
})

st.bar_chart(df, x="Mes", y=["Ventas", "Costos"], stack=False)
st.bar_chart(df, x="Mes", y="Ventas", horizontal=True, color="#E4572E")
""",
        ),
        Ejemplo(
            titulo="st.scatter_chart",
            desc="Dispersión con color y tamaño dependientes de columnas.",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

rng = np.random.default_rng(1)
df = pd.DataFrame({
    "x": rng.normal(size=60),
    "y": rng.normal(size=60),
    "tamaño": rng.integers(20, 200, size=60),
    "grupo": rng.choice(["A", "B", "C"], size=60),
})

st.scatter_chart(df, x="x", y="y", size="tamaño", color="grupo")
""",
        ),
        Ejemplo(
            titulo="st.map — mapa de puntos",
            desc="Necesita columnas `lat` y `lon` (también acepta `latitude`/`longitude`).",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

rng = np.random.default_rng(7)
puntos = pd.DataFrame({
    "lat": 4.711 + rng.normal(scale=0.03, size=40),    # alrededor de Bogotá
    "lon": -74.072 + rng.normal(scale=0.03, size=40),
})

st.map(puntos, size=60)
""",
        ),
        Ejemplo(
            titulo="st.pyplot — Matplotlib",
            desc="Pasa una figura de Matplotlib. Crea la figura con `plt.subplots()` (no uses `plt.show()`).",
            codigo=r"""
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

rng = np.random.default_rng(3)
fig, ax = plt.subplots(figsize=(6, 3))
ax.hist(rng.normal(size=500), bins=25, color="#E4572E", alpha=0.85)
ax.set_title("Histograma")
st.pyplot(fig)
""",
        ),
        Ejemplo(
            titulo="st.altair_chart — Altair",
            desc="Gráficos declarativos e interactivos (zoom, tooltips). Altair viene instalado con Streamlit.",
            codigo=r"""
import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

rng = np.random.default_rng(5)
df = pd.DataFrame({
    "x": rng.normal(size=80),
    "y": rng.normal(size=80),
    "grupo": rng.choice(["A", "B", "C"], size=80),
})

grafico = (
    alt.Chart(df)
    .mark_circle(size=70)
    .encode(x="x", y="y", color="grupo", tooltip=["x", "y", "grupo"])
    .interactive()
)
st.altair_chart(grafico, width="stretch")
""",
        ),
        Ejemplo(
            titulo="st.plotly_chart — Plotly",
            desc="Gráficos interactivos de Plotly. Requiere `pip install plotly`.",
            codigo=r"""
import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.DataFrame({
    "Categoría": ["A", "B", "C", "D"],
    "Valor": [23, 45, 12, 36],
})

fig = px.pie(df, names="Categoría", values="Valor", hole=0.4, title="Distribución")
st.plotly_chart(fig, width="stretch")
""",
        ),
        Ejemplo(
            titulo="st.vega_lite_chart — especificación Vega‑Lite",
            desc="Para quien quiere controlar la especificación JSON completa del gráfico.",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

rng = np.random.default_rng(9)
df = pd.DataFrame(rng.standard_normal((60, 3)), columns=["a", "b", "c"])

st.vega_lite_chart(df, {
    "mark": {"type": "circle", "tooltip": True},
    "encoding": {
        "x": {"field": "a", "type": "quantitative"},
        "y": {"field": "b", "type": "quantitative"},
        "size": {"field": "c", "type": "quantitative"},
        "color": {"field": "c", "type": "quantitative"},
    },
}, width="stretch")
""",
        ),
    ],
)
