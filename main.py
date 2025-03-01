# api key: e6bcf177-33ab-4d68-87ba-f2ab030011c5
import requests
import datetime
from ics import Calendar, Event
c = Calendar()


station_dict = {1:'9610291',
                2:'9610470',
                3:'9610192',
                4:'9610287',
                5:'9610219'}

dep_time = []
arr_time = []
train_date = []
train_duration = []
def main():
    global dep_time
    global arr_time
    global train_date
    global train_duration
    dep = 0
    arr = 0
    while dep == arr:
        dep_input = int(input('''
Выберите станцию отправления:'
    1) Обское море
    2) Сеятель
    3) Новосибирск-южный
    4) Речной вокзал
    5) Камышенская
-->'''))
        arr_input = int(input('''
Выберите станцию прибытия:
        1) Обское море
        2)Сеятель
        3) Новосибирск-южный
        4) Речной вокзал
        5) Камышенская
    -->'''))
        dep = station_dict.get(dep_input)
        arr = station_dict.get(arr_input)

    schedul = requests.get(f'https://api.rasp.yandex.net/v3.0/search/?apikey=e6bcf177-33ab-4d68-87ba-f2ab030011c5&format=json&from=s{dep}&to=s{arr}&page=1&date={datetime.date.today().isoformat()}').json()
    print(schedul)

    for i in schedul:
        for train in schedul['segments']:
            dep_time.append(train['departure'][11:16])
            arr_time.append(train['arrival'][11:16])
            train_date.append(train['start_date'])
            train_duration.append(int(train['duration']/60))
            #print(train['departure'][11:16], train['duration']/60, train['start_date'])
            if (dep_time[0] == train['departure'][11:16]) and (len(dep_time) > 1): break

    dep_time = dep_time[0:len(dep_time)-3]
    arr_time = arr_time[0:len(arr_time)-3]
    train_date = train_date[0:len(train_date)-3]
    train_duration = train_duration[0:len(train_duration)-3]

    for z in range(0, len(dep_time)):
        create_event(z, f'{train_date[z]}', f'{dep_time[z]}', f'{arr_time[z]}')

def create_event(number, date, dep, arr):
    name = Event()
    name.name = f'Электричка на {dep}'
    corrected_dep = datetime.datetime.strptime(f'{date} {dep}:00', '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=7)
    corrected_arr = datetime.datetime.strptime(f'{date} {arr}:00', '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=7)
    begin = corrected_dep.strftime('%Y-%m-%d %H:%M:%S')
    end = corrected_arr.strftime('%Y-%m-%d %H:%M:%S')
    name.begin = f'{begin}'
    name.end = f'{end}'
    c.events.add(name)
    c.events
    with open('my.ics', 'w') as my_file:
        my_file.writelines(c.serialize_iter())

def station_code ():
    '''
    Обское море - 9610291
    Сеятель - 9610470
    Новосибирск-южный - 9610192
    Речной вокзал - 9610287
    Камышенская - 9610219
    '''
    pass



if __name__ == '__main__':
    main()
