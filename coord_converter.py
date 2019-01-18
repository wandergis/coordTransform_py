#!/usr/bin/python

import csv
import sys
import getopt
from coordTransform_utils import gcj02_to_bd09
from coordTransform_utils import bd09_to_gcj02
from coordTransform_utils import wgs84_to_gcj02
from coordTransform_utils import gcj02_to_wgs84
from coordTransform_utils import bd09_to_wgs84
from coordTransform_utils import wgs84_to_bd09

# Configuation
# Input file name
INPUT = ''
# Output file name
OUTPUT = ''
# Convert type: g2b, b2g, w2g, g2w, b2w, w2b
TYPE = ''

def convert():
    with open(INPUT, 'r') as input_file:
        input_file_reader = csv.reader(input_file)
        results = []
        for lat, lng in input_file_reader:
            result = convert_by_type(float(lng), float(lat), TYPE)
            results.append(result)

    with open(OUTPUT, 'w') as output_file:
        output_file_writer = csv.writer(output_file)
        for result in results:
            output_file_writer.writerow(result)

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
        print('Usage: The <type> must be in one of g2b, b2g, w2g, g2w, b2w, w2b')
        sys.exit()

def usage():
    print('Usage: coord_converter.py -i <input> -o <output> -t <type>')
    print('')
    print('where <type> is one of:')
    print('    g2b, b2g, w2g, g2w, b2w, w2b')
    print('')
    print('Example: coord_converter.py -i /path/to/input_file.csv -o /path/to/output_file.csv -t b2g')

if __name__ == "__main__":
    argv = sys.argv[1:]
    try:
        opts, args = getopt.getopt(argv, "hi:o:t:", ["input=", "output=", "type="])
    except getopt.GetoptError:
        usage()
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ("-i", "--input"):
            INPUT = arg
        elif opt in ("-o", "--output"):
            OUTPUT = arg
        elif opt in ("-t", "--type"):
            TYPE = arg

    if not (INPUT and OUTPUT and TYPE):
        usage()
        sys.exit()

    convert()
