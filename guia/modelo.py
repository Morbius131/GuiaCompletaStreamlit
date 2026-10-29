"""Modelos de datos de la guía: cada sección contiene varios ejemplos."""
from dataclasses import dataclass, field


@dataclass
class Ejemplo:
    titulo: str
    desc: str
    codigo: str
    ejecutar: bool = True      # False => solo se muestra el código (no se ejecuta)
    lenguaje: str = "python"   # lenguaje para el resaltado del bloque de código


@dataclass
class Seccion:
    clave: str
    nombre: str
    icono: str
    intro: str
    ejemplos: list = field(default_factory=list)
