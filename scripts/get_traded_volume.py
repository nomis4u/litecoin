#!/usr/bin/python3
import sys
from optparse import OptionParser

# Ignore volume if the output has some special characters or empty
ignore_volume = ["-", " ", ":", "/"]


#Get traded volume of each crypto and display in millions(M)
def get_coin_volume(datafile, check_year):
    with open(datafile, 'r') as outfile:
        lines = outfile.readlines()
        for line in lines:
            result = [x.strip() for x in line.split(',')]
            coin = result[0]
            year = result[1].split("-")[2]
            volume = result[6]
            if year == check_year:
                if volume not in ignore_volume:
                    if coin not in volume_dict:
                        volume_dict[coin] = int(result[6])
                    else:
                        current_sum = volume_dict[coin]
                        new_sum = int(current_sum) + int(result[6])
                        volume_dict[coin] = int(new_sum)

    for key in volume_dict:
        volume_in_millions = volume_dict[key] / 1000000
        print("%s : %s%s" % (key, volume_in_millions, "M"))


if __name__ == "__main__":
    parser = OptionParser()
    usage = "usage: %prog [options] arg1 arg2"

    parser.add_option("-f", "--filepath", type="string",
                      dest="filepath",
                      help="path to the csv file")

    parser.add_option("-y", "--year", type="string",
                      help="year for which we need to check volume",
                      dest="year", default="2018")

    (options, args) = parser.parse_args()

    if not options.filepath:
        print("File path is missing. Check help")
        sys.exit(1)

    uniq_coin = []
    volume_dict = {}
    print("Coin   Volume")
    print("----    ------")

    datafile = options.filepath
    check_year = options.year
    get_coin_volume(datafile, check_year)
