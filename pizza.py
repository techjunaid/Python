bill = 0

print(" Small Pizza : $15 \n Medium Pizza : $20 \n Large Pizza : $25")
order = input("What size of pizza do you want 'S' 'M' 'L' :: ")
pepperoni = input("Do you want pepperoni, \n It costs $2 for small pizzas and $3 for medium and large pizzas Y or N? :: ")
extra_cheese = input("Do you want extra cheese \n It costs $1 extra charge\n Y or N :: ")

if order == "S":
    bill += 15
    
elif order == "M":
    bill += 20
    
    
elif order == "L":
    bill += 25
   


if pepperoni=="Y":
   if order == "S":
       bill +=2
   else:
        bill +=3
        
if extra_cheese =="Y":
    bill+=1
    
print(f" Your final bill is {bill}")
       
    
    

 
    
    

