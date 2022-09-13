### Steps
1. `kubectl apply -f deployment/udaconnect-app.yaml` - Set up the service and deployment for the web app

### Verifying it Works
Once the project is up and running, you should be able to see 1 deployments and 1 services in Kubernetes:
`kubectl get pods` and `kubectl get services` - should both return `udaconnect-app`

These pages should also load on your web browser:
* `http://localhost:30002/` - OpenAPI Documentation
