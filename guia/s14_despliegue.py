from .modelo import Ejemplo, Seccion

SECCION = Seccion(
    clave="despliegue",
    nombre="Subir a Streamlit Cloud",
    icono="☁️",
    intro=r"""
**Streamlit Community Cloud** (gratis) despliega tu app directamente desde un repositorio de **GitHub**.

### Pasos
1. **Organiza tu repo:** `app.py` (o el nombre que prefieras) + `requirements.txt` en la raíz.
2. **Sube el código a GitHub** (repositorio público o privado).
3. Entra a **[share.streamlit.io](https://share.streamlit.io)** e inicia sesión con GitHub.
4. Pulsa **New app** (o *Create app*) y elige: repositorio, rama (`main`) y archivo principal (`app.py`).
5. *(Opcional)* En **Advanced settings** elige la versión de Python y pega tus **Secrets** en formato TOML.
6. Pulsa **Deploy**. En 1–3 minutos tendrás una URL tipo `https://tu-app.streamlit.app`.

### Después de desplegar
- **Actualizar:** haz `git push` y la app se redespliega sola.
- **Secretos:** menú ⋮ de la app → **Settings → Secrets**.
- **Logs y reinicio:** botón *Manage app* (esquina inferior derecha) → logs / *Reboot app*.

### Errores típicos
- `ModuleNotFoundError` → falta la librería en `requirements.txt`.
- No incluyas módulos nativos de Python (`math`, `random`, `os`…) en `requirements.txt`.
- Usa **un solo** archivo de dependencias.
- No subas `secrets.toml` a GitHub (agrégalo a `.gitignore`).
""",
    ejemplos=[
        Ejemplo(
            titulo="requirements.txt",
            desc="Una dependencia por línea. Fijar versiones mejora la reproducibilidad.",
            lenguaje="text",
            ejecutar=False,
            codigo=r"""
streamlit>=1.50
pandas
numpy
matplotlib
plotly
altair
requests
""",
        ),
        Ejemplo(
            titulo=".gitignore",
            desc="Evita subir secretos y archivos temporales.",
            lenguaje="text",
            ejecutar=False,
            codigo=r"""
.venv/
__pycache__/
*.pyc
.streamlit/secrets.toml
.env
""",
        ),
        Ejemplo(
            titulo="Subir el proyecto a GitHub",
            desc="Desde la carpeta de tu proyecto (crea antes un repositorio vacío en github.com).",
            lenguaje="bash",
            ejecutar=False,
            codigo=r"""
git init
git add .
git commit -m "Guía interactiva de Streamlit"
git branch -M main
git remote add origin https://github.com/TU_USUARIO/TU_REPO.git
git push -u origin main
""",
        ),
        Ejemplo(
            titulo="Secrets en Community Cloud (formato TOML)",
            desc="Pega este contenido en *Advanced settings → Secrets* y léelo en tu código con `st.secrets`.",
            lenguaje="toml",
            ejecutar=False,
            codigo=r"""
API_KEY = "tu-clave-aqui"

[base_datos]
host = "mi-servidor.com"
usuario = "admin"
clave = "cambiar"
""",
        ),
        Ejemplo(
            titulo="Probar localmente antes de desplegar",
            desc="Verifica que la app arranca en un entorno limpio con solo lo que hay en `requirements.txt`.",
            lenguaje="bash",
            ejecutar=False,
            codigo=r"""
python -m venv .venv-prueba
source .venv-prueba/bin/activate
pip install -r requirements.txt
streamlit run app.py
""",
        ),
    ],
)
