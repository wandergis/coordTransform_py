#!/usr/bin/python
# -*- coding: utf-8 -*-

import csv
import sys
import argparse
from coordTransform_utils import gcj02_to_bd09
from coordTransform_utils import bd09_to_gcj02
from coordTransform_utils import wgs84_to_gcj02
from coordTransform_utils import gcj02_to_wgs84
from coordTransform_utils import bd09_to_wgs84
from coordTransform_utils import wgs84_to_bd09

# Configuration
# Input file name
INPUT = ''
# Output file name
OUTPUT = ''
# Convert type: g2b, b2g, w2g, g2w, b2w, w2b
TYPE = ''
# lng column name
LNG_COLUMN = ''
# lat column name
LAT_COLUMN = ''
# Skip invalid row
SKIP_INVALID_ROW = False

def convert():
    with open(INPUT, 'r') as input_file:
        input_file_reader = csv.reader(input_file)
        headers = next(input_file_reader)
        lng_index, lat_index = get_lng_lat_index(headers)
        results = []

        for index, row in enumerate(input_file_reader):
            result = []
            try:
                result = convert_by_type(float(row[lng_index]), float(row[lat_index]), TYPE)
            except ValueError:
                # Deal with ValueError(invalid lng or lat)
                # print(index + 2, row[lng_index], row[lat_index]) # '+ 2' is due to zero-based index and first row is header
                result = row[lng_index], row[lat_index]
            results.append(result)

    with open(OUTPUT, 'w') as output_file:
        output_file_writer = csv.writer(output_file, lineterminator='\n')

        with open(INPUT, 'r') as input_file:
            input_file_reader = csv.reader(input_file)
            headers = next(input_file_reader)
            lng_index, lat_index = get_lng_lat_index(headers)

            output_file_writer.writerow(headers)
            for index, row in enumerate(input_file_reader):
                row[lng_index] = results[index][0]
                row[lat_index] = results[index][1]
                if type(row[lng_index]) is not float or type(row[lat_index]) is not float:
                    # Data is invalid
                    if SKIP_INVALID_ROW:
                        # Skip invalid row
                        pass
                    else:
                        # Reserve invalid row
                        output_file_writer.writerow(row)
                else:
                    # Data is valid
                    output_file_writer.writerow(row)

def get_lng_lat_index(headers):
    try:
        if LNG_COLUMN == '' and LAT_COLUMN == '':
            return [headers.index('lng'), headers.index('lat')]
        else:
            return [headers.index(LNG_COLUMN), headers.index(LAT_COLUMN)]
    except ValueError as error:
        print('Error: ' + str(error).split('is', 1)[0] + 'is missing from csv header. Or use -n or -a to specify custom column name for lng or lat.')
        sys.exit()

def convert_by_type(lng, lat, type):
    if type == 'g2b':
        return gcj02_to_bd09(lng, lat)
    elif type == 'b2g':
        return bd09_to_gcj02(lng, lat)
    elif type == 'w2g':
        return wgs84_to_gcj02(lng, lat)
    elif type == 'g2w':
        return gcj02_to_wgs84(lng, lat)
    elif type == 'b2w':
        return bd09_to_wgs84(lng, lat)
    elif type == 'w2b':
        return wgs84_to_bd09(lng, lat)
    else:
        print('Usage: type must be in one of g2b, b2g, w2g, g2w, b2w, w2b')
        sys.exit()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert coordinates in csv files.', usage='%(prog)s [-h] -i INPUT -o OUTPUT -t TYPE [-n LNG_COLUMN] [-a LAT_COLUMN] [-s SKIP_INVALID_ROW]', formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    group = parser.add_argument_group('arguments')

    group.add_argument('-i', '--input', help='Location of input file', default=argparse.SUPPRESS, metavar='')
    group.add_argument('-o', '--output', help='Location of output file', default=argparse.SUPPRESS, metavar='')
    group.add_argument('-t', '--type', help='Convert type, must be one of: g2b, b2g, w2g, g2w, b2w, w2b', default=argparse.SUPPRESS, metavar='')
    group.add_argument('-n', '--lng_column', help='Column name for longitude', default='lng', metavar='')
    group.add_argument('-a', '--lat_column', help='Column name for latitude', default='lat', metavar='')
    group.add_argument('-s', '--skip_invalid_row', help='Whether to skip invalid row', default=False, type=bool, metavar='')

    args = parser.parse_args()
    # print('\nArguments you provide are:')
    # for arg in vars(args):
    #     print '{0:20} {1}'.format(arg, str(getattr(args, arg)))

    # Get arguments
    if not args.input or not args.output or not args.type:
        parser.print_help()
    else:
        INPUT = args.input
        OUTPUT = args.output
        TYPE = args.type

    if args.lng_column and args.lat_column:
        LNG_COLUMN, LAT_COLUMN = args.lng_column, args.lat_column

    if args.skip_invalid_row:
        SKIP_INVALID_ROW = args.skip_invalid_row

    convert()
