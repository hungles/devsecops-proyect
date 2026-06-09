# Docker Hub Setup for Kubernetes

This guide explains how to publish the container image to Docker Hub and configure Kubernetes to pull it.

## 1. Build and tag the Docker image

```bash
docker build -t devsecops-app:latest .
docker tag devsecops-app:latest YOUR_USERNAME/devsecops-app:latest
```

## 2. Log in to Docker Hub

```bash
docker login
```

Provide your Docker Hub username and password or access token.

## 3. Push the image to Docker Hub

```bash
docker push YOUR_USERNAME/devsecops-app:latest
```

## 4. Create the Kubernetes registry secret

Kubernetes needs a registry secret to pull images from Docker Hub. Run:

```bash
kubectl create secret docker-registry dockerhub-secret \
  --docker-server=docker.io \
  --docker-username=YOUR_USERNAME \
  --docker-password=DOCKERHUB_TOKEN \
  --docker-email=your.email@example.com \
  -n devsecops
```

## 5. Update the deployment image reference

Edit `k8s/deployment.yaml` and replace the image name with your Docker Hub repository:

```yaml
image: YOUR_USERNAME/devsecops-app:latest
```

## 6. Apply the Kubernetes manifest

```bash
kubectl apply -f k8s/deployment.yaml
```

## 7. Verify the secret and deployment

```bash
kubectl get secret dockerhub-secret -n devsecops
kubectl describe secret dockerhub-secret -n devsecops
kubectl get pods -n devsecops
```
