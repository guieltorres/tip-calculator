print("Welcome to the tip calculator")
bill = float(input("What was the total bill? "))
tip = float(input("What percentage tip you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

bill_with_tip = (tip / 100 * bill + bill) / 5

print("%.2f" % bill_with_tip)


