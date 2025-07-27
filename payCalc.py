# Gross income calculator for Store Assistant at ALDI #

# rates 
baseRate = 30.21
weekdayAfter6PM = 37
before7AM = 43.78
satBase = 37
sunBase = 43.78
sunBefore9AM = 57.36
pubHoliday = 64.15

asciiArt = r"""


      _      _____    ______  _____   _______                   ______       __                __        _                 
     / \    |_   _|  |_   _ `|_   _| |_   __ \                .' ___  |     [  |              [  |      / |_               
    / _ \     | |      | | `. \| |     | |__) ,--.   _   __  / .'   \_|,--.  | | .---. __   _  | | ,--.`| |-'.--.  _ .--.  
   / ___ \    | |   _  | |  | || |     |  ___`'_\ : [ \ [  ] | |      `'_\ : | |/ /'`\[  | | | | |`'_\ :| |/ .'`\ [ `/'`\] 
 _/ /   \ \_ _| |__/ |_| |_.' _| |_   _| |_  // | |, \ '/ /  \ `.___.'// | |,| || \__. | \_/ |,| |// | || || \__. || |     
|____| |____|________|______.|_____| |_____| \'-;__[\_:  /    `.____ .\'-;__[___'.___.''.__.'_[___\'-;__\__/'.__.'[___]    
                                                    \__.'                                                                  


"""
print(asciiArt)
print("NOTE: This calculator is for Store Assistants at ALDI Australia. Rates are set to Store Assistant rates and any calculations are based on those rates.")
print("If asked for any unit relating to time, format hours into decimals to the closest quarter of an hour. e.g. 5hrs45mins = 5.75hrs")
print("Input parameters can't do addition, please input the amount of hours using one number.")
print("")

# Weekdays 7am to 6pm
print("How many hours of work are rostered for weekdays after 7am & before 6pm?")
param1 = input()
# 6am starts on Weekdays & Saturdays
print("How many hours on weekdays or Saturdays, are rostered for a 6am start?")
param2 = input()
# Weekdays 6pm or later
print("On weekdays, how many hours are rostered for after 6pm?")
param3 = input()
# Saturday after 7am
print("How many hours are rostered on for Saturdays after 7am?")
param4 = input()
# Sunday after 9am
print("How many hours after 9am are rostered for Sundays?")
param5 = input()
# Sunday before 9am
print("How many hours before 9am are rostered for Sundays?")
param6 = input()

#Conversions code from str to float
float1 = float(param1)
float2 = float(param2)
float3 = float(param3)
float4 = float(param4)
float5 = float(param5)
float6 = float(param6)

def taxCalculation(grossIncome):
    annualIncome = grossIncome * 26
    taxable = max(0, annualIncome - 18200)  # Ensures no negative tax
    annualTax = taxable * 0.16

    medicareLevy = annualIncome * 0.02
    totalTax = annualTax + medicareLevy

    fortnightlyWitholding = round(totalTax / 26, 2)
    netIncome = round(grossIncome - fortnightlyWitholding, 2)

    taxPrompt = "Tax Estimate ≈ $" + str(fortnightlyWitholding)
    netIncomePrompt = "Net Income ≈ $" + str(netIncome)

    print(taxPrompt)
    print(netIncomePrompt)


# Total time rostered
totalHours = (float1 + float2 + float3 + float4 + float5 + float6)
strTotalHours = str(totalHours)
print("")
print("Total amount of hours rostered is "+ (strTotalHours) + ("hrs"))

calc1 = baseRate * float1
calc2 = before7AM * float2
calc3 = weekdayAfter6PM * float3
calc4 = satBase * float4
calc5 = sunBase * float5
calc6 = sunBefore9AM *float6

grossIncome = calc1 + calc2 + calc3 + calc4 + calc5 + calc6
floGrossIncome = float(grossIncome)
forcedFormat = f"{floGrossIncome:.2f}"
final = str(forcedFormat)
print("Estimated Gross Income ≈ $" + final)
print("")
taxCalculation(grossIncome)
input("Press Enter to exit...")

# End of payCalc.py