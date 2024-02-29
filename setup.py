import argparse
import asyncio
from route import send_request

parser = argparse.ArgumentParser(
    prog='SpiderScan'
    ,description="Program for complete scan website.")
parser.add_argument('-u',"--url",type=str, nargs="?", action='store',help="Url for scan.") #   URL      |   argument     |   store
parser.add_argument('-w',"--wordlist",type=str, nargs="?", action='store',help="Wordlist for used scan.") #   URL      |   argument     |   store
parser.add_argument('-c',"--cookies",type=str, nargs="?", action='store',help="Cookies for used scan.") #   URL      |   argument     |   store
parser.add_argument('-H',"--headers",type=str, nargs="?", action='store',help="Headers for used scan.") #   URL      |   argument     |   store
parser.add_argument('-v','--verbose',action='store_true',help='Used for verbose scan.')    #   VERBOSE  |   argument     |   store_true

args = parser.parse_args()


async def main():
    count = 0
    arguments = [args.url,args.wordlist]
    for c in arguments:
        for y in arguments:
            if len(c) >= len(y) :
                count += 1
        if count == len(arguments):
            maior = c
    print(maior)
    print(len(args.url))
    print(f"""
  +_______________________________________ +     
  |                                       |                 
  |                                       |         
  |              \033[033mSpider Scan\033[m              | 
  |              DEVELOPMENT              | 
  |                                       |
  |         By: Matheus Magalhães         |             
  |                                       |
  |_______________________________________|
  +                                       +

 _______________{'_'*len(maior)}____             
|               {' '*len(maior)}    |
|   URL       : {args.url}{' '*(len(maior)-len(args.url))}    |
|   VERBOSE   : {args.verbose}{' '*(len(maior)-5)}    |
|   WORDLIST  : {args.wordlist}{' '*(len(maior)-len(args.wordlist))}    |
|_______________{'_'*len(maior)}____|

""")
    urls = [linha.strip() for linha in open(args.wordlist)] 
    tasks = [send_request(f"{args.url}/{url}") for url in urls]
    for task in tasks:
        resultado = await task
        print(f"[x]> {urls[tasks.index(task)]} | {resultado.status}")

asyncio.run(main())
print(args.verbose)