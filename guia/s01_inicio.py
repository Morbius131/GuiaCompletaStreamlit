from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="inicio",
    nombre="Inicio rápido",
    icono="🚀",
    intro=r"""
**Streamlit** convierte scripts de Python en aplicaciones web interactivas, sin escribir HTML, CSS ni JavaScript.

**¿Cómo usar esta guía?**
- Elige una categoría en la barra lateral (o usa el buscador 🔎).
- Cada ejemplo muestra **el código** y, debajo, **el resultado ejecutándose en vivo**. Interactúa con él.
- Copia el código tal cual: cada snippet es autocontenido (incluye sus `import`).

**Idea clave:** cada vez que el usuario interactúa con un widget, Streamlit **vuelve a ejecutar el script de arriba abajo**.
Por eso existen `st.session_state` (memoria entre ejecuciones) y `st.cache_data` (evitar cálculos repetidos).
""",
    ejemplos=[
        Ejemplo(
            titulo="Instalación y ejecución",
            desc="Necesitas Python 3.9+ (recomendado 3.11+). Se recomienda usar un entorno virtual.",
            lenguaje="bash",
            ejecutar=False,
            codigo=r"""
# 1) Crear y activar un entorno virtual
python -m venv .venv
source .venv/bin/activate        # En Windows: .venv\Scripts\activate

# 2) Instalar Streamlit
pip install streamlit

# 3) Probar que funciona con la app de demo
streamlit hello

# 4) Ejecutar TU app
streamlit run app.py

# Opciones útiles
streamlit run app.py --server.port 8502
streamlit cache clear
""",
        ),
        Ejemplo(
            titulo="Tu primera app (Hola mundo)",
            desc="Un archivo `app.py` con un título, un cuadro de texto y un mensaje condicional.",
            codigo=r"""
import streamlit as st

st.title("Mi primera app 🚀")

nombre = st.text_input("¿Cómo te llamas?", key="inicio_nombre")
if nombre:
    st.success(f"¡Hola, {nombre}! Bienvenido a Streamlit.")
else:
    st.info("Escribe tu nombre para recibir un saludo.")
""",
        ),
        Ejemplo(
            titulo="El modelo de ejecución (reruns)",
            desc=(
                "El script se ejecuta completo en **cada interacción**. "
                "Observa cómo el contador de ejecuciones sube cada vez que mueves el slider. "
                "`st.session_state` conserva valores entre ejecuciones."
            ),
            codigo=r"""
import streamlit as st

if "ejecuciones" not in st.session_state:
    st.session_state.ejecuciones = 0
st.session_state.ejecuciones += 1

st.write(f"Este bloque se ha ejecutado **{st.session_state.ejecuciones}** veces en tu sesión.")
valor = st.slider("Mueve el slider para provocar un rerun", 0, 100, 25, key="inicio_slider")
st.write("Valor actual:", valor)
""",
        ),
        Ejemplo(
            titulo="Estructura recomendada de un proyecto",
            desc="Para subir a Streamlit Community Cloud solo necesitas `app.py` y `requirements.txt`; lo demás es opcional.",
            lenguaje="text",
            ejecutar=False,
            codigo=r"""
mi-repo/
├── app.py                  # archivo principal (entrypoint)
├── requirements.txt        # dependencias (una por línea)
├── .streamlit/
│   ├── config.toml         # tema y opciones del servidor (se sube a GitHub)
│   └── secrets.toml        # secretos locales (¡NO subir a GitHub! → .gitignore)
├── pages/                  # (opcional) páginas extra: modo multipágina clásico
│   ├── 1_Datos.py
│   └── 2_Graficos.py
└── utils/                  # (opcional) módulos de apoyo
    └── helpers.py
""",
        ),
    ],
)
