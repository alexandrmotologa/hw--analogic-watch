#main application module
from clock import *
from alarm import *
from time import sleep
from datetime import datetime

result = getAlarmTime()

while True:
    sleep(0.62)
    d = datetime.now()
    hour = int(datetime.now().strftime("%#I"))
    hourSystem = datetime.now().strftime("%p")
    printTime(hour, d.minute, d.second, hourSystem)
    drawClock(hour, d.minute, d.second)
    checkAlarm(result[0], result[1], result[2], hour, d.minute, hourSystem)