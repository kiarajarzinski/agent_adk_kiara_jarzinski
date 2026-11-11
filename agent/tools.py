import os
import json
from ddgs import DDGS

NOTES_DIR = "./apuntes_guardados"

def buscar_en_web(query: str, max_results: int = 5):
    """
    Herramienta para realizar búsquedas en internet en tiempo real utilizando DuckDuckGo.

    Args:
        query: str -> La consulta o término que se desea investigar en internet.
        max_results: int -> Cantidad máxima de resultados a devolver.
    """
    try:
        if not query or not str(query).strip():
            return "Error de validación: La consulta no puede estar vacía."

        limite = int(max_results) if max_results else 5
        if limite < 1 or limite > 10:
            limite = 5

        results = DDGS().text(query=str(query).strip(), max_results=limite)

        if not results:
            return f"No se encontraron resultados en internet para: '{query}'."

        return results
    except Exception as e:
        print("Error interno al utilizar la herramienta:", e)
        return f"Error al buscar en la web: {str(e)}"

def guardar_apunte(titulo: str, contenido: str) -> str:
    """
    Herramienta para guardar un apunte, resumen o nota de estudio en un archivo de texto local.

    Args:
        titulo: str -> Nombre o título del apunte (ej. 'redes_neuronales').
        contenido: str -> El texto o información detallada que se desea guardar.
    """
    try:
        if not titulo or not titulo.strip():
            return "Error de validación: El título del apunte no puede estar vacío."
        if not contenido or len(contenido.strip()) < 10:
            return "Error de validación: El contenido es demasiado corto o está vacío (mínimo 10 caracteres)."

        os.makedirs(NOTES_DIR, exist_ok=True)
        
        nombre_limpio = "".join(c for c in titulo.strip() if c.isalnum() or c in (" ", "_", "-")).rstrip()
        nombre_archivo = nombre_limpio.replace(" ", "_").lower() + ".txt"
        ruta_completa = os.path.join(NOTES_DIR, nombre_archivo)

        with open(ruta_completa, "w", encoding="utf-8") as f:
            f.write(contenido.strip())

        return f"Éxito: Apunte guardado correctamente como '{nombre_archivo}'."
    except Exception as e:
        return f"Error interno al guardar el apunte: {str(e)}"


def consultar_apuntes(titulo: str = "") -> str:
    """
    Herramienta para listar todos los apuntes guardados o leer el contenido de un apunte específico.

    Args:
        titulo: str -> (Opcional) Nombre del apunte a leer. Si se deja vacío (""), devuelve la lista de todos los apuntes disponibles.
    """
    try:
        if not os.path.exists(NOTES_DIR):
            return "Aún no existen apuntes guardados (el directorio no fue creado)."

        archivos = [f for f in os.listdir(NOTES_DIR) if f.endswith(".txt")]

        if not archivos:
            return "No hay ningún apunte guardado actualmente."

        if not titulo or not titulo.strip():
            return f"Apuntes disponibles ({len(archivos)}): {', '.join(archivos)}"

        busqueda = titulo.strip().replace(" ", "_").lower()
        if not busqueda.endswith(".txt"):
            busqueda += ".txt"

        ruta_completa = os.path.join(NOTES_DIR, busqueda)
        if not os.path.exists(ruta_completa):
            return f"No se encontró el apunte '{busqueda}'. Los apuntes disponibles son: {', '.join(archivos)}"

        with open(ruta_completa, "r", encoding="utf-8") as f:
            contenido = f.read()

        if not contenido.strip():
            return f"El apunte '{busqueda}' existe pero está vacío."

        return f"Contenido de '{busqueda}':\n{contenido}"
    except Exception as e:
        return f"Error interno al consultar apuntes: {str(e)}"


def calcular_estado_academico(notas: list[float], nota_aprobacion: float = 6.0) -> str:
    """
    Herramienta para calcular el promedio de calificaciones de un estudiante y determinar su estado académico.

    Args:
        notas: list[float] -> Lista de calificaciones numéricas (entre 1 y 10).
        nota_aprobacion: float -> Nota mínima requerida para aprobar (por defecto 6.0).
    """
    try:
        if not notas or not isinstance(notas, list) or len(notas) == 0:
            return "Error de validación: Debes proporcionar una lista con al menos una calificación."

        if nota_aprobacion < 1 or nota_aprobacion > 10:
            return "Error de validación: La nota de aprobación debe estar entre 1 y 10."

        notas_validas = []
        for n in notas:
            valor = float(n)
            if valor < 1 or valor > 10:
                return f"Error de validación: La calificación '{valor}' es inválida. Todas las notas deben estar entre 1 y 10."
            notas_validas.append(valor)

        promedio = round(sum(notas_validas) / len(notas_validas), 2)
        estado = "APROBADO" if promedio >= nota_aprobacion else "DESAPROBADO"

        return (
            f"Resultado del cálculo:\n"
            f"- Cantidad de evaluaciones: {len(notas_validas)}\n"
            f"- Calificaciones: {notas_validas}\n"
            f"- Nota mínima de aprobación: {nota_aprobacion}\n"
            f"- Promedio final: {promedio}\n"
            f"- Estado: {estado}"
        )
    except ValueError:
        return "Error de validación: Todos los elementos de la lista de notas deben ser números válidos."
    except Exception as e:
        return f"Error interno al calcular el promedio: {str(e)}"