from ascii import *
from rates import *

asciiArt()
#Inintial start prompt
print("NOTE: This calculator is for Store Assistants at ALDI Australia. Rates are set to Store Assistant rates and any calculations are based on those rates.\n" \
"If asked for any unit relating to time, format hours into decimals to the closest quarter of an hour. e.g. 5hrs45mins = 5.75hrs\n"
"Input parameters can't do addition, please input the amount of hours using one number.")
print("")

#These 6 questions are used to calculate the hours worked in different time slots.
questions = [
    "How many hours of work are rostered for weekdays after 7am & before 6pm?",
    "How many hours on weekdays or Saturdays, are rostered for a 6am start?",
    "On weekdays, how many hours are rostered for after 6pm?",
    "How many hours are rostered on for Saturdays after 7am?",
    "How many hours after 9am are rostered for Sundays?",
    "How many hours before 9am are rostered for Sundays?"
]

#Adds the users input to the list.
hours = []
for question in questions:
    while True:
        print(question)
        user_input = input()
        if user_input.strip() == "":
            print("Input cannot be empty. Please enter a number.")
            continue
        try:
            hours.append(float(user_input))
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")    

hours1 = hours[0]
hours2 = hours[1] 
hours3 = hours[2] 
hours4 = hours[3]  
hours5 = hours[4]  
hours6 = hours[5]

calc1 = baseRate * hours1
calc2 = before7AM * hours2
calc3 = weekdayAfter6PM * hours3
calc4 = satBase * hours4
calc5 = sunBase * hours5
calc6 = sunBefore9AM * hours6

# Function "Hours" calculates the toal number of hours worked and prints it.
def Hours():
    totalHours = (hours1 + hours2 + hours3 + hours4 + hours5 + hours6)
    strTotalHours = str(totalHours)
    print("")
    print("Total amount of hours rostered is "+ (strTotalHours) + ("hrs"))
    print("")

# Function "GrossIncome" calculates the total gross income from the hours worked and the corresponding rates.
def GrossIncome():
    strGrossIncome = calc1 + calc2 + calc3 + calc4 + calc5 + calc6
    floGrossIncome = float(strGrossIncome)
    roundingGrossIncome = f"{floGrossIncome:.2f}"
    final = str(roundingGrossIncome)
    print("Estimated Gross Income ≈ $" + final)
    return floGrossIncome

# Function "Taxcalculation" uses static tax rates and the medicare levy to rougly calculate the tax on the gross income.
# Results from this function and what you see on your pay slip may differ due to other factors, however this is the best estimate possible.
def TaxCalculation(grossIncome):
    projectedAnnualIncome = grossIncome * 26
    taxableIncome = max(0, projectedAnnualIncome - 18200)  # Ensures no negative tax
    annualTax = taxableIncome * 0.16

    medicareLevy = projectedAnnualIncome * 0.02
    totalTax = annualTax + medicareLevy

    fortnightlyTax = round(totalTax / 26, 2)
    netIncome = round(grossIncome - fortnightlyTax, 2)

    taxPrompt = "Tax Estimate ≈ $" + str(fortnightlyTax)
    netIncomePrompt = "Net Income ≈ $" + str(netIncome)

    print(taxPrompt)
    print(netIncomePrompt)
    input("Press Enter to quit the program...")

Hours()
calculationPassing = GrossIncome()
TaxCalculation(calculationPassing)

# End of main.py