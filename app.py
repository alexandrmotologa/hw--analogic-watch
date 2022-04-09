#main application module
from clock import *
from time import sleep
from datetime import datetime

while True:
    sleep(0.62)
    d = datetime.now()
    hour = int(datetime.now().strftime("%#I"))
    drawClock(hour, d.minute, d.second)