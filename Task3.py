import argparse
import sys

import parser

def check_ports(val):
    try:
        value=int(val)
    except ValueError:
        raise argeparse.ArguTypeError('Integer please')
    if(value<=0):
        print('not valid port')
        sys.exit()
    return value
parser.ArgumentParsser()
    