# api key: e6bcf177-33ab-4d68-87ba-f2ab030011c5
import requests
import datetime
from ics import Calendar, Event
from urllib3.filepost import choose_boundary

c = Calendar()


station_dict = {1:'9610291',
                2:'9610470',
                3:'9610192',
                4:'9610287',
                5:'9610219'}
back_station_dict = {1: 'Обское море',
                     2: 'Сеятель',
                     3: 'Новосибирск-южный',
                     4: 'Речной вокзал',
                     5: 'Камышенская'}
back_station_dict_en = {1: 'Ob sea',
                     2: 'Seyatel',
                     3: 'Novosibirsk-southern',
                     4: 'River station',
                     5: 'Kamychenskaya'}


dep_time = []
arr_time = []
train_date = []
train_duration = []
trip = {}
def main():
    global dep_time
    global arr_time
    global train_date
    global train_duration
    global arr
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
    2) Сеятель
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
            trip[train['departure'][11:16]] = ([train['arrival'][11:16], train['duration']/60])
            dep_time.append(train['departure'][11:16])
            if (dep_time[0] == train['departure'][11:16]) and (len(dep_time) > 1): break
    print(f'От станции {back_station_dict.get(dep_input)} до станции {back_station_dict.get(arr_input)} '
          f'найдены следующие поезда:')
    for k in trip.keys():
        print(f'Отправления: {k}, Прибытие: {trip[k][0]}, Время в пути: {trip[k][1]}')
    choose_train = ''
    while choose_train not in trip.keys():
        choose_train = input('Выбирете время отправления -->')
    print(choose_train)

    create_event(f'{datetime.date.today().isoformat()}', choose_train, f'{trip[choose_train][0]}', f'{back_station_dict_en.get(arr_input)}')

def create_event(date, dep, arr, st_arr):
    name = Event()
    name.name = f'Sub train to {st_arr}'
    corrected_dep = datetime.datetime.strptime(f'{date} {dep}:00', '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=7)
    corrected_arr = datetime.datetime.strptime(f'{date} {arr}:00', '%Y-%m-%d %H:%M:%S') - datetime.timedelta(hours=7)
    begin = corrected_dep.strftime('%Y-%m-%d %H:%M:%S')
    end = corrected_arr.strftime('%Y-%m-%d %H:%M:%S')
    name.begin = f'{begin}'
    name.end = f'{end}'
    c.events.add(name)
    c.events
    with open('train.ics', 'w') as my_file:
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
