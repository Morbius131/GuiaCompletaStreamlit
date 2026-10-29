from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="media",
    nombre="Archivos y multimedia",
    icono="🖼️",
    intro=r"""
Sube archivos, captura cámara o micrófono y muestra imágenes, audio y video.
""",
    ejemplos=[
        Ejemplo(
            titulo="st.file_uploader — subir archivos",
            desc="Devuelve un objeto tipo archivo (o `None`). Con `accept_multiple_files=True` devuelve una lista.",
            codigo=r"""
import pandas as pd
import streamlit as st

archivo = st.file_uploader("Sube un CSV", type=["csv"], key="up_csv")
if archivo is not None:
    df = pd.read_csv(archivo)
    st.success(f"Archivo «{archivo.name}» cargado: {df.shape[0]} filas × {df.shape[1]} columnas")
    st.dataframe(df.head())
else:
    st.info("Aún no has subido ningún archivo.")
""",
        ),
        Ejemplo(
            titulo="st.file_uploader — varios archivos",
            desc="Útil para imágenes, documentos, etc. Cada elemento tiene `.name`, `.type`, `.size` y `.getvalue()`.",
            codigo=r"""
import streamlit as st

archivos = st.file_uploader("Sube varios archivos", accept_multiple_files=True, key="up_varios")
for f in archivos:
    st.write(f"📄 **{f.name}** — {f.type or 'tipo desconocido'} — {f.size / 1024:.1f} KB")
""",
        ),
        Ejemplo(
            titulo="st.camera_input — foto desde la cámara",
            desc="Pide permiso al navegador y devuelve la foto como archivo.",
            codigo=r"""
import streamlit as st

foto = st.camera_input("Toma una foto", key="cam_foto")
if foto:
    st.image(foto, caption="Tu foto")
""",
        ),
        Ejemplo(
            titulo="st.audio_input — grabar audio",
            desc="Graba desde el micrófono y devuelve un archivo WAV.",
            codigo=r"""
import streamlit as st

grabacion = st.audio_input("Graba un mensaje de voz", key="mic_voz")
if grabacion:
    st.audio(grabacion)
""",
        ),
        Ejemplo(
            titulo="st.image",
            desc="Acepta rutas, URLs, arrays de NumPy, imágenes PIL o bytes. Controla el tamaño con `width`.",
            codigo=r"""
import numpy as np
import streamlit as st

# Degradado generado con NumPy (alto × ancho × RGB)
x = np.linspace(0, 255, 240, dtype=np.uint8)
imagen = np.stack([np.tile(x, (120, 1)), np.tile(x[::-1], (120, 1)), np.full((120, 240), 160, np.uint8)], axis=-1)

st.image(imagen, caption="Degradado generado con NumPy", width=360)
""",
        ),
        Ejemplo(
            titulo="st.audio",
            desc="Reproduce audio desde archivo, URL, bytes o un array de NumPy (indicando `sample_rate`).",
            codigo=r"""
import numpy as np
import streamlit as st

frecuencia = st.slider("Frecuencia (Hz)", 220, 880, 440, key="aud_freq")
sr = 22050
t = np.linspace(0, 2, 2 * sr, endpoint=False)
onda = 0.4 * np.sin(2 * np.pi * frecuencia * t)

st.audio(onda, sample_rate=sr)
""",
        ),
        Ejemplo(
            titulo="st.video",
            desc="Reproduce video desde archivo local, URL o bytes (YouTube también funciona pasando la URL).",
            codigo=r"""
import streamlit as st

st.video("https://www.w3schools.com/html/mov_bbb.mp4")
""",
        ),
    ],
)
