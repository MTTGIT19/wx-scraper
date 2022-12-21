import requests
from bs4 import BeautifulSoup

# Set to input, could be switched to permanent station
city = input("-- QUICK AVIATION WEATHER.GOV -- Enter 3 digit U.S. airport identifier: ")

try:
    url = "https://www.aviationweather.gov/metar/data?ids=K"+city+"&format=decoded&hours=0&taf=on&layout=on"
except requests.ConnectionError as e1:
    print("Connection error. Check internet or try again")
except requests.RequestException as e2:
    print("This script sucks, try again soon.")

print(url)
r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

search = soup.find_all('table')

for l in search:
    wx = l.text.replace("\n\n","\n")
    print(wx)
