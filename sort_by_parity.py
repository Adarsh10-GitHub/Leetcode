
nums=[3,1,2,4]
eve=[]
odd=[]
res=[]
for i in nums:
    if i%2==0:
        eve.append(i)
    else:
        odd.append(i)
print(eve+odd)
