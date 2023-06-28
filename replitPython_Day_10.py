print("This is a bill share calculator!")

myBill = float(input("What was the bill?: "))
numberOfPeople = int(input("How many people?: "))
tipPercentage = float(input("How much tip do you want to give? (whole numbers only)"))
totalBill = myBill*(1+(tipPercentage/100))
answer = round(totalBill / numberOfPeople,2)
print("Total Bill is",totalBill,"You all owe", answer)