#!/bin/bash

# Get current Git commit hash
VERSION=$(git rev-parse --short=7 HEAD)

# Replace version placeholder in deployment.yaml
sed -i "s/{{VERSION}}/${VERSION}/g" /home/teezer/Desktop/Devops_Projects/Full_stack_app/DeploymentAppBackDev.yaml

# Apply deployment to Minikube
kubectl apply -f /home/teezer/Desktop/Devops_Projects/Full_stack_app/DeploymentAppBackDev.yaml

# Get back the old tag because when next time the command is runned the tag will be replaced so we have to write {{VERSION}} back
sed -i "s/${VERSION}/{{VERSION}}/g" /home/teezer/Desktop/Devops_Projects/Full_stack_app/DeploymentAppBackDev.yaml
