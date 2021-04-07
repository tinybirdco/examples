# Kafka Demo
## Push the data project with the CLI

```
tb auth
tb push
```

# Producing and ingesting the events into Tinybird.

## start Zookeeper

`brew services start zookeeper`

## start Kafka

```
cd ~/Code/servers/kafka_2.12-2.5.0
./bin/kafka-server-start.sh config/server.properties
```

## start the producer

In this case it produces a record every ms to generate around 1000 records per second. Adjust at will. You can [download the .ndjson event file](https://storage.googleapis.com/tinybird-assets/datasets/guides/events_40M.ndjson)

```
cd tbakafka
. .venv38/bin/activate
python examples/producer.py ../csvtojson/events_40M.ndjson new_events --sleep 0.001
```

## start the agent

In a different tab (make sure theinifile.ini is in the tbakafka directory) and make sure it holds these configs:

```
tb_datasource = events_topic
tb_token = <token>
tb_endpoint = https://api.tinybird.co
tb_max_wait_seconds = 5
tb_max_wait_records = 5000
```
Then:

```
cd tbakafka
. .venv38/bin/activate
tbakafka --config theinifile.ini -vvv
```
