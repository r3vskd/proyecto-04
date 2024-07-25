from urllib.request import urlopen # se queda
from bs4 import BeautifulSoup # se queda
import requests # se queda
import nmap
import json
import re
import sys
from rich.console import Console
from home_nmap import query
from home_nmap import OutputParser
from home_nmap import fill_simple_table

scanner = nmap.PortScanner()

# Define target IP address or hostname
target = "scanme.nmap.org"

# Run a basic scan on the target
scanner.scan(target)

# Print the scan results
for host in scanner.all_hosts():
    print("Host: ", host)
    print("State: ", scanner[host].state())
    for proto in scanner[host].all_protocols():
        print("Protocol: ", proto)
        ports = scanner[host][proto].keys()
        for port in ports:
            print("Port: ", port, "State: ", scanner[host][proto][port]['state'])
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




