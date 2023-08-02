#!/usr/bin/python
# misst Temperaturen mit DS1820
import time
import driveTest
from datetime import datetime, timedelta

while 1:
    time.sleep(30)
    driveTest.create_csv(datetime.now().date())
    tempfile_20m = open("/sys/bus/w1/devices/28-3ce10457fddc/w1_slave")
    tempfile_15m = open("/sys/bus/w1/devices/28-3ce104571868/w1_slave")
    inhalt = tempfile_20m.read()
    tempfile_20m.close()
    inhalt_15m = tempfile_15m.read()
    tempfile_15m.close()
    tempdata = inhalt.split("\n")[1].split(" ")[9]
    temperatur = float(tempdata[2:])
    temperatur = temperatur / 1000
    tempdata_15m = inhalt_15m.split("\n")[1].split(" ")[9]
    temperatur_15m = float(tempdata_15m[2:])
    temperatur_15m = temperatur/1000
    driveTest.import_values_to_csv(datetime.now(), temperatur, temperatur_15m, 0)