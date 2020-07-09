#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sif Baksh"
__version__ = "1.0.0"
__website__ = "sifbaksh.com"
__twitter__ = "@sifbaksh"

import csv
import os
from itertools import islice

# Make sure to use the absolut path to where the exports are located
directory = '/Users/sbaksh/Dropbox/CCS_Perl_Scripts/DDI/ipam_solar_winds/networks'

file = open("infoblox-import.out","w")

print("[+] Starting to parsing data...")

file.write("header-network,address*,netmask*,comment\n")

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("[+] Working on... " + filename)
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for line in islice(csvfile, 2, 3):
                #print(line)
                a,b,c,d,e = line.split(",")
                #print(b,c,e)
                file.write("network," + c + "," + e.rstrip('\n') + ",""This is a test""\n")
