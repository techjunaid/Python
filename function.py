def mj():
    print("hello mj")
mj()

def add (x,y):
    c= x+y
    print(c)
add(5,7)

def add (x,y):
    c=x+y
    return c
print(add(4,7))

def user (**data):
    for i,j in data.items():
        print(i,j)
user(name='junaid', age=19)

x=input('enter your name :')
y=int(input('enter your age: '))
z=int(input('enter your phone: '))
def det(**data):
    for i,j in data.items():
        print(i,j)
det(name=x,age=y,phone=z)