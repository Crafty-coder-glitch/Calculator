def add(x,y):
    return x+y
def subtract(x,y):
    return x-y
def multiply(x,y):
    return x*y
def divide(x,y):
    return x/y
print("please choose your operation\n")
print("1.add\n 2.subtract\n 3.multiply\n 4. divide\n")
op=int(input("select from the above choice,use numbers:")) 
x=float(input("enter first number:"))
y=float(input("enter second number:"))
if op == 1:
    print(add(x,y))
elif op == 2:
    print(subtract(x,y))
elif op == 3:
    print(multiply(x,y))
elif op == 4:
    print(divide(x,y))
else:
    print("invalid input")