# Agente Asistente Académico con Google ADK

Este proyecto implementa un agente de inteligencia artificial desarrollado en Python utilizando **Google Agent Development Kit (ADK)** y **LiteLLM**, conectado con **Ollama**.

## ¿De qué se trata?

El agente funciona como un asistente integral para estudiantes. Además de responder consultas, puede tomar decisiones y utilizar herramientas locales y externas para:

1. Investigar conceptos actualizados en internet.
2. Guardar resúmenes y apuntes de clase en archivos locales.
3. Consultar y recuperar apuntes guardados previamente.
4. Calcular promedios de notas y determinar el estado académico del estudiante.

## Herramientas implementadas

El agente cuenta con cuatro herramientas, cada una con una responsabilidad diferente, validación de argumentos, control de resultados vacíos y manejo de excepciones:

1. `buscar_en_web(query: str, max_results: int = 5)`\
   Utiliza `ddgs` (DuckDuckGo Search) para realizar búsquedas en tiempo real en internet. Valida que la consulta no esté vacía y que el límite de resultados sea válido.

2. `guardar_apunte(titulo: str, contenido: str)`\
   Crea y almacena archivos `.txt` dentro del directorio `./apuntes_guardados`. Valida la longitud mínima del contenido y normaliza el nombre del archivo.

3. `consultar_apuntes(titulo: str = "")`\
   Si se invoca sin argumentos, lista todos los apuntes disponibles. Si recibe un título, lee y devuelve el contenido del archivo correspondiente.

4. `calcular_estado_academico(notas: list[float], nota_aprobacion: float = 6.0)`\
   Calcula el promedio de una lista de calificaciones, valida que estén en la escala del 1 al 10 e informa si el estudiante está aprobado o desaprobado.

## Requisitos previos

- Python 3.10 o superior
- Gestor de paquetes `uv`
- [Ollama](https://ollama.com/) instalado y ejecutándose localmente mediante `ollama serve`

## Instalación y uso

### 1. Clonar el repositorio

```bash
git clone https://github.com/kiarajarzinski/agent_adk_kiara_jarzinski.git
cd agent_adk_kiara_jarzinski
```

### 2. Crear y activar el entorno virtual

```bash
uv venv env
```

En Windows:

```powershell
env\Scripts\activate
```

En Linux o macOS:

```bash
source env/bin/activate
```

### 3. Instalar las dependencias

```bash
uv pip install -r requirements.txt
```

### 4. Ejecutar la interfaz web de ADK

```bash
adk web
```

Luego, abre en el navegador la dirección:

http://localhost:8000