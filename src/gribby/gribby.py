#!/bin/python3
# This script will create the url necessary to download .grb files from NOAA to
# use with chart plotters.
# This script is loosly based of the get_gfs.pl script found
# here: https://para.nomads.ncep.noaa.gov/txt_descriptions/fast_downloading_grib.shtml
from datetime import date, datetime, time
import argparse
from math import floor

#  Constants
BASE_URL="https://nomads.ncep.noaa.gov/pub/data/nccf/com/gfs/prod/"
#gfs.$YYYY$MM$DD/$HH/atmos/gfs.t${HH}z.pgrb2.0p25.f${FHR3}"

# Global Variables
# dateEntered : date

def ParseArguments():
    ArgParser = argparse.ArgumentParser(prog="gribby", description="Download grb files for chart plotters from NOAA.")
    ArgParser.add_argument('-s', '--startdate', type=str,
        help="Start date in YYYY-MM-DD format. If none is specified, it will use today's date.")
    ArgParser.add_argument('-H', '--hour', type=str, choices=['00', '06', '12', '18'],
        help="Start hour for forecast. If none specified, it will use the current 6h forecast window.")
    args = ArgParser.parse_args()

    # print(args.startdate,args.hour)

    # If the user entered a start date, parse it, otherwise the date to use will be today's date
    if args.startdate is not None:
        try:
            _date_entered = date.fromisoformat( args.startdate )
        except:
            print("Invalid ISO Date. Must be in YYYY-MM-DD format.\n")
            ArgParser.print_help()
            exit(1)
    else:
        _date_entered = date.today()

    # If the user entered start hour, parse it, otherwise use the current 6h forecast window
    if args.hour is not None:
        _hour_entered = args.hour
    else:
        _current_hour = datetime.now().time().hour
        # Amount of times the current hour is divisble by 6 so that we can use it to round down to 6h increments
        # A block of 0 refers to 00h-06h and a block of 1 = 06h-12h etc..
        _block = floor(_current_hour / 6)
        _hour_entered = str.format({0:0>2}, (_block*6))






    return _date_entered, _hour_entered


def GetDateString(inputDate: date):
    _date_str = inputDate.strftime("%Y%m%d")
    return _date_str

def main():
    _user_date, _user_hour = ParseArguments()
    print("Date: ", GetDateString(_user_date))
    print("Hour: ", _user_hour)

# if __name__ == "__main__":
#     main()
