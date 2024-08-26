# Is the website accessible?
# Create a code in Python to test if Pudim website is accessible by used computer.
import requests

url = "https://www.pudim.com.br"

try:
    r = requests.get(url, timeout=15, verify=False)
    if r.status_code == 200:
        print('\033[32m###\tPudim website is available\t###\033[m')
except:
    print('\033[31m###\tPudim website is not available\t###\033[m')
