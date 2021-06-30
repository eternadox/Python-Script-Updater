import time

second = 1
minute = 60
hour = minute * 60
day = hour * 24
week = day * 7
month = day * 30
year = month * 12
decade = year * 10
century = decade * 10
millenium = century * 10
seconds = 0
try:
  while True:
    time.sleep(second)
    seconds = seconds + 1
    print(f"it has been {seconds} seconds since you started")
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
