import argparse

parser = argparse.ArgumentParser(
    prog='SpiderScan'
    ,description="Program for complete scan website.")
parser.add_argument('-u',"--url",type=str, nargs="?", action='store',help="Url for scan.") #   URL      |   argument     |   store
parser.add_argument('-w',"--wordlist",type=str, nargs="?", action='store',help="Wordlist for used scan.") #   URL      |   argument     |   store
parser.add_argument('-c',"--cookies",type=str, nargs="?", action='store',help="Cookies for used scan.") #   URL      |   argument     |   store
parser.add_argument('-h',"--headers",type=str, nargs="?", action='store',help="Headers for used scan.") #   URL      |   argument     |   store
parser.add_argument('-v','--verbose',action='store_true',help='Used for verbose scan.')    #   VERBOSE  |   argument     |   store_true

args = parser.parse_args()

print(args.verbose)