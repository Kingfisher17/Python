a = int(input("Enter 1st No : "))
b = int(input("Enter 2nd No : "))

def arith (a,b):
    return a+b , a-b, a*b, a/b

add , sub, mul,div = arith(a,b)

print("Addition is : ",add)
print("Subtraction is : ",sub)
print("Multiplication is : ",mul)
print("division is : ",div)

