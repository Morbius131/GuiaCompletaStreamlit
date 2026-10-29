from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="texto",
    nombre="Texto y contenido",
    icono="✍️",
    intro=r"""
Elementos para mostrar texto, código, fórmulas y HTML. `st.write` es el «comodín»: detecta el tipo de
objeto (texto, DataFrame, figura, dict…) y lo muestra de la forma adecuada.
""",
    ejemplos=[
        Ejemplo(
            titulo="st.write — el comodín",
            desc="Acepta texto (con Markdown), números, listas, dicts, DataFrames, figuras de matplotlib/plotly, etc.",
            codigo=r"""
import pandas as pd
import streamlit as st

st.write("Hola **Streamlit** 👋")
st.write("Puedes pasar varios argumentos:", 42, [1, 2, 3])
st.write({"clave": "valor", "n": 3})
st.write(pd.DataFrame({"x": [1, 2, 3], "y": [4, 5, 6]}))
""",
        ),
        Ejemplo(
            titulo="Títulos y texto simple",
            desc="`st.title`, `st.header`, `st.subheader`, `st.caption` y `st.text` (monoespaciado, sin formato).",
            codigo=r"""
import streamlit as st

st.title("Título (st.title)")
st.header("Encabezado (st.header)", divider="rainbow")
st.subheader("Subencabezado (st.subheader)")
st.caption("Texto pequeño y gris: ideal para notas (st.caption)")
st.text("Texto de ancho fijo, sin formato Markdown (st.text)")
""",
        ),
        Ejemplo(
            titulo="st.markdown — formato enriquecido",
            desc="Soporta Markdown, colores (`:red[texto]`), emojis, iconos Material (`:material/home:`) y más.",
            codigo=r"""
import streamlit as st

st.markdown('''
**Negrita**, *cursiva*, ~~tachado~~ y `código en línea`.

- Elemento 1
- Elemento 2
    - Sub‑elemento

1. Primero
2. Segundo

:red[texto rojo] · :blue[azul] · :green[verde] · :orange-background[fondo naranja] · :rainbow[arcoíris]

Emoji :tada: e icono Material :material/home: · [Un enlace](https://streamlit.io)
''')
""",
        ),
        Ejemplo(
            titulo="st.code — bloques de código",
            desc="Resalta sintaxis y muestra un botón de copiar. Admite `language`, `line_numbers` y `wrap_lines`.",
            codigo=r"""
import streamlit as st

codigo = '''def saludar(nombre):
    return f"Hola, {nombre}"

print(saludar("mundo"))'''

st.code(codigo, language="python", line_numbers=True)
""",
        ),
        Ejemplo(
            titulo="st.latex — fórmulas matemáticas",
            desc="Escribe fórmulas en LaTeX. También puedes usar `$...$` dentro de `st.markdown`.",
            codigo=r"""
import streamlit as st

st.latex(r'''
    \bar{x} = \frac{1}{n}\sum_{i=1}^{n} x_i
    \qquad
    \sigma = \sqrt{\frac{1}{n}\sum_{i=1}^{n}(x_i-\bar{x})^2}
''')
st.markdown("En línea: la identidad de Euler es $e^{i\\pi} + 1 = 0$")
""",
        ),
        Ejemplo(
            titulo="st.badge y st.divider",
            desc="Etiquetas de colores (`st.badge`) y líneas separadoras (`st.divider`).",
            codigo=r"""
import streamlit as st

st.badge("Nuevo", icon=":material/star:", color="green")
st.badge("En revisión", color="orange")
st.badge("Error", color="red")
st.divider()
st.write("Contenido debajo de la línea separadora")
""",
        ),
        Ejemplo(
            titulo="st.html — HTML personalizado",
            desc="Inserta HTML/CSS sencillo (se sanea por seguridad: no ejecuta JavaScript).",
            codigo=r"""
import streamlit as st

st.html(
    "<div style='padding:12px;border-radius:8px;background:#fff3e0;'>"
    "<b style='color:#e4572e'>Caja HTML</b> con estilos propios.</div>"
)
""",
        ),
        Ejemplo(
            titulo="st.help — documentación al vuelo",
            desc="Muestra la documentación de cualquier objeto o función de Python (útil para depurar).",
            codigo=r"""
import streamlit as st

st.help(st.dataframe)
""",
        ),
        Ejemplo(
            titulo="st.echo — mostrar el código que se ejecuta",
            desc="Dentro de `with st.echo():` el código se muestra y se ejecuta. (Aquí solo se muestra el código; funciona al usarlo en un archivo `.py`.)",
            ejecutar=False,
            codigo=r"""
import streamlit as st

with st.echo():
    # Este código aparecerá en pantalla Y se ejecutará
    x = 10
    st.write("x al cuadrado =", x ** 2)
""",
        ),
    ],
)
