# ☁️ Cloud Native Flask Microservice Deployment on AWS EKS

This project demonstrates the deployment, monitoring, and automation of a lightweight Flask-based microservice on Amazon EKS using a fully integrated GitHub Actions CI/CD pipeline. The setup includes Prometheus + Grafana for observability, Docker + Kubernetes for container orchestration, and infrastructure-as-code practices via `eksctl`.

---

## 🚀 Project Overview

| Layer            | Tools Used                                |
|------------------|--------------------------------------------|
| Cloud Platform   | AWS (EKS, EC2, IAM, VPC)                   |
| Containerization | Docker                                     |
| Orchestration    | Kubernetes via Amazon EKS                  |
| CI/CD Pipeline   | GitHub Actions                             |
| Monitoring       | Prometheus + Grafana                       |
| Automation       | Bash (`monitor.sh`), Python (`prometheus_query.py`) |

---

## 📦 Microservice Description

A lightweight Flask web service that:
- Accepts user input via form (age, weight, height, gender)
- Calculates:
  - Maintenance Calories
  - Caloric Deficit (for weight loss)
  - Caloric Surplus (for weight gain)
- Exposes a `/metrics` endpoint using `prometheus_flask_exporter` for monitoring

---

## 🔁 CI/CD Pipeline

Implemented via GitHub Actions:
- On push to `main`:
  1. Docker image is built
  2. Pushed to Docker Hub
  3. Deployed to EKS via `kubectl apply`
  4. Rollout verified
  5. Prometheus queried to ensure metric ingestion

**Workflow File:** `.github/workflows/deploy.yml`


---

## 📈 Monitoring Stack

- **Prometheus** scrapes app metrics from `/metrics`
- **Grafana** visualizes:
  - HTTP request totals
  - Duration histograms
  - Exporter health
- Alerts (e.g., high CPU, pod down) are defined in `alert-rules.yml`

---

## ⚙️ Automation Scripts

| Script                | Description                                |
|------------------------|--------------------------------------------|
| `monitor.sh`          | Uses `kubectl top` to check pod resource usage |
| `prometheus_query.py` | Queries Prometheus for live metrics via REST API |

---

## ✅ Prerequisites

- AWS CLI configured
- IAM user with EKS access
- Docker Hub account
- EKS cluster provisioned (via `eksctl`)
- GitHub Secrets configured:
  - `DOCKER_USERNAME`, `DOCKER_PASSWORD`
  - `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_REGION`



## 📬 How to Use

1. Clone the repo  
2. Set up EKS using `eksctl`
3. Apply manifests:
   ```bash
   kubectl apply -f K8s-manifests/
4. Port-forward Prometheus and Grafana:
  ```bash
  kubectl port-forward svc/prometheus 9090 -n monitoring
  kubectl port-forward svc/grafana 3000 -n monitoring/
```
5. Access Flask app via LoadBalancer URL (kubectl get svc)

6. Use monitor.sh and prometheus_query.py for manual automation




