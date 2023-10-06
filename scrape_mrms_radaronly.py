import urllib.request
from urllib.request import HTTPError
from datetime import datetime
from datetime import timedelta
import os

start = datetime(2023, 4, 30, 0, 0)
end = datetime(2023, 10, 2, 0, 0)
hour = timedelta(hours=1)
#minute = timedelta(minutes=2)

missing_dates = []
fallback_to_radaronly = False #Enables a post-processing step that will go through the list of missing dates for gage-corrected
############################# and tries to go get the radar-only values if they exist.

destination = "/Volumes/WCNR-Network/Research/Kampf/Private/SearsM/MRMS_2023_radaronly"

date = start

while date <= end:
    url = "http://mtarchive.geol.iastate.edu/{:04d}/{:02d}/{:02d}/mrms/ncep/RadarOnly_QPE_01H/RadarOnly_QPE_01H_00.00_{:04d}{:02d}{:02d}-{:02d}0000.grib2.gz".format(
        date.year, date.month, date.day, date.year, date.month, date.day, date.hour, date.minute)
    filename = url.split("/")[-1]
    try:
        fetched_request = urllib.request.urlopen(url)
    except HTTPError as e:
        missing_dates.append(date)
    else:
        with open(destination + os.sep + filename, 'wb') as f:
            f.write(fetched_request.read())
    finally:
        date += minute

if fallback_to_radaronly:
    radar_also_missing = []
    for date in missing_dates:
        url = "http://mtarchive.geol.iastate.edu/{:04d}/{:02d}/{:02d}/mrms/ncep/RadarOnly_QPE_01H/RadarOnly_QPE_01H_00.00_{:04d}{:02d}{:02d}-{:02d}0000.grib2.gz".format(
            date.year, date.month, date.day, date.year, date.month, date.day, date.hour)
        filename = url.split("/")[-1]
        try:
            fetched_request = urllib.request.urlopen(url)
        except HTTPError as e:
            radar_also_missing.append(date)
        else:
            with open(destination + os.sep + filename, 'wb') as f:
                f.write(fetched_request.read())