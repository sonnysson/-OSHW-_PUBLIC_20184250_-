import socket
import csv

namafile = 'data.csv'
header1 = 'time'
header2 = 'roll'
header3 = 'pitch'
header4 = 'yaw'
header5 = 'distance'
fieldnames = [header1,header2,header3,header4,header5,]

def dataSave(time,roll,pitch,yaw,distance):
    with open(namafile, 'a') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        info = {
            header1: time,
            header2: roll,
            header3: pitch,
            header4: yaw,
            header5: distance
        }

        csv_writer.writerow(info)



# 서버의 주소입니다. hostname 또는 ip address를 사용할 수 있습니다.
HOST = '192.168.0.18'
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

    data = client_socket.recv(1024)

    if copy == data:
        continue
    else:
        data = data.decode('utf-8').split(',')
        print("측정시간 = ",data[0],"roll = ",data[1],"pitch = ",data[2],"yaw = ",data[3],"distance = ",data[4],)
        dataSave(data[0],data[1],data[2],data[3],data[4])


# 소켓을 닫습니다.
client_socket.close()