# num = input("Enter a Number : ")
# print("Reversed No is : ",int(num[::-1]))

num = int(input("Enter a Number : "))

rev = 0
while(num>0):
    rem = num%10
    rev = rev * 10 + rem
    num //= 10

print("Reversed Number is : ",rev)

