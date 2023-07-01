#!/usr/bin/python
# misst Temperaturen mit DS1820
import time
while 1:
    time.sleep(2)
    #und so lauten wie Ihr Verzeichnis
    tempfile = open("/sys/bus/w1/devices/28-3ce104577a04/w1_slave")
    inhalt = tempfile.read()
    tempfile.close()
    tempdata = inhalt.split("\n")[1].split(" ")[9]
    temperatur = float(tempdata[2:])
    temperatur = temperatur/1000
    print("Temperatur betraegt: " + str(temperatur) + " Grad")