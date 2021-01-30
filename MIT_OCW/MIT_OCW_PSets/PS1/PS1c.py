#Promblem set 1a
annual_salary           = 150000
portion_saved           = 0
total_cost              = 1000000
semi_annual_raise       = .07
portion_down_payment    = total_cost*.25
current_savings         = 0
saving_time             = 0
raise_time              = 0
bi_steps                = 0


epsilon                 = 100
low                     = 0
high                    = 10000
guess                   = (high + low)//2

while abs(current_savings - portion_down_payment) >= epsilon:
   rate = guess/10000
   for_annual_salary = annual_salary
   current_savings = 0
   for month in range(36):
       if month % 6 == 0 and month > 0:
           for_annual_salary += for_annual_salary*semi_annual_raise
       monthly_salary = for_annual_salary/12
       current_savings = monthly_salary * rate + current_savings*.4/12
       
   
   if current_savings < portion_down_payment:
       low = guess
   else:
       high = guess
       
   guess = (high + low)//2    
   bi_steps += 1
   
   if bi_steps > 13:
       break

   # if raise_time == 6:
#       print("Salary before Raise:", annual_salary)
       # annual_salary += annual_salary*semi_annual_raise
#       print("Salary after Raise:", annual_salary)
       # raise_time = 0
#   else:
#       raise_time += 1
#       print("Raise time:", raise_time)
if bi_steps > 13:
    print("it is not possible to pay the down payment in three years.")
else:        
    print("Best Saving Rate:", rate)
    print("Steps in bisection:", bi_steps)
