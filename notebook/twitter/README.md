# Twitter Example

Here are the Tinybird Data Source schemas, Pipes and API endpoint to generate the data for the chart section of this [blog post](https://blog.tinybird.co/2022/03/21/analysis-twitter-streaming/).

## Datasources

You can find the schemas for these Data Sources:

- `Personal.tweets`: all the tweets in a Data Source shared from the `Personal` workspace.
- `tws_min_mv`: materialized data of counts of occurrences of words per minute
- `tws_ten_min_mv`: materialized data of counts of occurrences of words per ten minutes
- `tws_thirty_min_mv`: materialized data of counts of occurrences of words per thirty minutes

## Pipes

You can find the following pipes:

- `tws_per_min`: materializes data from Personal.tweets to `tws_min_mv`
- `tws_per_ten_min`: Mmterializes data from Personal.tweets to `tws_ten_min_mv`
- `tws_per_thirty_min`: materializes data from Personal.tweets to `tws_thirty_min_mv`

## Endpoints

An example pipe that shows how to generate data for the [Retool dashboard](https://tinybird.retool.com/embedded/public/79825df4-c882-4746-986d-c4513457fab4).

## How to load data

You can download these files and use them in your Tinybird account. 

Clone the repo and push the resources to your account. For example:

```sh
tb auth

tb push pipes/tws_per_min --push-deps
```
