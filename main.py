from ascii import *
from rates import *

asciiArt()
print("NOTE: This calculator is for Store Assistants at ALDI Australia. Rates are set to Store Assistant rates and any calculations are based on those rates.\n" \
"If asked for any unit relating to time, format hours into decimals to the closest quarter of an hour. e.g. 5hrs45mins = 5.75hrs\n"
"Input parameters can't do addition, please input the amount of hours using one number.")
print("")

questions = [
    "How many hours of work are rostered for weekdays after 7am & before 6pm?",
    "How many hours on weekdays or Saturdays, are rostered for a 6am start?",
    "On weekdays, how many hours are rostered for after 6pm?",
    "How many hours are rostered on for Saturdays after 7am?",
    "How many hours after 9am are rostered for Sundays?",
    "How many hours before 9am are rostered for Sundays?"
]

hours = []
for question in questions:
    print(question)
    hours.append(float(input()))

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

def Hours():
    totalHours = (hours1 + hours2 + hours3 + hours4 + hours5 + hours6)
    strTotalHours = str(totalHours)
    print("")
    print("Total amount of hours rostered is "+ (strTotalHours) + ("hrs"))

def GrossIncome():
    strGrossIncome = calc1 + calc2 + calc3 + calc4 + calc5 + calc6
    floGrossIncome = float(strGrossIncome)
    roundingGrossIncome = f"{floGrossIncome:.2f}"
    final = str(roundingGrossIncome)
    print("Estimated Gross Income ≈ $" + final)
    print("")
    return floGrossIncome


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
    input("Press Enter to continue...")

Hours()
calculationPassing = GrossIncome()
TaxCalculation(calculationPassing)

# End of main.py