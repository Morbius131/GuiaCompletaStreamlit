# 📘 Guía interactiva de Streamlit

App en Streamlit con **cada componente explicado**: demo en vivo + código copiable.
14 categorías, ~90 ejemplos: texto, datos, gráficos, widgets, archivos/multimedia, layout,
mensajes, `session_state`, caché, chat, funciones avanzadas, mini‑apps y despliegue.

## Ejecutar en local
```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Subir a Streamlit Community Cloud
1. Sube esta carpeta a un repositorio de GitHub (`app.py` y `requirements.txt` en la raíz).
2. Entra a https://share.streamlit.io e inicia sesión con GitHub.
3. **New app** → elige repo, rama `main` y archivo principal `app.py` → **Deploy**.

## Estructura
```
app.py                  # navegación, buscador y layout
guia/
  modelo.py             # dataclasses Ejemplo / Seccion
  runner.py             # muestra el código y lo ejecuta en vivo (exec)
  s01_inicio.py … s14_despliegue.py   # contenido de cada categoría
.streamlit/config.toml  # tema
requirements.txt
```

## Agregar un ejemplo nuevo
Abre el archivo de la categoría (p. ej. `guia/s05_entradas.py`) y añade a la lista `ejemplos`:
```python
Ejemplo(
    titulo="st.mi_componente",
    desc="Qué hace.",
    codigo=r"""
import streamlit as st
st.write("Hola")
""",
)
```
Usa `ejecutar=False` si solo quieres mostrar el código. Recuerda dar un `key` único a cada widget de la misma categoría.
