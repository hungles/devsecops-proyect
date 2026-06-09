# DevSecOps Project - Quick Reference Guide

A quick command reference for common development and deployment tasks.

## Table of Contents

- [Development Setup](#development-setup)
- [Running the Application](#running-the-application)
- [Testing](#testing)
- [Docker Commands](#docker-commands)
- [Kubernetes Commands](#kubernetes-commands)
- [Troubleshooting](#troubleshooting)

---

## Development Setup

```bash
# Clone repository
git clone https://github.com/hungles/devsecops-proyect.git
cd devsecops-proyect

# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate          # Linux/macOS
# or: venv\Scripts\activate       # Windows

# Install dependencies
pip install -r requirements.txt

# Verify installation
python --version
pip list | grep -E "Flask|pytest|gunicorn"
```

---

## Running the Application

### Development Server

```bash
# Flask development server
python app.py
# Access: http://localhost:5000

# With debug enabled
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py

# With environment variable on Windows
set FLASK_ENV=development
set FLASK_DEBUG=1
python app.py
```

### Production Server

```bash
# Using Gunicorn
gunicorn --bind 0.0.0.0:5000 app:app

# With multiple workers
gunicorn --workers 4 --bind 0.0.0.0:5000 app:app

# With logging
gunicorn --access-logfile - --error-logfile - --bind 0.0.0.0:5000 app:app
```

### Flask CLI

```bash
export FLASK_APP=app.py
flask run --host=0.0.0.0 --port=5000
```

---

## Testing

### Basic Testing

```bash
# Run all tests
pytest

# Verbose output
pytest -v

# Stop on first failure
pytest -x

# Show local variables on failure
pytest -l

# Run specific test file
pytest tests/test_app.py

# Run specific test function
pytest tests/test_app.py::test_health_endpoint
```

### Coverage

```bash
# Generate coverage report
pytest --cov=.

# Coverage with missing line numbers
pytest --cov=. --cov-report=term-missing

# HTML coverage report
pytest --cov=. --cov-report=html
# Open: htmlcov/index.html

# Coverage percentage
pytest --cov=. --cov-report=term-missing | grep TOTAL
```

---

## Docker Commands

### Building Images

```bash
# Build locally
docker build -t devsecops-app:latest .

# Build with tag
docker build -t devsecops-app:v1.0.0 .

# Build with username
docker build -t YOUR_USERNAME/devsecops-app:latest .

# Build with build arguments
docker build --build-arg PYTHON_VERSION=3.12 -t devsecops-app:latest .
```

### Running Containers

```bash
# Run and remove after exit
docker run --rm -p 5000:5000 devsecops-app:latest

# Run in background
docker run -d -p 5000:5000 --name devsecops-app devsecops-app:latest

# Run with environment variables
docker run -e FLASK_ENV=production -p 5000:5000 devsecops-app:latest

# Run with volume mount
docker run -v $(pwd):/app -p 5000:5000 devsecops-app:latest

# Run with resource limits
docker run -m 512m --cpus 1 -p 5000:5000 devsecops-app:latest
```

### Container Management

```bash
# List running containers
docker ps

# List all containers
docker ps -a

# View container logs
docker logs CONTAINER_ID
docker logs -f CONTAINER_ID          # Follow logs
docker logs --tail 50 CONTAINER_ID   # Last 50 lines

# Stop container
docker stop CONTAINER_ID

# Start stopped container
docker start CONTAINER_ID

# Remove container
docker rm CONTAINER_ID

# Execute command in running container
docker exec -it CONTAINER_ID bash

# View container stats
docker stats CONTAINER_ID
```

### Image Management

```bash
# List images
docker images

# Show image details
docker inspect devsecops-app:latest

# Remove image
docker rmi devsecops-app:latest

# Remove unused images
docker image prune

# Tag image
docker tag devsecops-app:latest YOUR_USERNAME/devsecops-app:latest

# Save image to file
docker save devsecops-app:latest > devsecops-app.tar

# Load image from file
docker load < devsecops-app.tar
```

### Docker Hub Operations

```bash
# Login to Docker Hub
docker login

# Logout
docker logout

# Push image
docker push YOUR_USERNAME/devsecops-app:latest

# Pull image
docker pull YOUR_USERNAME/devsecops-app:latest

# Pull specific version
docker pull YOUR_USERNAME/devsecops-app:v1.0.0

# Search images
docker search devsecops
```

---

## Kubernetes Commands

### Cluster Information

```bash
# Get cluster info
kubectl cluster-info

# View cluster nodes
kubectl get nodes

# Node details
kubectl describe node NODE_NAME

# View all contexts
kubectl config get-contexts

# Switch context
kubectl config use-context CONTEXT_NAME
```

### Namespace Management

```bash
# List namespaces
kubectl get namespace

# Create namespace
kubectl create namespace devsecops

# Delete namespace
kubectl delete namespace devsecops

# Set default namespace
kubectl config set-context --current --namespace=devsecops
```

### Deployment Management

```bash
# Apply configuration
kubectl apply -f k8s/deployment.yaml

# Validate configuration
kubectl apply -f k8s/deployment.yaml --dry-run=client

# Get deployments
kubectl get deployment -n devsecops

# Describe deployment
kubectl describe deployment devsecops-app -n devsecops

# Edit deployment
kubectl edit deployment devsecops-app -n devsecops

# Delete deployment
kubectl delete deployment devsecops-app -n devsecops

# View deployment history
kubectl rollout history deployment/devsecops-app -n devsecops

# Rollback deployment
kubectl rollout undo deployment/devsecops-app -n devsecops

# Check rollout status
kubectl rollout status deployment/devsecops-app -n devsecops
```

### Pod Management

```bash
# List pods
kubectl get pods -n devsecops

# List pods with details
kubectl get pods -n devsecops -o wide

# Describe pod
kubectl describe pod POD_NAME -n devsecops

# View pod logs
kubectl logs POD_NAME -n devsecops

# Tail logs
kubectl logs -f POD_NAME -n devsecops

# Previous logs (crashed pod)
kubectl logs POD_NAME -n devsecops --previous

# Execute command in pod
kubectl exec -it POD_NAME -n devsecops -- bash

# Port forward to pod
kubectl port-forward POD_NAME 8080:5000 -n devsecops

# Delete pod
kubectl delete pod POD_NAME -n devsecops
```

### Service Management

```bash
# List services
kubectl get svc -n devsecops

# Describe service
kubectl describe svc devsecops-app -n devsecops

# Get service endpoints
kubectl get endpoints -n devsecops

# Port forward to service
kubectl port-forward svc/devsecops-app 8080:80 -n devsecops

# View service YAML
kubectl get svc devsecops-app -n devsecops -o yaml
```

### Scaling

```bash
# Manual scale
kubectl scale deployment devsecops-app --replicas=5 -n devsecops

# Set replicas
kubectl patch deployment devsecops-app -p '{"spec":{"replicas":3}}' -n devsecops

# View HPA status
kubectl get hpa -n devsecops

# Describe HPA
kubectl describe hpa devsecops-app -n devsecops

# Watch HPA scaling
kubectl get hpa -n devsecops -w
```

### Monitoring

```bash
# View events
kubectl get events -n devsecops

# Top nodes
kubectl top nodes

# Top pods
kubectl top pods -n devsecops

# Watch resources
kubectl get pods -n devsecops -w

# View pod metrics
kubectl describe node NODE_NAME | grep -A 5 "Allocated resources"
```

### Secret Management

```bash
# Create Docker Hub secret
kubectl create secret docker-registry dockerhub-secret \
  --docker-server=docker.io \
  --docker-username=USERNAME \
  --docker-password=TOKEN \
  --docker-email=email@example.com \
  -n devsecops

# List secrets
kubectl get secrets -n devsecops

# Describe secret
kubectl describe secret dockerhub-secret -n devsecops

# View secret YAML
kubectl get secret dockerhub-secret -n devsecops -o yaml

# Delete secret
kubectl delete secret dockerhub-secret -n devsecops
```

### Configuration

```bash
# Create ConfigMap
kubectl create configmap app-config --from-literal=ENV=production -n devsecops

# Create from file
kubectl create configmap app-config --from-file=config.yaml -n devsecops

# View ConfigMap
kubectl get configmap -n devsecops

# Edit ConfigMap
kubectl edit configmap app-config -n devsecops

# Delete ConfigMap
kubectl delete configmap app-config -n devsecops
```

---

## Troubleshooting

### Pods Not Starting

```bash
# Check pod status
kubectl describe pod POD_NAME -n devsecops

# View logs
kubectl logs POD_NAME -n devsecops

# Check image pull
kubectl get events -n devsecops | grep ImagePullBackOff

# Verify secret
kubectl get secret dockerhub-secret -n devsecops -o yaml

# Test image manually
docker pull YOUR_USERNAME/devsecops-app:latest
```

### Health Check Failures

```bash
# Check endpoints
kubectl get endpoints devsecops-app -n devsecops

# Test health manually
kubectl exec POD_NAME -n devsecops -- curl http://localhost:5000/api/health

# View readiness events
kubectl describe pod POD_NAME -n devsecops | grep -A 5 "Readiness"

# Check liveness events
kubectl describe pod POD_NAME -n devsecops | grep -A 5 "Liveness"
```

### Service Not Accessible

```bash
# Test port forward
kubectl port-forward svc/devsecops-app 8080:80 -n devsecops
# From another terminal: curl http://localhost:8080

# Check service selector
kubectl get svc devsecops-app -n devsecops -o yaml | grep -A 5 "selector"

# List matching pods
kubectl get pods -l app=devsecops-app -n devsecops

# Check service endpoints
kubectl get endpoints devsecops-app -n devsecops
```

### Resource Issues

```bash
# Check resource usage
kubectl top pods -n devsecops

# Check node capacity
kubectl describe nodes | grep -A 5 "Capacity\|Allocatable"

# View resource requests/limits
kubectl get pod POD_NAME -n devsecops -o yaml | grep -A 10 "resources"

# Check HPA scaling decisions
kubectl describe hpa devsecops-app -n devsecops
```

---

## Common Workflows

### Deploy New Version

```bash
# 1. Build and push image
docker build -t YOUR_USERNAME/devsecops-app:v1.1.0 .
docker push YOUR_USERNAME/devsecops-app:v1.1.0

# 2. Update image in deployment
kubectl set image deployment/devsecops-app \
  devsecops-app=YOUR_USERNAME/devsecops-app:v1.1.0 \
  -n devsecops

# 3. Monitor rollout
kubectl rollout status deployment/devsecops-app -n devsecops

# 4. Verify deployment
kubectl get pods -n devsecops
```

### Test Locally Before Deployment

```bash
# 1. Run tests
pytest --cov=. --cov-report=term-missing

# 2. Check code quality
flake8

# 3. Build Docker image
docker build -t devsecops-app:test .

# 4. Run container
docker run -p 5000:5000 devsecops-app:test

# 5. Test endpoints
curl http://localhost:5000/api/health
```

### Scale Application

```bash
# Quick scale up
kubectl scale deployment devsecops-app --replicas=10 -n devsecops

# Scale down
kubectl scale deployment devsecops-app --replicas=2 -n devsecops

# Let HPA handle scaling
kubectl get hpa -n devsecops -w
```

---

## Useful Aliases

Add to `.bashrc` or `.zshrc`:

```bash
# Kubernetes aliases
alias k='kubectl'
alias kgp='kubectl get pods'
alias kgs='kubectl get svc'
alias kdp='kubectl describe pod'
alias kl='kubectl logs'
alias klf='kubectl logs -f'
alias kd='kubectl describe'
alias ke='kubectl exec -it'
alias kaf='kubectl apply -f'
alias krf='kubectl delete -f'

# Docker aliases
alias d='docker'
alias dps='docker ps'
alias dimg='docker images'
alias drun='docker run'
alias dlogs='docker logs -f'
alias dstop='docker stop'
alias drm='docker rm'
```

---

## Environment Variables

```bash
# Kubernetes
export KUBECONFIG=~/.kube/config
export KUBE_NAMESPACE=devsecops

# Docker
export DOCKER_USERNAME=your_username
export DOCKERHUB_TOKEN=your_token

# Python
export PYTHONUNBUFFERED=1  # Don't buffer output
export FLASK_APP=app.py
export FLASK_ENV=development
```

---

**Last Updated**: June 8, 2026  
**Reference Version**: 1.0
