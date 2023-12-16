import datetime

day, month = input().split(' ')

days = datetime.datetime(2009, int(month), int(day))
print(days.strftime('%A'))