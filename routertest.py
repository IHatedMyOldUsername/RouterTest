import matplotlib.pyplot as plt
import numpy as np
import pythonping
import datetime

pingList = ['192.168.1.1', 'google.com', '1.1.1.1']
xAxis1 = []
yAxis1 = []
xAxis2 = []
yAxis2 = []
xAxis3 = []
yAxis3 = []

class PingConstruct:
    def __init__(self, ipToAdd):
        self.ip = ipToAdd
    
    def PrintIP(self):
        return(self.ip)

def plotPing(graph):
    if graph == 'global':
        pingres = pythonping.ping('google.com')
        if pingres.rtt_avg_ms >= 300:
            return 0
        yAxis1.append(pingres.rtt_avg_ms)
        xAxis1.append(datetime.datetime.now())
    elif graph == 'local':
        pingres = pythonping.ping('192.168.1.1')
        if(pingres.rtt_avg_ms >= 300):
            return 0
        yAxis2.append(pingres.rtt_avg_ms)
        xAxis2.append(datetime.datetime.now())
    elif graph == 'globalip':
        pingres = pythonping.ping('1.1.1.1')
        if(pingres.rtt_avg_ms >= 300):
            return 0
        yAxis3.append(pingres.rtt_avg_ms)
        xAxis3.append(datetime.datetime.now())

pingDict = {}
for ip in pingList:
    pingStruct = PingConstruct(ip)
    print(pingStruct.PrintIP())

try:
    i = 0
    while True:
        plotPing('global')
        plotPing('local')
        plotPing('globalip')
        i += 1
        print('Ping {} performed'.format(i))
except KeyboardInterrupt:
    pass

plt.title("Bad Modem is Bad")
plt.xlabel('Date and Time')
plt.ylabel('Ping Time (ms)')
plt.plot(xAxis1, yAxis1, label='Google (google.com)')
plt.plot(xAxis2, yAxis2, label='Local Router')
plt.plot(xAxis3, yAxis3, label='CloudFare (1.1.1.1)')
plt.legend()
plt.show()
