import matplotlib.pyplot as plt
import numpy as np
import pythonping
import datetime

xAxis1 = []
yAxis1 = []
xAxis2 = []
yAxis2 = []
xAxis3 = []
yAxis3 = []

def plotPing(graph):
    if graph == 'global':
        pingres = pythonping.ping('google.com')
        if(pingres.rtt_avg_ms >= 100):
            return
        yAxis1.append(pingres.rtt_avg_ms)
        xAxis1.append(datetime.datetime.now())
    elif graph == 'local':
        pingres = pythonping.ping('192.168.1.1')
        if(pingres.rtt_avg_ms >= 100):
            return
        yAxis2.append(pingres.rtt_avg_ms)
        xAxis2.append(datetime.datetime.now())
    elif graph == 'globalip':
        pingres = pythonping.ping('8.8.8.8')
        if(pingres.rtt_avg_ms >= 100):
            return
        yAxis3.append(pingres.rtt_avg_ms)
        xAxis3.append(datetime.datetime.now())


for i in range(1,100):
    plotPing('global')
    plotPing('local')
    plotPing('globalip')
    print('Ping {} of 100 performed'.format(i))

plt.title("Bad Router is Bad")
plt.xlabel('Date and Time')
plt.ylabel('Ping Time (ms)')
plt.plot(xAxis1, yAxis1, label='Google (google.com)')
plt.plot(xAxis2, yAxis2, label='Local Router')
plt.plot(xAxis3, yAxis3, label='Google (8.8.8.8)')
plt.legend()
plt.show()
