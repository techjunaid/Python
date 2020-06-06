## Recursion function

'''def rec():
    print('hello')
    rec()
rec()'''

##factorial using recursion

def fact(n):

    if (n==0):
        return 1

    return n*fact(n-1)
n=int(input('enter the no you want factorial :; '))
result = fact(n)
print(result)