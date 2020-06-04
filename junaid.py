## code for J
for i in range(4):
    for j in range (3):
        if j==1 or (i==0 and j!=1) or (i==3 and (j<1)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
print()
##code for U
for i in range(4):
    for j in range (3):
        if j==0 or j==2 or ((j==1 ) and (i==3)):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
print()
## code for N
for i in range(3):
    for j in range (3):
        if j==0 or j==2 or (i==1 and j==1) :
            print('*',end=' ')
        else:
            print(end='  ')
    print()
print()
## code for A

for i in range(4):
    for j in range(3):
        if ((j == 0 or j == 2) and (i == 1 or i == 2 or i == 3)) or (j == 1 and (i == 0 or i == 2)):
            print('*', end=' ')
        else:
            print(end='  ')
    print()
print()
##code for I
for i in range (4):
    for j in range(3):
        if j==1 or (i==0 and j!=1  ) or (i==3 and j!=1):
            print('*',end=' ')
        else:
            print(end='  ')
    print()
print()

## code for D

for i in range(4):
    for j in range(4):
        if j==0 or ((j==1 ) and(i==0 or i==3)) or (j==2 and (i==1 or i==2)):
            print('*', end=' ')
        else:
            print(end='  ')
    print()
print()