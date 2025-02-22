# api key: e6bcf177-33ab-4d68-87ba-f2ab030011c5
import requests
import json

schedul = requests.get(f'https://api.rasp.yandex.net/v3.0/search/?apikey=e6bcf177-33ab-4d68-87ba-f2ab030011c5&format=json&from=s{9610291}&to=s{9610287}&page=1&date=2025-02-22').json()
print(schedul)
dep_time = []
for i in schedul:
    for train in schedul['segments']:
        dep_time.append(train['departure'][11:16])
        print(train['stops'], train['departure'][11:16], train['duration']/60, train['start_date'])
        if (dep_time[0] == train['departure'][11:16]) and (len(dep_time) > 1): break



def station_code ():
    '''
    Обское море - 9610291
    Сеятель - 9610470
    Новосибирск-южный - 9610192
    Речной вокзал - 9610287
    Камышенская - 9610219
    '''
    pass
help(station_code)
