stringHours = input("Enter hours: ")
stringRate = input("Enter rate: ")
floatHours = float(stringHours)
floatRate = float(stringRate)

if floatHours > 40:
    print("\nOvertime")
    regPay = floatRate * floatHours
    otPay = (floatHours - 40.0) * (floatRate * 0.5)
    print("Your regular pay is", regPay, "and your overtime pay is", otPay)
    wage = regPay + otPay
else:
    print("\nRegular")
    wage = floatHours * floatRate
print("Your total wage is", wage)
