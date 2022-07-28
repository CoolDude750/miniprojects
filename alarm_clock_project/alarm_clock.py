from datetime import datetime
from playsound import playsound

alarm_time = input("Enter the time to set alarm:HH:MM:SS:pm\n")
alarm_hour = alarm_time[0:2]
alarm_minute = alarm_time[3:5]
alarm_seconds = alarm_time[6:8]
alarm_period = alarm_time[9:11].upper()
print("setting up alarm for you..")
#playsound('Loud.mp3')
while True:
    now = datetime.now()
    current_hour = now.strftime("%I")
    current_minute = now.strftime("%M")
    current_seconds = now.strftime("%S")
    current_period = now.strftime("%p")
    if(alarm_hour == current_hour):
        if(alarm_minute == current_minute):
            if(alarm_seconds == current_seconds):
                if(alarm_period == current_period):
                    print("Wake up dude !")
                    playsound('Loud.mp3')
                    break

