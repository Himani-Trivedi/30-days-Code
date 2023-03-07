# 1. Get the current day, month, year, hour, minute,
#  and timestamp from datetime module and print
# Format the current date using this format: ("%m/%d/%Y, %H:%M:%S") also Today is 20 February 2023. Change this time string to time.


from datetime import date, datetime

print(datetime.now())
print(datetime.now().date())
print(datetime.now().hour)
print(datetime.now().minute)
print(datetime.now().month)
print(datetime.today().year)
print(datetime.now().weekday())

print("Time stamp : " + str(datetime.timestamp(datetime.now())))
print("Time stamp : " + str(datetime.timestamp(datetime.now()) +
      datetime.timestamp(datetime.now())))

print(datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))

strtime = "20 February 2023"
newtime = datetime.strptime(strtime, "%d %B %Y")
print(newtime)

# 2. Calculate the time difference between now and the new year.

t1 = datetime.now()
t2 =datetime(year=2024,day=1,month=1)

print(t1-t2)