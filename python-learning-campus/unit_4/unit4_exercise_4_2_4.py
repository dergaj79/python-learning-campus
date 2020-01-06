# 4.2.4 - this excerise will get date from a user and print the day of the week to enter date value:
# Python3 program to find day 
# of a given date 
import datetime 
import calendar 


def findDay(number_of_day_of_week): 
    number_of_day_of_week = datetime.datetime.strptime(number_of_day_of_week, '%d/%m/%Y').weekday()
    return (calendar.day_name[number_of_day_of_week])
  
# Driver program 
input_date = input ("Please enter a date in the following format'dd/mm/yyyy':")

print("Day Name: ",findDay(input_date))
print (calendar.day_name[0])
print (calendar.day_name[1])
print (calendar.day_name[2])
print (calendar.day_name[3])
print (calendar.day_name[4])
print (calendar.day_name[5])
print (calendar.day_name[6])
print (calendar.month_name[6])
print (calendar.month_abbr[6])



