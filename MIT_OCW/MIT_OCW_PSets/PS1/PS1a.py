#Promblem set 1a
annual_salary           = float(input("Enter your annual salary: "))
portion_saved           = float(input("Enter the percent of your salary to save, as a decimal: "))
total_cost              = float(input("Enter the cost of your dream home: "))
portion_down_payment    = total_cost*.25
current_savings         = 0
saving_time             = 0

print("Enter your annual salary:", annual_salary)
print("Enter the percent of your salary to save, as a decimal:", portion_saved)
print("Enter the cost of your dream home:", total_cost)

while(current_savings < portion_down_payment):
    current_savings += current_savings*.04/12 + (annual_salary/12)*portion_saved
    saving_time += 1                                                            #Adds to the saving_time counter to calculate the number of months required to save up for the down payment.
    
    
print("Number of months:", saving_time)    
