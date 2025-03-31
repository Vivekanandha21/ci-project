#!/bin/bash
set -e

# Pull the Docker image from Docker Hub
docker pull vivekanandha/cicd-python-app-deploy-project

# Run the Docker image as a container
docker run -d -p 5000:5000 vivekanandha/cicd-python-app-deploy-project

