from time import strptime
from datetime import datetime
import time
import requests
import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

response = requests.get("https://api.sunrise-sunset.org/json?lat=-36.111413&lng=174.585372&date=today")
s = response.json()['results']['sunset']
e = response.json()['results']['astronomical_twilight_end']
start = s[:4]
end = e[:4]
yn = 0

while True:
    # defines time \/
    nowww = datetime.now()
    noww = nowww.strftime('%I:%M')
    now = noww[1:]
    if now != start:
        if now != end:
            if yn == 0:
                with open('Test.txt', 'w') as file:
                    file.write("")
    if now == start:
        with open('Test.txt', 'w') as file:
            file.write(".")
            yn = 1
    if now == end:
        yn = 0
    time.sleep(59)
