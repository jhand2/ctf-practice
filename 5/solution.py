import requests as r
from bs4 import BeautifulSoup
import re
import time

url = "https://drivetothetarget.web.ctfcompetition.com/"

lat = 51.6498
lon = 0.0982
referer = url
user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36"

# Guess and check to get optimal values
speed_lat = 0
speed_lon = -0.0001

def get(url, query, headers):
    full = url + query
    return r.get(full, headers=headers)


def get_initial_token():
    res = get(url, "", {})
    parsed = BeautifulSoup(res.text, "html.parser")
    return parsed.find('input', {"name": "token"}).get("value")


def move(curr_lat, curr_lon, curr_token, dlat, dlon):
    global referer

    new_lat = round(curr_lat + dlat, 4)
    new_lon = round(curr_lon + dlon, 4)

    # I thought setting the headers was important but I don't think it really
    # is. Oh well.
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

    # Parse out state information
    parsed = BeautifulSoup(res.text, "html.parser")
    new_token = parsed.find('input', {"name": "token"}).get("value")

    closer = False
    if parsed.find("p", text=re.compile(r"this is too fast!")):
        print("Too fast")
        print(parsed)
    elif parsed.find("p", text=re.compile(r"You are getting closer")):
        p = parsed.find("p", text=re.compile(r"You are getting closer"))
        referer = url + query
        closer = True
    elif parsed.find("p", text=re.compile(r"away")):
        print(parsed)
    else:
        print(parsed)
        exit(1)

    return (new_lat, new_lon, new_token, closer)


token = get_initial_token()
time.sleep(0.5)

backtrack = False
flip_speed = False
turn = False
while True:
    if backtrack:
        backtrack = False
        (lat, lon, token, is_closer) = move(lat, lon, token, -speed_lat, -speed_lon)
    elif turn:
        tmp = speed_lat
        speed_lat = speed_lon
        speed_lon = tmp
        (lat, lon, token, is_closer) = move(lat, lon, token, speed_lat, speed_lon)
    else:
        (lat, lon, token, is_closer) = move(lat, lon, token, speed_lat, speed_lon)

    if is_closer:
        print("%s, %s : Getting closer" % (lat, lon))
    else:
        print("%s, %s : Too far, turning around" % (lat, lon))
        turn = True
        backtrack = True

    # Seems like the google backend needs some time to load the token. If I
    # remove this wait, it says "too fast"
    time.sleep(0.35)

