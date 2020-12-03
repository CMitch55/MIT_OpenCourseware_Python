# -*- coding: utf-8 -*-
"""
Created on Fri Oct 30 13:56:58 2020

@author: Nygel
"""
annual_salary        = int(input("Enter your annual salary:"))
total_cost           = 1000000
portion_down_payment = total_cost * .25
guess_rate           = 0
raise_rate           = .07
annual_return        = .04
current_savings      = 0
bi_searches          = 0
steps                = 0
monthly_salary       = 0

high                 = 10000
low                  = 0
epsilon              = 100
guess                = (high + low)//2

while abs(current_savings - portion_down_payment) >= epsilon:
    current_savings = 0
    guess_rate = guess/10000
    for_annual_salary = annual_salary
    
    for month in range(36):
        if month % 6 == 0 and month > 0:
            for_annual_salary += for_annual_salary*raise_rate
        monthly_salary = for_annual_salary / 12
        current_savings += current_savings * annual_return/12 + monthly_salary*guess_rate
        
    if current_savings < portion_down_payment:
        low = guess
    else:
        high = guess
        
    guess = (high + low)//2
    steps += 1
    
    if steps > 13:
        break
    
if steps > 13:
    print("It is not possible to save for down payment in 36 months.")
else:
    print("Here is your saving rate:", guess_rate)
    print("It took this many steps to complete:", steps)