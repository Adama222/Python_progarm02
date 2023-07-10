import time
pre_Y = int(time.strftime("%Y"))
bir_Y = int(input("Enter the birth year:"))
age = pre_Y - bir_Y
print("Your age is ", age)
print("Total days is ", age * 365)

import time
day = int(input("Enter your date:"))
month = int(input("Enter your month: "))
year = int(input("Enter the year:"))
print(f"Previous date in DD/MM/YYY is {day-1}/{month}/{year}")

import random
for i in range(0, 4):
    print(random.randrange(1, 50), end = "")