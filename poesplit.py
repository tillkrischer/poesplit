import re
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 16834))

logpath = "C:/Program Files (x86)/Steam/steamapps/common/Path of Exile/logs/Client.txt"
maps = [ "Courthouse" ]

f = open(logpath, encoding="utf8")

location = ""
line = f.readline()
while line:
    m = re.search("You have entered ([^.]*)", line)
    if m:
        location = m.group(1)
    line = f.readline()

while True:
    time.sleep(0.05)
    line = f.readline()
    while line:
        m = re.search("You have entered ([^.]*)", line)
        if m:
            newlocation = m.group(1)
            if location in maps and re.search("Hideout", newlocation):
                s.send(b'pause\r\n')
            if re.search("Hideout", location) and newlocation in maps:
#                s.send(b'split\r\n')
                s.send(b'reset\r\n')
                s.send(b'starttimer\r\n')
            location = newlocation
            print(location)
        line = f.readline()

