# Merge State Example

This project shows how, and when, to use `-mergeState` Clickhouse function.

## Datasources

You can find the following datasources:

- `ds_readings`: It stores the events coming from IoT devices about rooms' temperature. 
- `ds_hourly_temp`: It stores hourly aggregated data about rooms' temperature.
- `ds_pos_temp`: It stores day aggregated data for areas (`in` room, `out` room).

## Pipes

You can find the following pipes:

- `mv_hourly_temp`: Materializes data from `ds_readings` to `ds_hourly_temp`.
- `mv_pos_temp`: Materializes data from `ds_hourly_temp` to `ds_pos_temp`. This materialization is very basic. You can do it right from `ds_readings`. However, with more complex use cases you might need to join different tables or make more complex aggregations.

## How to load data

You can download these files and use them in your Tinybird account. 

Clone the repo and push the resources to your account:

```sh
tb auth

tb push pipes/mv_hourly_temp --push-deps
tb push pipes/mv_pos_temp --push-deps
```

For loading data, you can download the dataset from this [link](https://storage.googleapis.com/tinybird-demo/iot-temp.zip) and extract the CSV file.

```sh
tb datasource append ds_readings IOT-temp.csv
```
