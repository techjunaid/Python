
print("Welcome to the Tip calculator\n ")
Bill = float(input("what was the bill"))
print(" Your bill is generated and its cost is\n", Bill)

tip = int(input(print("How much percent tip you want to give 12%, 15% or 20%\n")))

tip2 = (Bill*tip)/100
Bill2 = Bill+tip2

split = int(input("In how many people to split the bill \n"))

result=Bill2/split

print(f" Each person should have {result} rupees")