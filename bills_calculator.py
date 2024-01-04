print("welcome to the top calculator")
total_bill = input("What was the total bill? $")
percentage_tip = input("What percentage tip would you like to give? 10, 12, or 15? ")
people = input("How many peaple to split the bill? ")

print(
    f"Each person shold pay: ${round((float(total_bill)*(1+(int(percentage_tip)/100)))/int(people),2)}"
)
