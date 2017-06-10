from datetime import datetime, timedelta
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU')

date = datetime.now()
delta = timedelta(days=1)
#print(date-delta)

st_time = datetime.now()
time = st_time.strftime('%A %d %B %Y')
#print(time)

st_time2 = "01/01/17 12:10:03.234567"
time2 = datetime.strptime(st_time2, '%m/%d/%y %H:%M:%S.%f')
time2 = time2.strftime('%A %d %B %Y')
print(time2)