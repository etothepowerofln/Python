import datetime
import pytz

print("Time fixed value:\t" + str(datetime.time(12, 12, 12)))

print("Date fixed value:\t" + str(datetime.date(1212, 12, 12)))
print("Date today:\t\t" + str(datetime.date.today()))

print("Datetime fixed value:\t" + str(datetime.datetime(1212, 12, 12, 12, 12, 12)))
print("Datetime deltatime +:\t" + str(datetime.datetime(1212, 12, 12, 12, 12, 12)
                                      + datetime.timedelta(days=2, hours=2, minutes=2, seconds=2)))
print("Datetime deltatime -:\t" + str(datetime.datetime(1212, 12, 12, 12, 12, 12)
                                      - datetime.timedelta(days=2, hours=2, minutes=2, seconds=2)))
print("Datetime strftime:\t" + str(datetime.datetime(1212, 12, 12, 12, 12, 12).strftime("%H:%M:%S %m/%d/%Y")))
print("Datetime strptime:\t" + str(datetime.datetime.strptime("12:12:12 12/12/1212", "%H:%M:%S %m/%d/%Y")))
print("Datetime today:\t\t" + str(datetime.datetime.today()))
print("Datetime now:\t\t" + str(datetime.datetime.now()))
print("Datetime pytz SP:\t" + str(datetime.datetime.now(pytz.timezone("America/Sao_Paulo"))))
print("Datetime pytz NY:\t" + str(datetime.datetime.now(pytz.timezone("America/New_York"))))
print("Datetime pytz Lisbon:\t" + str(datetime.datetime.now(pytz.timezone("Europe/Lisbon"))))
