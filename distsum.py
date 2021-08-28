import subprocess
import json
from datetime import datetime, timedelta

# cp /Volumes/ROW/Concept2/Logbook/* ~/Logbook
# diskutil unmountDisk disk2

process = subprocess.Popen(["/Users/fallalex/go/src/pm5conv/cmd/pm5conv", "/Users/fallalex/Logbook"],
                        stdin =subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE)
pout, perr = process.communicate()

row_data = json.loads(pout)

distances = [(datetime.strptime('-'.join(x['Date'].split('-')[:-1]),'%Y-%m-%dT%H:%M:%S'),x['TotalDistance']) for x in row_data]

dist_over_month = 0
dist_over_week = 0
dist_this_month = 0
dist_this_week = 0
dist_total = 0

now = datetime.now()
for wdate, wdist in distances:
    dist_total += wdist
    if wdate > (now - timedelta(days=28)):
        dist_over_month += wdist
        if wdate > (now - timedelta(days=7)):
            print(wdate.date().isoformat(), wdist)
            dist_over_week += wdist
    if wdate.year == now.year and wdate.month == now.month:
        dist_this_month += wdist
        if wdate.isocalendar()[1] == now.isocalendar()[1]:
            dist_this_week += wdist


# TODO: goals
# TODO: days left for cal week and month
# TODO: calculate how many meters are needed each day to hit goals
# TODO: track current year

print()
print("Week", now.isocalendar()[1])
print(dist_this_week)
print()

print("Month", now.month)
print(dist_this_month)
print()

print("Last 7 days")
print(dist_over_week)
print()

print("Last 28 days")
print(dist_over_month)
print()

print("Total")
print(dist_total)
print()

