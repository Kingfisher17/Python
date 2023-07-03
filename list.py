# l = [i for i in range(1,11)]

# print(l)

# for i in l:
#     print(i,", ",end="",sep="")
# print()

# for i in range(len(l)-1):
#     print(l[i],", ",end="",sep="")

# print(l[len(l)-1])
    
n = int(input("How many elemets you wants to enter : "))

l = list()

for i in range(n):
    x = int(input())
    l.append(x)

print("l : ",l)

