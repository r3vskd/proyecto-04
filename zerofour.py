from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import nmap
import json
import re
import sys
from rich.console import Console
from rich import print
import socket

nm = nmap.PortScanner()

print("<<=============================================>>")
print("Use the Default Gateway [bold magenta]World[]")
ipaddr = input("Please enter the IP address and range to scan for devices on your local network: ")
print("The IP/range you entered is: ", ipaddr)

options = "-sn"

print("Starting the scan...")
nm.scan(ipaddr, arguments='-sP')
nm.command_line()

print(nm.scaninfo())

print("\nScan results, [bold magenta]World[/bold magenta]!", ":vampire:", locals())

for host in nm.all_hosts():
    if nm[host].state() == 'up':
        print(f'Host: {host}')
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
