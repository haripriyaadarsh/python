from datetime import datetime
timestamp=1294113662
date_time=datetime.fromtimestamp(timestamp)
d=date_time.strftime("%Y/%m/%d , %H:%M:%S")
print(d)