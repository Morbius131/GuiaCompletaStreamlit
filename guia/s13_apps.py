from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="apps",
    nombre="Mini‑apps completas",
    icono="🧩",
    intro=r"""
Ejemplos que combinan varios componentes: filtros, métricas, gráficos, formularios y descargas.
Úsalos como plantilla para tus propias aplicaciones.
""",
    ejemplos=[
        Ejemplo(
            titulo="Dashboard de ventas con filtros",
            desc="Filtros en columnas, KPIs, gráfico, tabla y descarga del resultado filtrado.",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

@st.cache_data
def generar_datos():
    rng = np.random.default_rng(11)
    fechas = pd.date_range("2026-01-01", periods=180)
    regiones = rng.choice(["Norte", "Sur", "Centro"], size=180)
    return pd.DataFrame({
        "fecha": fechas,
        "region": regiones,
        "ventas": rng.integers(50, 500, size=180),
        "unidades": rng.integers(1, 40, size=180),
    })

df = generar_datos()

f1, f2 = st.columns(2)
regiones = f1.multiselect("Región", sorted(df["region"].unique()),
                          default=sorted(df["region"].unique()), key="dash_regiones")
minimo = f2.slider("Ventas mínimas", 50, 500, 100, key="dash_min")

filtrado = df[df["region"].isin(regiones) & (df["ventas"] >= minimo)]

k1, k2, k3 = st.columns(3)
k1.metric("Registros", len(filtrado))
k2.metric("Ventas totales", f"{filtrado['ventas'].sum():,}")
k3.metric("Ticket promedio", f"{filtrado['ventas'].mean():.0f}" if len(filtrado) else "–")

if filtrado.empty:
    st.warning("No hay datos con esos filtros.")
else:
    por_mes = filtrado.groupby(filtrado["fecha"].dt.to_period("M").astype(str))["ventas"].sum()
    st.bar_chart(por_mes)
    st.dataframe(filtrado, height=200, hide_index=True, width="stretch")
    st.download_button("Descargar CSV filtrado", filtrado.to_csv(index=False).encode("utf-8"),
                       "ventas_filtradas.csv", "text/csv", key="dash_descarga")
""",
        ),
        Ejemplo(
            titulo="Calculadora de IMC",
            desc="Formulario con validación y resultado interpretado.",
            codigo=r"""
import streamlit as st

with st.form("form_imc"):
    c1, c2 = st.columns(2)
    peso = c1.number_input("Peso (kg)", 20.0, 250.0, 70.0, step=0.5, key="imc_peso")
    altura = c2.number_input("Altura (cm)", 100, 230, 170, key="imc_altura")
    calcular = st.form_submit_button("Calcular", type="primary")

if calcular:
    imc = peso / ((altura / 100) ** 2)
    if imc < 18.5:
        estado, aviso = "Bajo peso", st.warning
    elif imc < 25:
        estado, aviso = "Peso normal", st.success
    elif imc < 30:
        estado, aviso = "Sobrepeso", st.warning
    else:
        estado, aviso = "Obesidad", st.error
    st.metric("Tu IMC", f"{imc:.1f}")
    aviso(estado)
""",
        ),
        Ejemplo(
            titulo="Explorador de CSV",
            desc="Sube un archivo, elige columnas y obtén estadísticas y un gráfico. Si no subes nada, usa datos de ejemplo.",
            codigo=r"""
import numpy as np
import pandas as pd
import streamlit as st

archivo = st.file_uploader("Sube un CSV (opcional)", type="csv", key="exp_csv")
if archivo:
    df = pd.read_csv(archivo)
else:
    rng = np.random.default_rng(2)
    df = pd.DataFrame(rng.standard_normal((100, 4)), columns=["a", "b", "c", "d"])
    st.caption("Mostrando datos de ejemplo.")

numericas = df.select_dtypes("number").columns.tolist()
elegidas = st.multiselect("Columnas a graficar", numericas, default=numericas[:2], key="exp_cols")

tab1, tab2, tab3 = st.tabs(["Vista previa", "Estadísticas", "Gráfico"])
tab1.dataframe(df.head(20))
tab2.dataframe(df.describe())
if elegidas:
    tab3.line_chart(df[elegidas])
else:
    tab3.info("Elige al menos una columna.")
""",
        ),
    ],
)
