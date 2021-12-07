## Deduplication at query time 
Copy the credentials: `cp ../.tinyb ./` and make sure are the correct ones `tb workspace current`.

## Upload datasource
Upload the videos.datasource to the workspace. Note it comes with a sample csv in the fixtures folder.

`tb push datasources/videos.datasource --fixtures`

## Upload endpoints with the three differen strategies
Pushing pipes with Subquery, argMax, and LIMIT BY

`tb push endpoints/*.pipe `