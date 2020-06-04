for i in range(5):
    for j in range(5-i-1):
        print(' ',end=' ')
    for j in range(i+1):
        print('*', end=' ')
    print()
for i in range(4,0,-1):
    for j in range(4-i+1):
        print(' ',end=' ')
    for j in range(i):

        print('*', end=' ')
    print()


    for i in range(3):
    print('@',end=' ')
print()
for i in range(5):
    for j in range(5):
        if (i==1 and (j==1 or j==2 or j==3)) or (i==2 and (j>=0 or j<=4)) or (i==0 and j==2 ) or (j==2 and (i>2 or i<5)):

            print('*',end='')

        else:
            print(end=' ')
    print()


for i in range(0,10,2):
    for j in range(10-i):
        print(end=' ')
    for j in range(i+1):
        print('*',end= ' ')
    print()



'''

        *
      *
     *
      *
        *
'''

j=5
for i in range(1,5):
    print(' '*j+1*'*')
    j-=1
for i in range(5):
    print(' '*i,'*')