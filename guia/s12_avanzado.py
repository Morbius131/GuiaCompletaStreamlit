from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="avanzado",
    nombre="Funciones avanzadas",
    icono="🛠️",
    intro=r"""
Configuración de página, apps multipágina, parámetros en la URL, secretos, conexiones a datos y más.
Varios de estos ejemplos solo se muestran como código porque afectan a la app completa (por ejemplo, `set_page_config`).
""",
    ejemplos=[
        Ejemplo(
            titulo="st.set_page_config",
            desc="Debe ser **la primera llamada de Streamlit** del script (una sola vez). Define título, icono, ancho y barra lateral.",
            ejecutar=False,
            codigo=r"""
import streamlit as st

st.set_page_config(
    page_title="Mi aplicación",
    page_icon="📘",
    layout="wide",                    # "centered" (por defecto) o "wide"
    initial_sidebar_state="expanded", # "auto" | "expanded" | "collapsed"
    menu_items={
        "Get help": "https://docs.streamlit.io",
        "Report a bug": "mailto:soporte@ejemplo.com",
        "About": "App creada con Streamlit",
    },
)
""",
        ),
        Ejemplo(
            titulo="Multipágina con st.navigation y st.Page",
            desc=(
                "Define las páginas en el archivo principal y Streamlit crea el menú de navegación automáticamente. "
                "Cada página es un archivo `.py` o una función."
            ),
            ejecutar=False,
            codigo=r"""
# app.py  (entrypoint)
import streamlit as st

def inicio():
    st.title("Inicio")

pagina_datos = st.Page("paginas/datos.py", title="Datos", icon=":material/table:")
pagina_graficos = st.Page("paginas/graficos.py", title="Gráficos", icon=":material/insights:")
pagina_inicio = st.Page(inicio, title="Inicio", icon=":material/home:", default=True)

nav = st.navigation({
    "General": [pagina_inicio],
    "Análisis": [pagina_datos, pagina_graficos],
})
nav.run()

# Para enlazar entre páginas:
# st.page_link("paginas/datos.py", label="Ir a Datos", icon="📊")
# st.switch_page("paginas/graficos.py")
""",
        ),
        Ejemplo(
            titulo="st.query_params — parámetros en la URL",
            desc="Lee y escribe parámetros (`?tema=oscuro&n=5`) para compartir el estado de la app mediante un enlace.",
            codigo=r"""
import streamlit as st

st.write("Parámetros actuales:", dict(st.query_params))

valor = st.text_input("Guardar un valor en la URL", key="qp_valor")
if st.button("Aplicar a la URL", key="qp_aplicar"):
    st.query_params["valor"] = valor
    st.rerun()
""",
        ),
        Ejemplo(
            titulo="st.secrets — claves y contraseñas",
            desc=(
                "Lee secretos desde `.streamlit/secrets.toml` (local) o desde *Settings → Secrets* (Community Cloud). "
                "**Nunca subas `secrets.toml` a GitHub.**"
            ),
            ejecutar=False,
            codigo=r"""
# .streamlit/secrets.toml
# API_KEY = "sk-xxxx"
#
# [base_datos]
# host = "localhost"
# usuario = "admin"
# clave = "1234"

import streamlit as st

api_key = st.secrets["API_KEY"]
host = st.secrets["base_datos"]["host"]

# Acceso seguro con valor por defecto:
debug = st.secrets.get("DEBUG", False)
""",
        ),
        Ejemplo(
            titulo="st.connection — bases de datos y APIs",
            desc="Conexiones cacheadas y reutilizables (SQL, Snowflake, etc.). Se configuran en `secrets.toml` bajo `[connections.nombre]`.",
            ejecutar=False,
            codigo=r"""
# .streamlit/secrets.toml
# [connections.mi_bd]
# url = "postgresql://usuario:clave@host:5432/basedatos"

import streamlit as st

conn = st.connection("mi_bd", type="sql")
df = conn.query("SELECT * FROM clientes LIMIT 100", ttl=600)   # caché de 10 min
st.dataframe(df)
""",
        ),
        Ejemplo(
            titulo="Consumir una API REST (con caché)",
            desc="Patrón habitual para conectar la app con un backend (Django REST, FastAPI, etc.) usando `requests` y `st.cache_data`.",
            ejecutar=False,
            codigo=r"""
import pandas as pd
import requests
import streamlit as st

API = st.secrets.get("API_URL", "https://api.ejemplo.com")

@st.cache_data(ttl=120, show_spinner="Consultando API...")
def obtener_items(token: str):
    r = requests.get(f"{API}/items/", headers={"Authorization": f"Bearer {token}"}, timeout=15)
    r.raise_for_status()
    return pd.DataFrame(r.json())

token = st.text_input("Token", type="password")
if token:
    try:
        st.dataframe(obtener_items(token))
    except requests.RequestException as e:
        st.error(f"No se pudo consultar la API: {e}")
""",
        ),
        Ejemplo(
            titulo="st.login / st.user — autenticación",
            desc="Login con proveedores OIDC (Google, Microsoft, etc.) configurados en `secrets.toml`. Ver la documentación de *Authentication*.",
            ejecutar=False,
            codigo=r"""
import streamlit as st

if not st.user.is_logged_in:
    st.title("Debes iniciar sesión")
    st.button("Iniciar sesión con Google", on_click=st.login)   # st.login("google")
    st.stop()

st.write(f"Bienvenido, {st.user.name} ({st.user.email})")
st.button("Cerrar sesión", on_click=st.logout)
""",
        ),
        Ejemplo(
            titulo="st.context — información de la sesión",
            desc="Acceso de solo lectura a cookies, cabeceras HTTP, zona horaria, idioma y tema del navegador.",
            codigo=r"""
import streamlit as st

st.write("Zona horaria del navegador:", st.context.timezone)
st.write("Idioma del navegador:", st.context.locale)
st.write("Tema:", st.context.theme.type)
""",
        ),
        Ejemplo(
            titulo="st.iframe — incrustar HTML/JS o páginas externas",
            desc=(
                "Incrusta HTML con JavaScript, una URL externa o un archivo local en un iframe. "
                "Reemplaza a `components.html`, que quedó obsoleto. ⚠️ Nunca pases HTML de fuentes no confiables."
            ),
            codigo=r"""
import streamlit as st

html = '''
<div style="font-family:sans-serif;padding:16px;border-radius:8px;background:#e3f2fd">
  <h3 id="t">Hola desde un iframe</h3>
  <button onclick="document.getElementById('t').innerText='¡JavaScript funciona!'">Probar JS</button>
</div>
'''

st.iframe(html, height=130)
# También: st.iframe("https://streamlit.io", height=400)  → página externa
""",
        ),
        Ejemplo(
            titulo="Tema y opciones: .streamlit/config.toml",
            desc="Personaliza colores, tipografía y comportamiento del servidor sin tocar el código.",
            lenguaje="toml",
            ejecutar=False,
            codigo=r"""
[theme]
base = "light"                 # "light" | "dark"
primaryColor = "#E4572E"
backgroundColor = "#FFFFFF"
secondaryBackgroundColor = "#F5F5F5"
textColor = "#222222"
font = "sans serif"            # "sans serif" | "serif" | "monospace"

[server]
maxUploadSize = 200            # MB para st.file_uploader
runOnSave = true               # re-ejecutar al guardar el archivo

[browser]
gatherUsageStats = false
""",
        ),
    ],
)
