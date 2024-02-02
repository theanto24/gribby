#!/bin/python3
# This script will create the url necessary to download .grb files from NOAA to
# use with chart plotters.
# This script is loosly based of the get_gfs.pl script found
# here: https://para.nomads.ncep.noaa.gov/txt_descriptions/fast_downloading_grib.shtml
from datetime import date
import argparse

#  Constants
BASE_URL="https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/"
#gfs.$YYYY$MM$DD/$HH/atmos/gfs.t${HH}z.pgrb2.0p25.f${FHR3}"

def ParseArguments():
    ArgParser = argparse.ArgumentParser(prog="gribby", description="Download grb files for chart plottes from NOAA.")
    ArgParser.add_argument('-s', '--startdate', type=str, help="Start date in YYYY-MM-DD format.")
    ArgParser.add_argument('-H', '--hour', type=str, choices=['00', '06', '12', '18'], help="Start hour for forecast.")
    ArgParser.parse_args()

def GetDateString(inputDate: date):
    _date_str = inputDate.strftime("%Y%m%d")
    return _date_str

def main():
    ParseArguments()
    _date_today = date.today()
    print("Today's Date: ", GetDateString(_date_today))


if __name__ == "__main__":
    main()
