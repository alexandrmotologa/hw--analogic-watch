# alarm module
import turtle as t
import winsound

def getAlarmTime():
    alarmHour = int(input("Write an alarm hour ( from 1 to 12 ): " ))
    if alarmHour <= 12 or alarmHour >= 1:
        alarmMinutes = int(input("Write an alarm minutes ( from 0 to 59 ): "))
        if alarmMinutes <= 59 or alarmMinutes >= 0:
            alarmSystem = input("Write a time system ( am or pm ): ").lower()
            if alarmSystem == "am" or alarmSystem == "pm":
                print(f"Alarm has been set at {alarmHour}:{alarmMinutes} {alarmSystem.upper()}")
                return alarmHour, alarmMinutes, alarmSystem


def checkAlarm(alarmHour, alarmMinutes, alarmSystem, hour, minute, hourSystem):
    if alarmHour == hour:
        if alarmMinutes == minute:
            if alarmSystem == hourSystem.lower():
                frequency = 2500  # Set Frequency To 2500 Hertz
                duration = 1000  # Set Duration To 1000 ms == 1 second
                winsound.Beep(frequency, duration)
                pic = t.Screen()
                pic.bgpic('bg.gif')
                print("ALARM")
        else:
            pic = t.Screen()
            pic.bgpic("nopic")
