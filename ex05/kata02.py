import datetime

t = (3,30,2019,9,25)
time = datetime.time(t[0], t[1])
d = datetime.date(t[2], t[3], t[4])
print (d.strftime("%m/%d/%Y"), time.strftime("%H:%M"))
