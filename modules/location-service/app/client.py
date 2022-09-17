import grpc

import locations_pb2
import locations_pb2_grpc


print("Coordinates sending...")

channel = grpc.insecure_channel("127.0.0.1:30003")
stub = locations_pb2_grpc.LocationServiceStub(channel)

location1 = locations_pb2.LocationMessage(
    person_id=7,
    longitude=10,
    latitude=-40
)

locarion2 = locations_pb2.LocationMessage(
    person_id=8,
    longitude=-30,
    latitude=15
)

response1 = stub.Create(location1)
response2 = stub.Create(locarion2)

print(response1)
print(response2)