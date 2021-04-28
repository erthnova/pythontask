import time
import csv
import sys

class Barrel():
    def __init__(self, size, general_volume=0):
        self.size = size #размер бочки
        self.general_volume = general_volume #начальный объём
        self.attempts_top_up=0 #количество попыток налить воду в бочку было за указанный период
        self.volume_top_up = 0 #объем воды был налит в бочку за указанный период
        self.volume_no_top_up = 0 #объем воды был не налит в бочку за указанный период

        self.attempts_scoop=0 #количество попыток забора воды из бочки было за указанный период
        self.volume_scoop = 0 #объем воды был забран воды из бочки за указанный период
        self.volume_no_scoop = 0 #объем воды был не взят из бочки за указанный период

        self.error = 0 #количество ошибок был допущено за указанный период

    def top_up(self, volume): #наливаем воду
        self.attempts_top_up += 1

        if self.general_volume + volume <= self.size:
            self.general_volume += volume
            self.volume_top_up += volume

        else:
            self.volume_no_top_up += 1
            self.error += 1

    def scoop(self, volume): #забираем воду
        self.attempts_scoop += 1

        if self.general_volume - volume >= 0:
            self.general_volume -= volume
            self.volume_scoop += volume

        else:
            self.volume_no_scoop += 1
            self.error += 1

if __name__ == "__main__":
    usage = 'Неверно введены аргументы!\nПример правильного ввода: ./log.log 2020-01-01T12:00:00 2021-01-01T13:00:00'
    try:
        if len (sys.argv) == 4:
            filedict = sys.argv[1]
            timestart = sys.argv[2]
            timefinish = sys.argv[3]
        else:
            print(usage)
            sys.exit(1)
    except Exception:
        print(usage)
        sys.exit (1)




timestart=timestart.replace('T', ' ')
timefinish=timefinish.replace('T', ' ')

count = 0
with open(filedict, encoding='utf-8') as f:
    for line in f:
        if '(объем бочки)' in line:
            sizebarrel = line.split()[0]
            barbefore = Barrel(int(sizebarrel))  # создаём обьект класса бочка до времени отсчета

        elif '(текущий объем воды в бочке)' in line:
            valuestart = line.split()[0]
            barbefore.general_volume = int(valuestart)

        elif line[0].isdigit():
            timeact = line.split('.')[0]
            timeact=timeact.replace('Т', ' ')
            act = line.split('-')[3].replace('wanna', '').lstrip()
            #если время в логах не совпадёт с запрашиваемым, то barintime не будет создан
            if count == 0:
                barintime = Barrel(barbefore.size, barbefore.general_volume)
            # до начала заданного периода все значения пишем в barbefore для подсчета стартовых значений
            if time.strptime(timeact,'%Y-%m-%d %H:%M:%S') < time.strptime(timestart,'%Y-%m-%d %H:%M:%S'):
                if act.split(' ')[0] == 'top':
                    barbefore.top_up(int(act.split(' ')[2].replace('l', '')))
                elif act.split(' ')[0] == 'scoop':
                    barbefore.scoop(int(act.split(' ')[1].replace('l', '')))
            #после начала заданного периода все значения пишем в barintime
            elif time.strptime(timeact,'%Y-%m-%d %H:%M:%S') > time.strptime(timestart,'%Y-%m-%d %H:%M:%S') and time.strptime(timeact,'%Y-%m-%d %H:%M:%S') < time.strptime(timefinish,'%Y-%m-%d %H:%M:%S'):
                count = 1
                if act.split(' ')[0] == 'top':
                    barintime.top_up(int(act.split(' ')[2].replace('l', '')))
                elif act.split(' ')[0] == 'scoop':
                    barintime.scoop(int(act.split(' ')[1].replace('l', '')))

#проверяем были ли записи в логе за указанное время и в зависимости от этого пишет report
if barintime.size == 0:
    report = [
        ["В указаный период не было записей в логе!"],
    ]
else:
    if barintime.error == 0:
        errorchar = 0
    else:
        errorchar = int((barintime.attempts_top_up +barintime.attempts_scoop)/barintime.error)
    report = [
        ["Количество попыток налить воду в бочку было за указанный период", barintime.attempts_top_up],
        ["Процент ошибок был допущено за указанный период", errorchar],
        ["Объем воды был налит в бочку за указанный период", barintime.volume_top_up],
        ["Объем воды был не налит в бочку за указанный период", barintime.volume_no_top_up],
        ["Количество попыток забора воды из бочки было за указанный период", barintime.attempts_scoop],
        ["Объем воды был забран воды из бочки за указанный период", barintime.volume_scoop],
        ["Объем воды был не взят из бочки за указанный период", barintime.volume_no_scoop],
        ["Объем воды был в бочке в начале указанного периода", barbefore.general_volume],
        ["Объем воды был в бочке в конце указанного периода", barintime.general_volume],
    ]

with open('report.csv',  "w", encoding='utf-8', newline="") as file:
    writer = csv.writer(file)
    writer.writerows(report)

print('Результат записан в файл report.csv')
