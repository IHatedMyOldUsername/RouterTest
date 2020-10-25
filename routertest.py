import matplotlib.pyplot as plt
import numpy as np
import pythonping
import datetime

pingList = ['192.168.1.1', 'google.com', '1.1.1.1']

class PingConstruct:
    def __init__(self, ipToAdd):
        self.ip = ipToAdd
        self.xAxis = []
        self.yAxis = []
    def PrintIP(self):
        return(self.ip)
    def PingIP(self):
        pingres = pythonping.ping(ip)
        if pingres.rtt_avg_ms >= 300:
            return 0
        self.xAxis.append(datetime.datetime.now())
        self.yAxis.append(pingres.rtt_avg_ms)
        print(self.yAxis)
    def GraphIP(self):
        plt.plot(self.xAxis, self.yAxis, label=self.ip)

ipDict = {}
for ip in pingList:
    pingStruct = PingConstruct(ip)
    ipDict[ip] = pingStruct

try:
    while True:
        for ip in ipDict:
            ipDict[ip].PingIP()
except KeyboardInterrupt:
    pass

plt.title("Bad Modem is Bad")
plt.xlabel('Date and Time')
plt.ylabel('Ping Time (ms)')

for ip in ipDict:
    ipDict[ip].GraphIP()

plt.legend()
plt.show()
