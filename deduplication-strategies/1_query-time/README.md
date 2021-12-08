## Deduplication at query time 
Copy the credentials
```
cp ../.tinyb ./
```
and make sure are the correct ones 
```
tb workspace current
```

## Upload datasource
Upload the videos.datasource to the workspace. Note it comes with a sample csv in the fixtures folder.
```
tb push datasources/videos.datasource --fixtures
```

## Upload endpoints with the three different strategies
Pushing pipes with Subquery, argMax, and LIMIT BY

```
tb push endpoints/*.pipe
```

## Run the continuous appends
It will append 1000 new rows every ~12 seconds. Feel free to modify, but note the [API Limits](https://docs.tinybird.co/api-reference/api-reference.html#limits-title).
```
cp ../data-generator/append1000.sh ./
chmod +x append1000.sh
. ./append1000.sh
```