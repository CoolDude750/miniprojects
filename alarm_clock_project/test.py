from datetime import datetime
from playsound import playsound

now = datetime.now()
print(now)
current_hour = now.strftime("%I")
current_minute = now.strftime("%M")
current_seconds = now.strftime("%S")
current_period = now.strftime("%p")
print(current_period)
#playsound('Loud.mp3')
