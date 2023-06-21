import datetime
from datetime import date
current_time=datetime.datetime.now()
print("a.current date and time : ",current_time)
today=date.today()
print("b.current year : ",today.year)
print("c.current month : ",today.month)
print("d.week number of year : ",datetime.date(2023,3,28).isocalendar()[1])
print("e.week day of the week : ",current_time.isoweekday())
print("f.day of year : ",datetime.date(2023,3,28).day)
print("g.day of month : ",today.day)
print("h.day of week : ",current_time.strftime('%A'))