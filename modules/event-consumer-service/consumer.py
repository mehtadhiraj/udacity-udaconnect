from kafka import KafkaConsumer
import os
import json
import logging

logging.basicConfig(filename='logs/consumer.txt', level=logging.INFO)

KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]


consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_URL])

print("Connected !!!")
logging.info("Start consuming kafka event...")

for event in consumer:
    logging.info("Event received")
    location = event.value.decode("utf-8")
    locationJson = json.loads(location)
    logging.info("Event data is : ")
    logging.info(locationJson)

