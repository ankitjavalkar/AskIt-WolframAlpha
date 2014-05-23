#!/usr/bin/env python

import argparse
import sys
import urllib2
import xml.etree.ElementTree as ET


def main():

    wolfram_API_ID= "" #Enter the Wolfram Alpha API Key here

    #Parse command-line to obtain the arguments and/or options
    askit_parser = argparse.ArgumentParser(prog="askitwa", 
                                            usage=" askitwa [--help] [--version] [--assumption] [query ...]")
    askit_parser.add_argument("query", 
                            type=str, 
                            nargs='+', 
                            help="enter the Query to be answered")
    askit_parser.add_argument("-a", 
                            "--assumption", 
                            action="store_true", 
                            help="display the assumptions made (if any) in case of ambiguity")
    askit_parser.add_argument("-v", 
                            "--version", 
                            action="version", 
                            version="AskIt-Wolfram Alpha version 0.1")
    args = askit_parser.parse_args()
    query = "+".join(args.query)
    if (args.assumption):
        assum = 1
    else:
        assum = 0
    
    askit_getans(query, assum, wolfram_API_ID)
    

def askit_getans(q, a, API_ID):
    
    req = urllib2.Request("http://api.wolframalpha.com/v2/query?" 
                            + "podindex=2&format=plaintext&appid=" + API_ID 
                            + "&input=" + q)

    try:
        #Obtain the xml response
        ret = urllib2.urlopen(req)
        retxml = ET.parse(ret)
        retxmlroot = retxml.getroot()

        #Parse the xml response obtained from api
        if (retxmlroot.get('success')):
            for plaintext in retxmlroot.iter('plaintext'):
                print ("\n" + plaintext.text + "\n")   
            if (a == 1):
                for spellcheck in retxmlroot.iter('spellcheck'):
                    print ("Assumptions: " + spellcheck.get('text') + "\n")
            sys.exit(1)
        else:
            print ("Sorry, I'm unable to answer that question")
            sys.exit(1)

    except urllib2.URLError:
        print "Error while fetching Request"
        sys.exit(1)


if __name__ == "__main__":

    main()
