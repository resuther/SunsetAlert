from time import strptime
from datetime import datetime
import time
import requests
import json
def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

time.time()
response = requests.get("https://api.sunrise-sunset.org/json?lat=-36.111413&lng=174.585372&date=today")
s = response.json()['results']['sunset']
e = response.json()['results']['astronomical_twilight_end']

start = s[:7]
endedit = e[:7]
endeditt = endedit[:1]
endedittt = int(endeditt)
endeditttt = (f"{endedittt + 1}")

sky = 0

def manual_replace(s, char, index):
    return s[:index] + char + s[index +1:]

string = endedit
end = (manual_replace(string, endeditttt, 0))

while True:
    text = (f"{datetime.utcnow()}")
    textt = text[12:]
    utctime = textt[:7]
    if utctime != start:
        if utctime != endedit:
            if sky == 0:
                with open('Test.txt', 'w') as file:
                    file.write("")
    if utctime == start:
        with open('Test.txt', 'w') as file:
            file.write(".")
            sky = 1
    if utctime == endedit:
        sky = 0