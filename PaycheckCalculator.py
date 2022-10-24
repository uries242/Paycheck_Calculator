#! /usr/local/bin/python3
from curses.ascii import isalpha, isdigit
from time import sleep

print("Hi! Welcome to The Paycheck Calculator!")

sleep(2)

def payCheckCalculator():
    while True:
      employee_name = str(input("Enter Employee First and Last Name: "))
      if employee_name.isdigit():
          print("Letters only; try again")
          continue
      else:
          print("Awesome! Let\'s Calculate!")
          break

    while True: 
        try:
            hourly_rate = float(input("What is the Hourly Rate: $"))
        except ValueError:
            print("Invalid input; enter numerical values only")
            continue                   
        try:
            hours_worked = float(input("Enter the Total Hours Worked: "))
        except ValueError:
            print("Invalid input; enter numerical values only")
            continue
        else:
            break

    print("Thank you for your input. Here\'s your Paycheck information:")
    sleep(2)

#Calculate Regular Pay
    def regular_pay():
        regPayCalc = (hourly_rate * 40)
        return regPayCalc
    regPayCalc = regular_pay()  
    print(f"Regular Pay is ${regular_pay():,.2f}")

# #Calculate Overtime Pay
    def overtime_pay():
        if hours_worked > 40:
            otCalc = ((hours_worked - 40) * (1.5 * hourly_rate))
        elif hours_worked <= 40:
            otCalc = (hours_worked * hourly_rate)
        return otCalc
    print(f"Overtime Pay is ${overtime_pay():,.2f}")

# #Calculate Gross Pay  
    def gross_pay():
        gpCalc = (regular_pay() + overtime_pay())  
        return gpCalc
    gpCalc = gross_pay()  
    print(f"Gross Pay is ${gross_pay():,.2f}")

# #Calculate Taxes
    def fed_tax():
        fedTaxCalc = .15 * gpCalc
        return fedTaxCalc  
    print(f"Federal Tax is ${fed_tax():,.2f}")

# Calculate State Taxes
    def state_tax():
        stateTaxCalc = .10 * gpCalc
        return stateTaxCalc
    stateTaxCalc = state_tax()
    print(f"State Tax is ${state_tax():,.2f}")

    def fica_tax():
        ficaTaxCalc = .02 * gpCalc
        return ficaTaxCalc
    ficaTaxCalc = fica_tax()
    print(f"FICA Tax is ${fica_tax():,.2f}")

# #Calculate Net Pay
    def net_pay():
        npCalc = (gross_pay() - fed_tax() - state_tax() - fica_tax())
        return npCalc  
    print(f"Net Pay is ${net_pay():,.2f}")

print("")
sleep(2)

# Next Emloyee loop
while True:
    try:
        nextEmployeeCheck = str(input('Would you like to calculate for another employee? Press Enter key or "n" to quit. '))
    except ValueError:
        if nextEmployeeCheck.isdigit():
         print("Invalid input, enter 'y' or 'n'")
        continue
    if nextEmployeeCheck == "n":
        print("Pleasure to help, Goodbye!")
        break
    else:
        payCheckCalculator()

        