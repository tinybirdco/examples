import datetime
import csv
import random
import click
import sys

ROWS = 500_000
TOTAL_VIDEOS = 1_000_000
BASE_DATE = datetime.datetime.strptime('2021-12-01','%Y-%m-%d')

headers = ['id','views','likes','dislikes','timestamp']
now = datetime.datetime.now()
delta = (now - BASE_DATE).seconds/60 #used for having incremental values
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

FILE_NAME = f'data_{ROWS}_{now.strftime("%Y-%m-%d_%H:%M:%S")}.csv'


@click.command()
@click.option('--rows', default=ROWS, help=f'number of generated rows. Defaults to {ROWS}')
@click.option('--total-videos', default=TOTAL_VIDEOS, help=f'total number of videos. Defaults to {TOTAL_VIDEOS}')
@click.option('--file-name', default='', help= 'name of the output csv file. Defaults to "rows_ROWS_over_TOTAL_VIDEOS_datetime"')
def generate_csv(rows, total_videos, file_name):
  if total_videos < rows:
    total_videos = rows
    video_sample = range(rows)
  else:
    video_sample = random.sample(range(total_videos),min(rows,total_videos))

  if not file_name:
    file_name = f'rows_{rows}_over_{total_videos}_{now.strftime("%Y-%m-%d_%H:%M:%S")}.csv'

  with open (file_name,'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for r in video_sample:
      id = 1+r
      views = int(delta + 1000*random.lognormvariate(5,1))
      likes = int(delta/10 + 10*random.lognormvariate(5,1))
      dislikes = int(delta/100 + random.lognormvariate(5,1)) 
      writer.writerow([id, views, likes, dislikes, timestamp])
  print(file_name)
 
if __name__ == '__main__':
  generate_csv()
