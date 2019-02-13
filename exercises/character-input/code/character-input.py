#!/usr/bin/python
import datetime
age = input("Hi There!! Enter your age : ")
age = int(age)
yearsToHunderd = 100 - age
currentYear = datetime.datetime.now()
centuryYear = currentYear.year + yearsToHunderd
print("You will be 100 years old in Year :{:d} ".format(centuryYear))

