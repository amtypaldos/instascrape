#!/usr/bin/python

import sys, getopt


def scrape(username,password,hashtag):
   print(username,password,hashtag)


def main(argv):
   username = ''
   pw = ''
   hashtag = ''
   try:
      opts, args = getopt.getopt(argv,"u:p:t:",["username=","pw=","hashtag="])
   except getopt.GetoptError:
      print('scrape.py -u <username> -p <password> -t <hastag>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h' or opt == '--help':
         print('scrape.py -u <username> -p <password> -t <hastag>')
         sys.exit()
      elif opt in ("-u", "--username"):
         username = arg
      elif opt in ("-p", "--password"):
         pw = arg
      elif opt in ("-t", '--hashtag'):
         hashtag = arg

   scrape(username,pw,hashtag)

if __name__ == "__main__":
   main(sys.argv[1:])
