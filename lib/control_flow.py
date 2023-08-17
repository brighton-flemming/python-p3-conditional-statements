#!/usr/bin/env python3

def admin_login(username, password):
   if (username == "admin" or username =="ADMIN") and (password == "12345" or password == "123456") :
       return 'Access granted'
   else :
       return 'Access denied'
      
admin_login("sudo", "12345")
admin_login("admin", "123456")
admin_login("ADMIN", "12345")     


def hows_the_weather(temperature):
  if temperature < 40 :
      return "It's brisk out there!"
  elif (temperature > 40) and (temperature < 65):
       return "It's a little chilly out there!"
  elif temperature > 85 :
      return "It's too dang hot out there!"
  else:
      return "It's perfect out there!"
  
hows_the_weather(56)
hows_the_weather(90)
hows_the_weather(36)



def fizzbuzz(num):
   if (num % 3 == 0) and (num % 5 == 0): 
        return "FizzBuzz"
   elif (num % 3 == 0):
       return "Fizz"
   elif (num % 5 == 0): 
        return "Buzz"
   else:
       return num
   
fizzbuzz(0)
fizzbuzz(15)
fizzbuzz(45)


def calculator(operation, num1, num2):
    # your code here
    pass
