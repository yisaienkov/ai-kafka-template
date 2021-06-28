import time
import json
import logging

from kafka import KafkaConsumer

KAFKA_SERVER = "kafka"
KAFKA_PORT = 9092
TOPIC = "ai-topic"
GROUP = "ai-worker-01"

WORK_TIME = 10


logging.basicConfig(
    format="%(asctime)s ~~~ %(levelname)s ~~~ %(module)s ~~~ %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)


if __name__ == "__main__":
    while True:
        try:
            consumer = KafkaConsumer(
                TOPIC,
                bootstrap_servers=[f"{KAFKA_SERVER}:{KAFKA_PORT}"], 
                auto_offset_reset="earliest",
                enable_auto_commit=True,
                auto_commit_interval_ms=1,
                group_id=GROUP,
                value_deserializer=lambda x: json.loads(x.decode("utf-8"))
            )
            break
        except Exception as ex:
            logger.exception(ex)
            time.sleep(5)

    for message in consumer:
        data = message.value
        logger.info(f"Received: {data}")

        time.sleep(WORK_TIME)
        result = int(data["number_of_floors"]) * 20 + int(data["total_area"]) * 2

        logger.info(f"Done {data['id']}. Result: {result}")
