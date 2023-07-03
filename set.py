# a = {10,20,30,40,50,10,10,20}
# b = {10,20,40,50}

# print("A : ",a)
# print(a.intersection(b))

# a = {'a','b','c','a'}

# for i in a:
#     print(i)

s = {10,20,30,40,50,60}
b = {40,10,50,60}
# b.difference_update(s)

print("A : ",s)
print("B : ",b)
# print("Diff : ",b.difference(s))

if(s.issuperset(b)):
    print("YES")
else:
    print("NO")

