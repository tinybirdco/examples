#!/bin/bash
while :
do
    data=$(python3 ../data-generator/gen.py --rows 1000)
    tb datasource append videos $data   
    #!current api limits are 5 appends per minute
    rm $data
    sleep 12
done