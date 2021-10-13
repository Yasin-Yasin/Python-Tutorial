import datetime
import pytz

# ---------------------------------------- datetime.date ---------------------------------------------

d = datetime.date(2021, 7, 24)
print(d)

# Current Local Date
tday  = datetime.date.today()
print(tday)
print(tday.year)
print(tday.weekday()) # Monday == 0, SUnday == 6
print(tday.isoweekday()) # Monday == 1 Sunday == 7
print(tday.day)

# Timedelta
tdelta = datetime.timedelta(days=7)
print(tday + tdelta) # What will be the date after a week/7 days
print(tday - tdelta) # What was the date before a week/7 

# If we add or subtract 2 dates we will get timedelta
# How many days untill my birthday
bday = datetime.date(2022, 7, 2)
till_bday = bday - tday
# print(till_bday)
print(till_bday.days)
print(till_bday.total_seconds())

# -------------------------------------- datetime.time ----------------------------------------------

t = datetime.time(9, 10, 30,100000)
print(t)
print(t.hour)
print(t.minute)
print(t.second)

# datetime.datetime

dt = datetime.datetime(2021, 7, 2, 10, 23, 12, 100000)
print(dt)
print(dt.date())
print(dt.time())
print("Hour : ", dt.hour)
print("Year : ", dt.year)
print("Month : ", dt.month)

tdelta1 = datetime.timedelta(hours = 7)
print(dt + tdelta1)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()

print()
print(dt_today)
print(dt_now)
print(dt_utcnow)

# TimeZone

# dt1 = datetime.datetime(2021, 7, 10, 11, 23, 30, tzinfo = pytz.UTC)
# print(dt1)

dt1_now = datetime.datetime.now(tz=pytz.UTC) # Preferable
print(dt1_now)

# dt1_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
# print(dt1_utcnow)

dt2_now = datetime.datetime.now(tz=pytz.UTC)
print(dt2_now)

dt_ind  = dt2_now.astimezone(pytz.timezone('Asia/Kolkata'))
print(dt_ind)

# Convert naive datetime into timezone aware
dt3_now = datetime.datetime.now() 
print(dt3_now)

ind_tz = pytz.timezone("Asia/Kolkata")
dt1_ind = ind_tz.localize(dt3_now)
print(dt1_ind)

# Convert datetime to string
dt2_ind = datetime.datetime.now(tz=pytz.timezone('Asia/Kolkata'))
print(dt2_ind.strftime('%B %d, %Y'))

# Convert String into datetime
dt_str = "July 26, 2020"
dt5 = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt5)


# List of Timezone in Pytz
# for tz in pytz.all_timezones:
#     print(tz)