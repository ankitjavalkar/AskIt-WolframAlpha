#!/usr/bin/env python

import argparse
import sys
import urllib2
import xml.etree.ElementTree as ET


def main():

    wolfram_API_ID=12345 #Enter the Wolfram Alpha API Key here

    askit_parser = argparse.ArgumentParser(prog="askitwa", 
                                            usage=" askitwa [--help] [--version] [query ...]")
    askit_parser.add_argument("query", 
                            type=str, 
                            nargs='+', 
                            help="Enter the Query to be answered")
    askit_parser.add_argument("-v", 
                            "--version", 
                            action="version", 
                            version="AskIt-Wolfram Alpha version 0.1")
    args = askit_parser.parse_args()
    query = " ".join(args.query)
    
    askit_getans(query, wolfram_API_ID)
    

def askit_getans(q, API_ID):
    
    req = urllib2.Request("http://api.wolframalpha.com/v2/query?" 
                            + "podindex=2&format=plaintext&appid=" + API_ID 
                            + "&input=" + q)

    try:
        ret = urllib2.urlopen(req)
    except urllib2.URLError:
        print "Error while fetching Request"
        sys.exit(1)

    print ret


if __name__ == "__main__":

    main()
