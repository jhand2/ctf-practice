import requests as r

url = "https://drivetothetarget.web.ctfcompetition.com/"

lat = 51.6498
lon = 0.0982
token = "gAAAAABdO4gjUEgzqOLjgDiogyAPX6xMqX2PdxLrZSi5G8C2Dp57DADOQr0mTzzCfuoEVbSxlUtoO9IM_Zo-mFB-oco9hofsReKkkoiPFgdJ5DpO5lf_cUKn6c3JoCUAwB9wdUKU-837"

for i in range(3):
    lon -= 0.001
    full = url + "?lat=%s&lon=%s&token=%s" % (lat, lon, token)
    res = r.get(full)
    print(res.text)
    print()


