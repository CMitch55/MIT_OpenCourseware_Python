#Promblem set 1a
annual_salary           = float(input("Enter your annual salary: "))
portion_saved           = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost              = float(input("Enter the cost of your dream home: "))
semi_annual_raise       = float(input("Enter the semi annual raise, as a decimal: "))
portion_down_payment    = total_cost*.25
current_savings         = 0
saving_time             = 0
raise_time              = 0

print("Enter your annual salary:", annual_salary)
print("Enter the percent of your salary to save, as a decimal:", portion_saved)
print("Enter the cost of your dream home:", total_cost)
print("Enter the semi annual raise, as a decimal:", semi_annual_raise)

while(current_savings < portion_down_payment):
    current_savings += current_savings*.04/12 + (annual_salary/12)*portion_saved
    saving_time += 1
    raise_time  += 1

    if raise_time == 6:
#        print("Salary before Raise:", annual_salary)
        annual_salary += annual_salary*semi_annual_raise
#        print("Salary after Raise:", annual_salary)
        raise_time = 0
#    else:
#        raise_time += 1
#        print("Raise time:", raise_time)
        
print("Number of months:", saving_time)    
