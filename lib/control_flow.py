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
    # your code here
    pass

def fizzbuzz(num):
    # your code here
    pass

def calculator(operation, num1, num2):
    # your code here
    pass
