# Deduplication Strategies repo
This repository can be used as a complement to [this guide](https://guides.tinybird.co/guide/deduplication-strategies).

Clone the examples repository to your local environment

`git clone git@github.com:tinybirdco/examples.git`

and move to the deduplication-strategies folder

`cd deduplication-strategies`

## CLI virtual environment
If you don't have a [tinybird CLI](https://docs.tinybird.co/cli.html) installed yet, run the following commands:
```
virtualenv -p python3 .e
. .e/bin/activate
pip install tinybird-cli
tb auth
```
Go to your workspace, copy an admin token and paste it. A new __.tinyb__ file will be generated.
You can check the token was the right one by running `tb workspace current`

## Folders

- __data-generator__: scripts to generate mock data files.
- __1_query-time__: data project for the first and easiest use case. Deduplication at query time
- __2_materialized-views__: data project for deduplication using MVs
- __3.1_snapshots-append-endpoint__: data project for deduplication using endpoints + appends to snapshot table
- __3.2_snapshots-mv-populate__: data project for deduplication using ephemeral MVs + populates
