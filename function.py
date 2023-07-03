# def add(*argv):
#     sum =0
#     for i in argv:
#         sum += i
#     return sum

# print("Sum is : ",add(10,20))


# # Recursion is faster than loop
# def sum(n):
#     if n == 0:
#         return 0
#     return n + sum(n-1) # Function Call

# print("Sum of 1 to 10 is : ",sum(10))

add = lambda a,b : a+b   
print("Addition is : ",add(5,8))