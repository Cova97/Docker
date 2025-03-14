# Docker - API sencilla con Flask

Este proyecto es un ejemplo de una API sencilla creada con Flask, diseñada para ser desplegada en Render utilizando Docker para la creación de un contenedor.

## Objetivo

El objetivo de este proyecto es demostrar cómo se puede construir y desplegar una API con Flask utilizando Docker. Se incluyen instrucciones detalladas para la instalación y ejecución del contenedor en un entorno de desarrollo y producción.

## Instalación

Sigue estos pasos para instalar y ejecutar el proyecto en tu entorno local:

### Prerrequisitos

Asegúrate de tener instalados los siguientes programas en tu sistema:
- [Git](https://git-scm.com/downloads)
- [Docker](https://www.docker.com/get-started)
- [Python 3](https://www.python.org/downloads/)

### Clonar el repositorio

```bash
git clone https://github.com/tu-usuario/Docker.git
cd Docker
```

### Crear y activar un entorno virtual (opcional pero recomendado)

#### En Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

#### En Windows (cmd o PowerShell):
```powershell
python -m venv venv
venv\Scripts\activate
```

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Construir y ejecutar el contenedor Docker

### Desarrollo:
```bash
docker-compose up dev --build
```
Accede en: [http://localhost:5000](http://localhost:5000)

### Producción:
```bash
docker-compose up prod --build
```
Accede en: [http://localhost:8000](http://localhost:8000)

## Despliegue en Render

Para desplegar la API en Render, sigue estos pasos:
1. Crea una cuenta en [Render](https://render.com/).
2. Sube el código del proyecto a un repositorio en GitHub.
3. En Render, crea un nuevo servicio web y conecta tu repositorio.
4. En la configuración del servicio:
   - Elige un entorno de ejecución basado en Docker.
   - Define el comando de ejecución según tu `Dockerfile`.
5. Despliega y obtén la URL pública para acceder a la API.

---

¡Listo! Has creado y desplegado una API sencilla con Flask utilizando Docker.

## Sitio de ejemplo simple y sensillo

Aqui puedes ver mi ejemplo ya en [Render](https://docker-o6cm.onrender.com)
