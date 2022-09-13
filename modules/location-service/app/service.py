import json
import os;
from kafka import KafkaProducer;
import locations_pb2;
import locations_pb2_grpc;
import grpc
from concurrent import futures

KAFKA_URL = os.environ['KAFKA_URL']
KAFKA_TOPIC = os.environ['KAFKA_TOPIC']

producer = KafkaProducer(bootstrap_servers=KAFKA_URL)

class LocationsService(locations_pb2_grpc.LocationServiceServicer):
    def Create(self, req, context):
        location = {
            "person_id": int(req.person_id),
            "longitude": int(req.longitude),
            "latitude": int(req.latitude)
        }

        encodeData = json.dumps(location, indent=4).encode("utf-8")
        producer.send(KAFKA_TOPIC, encodeData)
        return locations_pb2.LocationMessage(**location)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
locations_pb2_grpc.add_LocationServiceServicer_to_server(LocationsService(), server)

server.add_insecure_port('[::]:5005')
server.start()
server.wait_for_termination()