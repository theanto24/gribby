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

# Global Variables
# dateEntered : date

def ParseArguments():
    ArgParser = argparse.ArgumentParser(prog="gribby", description="Download grb files for chart plotters from NOAA.")
    ArgParser.add_argument('-s', '--startdate', type=str, help="Start date in YYYY-MM-DD format.")
    ArgParser.add_argument('-H', '--hour', type=str, choices=['00', '06', '12', '18'], help="Start hour for forecast.")
    args = ArgParser.parse_args()

    # print(args.startdate,args.hour)

    if args.startdate is not None:
        try:
            _date_entered = date.fromisoformat( args.startdate )
        except:
            print("Invalid ISO Date. Must be in YYYY-MM-DD format.\n")
            ArgParser.print_help()
            exit(1)
    else:
        _date_entered = date.today()

    return _date_entered


def GetDateString(inputDate: date):
    _date_str = inputDate.strftime("%Y%m%d")
    return _date_str

def main():
    _user_date = ParseArguments()
    print("Date: ", GetDateString(_user_date))


if __name__ == "__main__":
    main()
