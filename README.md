# DevSecOps Project

Proyecto de ejemplo en Python con API y una interfaz web simple, junto con un pipeline de CI/CD para pruebas, análisis de código con SonarQube y despliegue de imagen Docker a Docker Hub.

## Estructura

- `app.py`: aplicación Flask con API y interfaz web.
- `templates/index.html`: página web principal.
- `static/style.css`: estilo básico de la interfaz.
- `tests/test_app.py`: pruebas unitarias de la aplicación.
- `Dockerfile`: imagen de la aplicación.
- `.github/workflows/ci-cd.yml`: pipeline de CI/CD.
- `sonar-project.properties`: configuración básica para SonarQube.

## Requisitos

- Python 3.11+ o 3.12
- Docker
- Cuenta en Docker Hub
- Secrets en GitHub: `DOCKERHUB_USERNAME`, `DOCKERHUB_TOKEN`, `SONAR_HOST_URL`, `SONAR_TOKEN`

## Uso local

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

Abrir `http://localhost:5000` en el navegador.

## Ejecutar pruebas

```bash
pytest --cov=app --cov-report=xml
```

## Construir imagen Docker

```bash
docker build -t ${DOCKERHUB_USERNAME}/devsecops-proyect:latest .
```

## GitHub Actions

El flujo de trabajo `.github/workflows/ci-cd.yml` contiene:

1. CI: instalación de dependencias, ejecución de pruebas y análisis con SonarQube.
2. CD: construcción de la imagen Docker y subida a Docker Hub.

> Recuerda configurar los secretos en el repositorio de GitHub antes de ejecutar el pipeline.
