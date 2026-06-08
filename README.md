# DevSecOps Project

> A sample Flask application demonstrating DevSecOps best practices with Docker, Kubernetes, automated testing, and CI/CD integration.

## Quick Links

- 📚 **[Complete Documentation](DOCUMENTATION.md)** - Full project guide with all details
- 🚀 **[Kubernetes Deployment Guide](k8s/README.md)** - K8s setup instructions
- 🐳 **[Docker Hub Setup](k8s/DOCKERHUB_SETUP.md)** - Container registry configuration

## Overview

This project showcases a modern containerized microservice architecture with:

- **Web Application**: Python Flask REST API with HTML interface
- **Containerization**: Docker support for consistent deployments
- **Orchestration**: Kubernetes manifests with auto-scaling
- **Testing**: Automated test suite with coverage tracking
- **Code Quality**: SonarQube integration for security and quality analysis
- **CI/CD**: GitHub Actions pipeline for automated workflows
- **Security**: Non-root containers, resource limits, health probes

## Quick Start

### 1. Local Development

```bash
# Clone repository
git clone https://github.com/hungles/devsecops-proyect.git
cd devsecops-proyect

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run application
python app.py
# Visit: http://localhost:5000
```

### 2. Docker Deployment

```bash
# Build image
docker build -t devsecops-app:latest .

# Run container
docker run -p 5000:5000 devsecops-app:latest

# Push to Docker Hub (requires authentication)
docker login
docker tag devsecops-app:latest YOUR_USERNAME/devsecops-app:latest
docker push YOUR_USERNAME/devsecops-app:latest
```

### 3. Kubernetes Deployment

```bash
# Setup Docker Hub credentials
./k8s/setup-dockerhub.sh YOUR_USERNAME YOUR_TOKEN

# Deploy to cluster
kubectl apply -f k8s/deployment.yaml

# Access application
kubectl port-forward -n devsecops svc/devsecops-app 8080:80
# Visit: http://localhost:8080
```

## Testing

```bash
# Run test suite
pytest

# Run with coverage
pytest --cov=.

# Run linting
flake8
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Home page with web UI |
| GET | `/api/health` | Health check for monitoring |
| POST | `/api/message` | Message processing endpoint |

## Deployment Options

| Environment | Method | Command |
|-------------|--------|---------|
| Local Dev | Python/Gunicorn | `python app.py` or `gunicorn` |
| Docker Local | Docker | `docker build` and `docker run` |
| Production K8s | Kubernetes | `kubectl apply -f k8s/deployment.yaml` |

## Project Structure

```
devsecops-proyect/
├── app.py                 # Main Flask application
├── Dockerfile             # Container specification
├── requirements.txt       # Python dependencies
├── tests/                 # Test suite
├── static/                # CSS and static assets
├── templates/             # HTML templates
├── k8s/                   # Kubernetes configurations
├── .github/               # GitHub Actions workflows
└── DOCUMENTATION.md       # Comprehensive documentation
```

## Key Features

✅ **Scalability**: Horizontal Pod Autoscaler (2-10 replicas)  
✅ **Health Monitoring**: Liveness and readiness probes  
✅ **Security**: Non-root containers, resource limits  
✅ **Testing**: Automated test suite with coverage  
✅ **Quality**: SonarQube code quality analysis  
✅ **CI/CD**: GitHub Actions automated pipeline  
✅ **Containerization**: Docker with optimized images  
✅ **Orchestration**: Production-grade Kubernetes manifests  

## Technology Stack

- **Framework**: Flask 2.2.5+
- **Server**: Gunicorn 20.1.0+
- **Language**: Python 3.12
- **Testing**: pytest 7.4.0+
- **Container**: Docker
- **Orchestration**: Kubernetes 1.20+
- **CI/CD**: GitHub Actions
- **Code Quality**: SonarQube Cloud

## Prerequisites

- Python 3.12+
- Docker 20.10+
- kubectl 1.20+
- Git

## Documentation

For complete information, see [DOCUMENTATION.md](DOCUMENTATION.md) which includes:

- Architecture overview
- Detailed setup instructions
- Kubernetes deployment guide
- Testing and coverage information
- CI/CD pipeline details
- Troubleshooting guide
- API documentation
- Security best practices

## Contributing

1. Create a feature branch: `git checkout -b feature/name`
2. Make changes and test: `pytest --cov=.`
3. Commit with message: `git commit -m "feat: description"`
4. Push and create pull request

## Support

- **GitHub Issues**: Bug reports and feature requests
- **GitHub Discussions**: Questions and ideas
- **Organization**: [hungles](https://github.com/hungles)

## License

Educational and demonstrative purposes - DevSecOps practices.

---

**Status**: Active Development | **Last Updated**: June 8, 2026 | **Version**: 1.0
