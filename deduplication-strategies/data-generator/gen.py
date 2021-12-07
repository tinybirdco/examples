import datetime
import csv
import random

ROWS = 500_000
TOTAL_VIDEOS = 1_000_000
BASE_DATE = datetime.datetime.strptime('2021-12-01','%Y-%m-%d')

headers = ['id','views','likes','dislikes','timestamp']
now = datetime.datetime.now()
delta = (now - BASE_DATE).seconds/60 #used for having incremental values
timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

FILE_NAME = f'data_{ROWS}_{now.strftime("%Y-%m-%d_%H:%M:%S")}.csv'

# print(datetime.datetime.now())

def generate_csv():
  with open (FILE_NAME,'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(headers)
    for r in random.sample(range(TOTAL_VIDEOS),min(ROWS,TOTAL_VIDEOS)):
      id = 1+r
      views = int(delta + 1000*random.lognormvariate(5,1))
      likes = int(delta/10 + 10*random.lognormvariate(5,1))
      dislikes = int(delta/100 + random.lognormvariate(5,1)) 
      writer.writerow([id, views, likes, dislikes, timestamp])
  print (FILE_NAME,' generated')
  # print(datetime.datetime.now())

if __name__ == '__main__':
  generate_csv()