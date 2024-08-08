from datetime import datetime, date, timedelta

my_date = datetime(2024,8,6,9,12,00)
now = datetime.now()

print(now.strftime("%d %b %Y, %H:%M"))

date_input = input("Enter a date: ")

my_date = datetime.strptime(date_input,"%d/%m/%Y")

print(my_date.strftime("%d %B %Y"))

another_date = datetime(2024,8,6)

future_date = another_date + timedelta(days=7)

print(future_date.strftime("%d %B %Y"))



