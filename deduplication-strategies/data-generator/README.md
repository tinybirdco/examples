## Data Generator for Deduplication Strategies
The script generates a CSV file with 5 columns: _'id','views','likes','dislikes','timestamp'_

### Install
```
pip install click
```

### Run script
```
python3 gen.py --rows 50_000 --total-videos 1_000_000
```

this generates a csv file with 50k rows with ids from 1 to 1.000.000.

### Parameters
the folowing parameters can be specified, although none of them is required.
- __rows__ : number of generated rows
- __total-videos__: total number of videos
- __file-name__: name of the output csv file

### Help
```
python3 gen.py --help
```

### Append script
the script needs to be run from a data-project folder with the tb CLI activated and the correct credentials —the _.tinyb_ file—.
By default it appends 1000 rows, but feel free to edit but note the [API Limits](https://docs.tinybird.co/api-reference/api-reference.html#limits-title).