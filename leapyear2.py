year = int(input("Enter the year to check wheather it is leap year or not : "))

if ((year%400 ==0) or (year%100!= 0) and (year % 4 == 0)):
    print(f"{year} is a leap year")
    
else:
    print(f"{year} is not a leap year")