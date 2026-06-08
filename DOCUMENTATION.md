# DevSecOps Project - Complete Documentation

## Table of Contents

1. [Project Overview](#project-overview)
2. [Architecture](#architecture)
3. [Technology Stack](#technology-stack)
4. [Project Structure](#project-structure)
5. [Prerequisites](#prerequisites)
6. [Getting Started](#getting-started)
7. [Running the Application](#running-the-application)
8. [Docker Containerization](#docker-containerization)
9. [Kubernetes Deployment](#kubernetes-deployment)
10. [Testing](#testing)
11. [CI/CD Pipeline](#cicd-pipeline)
12. [Code Quality & Security](#code-quality--security)
13. [API Documentation](#api-documentation)
14. [Monitoring & Troubleshooting](#monitoring--troubleshooting)
15. [Contributing Guidelines](#contributing-guidelines)

---

## Project Overview

**DevSecOps Project** is a sample Python Flask application designed to demonstrate best practices in DevSecOps (Development, Security, and Operations). The project showcases a modern containerized microservice with comprehensive CI/CD integration, automated testing, security scanning, and Kubernetes deployment capabilities.

### Key Features

- **RESTful API**: Simple Flask-based REST API with health checks and message processing
- **Containerization**: Docker support for consistent environments across development and production
- **Kubernetes Ready**: Production-grade Kubernetes deployment with auto-scaling and health probes
- **Automated Testing**: Comprehensive test suite with code coverage tracking
- **Security Scanning**: SonarQube integration for code quality and security analysis
- **CI/CD Pipeline**: GitHub Actions workflow for automated testing and deployment
- **Scalability**: Horizontal Pod Autoscaler for automatic container orchestration
- **Non-Root Containers**: Security-hardened containers running with restricted privileges

---

## Architecture

### High-Level Architecture Diagram

```
┌─────────────────────────────────────────────────────────┐
│                    Internet/Users                        │
└──────────────────┬──────────────────────────────────────┘
                   │
┌──────────────────▼──────────────────────────────────────┐
│              Kubernetes Cluster                          │
│                                                          │
│  ┌──────────────────────────────────────────────────┐  │
│  │  LoadBalancer Service (Port 80 → 5000)           │  │
│  └──────────────────┬───────────────────────────────┘  │
│                     │                                    │
│  ┌──────────────────▼───────────────────────────────┐  │
│  │  HPA (2-10 Replicas)                             │  │
│  │                                                   │  │
│  │  ┌────────────┬────────────┬────────────┐       │  │
│  │  │ Pod 1      │ Pod 2      │ Pod 3      │  ...  │  │
│  │  │ Flask App  │ Flask App  │ Flask App  │       │  │
│  │  │ Port 5000  │ Port 5000  │ Port 5000  │       │  │
│  │  └────────────┴────────────┴────────────┘       │  │
│  │                                                   │  │
│  └───────────────────────────────────────────────────┘  │
│                                                          │
└──────────────────────────────────────────────────────────┘

   ↓
   
┌─────────────────────────────────────────────────────────┐
│            Docker Hub Registry                           │
│  (scarmona04/devsecops-proyect:latest)                  │
└─────────────────────────────────────────────────────────┘
```

### Component Interactions

1. **Client Request** → LoadBalancer Service
2. **Service** → Distributes traffic to available Pods
3. **HPA** → Monitors resource usage and scales pods
4. **Pod** → Runs containerized Flask application
5. **Container** → Pulls image from Docker Hub with credentials

---

## Technology Stack

| Component | Technology | Version | Purpose |
|-----------|-----------|---------|---------|
| **Framework** | Flask | ≥2.2.5 | Web framework for REST API |
| **Server** | Gunicorn | ≥20.1.0 | WSGI application server |
| **Language** | Python | 3.12 | Programming language |
| **Testing** | pytest | ≥7.4.0 | Unit and integration testing |
| **Code Coverage** | pytest-cov | ≥4.1.0 | Coverage measurement |
| **Linting** | flake8 | ≥6.0.0 | Code style and quality checks |
| **Containerization** | Docker | Latest | Container runtime |
| **Orchestration** | Kubernetes | ≥1.20 | Container orchestration |
| **Code Quality** | SonarQube Cloud | Latest | Security and code quality analysis |
| **CI/CD** | GitHub Actions | Latest | Automated workflows |
| **Registry** | Docker Hub | Latest | Container image registry |

---

## Project Structure

```
devsecops-proyect/
├── app.py                          # Main Flask application
├── Dockerfile                      # Docker container specification
├── requirements.txt                # Python dependencies
├── sonar-project.properties        # SonarQube configuration
├── README.md                       # This comprehensive documentation
├── .github/                        # GitHub Actions workflows
│   └── workflows/                  # CI/CD pipeline definitions
├── k8s/                            # Kubernetes configurations
│   ├── deployment.yaml             # Complete K8s deployment spec
│   ├── README.md                   # K8s deployment guide
│   ├── DOCKERHUB_SETUP.md         # Docker Hub authentication guide
│   └── setup-dockerhub.sh         # Automated setup script
├── static/                         # Static assets
│   └── style.css                   # Web UI styling
├── templates/                      # HTML templates
│   └── index.html                  # Web UI home page
├── tests/                          # Test suite
│   └── test_app.py                # Application tests
└── actions-runner/                 # GitHub Actions runner configuration
    └── [runner files]              # Self-hosted runner setup
```

---

## Prerequisites

### System Requirements

- **OS**: Linux, macOS, or Windows (with WSL2)
- **RAM**: Minimum 4GB (8GB+ recommended)
- **Storage**: Minimum 5GB free space
- **Network**: Internet connection for downloading dependencies

### Required Software

```bash
# Python 3.12
python3 --version  # Should be 3.12+

# pip (Python package manager)
pip --version

# Docker (for containerization)
docker --version  # Should be 20.10+

# kubectl (for Kubernetes)
kubectl version --client

# git (for version control)
git --version
```

### Optional Tools

- **Docker Desktop**: Comes with Kubernetes support
- **kind** or **minikube**: Local Kubernetes clusters for development
- **curl** or **Postman**: For API testing

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/hungles/devsecops-proyect.git
cd devsecops-proyect
```

### 2. Create Python Virtual Environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate virtual environment
# On Linux/macOS:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables (Optional)

```bash
# Create .env file (if needed)
# export FLASK_ENV=development
# export FLASK_DEBUG=1
```

---

## Running the Application

### Local Development

#### Method 1: Direct Python Execution

```bash
# Activate virtual environment
source venv/bin/activate

# Run Flask development server
python app.py
```

**Access the application**: http://localhost:5000

#### Method 2: Using Gunicorn (Production-like)

```bash
# Activate virtual environment
source venv/bin/activate

# Run with Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app
```

#### Method 3: Using Flask CLI

```bash
export FLASK_APP=app.py
export FLASK_ENV=development
flask run --host=0.0.0.0 --port=5000
```

### Stopping the Application

```bash
# Press Ctrl+C in the terminal running the application
```

---

## Docker Containerization

### Building Docker Image

```bash
# Build image locally
docker build -t devsecops-app:latest .

# Or with your Docker Hub username
docker build -t YOUR_USERNAME/devsecops-app:latest .
```

### Running Docker Container

```bash
# Run container locally
docker run -p 5000:5000 devsecops-app:latest

# Run with environment variables
docker run -e FLASK_ENV=production -p 5000:5000 devsecops-app:latest

# Run in background (detached mode)
docker run -d -p 5000:5000 --name devsecops-app devsecops-app:latest
```

### Docker Commands

```bash
# List running containers
docker ps

# List all containers
docker ps -a

# View container logs
docker logs -f CONTAINER_ID

# Stop container
docker stop CONTAINER_ID

# Remove container
docker rm CONTAINER_ID

# Remove image
docker rmi devsecops-app:latest
```

### Pushing to Docker Hub

```bash
# Login to Docker Hub
docker login

# Tag image for Docker Hub
docker tag devsecops-app:latest YOUR_USERNAME/devsecops-app:latest

# Push to Docker Hub
docker push YOUR_USERNAME/devsecops-app:latest

# Verify image in Docker Hub
docker pull YOUR_USERNAME/devsecops-app:latest
```

---

## Kubernetes Deployment

### Prerequisites for Kubernetes

- Kubernetes cluster running (v1.20+)
- `kubectl` configured to access your cluster
- Docker image pushed to Docker Hub
- Docker Hub credentials configured

### Setup Process

#### Step 1: Create Docker Hub Secret

**Option A: Using the automated script**

```bash
chmod +x k8s/setup-dockerhub.sh
./k8s/setup-dockerhub.sh YOUR_USERNAME DOCKERHUB_TOKEN
```

**Option B: Manual setup with kubectl**

```bash
kubectl create secret docker-registry dockerhub-secret \
  --docker-server=docker.io \
  --docker-username=YOUR_USERNAME \
  --docker-password=DOCKERHUB_TOKEN \
  --docker-email=your.email@example.com \
  -n devsecops
```

#### Step 2: Update deployment.yaml

Edit `k8s/deployment.yaml` and replace `YOUR_USERNAME_DOCKERHUB` with your actual Docker Hub username:

```yaml
image: scarmona04/devsecops-proyect:latest
```

#### Step 3: Apply Kubernetes Configuration

```bash
kubectl apply -f k8s/deployment.yaml
```

### Deployment Components

The `k8s/deployment.yaml` includes:

1. **Namespace**: `devsecops` (isolated environment)
2. **Deployment**: 
   - 3 initial replicas
   - Rolling update strategy
   - Health checks (liveness & readiness probes)
   - Resource limits and requests
   - Security context (non-root user)

3. **Service**: 
   - Type: LoadBalancer
   - Exposes port 80 → 5000

4. **HorizontalPodAutoscaler (HPA)**:
   - Min replicas: 2
   - Max replicas: 10
   - CPU trigger: 70% utilization
   - Memory trigger: 80% utilization

### Verifying Deployment

```bash
# Check namespace
kubectl get namespace

# Check deployment status
kubectl get deployment -n devsecops
kubectl describe deployment devsecops-app -n devsecops

# Check running pods
kubectl get pods -n devsecops
kubectl describe pod POD_NAME -n devsecops

# Check service
kubectl get svc -n devsecops

# Check HPA status
kubectl get hpa -n devsecops
kubectl describe hpa devsecops-app -n devsecops
```

### Accessing the Application

```bash
# Port forward to local machine
kubectl port-forward -n devsecops svc/devsecops-app 8080:80

# Access via: http://localhost:8080
```

### Updating Deployment

```bash
# Update image
kubectl set image deployment/devsecops-app \
  devsecops-app=YOUR_USERNAME/devsecops-app:v2.0.0 \
  -n devsecops

# Verify rollout
kubectl rollout status deployment/devsecops-app -n devsecops

# View rollout history
kubectl rollout history deployment/devsecops-app -n devsecops

# Rollback to previous version
kubectl rollout undo deployment/devsecops-app -n devsecops
```

### Scaling

```bash
# Manual scaling
kubectl scale deployment devsecops-app --replicas=5 -n devsecops

# Monitor autoscaling
kubectl get hpa -n devsecops -w
```

### Cleanup

```bash
# Delete everything in the namespace
kubectl delete namespace devsecops

# Or delete individual resources
kubectl delete deployment devsecops-app -n devsecops
kubectl delete service devsecops-app -n devsecops
kubectl delete hpa devsecops-app -n devsecops
```

---

## Testing

### Running Tests Locally

```bash
# Activate virtual environment
source venv/bin/activate

# Run all tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_app.py

# Run specific test function
pytest tests/test_app.py::test_health_endpoint

# Run with coverage report
pytest --cov=.

# Generate HTML coverage report
pytest --cov=. --cov-report=html
```

### Test Structure

The project includes the following test cases in `tests/test_app.py`:

#### Test 1: Home Page
```python
def test_home_page(client):
    # Verifies the home page loads and contains expected content
    # Asserts: HTTP 200 and 'DevSecOps Sample App' in response
```

#### Test 2: Health Check Endpoint
```python
def test_health_endpoint(client):
    # Verifies the /api/health endpoint works
    # Asserts: HTTP 200 and correct JSON response
```

#### Test 3: Message Processing Endpoint
```python
def test_message_endpoint(client):
    # Verifies the /api/message endpoint processes POST requests
    # Asserts: HTTP 200 and correct message length calculation
```

### Coverage Metrics

The project uses `pytest-cov` to measure code coverage:

```bash
# Generate coverage report
pytest --cov=. --cov-report=term-missing

# HTML report
pytest --cov=. --cov-report=html
# Open: htmlcov/index.html
```

### Test Best Practices

- ✅ All tests pass before deployment
- ✅ Minimum 80% code coverage
- ✅ Tests run automatically in CI/CD pipeline
- ✅ Use meaningful test names
- ✅ Test both happy paths and error cases

---

## CI/CD Pipeline

### GitHub Actions Workflow

The project includes automated CI/CD through GitHub Actions (configured in `.github/workflows/`).

### Pipeline Stages

1. **Code Checkout**: Clone repository
2. **Environment Setup**: Install Python and dependencies
3. **Linting**: Run flake8 code quality checks
4. **Testing**: Execute test suite with coverage
5. **Security Scan**: Run SonarQube analysis
6. **Build**: Build Docker image
7. **Publish**: Push image to Docker Hub
8. **Deploy**: Update Kubernetes deployment

### Workflow Triggers

- **On Push**: To main/master branch
- **On Pull Request**: To verify changes
- **Scheduled**: Nightly builds
- **Manual**: Via GitHub Actions UI

### Viewing Workflow Status

```bash
# Via GitHub:
# 1. Go to repository → Actions tab
# 2. View workflow runs and logs

# Via CLI:
gh run list
gh run view RUN_ID
gh run view RUN_ID --log
```

### Configuring Secrets

For the CI/CD pipeline to work, configure these secrets in GitHub:

```
Settings → Secrets and variables → Actions → New repository secret
```

**Required Secrets:**
- `DOCKERHUB_USERNAME`: Your Docker Hub username
- `DOCKERHUB_TOKEN`: Your Docker Hub personal access token
- `SONARQUBE_TOKEN`: Your SonarQube token
- `KUBE_CONFIG`: Base64-encoded kubeconfig file (optional)

### Manual Workflow Triggers

```bash
# Trigger workflow via CLI
gh workflow run "CI/CD Pipeline" --ref main

# View workflow details
gh workflow view "CI/CD Pipeline"
```

---

## Code Quality & Security

### SonarQube Integration

#### Configuration

The project uses **SonarQube Cloud** for code quality analysis.

**File**: `sonar-project.properties`

```properties
sonar.host.url=https://sonarcloud.io
sonar.projectKey=hungles_devsecops-proyect
sonar.organization=hungles
sonar.sources=.
sonar.exclusions=tests/**
sonar.tests=tests
sonar.python.coverage.reportPaths=coverage.xml
```

#### Accessing SonarQube Dashboard

```
https://sonarcloud.io/dashboard?id=hungles_devsecops-proyect
```

#### Running SonarQube Analysis Locally

```bash
# Install SonarScanner
brew install sonar-scanner  # macOS
# or download from https://docs.sonarqube.org/latest/analysis/scan/sonarscanner/

# Run analysis
sonar-scanner \
  -Dsonar.projectKey=hungles_devsecops-proyect \
  -Dsonar.sources=. \
  -Dsonar.exclusions=tests/** \
  -Dsonar.python.coverage.reportPaths=coverage.xml
```

### Code Quality Metrics

| Metric | Target | Tool |
|--------|--------|------|
| Code Coverage | ≥80% | pytest-cov |
| Code Smells | <5 | SonarQube |
| Security Hotspots | 0 Critical | SonarQube |
| Vulnerabilities | 0 | SonarQube |
| Code Standards | Passed | flake8 |

### Linting with flake8

```bash
# Run flake8 checks
flake8 .

# Check specific file
flake8 app.py

# Generate HTML report
flake8 --format=html --htmldir=flake8_report .
```

### Security Best Practices

1. **Container Security**:
   - ✅ Non-root user (uid: 1000)
   - ✅ Read-only root filesystem
   - ✅ Minimal capabilities
   - ✅ No privilege escalation

2. **Kubernetes Security**:
   - ✅ Network policies
   - ✅ Resource limits
   - ✅ Security context
   - ✅ Image pull secrets

3. **Code Security**:
   - ✅ Input validation
   - ✅ No hardcoded secrets
   - ✅ HTTPS ready
   - ✅ Secure dependencies

4. **Deployment Security**:
   - ✅ Health checks
   - ✅ Auto-recovery
   - ✅ Resource quotas
   - ✅ Pod disruption budgets

---

## API Documentation

### Base URL

- **Local Development**: `http://localhost:5000`
- **Kubernetes**: `http://service-ip` or port-forward

### Endpoints

#### 1. Home Page

**Endpoint**: `GET /`

**Description**: Returns the home page HTML

**Response**: HTML page with web UI

**Example**:
```bash
curl http://localhost:5000/
```

#### 2. Health Check

**Endpoint**: `GET /api/health`

**Description**: Returns application health status

**Response**:
```json
{
  "status": "ok",
  "message": "DevSecOps app running"
}
```

**Example**:
```bash
curl http://localhost:5000/api/health
```

**Use Cases**:
- Kubernetes liveness probe
- Kubernetes readiness probe
- Health monitoring
- Load balancer checks

#### 3. Message Processing

**Endpoint**: `POST /api/message`

**Description**: Accepts a JSON message and returns processing results

**Request Body**:
```json
{
  "text": "Your message here"
}
```

**Response**:
```json
{
  "received": "Your message here",
  "length": 18
}
```

**Example**:
```bash
curl -X POST http://localhost:5000/api/message \
  -H "Content-Type: application/json" \
  -d '{"text": "Hello DevSecOps"}'
```

**Response**:
```json
{
  "received": "Hello DevSecOps",
  "length": 15
}
```

### Error Handling

The application handles various error scenarios:

| Scenario | Status Code | Response |
|----------|-------------|----------|
| Endpoint not found | 404 | JSON error message |
| Invalid method | 405 | JSON error message |
| Server error | 500 | JSON error message |
| Invalid JSON | 400 | Empty object (handled gracefully) |

---

## Monitoring & Troubleshooting

### Checking Application Status

#### Docker

```bash
# Check container status
docker ps | grep devsecops-app

# View container logs
docker logs -f devsecops-app

# Check container resource usage
docker stats devsecops-app

# Inspect container details
docker inspect devsecops-app
```

#### Kubernetes

```bash
# Check deployment status
kubectl get deployment devsecops-app -n devsecops -o wide

# View pod status
kubectl get pods -n devsecops -o wide

# Check pod events
kubectl describe pod POD_NAME -n devsecops

# View pod logs
kubectl logs -f POD_NAME -n devsecops

# Check resource usage
kubectl top pods -n devsecops
kubectl top nodes

# View events
kubectl get events -n devsecops
```

### Common Issues and Solutions

#### Issue 1: Pods Not Starting

**Symptoms**: Pods remain in `Pending` or `ImagePullBackOff` state

**Solutions**:
```bash
# Check pod events
kubectl describe pod POD_NAME -n devsecops

# Verify image exists
docker pull scarmona04/devsecops-proyect:latest

# Check Docker Hub secret
kubectl get secret dockerhub-secret -n devsecops -o yaml

# Recreate secret if needed
kubectl delete secret dockerhub-secret -n devsecops
./k8s/setup-dockerhub.sh USERNAME TOKEN
```

#### Issue 2: Health Probe Failures

**Symptoms**: Pods crash with CrashLoopBackOff

**Solutions**:
```bash
# Check application logs
kubectl logs POD_NAME -n devsecops

# Test health endpoint manually
kubectl exec POD_NAME -n devsecops -- curl http://localhost:5000/api/health

# Increase initial delay if needed (edit deployment.yaml)
initialDelaySeconds: 15  # Increase from 10
```

#### Issue 3: Service Not Accessible

**Symptoms**: Cannot access service from outside cluster

**Solutions**:
```bash
# Verify service exists
kubectl get svc -n devsecops

# Check service endpoints
kubectl get endpoints -n devsecops

# Port forward and test
kubectl port-forward -n devsecops svc/devsecops-app 8080:80
curl http://localhost:8080

# Check service type
kubectl get svc devsecops-app -n devsecops -o yaml | grep type
```

#### Issue 4: High Resource Usage

**Symptoms**: HPA scaling aggressively or pods using excessive resources

**Solutions**:
```bash
# Check resource usage
kubectl top pods -n devsecops

# View HPA metrics
kubectl get hpa -n devsecops
kubectl describe hpa devsecops-app -n devsecops

# Update resource limits in deployment.yaml
resources:
  limits:
    cpu: 500m
    memory: 512Mi
```

### Performance Monitoring

```bash
# Real-time monitoring
watch kubectl get pods -n devsecops

# Monitor HPA scaling
watch kubectl get hpa -n devsecops

# Continuous resource monitoring
kubectl top nodes -w
kubectl top pods -n devsecops -w

# Create metrics dashboard
# Use Kubernetes Dashboard, Grafana, or Prometheus
```

### Logging

#### Local Logs

```bash
# Flask development logs
python app.py  # See console output

# Gunicorn logs
gunicorn --bind 0.0.0.0:5000 app:app
```

#### Docker Logs

```bash
# View logs
docker logs -f devsecops-app

# Tail last 100 lines
docker logs --tail 100 devsecops-app
```

#### Kubernetes Logs

```bash
# View pod logs
kubectl logs -f POD_NAME -n devsecops

# View logs from all pods
kubectl logs -l app=devsecops-app -n devsecops

# View previous logs (if pod crashed)
kubectl logs POD_NAME -n devsecops --previous
```

---

## Contributing Guidelines

### Code Style

Follow these standards when contributing:

- **PEP 8**: Python Enhancement Proposal 8
- **Line Length**: 79 characters maximum
- **Indentation**: 4 spaces
- **Imports**: Organized and sorted

**Check with flake8**:
```bash
flake8 your_file.py
```

### Adding Features

1. Create a feature branch:
```bash
git checkout -b feature/your-feature-name
```

2. Make changes and test:
```bash
pytest --cov=.
```

3. Commit with clear messages:
```bash
git commit -m "feat: add new feature description"
```

4. Push and create pull request:
```bash
git push origin feature/your-feature-name
```

### Adding Tests

When adding new functionality:

```python
def test_new_feature(client):
    """Test description of what this test verifies"""
    response = client.get('/api/endpoint')
    assert response.status_code == 200
    # Add more assertions
```

Run tests before submitting:
```bash
pytest -v
```

### Version Control

- Main branch: Stable, production-ready code
- Develop branch: Integration branch for features
- Feature branches: Individual feature development

### Release Process

1. Update version in `app.py`
2. Update `CHANGELOG.md`
3. Create release tag
4. Build and push Docker image
5. Update Kubernetes deployment
6. Deploy to production

---

## Additional Resources

### Official Documentation

- [Flask Documentation](https://flask.palletsprojects.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Kubernetes Documentation](https://kubernetes.io/docs/)
- [SonarQube Documentation](https://docs.sonarqube.org/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

### Learning Resources

- [DevSecOps Best Practices](https://www.devsecops.org/)
- [Kubernetes Best Practices](https://kubernetes.io/docs/concepts/configuration/overview/)
- [Container Security](https://kubernetes.io/docs/concepts/security/)
- [CI/CD Pipeline Patterns](https://martinfowler.com/articles/continuousIntegration.html)

### Tools and Services

- [Docker Hub](https://hub.docker.com/)
- [SonarCloud](https://sonarcloud.io/)
- [GitHub](https://github.com/)
- [Kubernetes](https://kubernetes.io/)

---

## Support and Contact

For issues, questions, or contributions:

- **GitHub Issues**: Report bugs and request features
- **GitHub Discussions**: Ask questions and share ideas
- **Organization**: hungles
- **Repository**: devsecops-proyect

---

## License

This project is provided as-is for educational and demonstrative purposes in DevSecOps practices.

---

**Last Updated**: June 8, 2026  
**Version**: 1.0  
**Status**: Active Development
