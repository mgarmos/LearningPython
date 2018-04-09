import time
import datetime

print ("Time in seconds since the epoch: %s" %time.time()) 
localtime = time.localtime(time.time())
print ("Local current time :", localtime)


                            
print ("Current date and time: " , datetime.datetime.now())
print ("Or like this: " ,datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))                                                                                       
print ("Current year: ", datetime.date.today().strftime("%Y"))
print ("Month of year: ", datetime.date.today().strftime("%B"))
print ("Week number of the year: ", datetime.date.today().strftime("%W"))
print ("Weekday of the week: ", datetime.date.today().strftime("%w"))
print ("Day of year: ", datetime.date.today().strftime("%j"))
print ("Day of the month : ", datetime.date.today().strftime("%d"))
print ("Day of week: ", datetime.date.today().strftime("%A"))
                                                                                       

# from datetime import datetime
# print("now: ", datetime.now()) 
name = input('Please, insert your name: ')
age = int(input('Please, insert your age: '))


actualYear = datetime.now().year

anio100 = actualYear + 100 - age

print(type(datetime.now()))
print(actualYear)
print(name)
print(anio100);
print("nowAgain: ", datetime.now()) 
