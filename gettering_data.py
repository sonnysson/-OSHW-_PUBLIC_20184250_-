import serial
import time
import minimalmodbus as M

mydev = "/dev/ttyUSB0"
ser = serial.Serial(mydev,921600)

def L_distance():
    if 1:
        M.serial.baudrate= 115200
        instrument = M.Instrument('/dev/ttyUSB1',1,M.MODE_RTU)
        instrument.serial.baudrate = 115200
        try :
            dtn = float(instrument.read_register(24,0,functioncode=int('0x04',16)))
            dtn2 = dtn/10
            return dtn2
        except:
            print("failed to connect instrument")


def IMU():
    while True:
        try:
            data = ser.readline()
            data = data.decode('utf-8')
            f = open('rpidata.txt','w')
            datas = data.split(",")
            roll = datas[1]
            pitch = datas[2]
            yaw = datas[3]

            distance = str(L_distance())
                
            datas = [roll,pitch,yaw,distance]
             
            now = time.localtime()
            now_time = "%02d:%02d:%02d" %(now.tm_hour, now.tm_min, now.tm_sec)
                
            datas = [now_time,roll,pitch,yaw,distance]
            web_datas = ",".join(datas)
                
            print(web_datas)
            f.write(web_datas+',')
            f.close()
        except:
            print("fail")
            pass

IMU()