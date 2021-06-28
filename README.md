# AI Kafka Template


### Run Kafka
```bash
docker-compose --file kafka-docker-compose.yml up --build
```


### Debug
```bash
docker build -t kafka-producer:latest -f Dockerfile_producer . 
docker run --name kafka-producer --net ai-kafka-template_default kafka-producer

docker build -t kafka-consumer:latest -f Dockerfile_consumer . 
docker run --name kafka-consumer --net ai-kafka-template_default kafka-consumer
```