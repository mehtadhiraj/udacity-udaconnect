### Steps
1. `kubectl apply -f deployment/db-configmap.yaml` - Set up environment variables for the pods
2. `kubectl apply -f deployment/db-secret.yaml` - Set up secrets for the pods
3. `kubectl apply -f deployment/postgres.yaml` - Set up a Postgres database running PostGIS
4. `kubectl apply -f deployment/udaconnect-api.yaml` - Set up the service and deployment for the API
5. `sh scripts/run_db_command.sh <POD_NAME>` - Seed your database against the `postgres` pod. (`kubectl get pods` will give you the `POD_NAME`)

### Verifying it Works
Once the project is up and running, you should be able to see 2 deployments and 2 services in Kubernetes:
`kubectl get pods` and `kubectl get services` - should both return `udaconnect-connections` and `connections-postgres`

These pages should also load on your web browser:
* `http://localhost:30000/` - OpenAPI Documentation
