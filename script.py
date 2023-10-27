import pywhatkit
import datetime
import time

def send_schedule_message(numero, message, hour, minute):
    now = datetime.datetime.now()

    scheduling = datetime.datetime(now.year, now.month, now.day, hour, minute)

    pywhatkit.sendwhatmsg(numero, message, scheduling.hour, scheduling.minute + 1)

# exemplo de message programada
send_schedule_message("+55 31 99999-9999", "Essa message é automatica!", 4, 25)

def send_message_to_nnumbers(numbers, message):
    for numero in numbers:

        now = datetime.datetime.now()

        now += datetime.timedelta(minutes=1) 

        scheduling = datetime.datetime(now.year, now.month, now.day, now.hour, now.minute, now.second)

        pywhatkit.sendwhatmsg(numero, message, scheduling.hour, scheduling.minute)

        time.sleep(5)

numbers = ["+55 99 99999-9999", "+55 31 98888-8888"]

# exemplo de message encaminhada para diversos numbers
message = "This is an automatic message!"
send_message_to_nnumbers(numbers, message)