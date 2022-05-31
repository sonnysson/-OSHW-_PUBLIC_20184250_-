from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

fig = plt.figure(figsize = (6,6))
ax = fig.add_subplot(projection='3d')

namafile = 'data3D.csv'
header1 = "x_value"
header2 = "y_value"
header3 = "z_value"

index = count()


def animate(i):
    data = pd.read_csv('data.csv')
    x = data[header1]
    y = data[header2]
    z = data[header3]

    plt.cla()

    ax.scatter(x, y, z, 'red')



ani = FuncAnimation(fig, animate, interval=100) #그림 0.5초 간격으로 재생

plt.show()
