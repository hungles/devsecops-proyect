# Kubernetes Deployment Guide

This guide explains how to deploy the project to Kubernetes, including local cluster setup with `kind` and container registry configuration.

## Purpose

Use this guide when you want to:
- Run the application in a local Kubernetes cluster with `kind`
- Deploy the app using the existing `k8s/deployment.yaml`
- Configure Docker Hub credentials for image pulls

## Prerequisites

- Docker installed and running
- `kubectl` configured
- `kind` installed for local Kubernetes testing
- A Docker Hub account (optional for `kind`, required for remote cluster deployments)

## 1. Create a local `kind` cluster

Install `kind` if needed:

```bash
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.32.0/kind-linux-amd64
chmod +x ./kind
sudo mv ./kind /usr/local/bin/kind
```

Create a cluster named `devsecops`:

```bash
kind create cluster --name devsecops
```

Verify the cluster is ready:

```bash
kubectl cluster-info --context kind-devsecops
kubectl get nodes
```

## 2. Build the Docker image and load it into `kind`

For local `kind` deployments, load the image directly into the cluster:

```bash
docker build -t devsecops-app:latest .
kind load docker-image devsecops-app:latest --name devsecops
```

If you prefer to use Docker Hub instead of loading the image directly, see `k8s/DOCKERHUB_SETUP.md`.

## 3. Deploy the application

Apply the Kubernetes manifest:

```bash
kubectl apply -f k8s/deployment.yaml
```

Verify the deployment:

```bash
kubectl get namespace
kubectl get pods -n devsecops
kubectl get svc -n devsecops
```

## 4. Access the application

Port-forward the service to your local machine:

```bash
kubectl port-forward -n devsecops svc/devsecops-app 8080:80
```

Open:

```text
http://localhost:8080
```

## 5. Docker Hub setup for Kubernetes

If you need to push images to Docker Hub and let Kubernetes pull them, see:

```bash
cat k8s/DOCKERHUB_SETUP.md
```
