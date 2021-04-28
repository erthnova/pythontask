from math import sqrt
import sys

def point_in_line(x, y, z): #проверка принадлежности точки пересения линии и сферы отрезку
    if px <= x <=vx or  vx <= x <=px and py <= y <=vy or  vy <= y <=py and pz <= z <=vz or  vz <= z <=pz:
        print(x, y, z)

if __name__ == "__main__":
    filedict = sys.argv[1]


with open(filedict) as f: #парсим значения из файла
    for line in f:
        parsstr = line.replace('},', ' ').replace('{', '').replace('}', '').replace('], ', '] ').replace(', ', ',').split()
        for i in range(len(parsstr)):
            if parsstr[i] == 'center:':
                centerpos = parsstr[i+1].replace('[', '').replace(']', '').replace('[', '').split(',')
            elif parsstr[i] == 'radius:':
                radiuspos = parsstr[i+1]
            elif parsstr[i] == 'line:':
                linepos1 = parsstr[i + 1].replace('[', '').replace(']', '').replace('[', '').split(',')
                linepos2 = parsstr[i + 2].replace('[', '').replace(']', '').replace('[', '').split(',')
#для удобства подстановки в формулы
px = float(linepos1[0])
py = float(linepos1[1])
pz = float(linepos1[2])

vx = float(linepos2[0])
vy = float(linepos2[1])
vz = float(linepos2[2])

r = float(radiuspos)

cx = float(centerpos[0])
cy = float(centerpos[1])
cz = float(centerpos[2])
#решение квадратичного уравнения через дискриминант
C= (px-cx)**2 + (py-cy)**2 + (pz-cz)**2 - r**2
A= (px-vx)**2 + (py-vy)**2 + (pz-vz)**2
B= (vx-cx)**2 + (vy-cy)**2 + (vz-cz)**2 - A - C - r**2
D = B**2 - 4 * A * C
#при D < 0 линия не будет касаться сферы
if (D < 0):
    print('Коллизий не найдено')
#вычисление точек касания линии и сферы
else:
    t1 = (0-B - sqrt(D) ) / (2*A)
    t2 = (0-B + sqrt(D) ) / (2*A)

    x1 = px * (1 - t1) + t1 * vx
    y1 = py * (1 - t1) + t1 * vy
    z1 = pz * (1 - t1) + t1 * vz

    x2 = px * (1 - t2) + t2 * vx
    y2 = py * (1 - t2) + t2 * vy
    z2 = pz * (1 - t2) + t2 * vz
    # при D = 0 линия будет касаться сферы
    if (D == 0):
        print(point_in_line(x1, y1, z1))
    # при D = 0 линия будет пересекать сферу
    if(D > 0):
        print(point_in_line(x1, y1, z1))
        print(point_in_line(x2, y2, z2))
