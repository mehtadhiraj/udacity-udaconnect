### Steps
1. `kubectl apply -f deployment/udaconnect-script.yaml` - Set up the service and deployment for the API

### Verifying it Works
Once the project is up and running, you should be able to see 1 deployments and 1 services in Kubernetes:
`kubectl get pods` and `kubectl get services` - should both return `udaconnect-consumer`
* Execute commands
1. `kubectl exec -it < udaconnect consumer pod name > -- sh`
2. `cd logs`
3. `tail -F consumer.txt` - to check the logs
4. Now in another console execute client.py from location-service module `python app/client.py`
5. Now check back the console where consumer.txt file logs are open. You should see latest events pushed via client.py file. 

### Further improvements
1. We can do a http call to other service like connections-service which will store the location details in the database. We need to expose a post API for the same on connections service. 
2. Or else we can connect to same connections-postgress db from this application and store the data direclty in the db instead of doing the API call. 

Choosing the first option is fruitfull as connections service responsibility is to manage connections data. Hence any kind of validations and other logical operations can be done on connections service which make consumer and connections both independently scalable.