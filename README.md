Full Stack CRUD App with Docker, Kubernetes, and Monitoring

This repository contains a Full Stack CRUD Application running in Docker containers, managed by Kubernetes, and monitored using Prometheus and Grafana. The app demonstrates a simple CRUD system, utilizing Ingress, Persistent Volumes, and other Kubernetes services.
Project Overview

This project showcases:

    A React.js frontend for the user interface.
    A Python Flask backend handling API requests and logic.
    An SQLite database stored on the backend container using a Persistent Volume.
    Continuous Integration/Continuous Deployment (CI/CD) pipeline using GitHub Actions.
    Monitoring with Prometheus and Grafana for tracking performance and availability.
    Kubernetes setup with Ingress for routing traffic, and Persistent Volumes to ensure data persistence.

Tech Stack

    Frontend: React.js
    Backend: Python Flask
    Database: SQLite (stored on backend)
    Containerization: Docker
    Orchestration: Kubernetes (Minikube or cloud-based cluster)
    Monitoring: Prometheus and Grafana
    CI/CD: GitHub Actions
    Routing: Ingress Controller (NGINX)
    Persistent Storage: Kubernetes Persistent Volume

Features

    CRUD Operations: Full functionality for Create, Read, Update, and Delete operations on a simple data model.
    Dockerized Application: All components (frontend, backend, database) are containerized using Docker for consistent development and deployment.
    Kubernetes Orchestration: The application is deployed and managed using Kubernetes, allowing for scalability and resilience.
    Persistent Storage: The SQLite database uses a persistent volume to ensure data is not lost when containers are restarted.
    Monitoring: Prometheus collects metrics, while Grafana provides dashboards for real-time visualization of the application's performance.
    CI/CD Pipeline: Automated builds and deployments using GitHub Actions.

Prerequisites

To run this project locally or on a Kubernetes cluster, you'll need:

    Docker
    Kubernetes (Minikube or a cloud provider like GKE, EKS, or AKS)
    kubectl command-line tool
    Helm (for Prometheus and Grafana installation)
    Python and Flask installed

Setup and Installation
1. Clone the Repository

git clone https://github.com/jovan99djokic/Full_stack_app.git
cd Full_stack_app

2. Build Docker Images

Build the backend and frontend Docker images:

docker build -t your-username/backend-app ./backend
docker build -t your-username/frontend-app ./frontend

3. Deploy to Kubernetes

Ensure you have a running Kubernetes cluster (e.g., Minikube) and apply the necessary Kubernetes configurations:

kubectl apply -f k8s/backend-deployment.yaml
kubectl apply -f k8s/frontend-deployment.yaml
kubectl apply -f k8s/ingress.yaml

4. Access the Application

Once deployed, the application can be accessed via the Ingress controller URL.
5. Monitoring Setup

    Install Prometheus & Grafana using Helm:

helm install prometheus prometheus-community/kube-prometheus-stack
helm install grafana grafana/grafana

Access Prometheus:

kubectl port-forward svc/prometheus-service -n monitoring 9090:9090

Open your browser at http://localhost:9090.

Access Grafana:

    kubectl port-forward svc/grafana-service -n monitoring 3000:3000

    Open your browser at http://localhost:3000 (default credentials: admin/admin).

6. Continuous Deployment

This project uses GitHub Actions for automated Docker image builds and Kubernetes deployments. Any push to the main branch triggers the pipeline defined in .github/workflows.
Project Structure

    backend/ - Contains the Node.js/Express server and SQLite database setup.
    frontend/ - React.js frontend for interacting with the CRUD system.
    k8s/ - Kubernetes deployment, service, and ingress configuration files.
    .github/ - GitHub Actions workflows for CI/CD.

Contributions

Feel free to fork this project, submit issues, or open pull requests for improvements.
