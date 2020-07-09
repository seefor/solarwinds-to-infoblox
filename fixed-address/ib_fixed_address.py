#!/usr/local/bin/python3
# -*- coding: utf-8 -*-

__author__ = "Sif Baksh"
__version__ = "1.0.0"
__website__ = "sifbaksh.com"
__twitter__ = "@sifbaksh"

import csv
import os

# Make sure to use the absolut path to where the exports are located
directory = '/Users/sbaksh/Dropbox/CCS_Perl_Scripts/DDI/ipam_solar_winds/fixed_address'

file = open("infoblox-fixed-address.out","w")

print("[+] Starting to parsing data...")

file.write(
    "header-fixedaddress,ip_address*,_new_ip_address,always_update_dns,boot_file,boot_server,broadcast_address,circuit_id,cli_credentials,comment,ddns_domainname,ddns_hostname,deny_bootp,dhcp_client_identifier,disabled,domain_name,domain_name_servers,enable_ddns,enable_discovery,enable_immediate_discovery,enable_pxe_lease_time,ignore_client_requested_options,lease_time,mac_address,match_option,ms_server,_new_ms_server,name,network_view,next_server,option_logic_filters,override_cli_credentials,override_credential,prepend_zero,pxe_lease_time,remote_id,routers,snmpv1v2_credential,snmpv3_credential,use_snmpv3_credential\r\n")

for filename in os.listdir(directory):
    if filename.endswith(".csv"):
        print("[+] Working on... " + filename)

        #f = open(filename)
        with open(filename) as csvfile:
            readCSV = csv.reader(csvfile, delimiter=',')
            for row in readCSV:
                if 'Dynamic' not in row and 'Available' not in row and 'Reserved' not in row and 'DHCP Client Name' not in row and 'fixaddress' not in row:
                    #print("fixedaddress," + row[0] + ",,FALSE,,,,,," + row[4] + ",,,,,FALSE,,,,TRUE,FALSE,,,,00:00:00:00:00:00,RESERVED,,," + row[2] + ",default,,,FALSE,FALSE,FALSE,,,,,,FALSE,Test CT 2,INHERIT,,,Testing EA")
                    file.write("fixedaddress," + row[0] + ",,FALSE,,,,,," + row[4] + ",,,,,FALSE,,,,TRUE,FALSE,,,,00:00:00:00:00:00,RESERVED,,," + row[2] + ",default,,,FALSE,FALSE,FALSE,,,,,,FALSE\r\n")

        continue
    else:
        continue

print("[+] Done")