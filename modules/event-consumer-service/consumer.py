from kafka import KafkaConsumer
import os
import json
import logging

logging.basicConfig(filename='logs/consumer.txt', level=logging.INFO)

KAFKA_URL = os.environ["KAFKA_URL"]
KAFKA_TOPIC = os.environ["KAFKA_TOPIC"]
DB_USERNAME = os.environ["DB_USERNAME"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_HOST = os.environ["DB_HOST"]
DB_PORT = os.environ["DB_PORT"]
DB_NAME = os.environ["DB_NAME"]


consumer = KafkaConsumer(KAFKA_TOPIC, bootstrap_servers=[KAFKA_URL])

print("Connected !!!")
logging.info("Start consuming kafka event...")

def save(location):
    from sqlalchemy import create_engine
    try:
        logging.info("Storing in db. Connecting...")
        engine = create_engine(f"postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}", echo=True)
        conn = engine.connect()
        logging.info("Connection established!!!")
        personId = int(location["person_id"])
        latitude, longitude = int(location["latitude"]), int(location["longitude"])
        insert = "INSERT INTO location (person_id, coordinate) VALUES ({}, ST_Point({}, {}))" .format(personId, latitude, longitude)
        logging.info(insert)
        conn.execute(insert)
        logging.info("Insertion successfull!!!")
    except:
        logging.exception("Exception occurred!!!")

for event in consumer:
    logging.info("Event received")
    location = event.value.decode("utf-8")
    locationJson = json.loads(location)
    logging.info("Event data is : ")
    logging.info(locationJson)
    save(locationJson)

