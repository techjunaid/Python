j = input("Enter your name ::")
i = input("enter her name ::")
j1 = j.lower()
#print(j1)
i1 = i.lower()

if (j !="junaid" and i !="ifra"):
    T = j1.count("t")
    R = j1.count("r")
    U = j1.count("u")
    E = j1.count("e")

    L = i1.count("l")
    O = i1.count("o")
    V = i1.count("v")
    E = i1.count("e")

    true = T+R+U+E
    love = L+O+V+E
    sum = true+love
    result = 100-sum
    print(f"your love percentage is",result,"%")
else:
    print("your love is True love with 99%")

