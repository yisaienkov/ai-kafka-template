import time
import json
import random
import logging

from kafka import KafkaProducer
from kafka.errors import KafkaError


KAFKA_SERVER = "kafka"
KAFKA_PORT = 9092
TOPIC = "ai-topic"

PAUSE_TIME = 15


logging.basicConfig(
    format="%(asctime)s ~~~ %(levelname)s ~~~ %(module)s ~~~ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    while True:
        try:
            producer = KafkaProducer(
                bootstrap_servers=[f"{KAFKA_SERVER}:{KAFKA_PORT}"], 
                value_serializer=lambda x: json.dumps(x).encode("utf-8")
            )
            break
        except Exception as ex:
            logger.exception(ex)
            time.sleep(5)

    for i in range(1000):
        data = {
            "id": str(i).zfill(5),
            "number_of_floors" : random.randint(1, 5), 
            "total_area": random.randint(0, 100),
        }
        
        future = producer.send(TOPIC, value=data)

        try:
            record_metadata = future.get(timeout=10)
            logging.info(data)
        except KafkaError as ex:
            logging.exception(ex)

        time.sleep(PAUSE_TIME)