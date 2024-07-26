from urllib.request import urlopen # se queda
from bs4 import BeautifulSoup # se queda
import requests # se queda
import nmap
import json
import re
import sys
from rich.console import Console
# from home_nmap.home_nmap import query
# from home_nmap import OutputParser
# from home_nmap import fill_simple_table

nm = nmap.PortScanner()

print("<<=============================================>>")

ipaddr = input("Please enter the IP address and range to scan for devices on your local network: ")
print("The IP/range you entered is: ", ipaddr)

options = "-sn"

print("Starting the scan...")
nm.scan(ipaddr, arguments='-sP' )
nm.command_line()

print(nm.scaninfo())

for host in nm.all_hosts():
    if nm[host].state() == 'up':
        print('Host: %s' % host)

print("\nScan results:")
for host in nm.all_hosts():
    print(f"\nHost: {host}")
    
    hostnames = nm[host].hostname()
    print(f"Hostname: {hostnames if hostnames else 'No hostname'}")
    
    state = nm[host].state()
    print(f"State: {state}")
    
    if 'addresses' in nm[host] and 'mac' in nm[host]['addresses']:
        mac_address = nm[host]['addresses']['mac']
        print(f"MAC Address: {mac_address}")
    else:
        print("MAC Address: No MAC address found")
    
    if 'hostscript' in nm[host]:
        for script in nm[host]['hostscript']:
            print(f"Script: {script['id']}, Output: {script['output']}")
    
    for protocol in nm[host].all_protocols():
        print(f"Protocol: {protocol}")
        ports = nm[host][protocol].keys()
        for port in ports:
            print(f"Port: {port}\tState: {nm[host][protocol][port]['state']}")
            
#########################
# urlstr = input("Ingresa la url para acceder a tu modem: \n")
# username = input("Ingresa el nombre de usuario para acceder a tu modem: \n")
# password = input("Ingresa la contraseña para acceder a tu modem: \n")

# page = urlopen(urlstr)

# html_bytes = page.read()
# html = html_bytes.decode("utf-8")

# title_index = html.find("<title>")
# title_index

# match_results = re.search("ab*c", "ABC", re.IGNORECASE)
# match_results.group()

# response = requests.post(urlstr, 
#     data={"key": "value"},
#     headers={"Content-Type": "application/json"},
# )

# session = requests.Session()

# session.headers.update({'Content-Type': 'application/json'})

# response = session.post(urlstr, json=data)

# print(response.json())

# print(urlstr, username, password)




