## Materialized view with intermediate states 
Copy the credentials
```
cp ../.tinyb ./
```
and make sure are the correct ones 
```
tb workspace current
```

## Upload datasource
### __If you come from previous steps you can skip this step and the next one _"Run the continuous appends"_. You should already have the videos.datasource pushed and know how to continuously append data.__
Upload the videos.datasource to the workspace. Note it comes with a sample csv in the fixtures folder.
```
tb push datasources/videos.datasource --fixtures
```

## Run the continuous appends
It will append 1000 new rows every ~12 seconds. Feel free to modify, but note the [API Limits](https://docs.tinybird.co/api-reference/api-reference.html#limits-title).
```
cp ../data-generator/append1000.sh ./
chmod +x append1000.sh
. ./append1000.sh
```
### __Resume here if you skipped the last two steps__
## Upload the mv pipe with its dependencies
Pushing the MV pipe. Adding _--push-deps_ to upload mv_videos.datasource as well. The mv will be triggered with every new ingestion at origin _videos.datasource_. If you want it filled at creation time, add the _--populate_ option.
```
tb push pipes/mv_videos.pipe --push-deps
```
## Query the mv datasource
Push the endpoint
```
tb push endpoints/latest_status_videos.pipe
```
And double check token security in case you need it.