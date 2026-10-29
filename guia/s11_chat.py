from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="chat",
    nombre="Chat y streaming",
    icono="🤖",
    intro=r"""
Elementos específicos para interfaces conversacionales (chatbots, asistentes con IA).
`st.chat_message` dibuja los globos, `st.chat_input` captura el mensaje y `st.write_stream` muestra texto token a token.
""",
    ejemplos=[
        Ejemplo(
            titulo="st.chat_message",
            desc="Globos de mensaje con rol (`user`, `assistant`) o avatar personalizado. Puede contener cualquier elemento.",
            codigo=r"""
import numpy as np
import streamlit as st

with st.chat_message("user"):
    st.write("Muéstrame un gráfico aleatorio")

with st.chat_message("assistant"):
    st.write("¡Claro! Aquí tienes:")
    st.line_chart(np.random.default_rng(0).standard_normal((20, 2)))

with st.chat_message("ai", avatar="🧑‍🚀"):
    st.write("También puedes usar avatares personalizados.")
""",
        ),
        Ejemplo(
            titulo="Chatbot de eco con historial",
            desc="Patrón completo: guarda los mensajes en `session_state`, píntalos y responde al nuevo mensaje de `st.chat_input`.",
            codigo=r"""
import streamlit as st

if "mensajes" not in st.session_state:
    st.session_state.mensajes = [{"role": "assistant", "content": "¡Hola! Escríbeme algo y te lo repito 🦜"}]

for m in st.session_state.mensajes:
    with st.chat_message(m["role"]):
        st.write(m["content"])

if prompt := st.chat_input("Escribe un mensaje...", key="chat_demo_input"):
    st.session_state.mensajes.append({"role": "user", "content": prompt})
    st.session_state.mensajes.append({"role": "assistant", "content": f"Dijiste: {prompt}"})
    st.rerun()
""",
        ),
        Ejemplo(
            titulo="st.write_stream — respuesta en streaming",
            desc="Muestra el texto de un generador poco a poco (como los LLM). Devuelve el texto completo al terminar.",
            codigo=r"""
import time
import streamlit as st

def generar_texto():
    texto = "Streamlit permite mostrar respuestas palabra por palabra, igual que un chatbot moderno. "
    for palabra in texto.split(" "):
        yield palabra + " "
        time.sleep(0.05)

if st.button("Generar respuesta", key="stream_btn"):
    with st.chat_message("assistant"):
        completo = st.write_stream(generar_texto)
    st.caption(f"Total de caracteres: {len(completo)}")
""",
        ),
        Ejemplo(
            titulo="Conectar con un LLM (OpenAI / Anthropic)",
            desc=(
                "Esqueleto de chatbot real con la API de Anthropic. La clave se guarda en `st.secrets` "
                "(ver sección *Funciones avanzadas*). No se ejecuta aquí porque requiere una API key."
            ),
            ejecutar=False,
            codigo=r"""
import anthropic
import streamlit as st

client = anthropic.Anthropic(api_key=st.secrets["ANTHROPIC_API_KEY"])

if "msgs" not in st.session_state:
    st.session_state.msgs = []

for m in st.session_state.msgs:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

if prompt := st.chat_input("Pregúntame algo"):
    st.session_state.msgs.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        def stream():
            with client.messages.stream(
                model="claude-sonnet-5-5",   # usa el modelo vigente que prefieras
                max_tokens=1024,
                messages=st.session_state.msgs,
            ) as s:
                yield from s.text_stream

        respuesta = st.write_stream(stream)
    st.session_state.msgs.append({"role": "assistant", "content": respuesta})
""",
        ),
    ],
)
