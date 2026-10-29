"""Paquete de contenido de la guía interactiva de Streamlit."""
from . import (
    s01_inicio,
    s02_texto,
    s03_datos,
    s04_graficos,
    s05_entradas,
    s06_media,
    s07_layout,
    s08_estado_visual,
    s09_sesion,
    s10_rendimiento,
    s11_chat,
    s12_avanzado,
    s13_apps,
    s14_despliegue,
)

SECCIONES = [
    m.SECCION
    for m in (
        s01_inicio,
        s02_texto,
        s03_datos,
        s04_graficos,
        s05_entradas,
        s06_media,
        s07_layout,
        s08_estado_visual,
        s09_sesion,
        s10_rendimiento,
        s11_chat,
        s12_avanzado,
        s13_apps,
        s14_despliegue,
    )
]


def buscar(consulta: str):
    """Devuelve [(seccion, ejemplo)] que coinciden con la consulta.

    Orden: primero coincidencias en el título, luego en la descripción y al final en el código.
    """
    q = consulta.strip().lower()
    if not q:
        return []
    resultados = []
    for sec in SECCIONES:
        for ej in sec.ejemplos:
            if q in ej.titulo.lower():
                prioridad = 0
            elif q in ej.desc.lower():
                prioridad = 1
            elif q in ej.codigo.lower():
                prioridad = 2
            else:
                continue
            resultados.append((prioridad, sec, ej))
    resultados.sort(key=lambda r: r[0])  # sort estable: conserva el orden de la guía
    return [(sec, ej) for _, sec, ej in resultados]
