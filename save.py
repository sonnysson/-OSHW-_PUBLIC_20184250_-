import socket
import csv
import math
import random
from itertools import count
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np


namafile = 'data.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"
fieldnames = [header1, header2, header3]

def dataSave(xs, ys, zs):


    with open(namafile, 'a') as csv_file:
        '''
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            header1: xs,
            header2: ys,
            header3: zs
        }

        csv_writer.writerow(info)

        print(xs, ys, zs)
        '''
    with open(namafile, "a") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow([xs, ys, zs])
        print(xs, ys, zs)

if __name__ == '__main__':

    with open(namafile, 'w') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()

def calculate(roll,pitch,yaw,distance):
    #roll,pitch,yaw,distance = hello_world()

    theta = math.radians(yaw)
    phi = math.radians(90 - pitch)

    # print theta, phi

    R = distance
    xs = R * math.cos(theta) * math.cos(phi)
    ys = R * math.sin(phi) * math.sin(theta)
    zs = R * math.sin(phi)

    #print('roll :', a, 'pitch :', b, 'yaw : ', c, 'xs : ', xs, 'ys : ', ys, 'zs : ', zs)
    #print('xs : ', xs, 'ys : ', ys, 'zs : ', zs, R)

    return round(xs, 4),round(ys, 4),round(zs, 4)

# 서버의 주소입니다. hostname 또는 ip address를 사용할 수 있습니다.
HOST = '192.168.0.82'
# 서버에서 지정해 놓은 포트 번호입니다.
PORT = 8080

# 소켓 객체를 생성합니다.
# 주소 체계(address family)로 IPv4, 소켓 타입으로 TCP 사용합니다.
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 지정한 HOST와 PORT를 사용하여 서버에 접속합니다.
client_socket.connect((HOST, PORT))

# 메시지를 전송합니다.

# 메시지를 수신합니다.

copy = '0'

while True:
    try:
        data = client_socket.recv(1024)

        if copy == data:
            continue
        else:
            data = data.decode('utf-8').split(',')
            calculated = calculate(float(data[1]),float(data[2]),float(data[3]),float(data[4]))
            dataSave(calculated[0],calculated[1],calculated[2])
    except:
        pass


# 소켓을 닫습니다.
client_socket.close()