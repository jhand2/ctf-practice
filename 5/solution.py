import requests as r
from bs4 import BeautifulSoup
import re
import time

url = "https://drivetothetarget.web.ctfcompetition.com/"

lat = 51.6498
lon = 0.0982
referer = url
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"

speed = 0.00005

def get(url, query, headers):
    full = url + query
    return r.get(full, headers=headers)


def get_initial_token():
    res = get(url, "", {})
    parsed = BeautifulSoup(res.text, "html.parser")
    return parsed.find('input', {"name": "token"}).get("value")


def move(curr_lat, curr_lon, curr_token, dlat, dlon):
    global referer

    new_lat = curr_lat + dlat
    new_lon = curr_lon + dlon

    headers = {
        "Referer": referer,
        "User-Agent": user_agent,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-origin",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1"
    }

    query ="?lat=%s&lon=%s&token=%s" % (new_lat, new_lon, curr_token)
    res = get(url, query, headers)


    parsed = BeautifulSoup(res.text, "html.parser")
    new_token = parsed.find('input', {"name": "token"}).get("value")

    if parsed.find("p", text=re.compile(r"this is too fast!")):
        print("Too fast")
        print(parsed)
        return None
    elif parsed.find("p", text=re.compile(r"You are getting closer")):
        p = parsed.find("p", text=re.compile(r"You are getting closer"))
        print(p)
        referer = url + query
        return (new_lat, new_lon, new_token)

token = get_initial_token()
time.sleep(0.4)
for i in range(100):
    new_pos = move(lat, lon, token, -speed, -speed)
    time.sleep(0.4)
    if new_pos is not None:
        lat = new_pos[0]
        lon = new_pos[1]
        token = new_pos[2]


