## pass list to a function

def count(lst):
    even=0
    odd=0
    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return even,odd

lst = [2,33,45,66,77,89]
even,odd = count(lst)

print(even)
print(odd)
print("even: {} and odd : {}" .format(even,odd))

## fibonacci series

def fib(n):
    a=0
    b=1

    for i in range(n):
        print(a, end=' ')
        a,b=b,a+b

n = int(input(' enter the no of fib :'))
fib(n)

##factorial of a number
def fact (n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f
x=4
result = fact(x)
print(result)
