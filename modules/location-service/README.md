### Steps
1. `kubectl apply -f deployment/configmap.yaml` - Set up environment variables for the pods
2. `kubectl apply -f deployment/udaconnect-api.yaml` - Set up the service and deployment for the API

### Verifying it Works
Once the project is up and running, you should be able to see 1 deployments and 1 services in Kubernetes:
`kubectl get pods` and `kubectl get services` - should both return `udaconnect-locations`

### To send the request the gRPC server running on http://127.0.0.1:30003
* Run the client using command 
- 1. cd into location-service 
- 2. Run command `python ./app/client.py`

This will send the locations details to gRPC server. Which futher publish it on Kafka. 
