#!/bin/python3
# This script will create the url necessary to download .grib files from NOAA to
# use with chart plotters.
# This script is loosly based of the get_gfs.pl script found on NOAA's website
import datetime

#  Constants
BASE_URL="https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/"
#gfs.$YYYY$MM$DD/$HH/atmos/gfs.t${HH}z.pgrb2.0p25.f${FHR3}"

def GetDateString(date: datetime.date):
    _date_str = date.strftime("%Y%m%d")
    return _date_str

def main():
    _date_today = datetime.date.today()
    print("Today's Date: ", GetDateString(_date_today))


if __name__ == "__main__":
    main()
