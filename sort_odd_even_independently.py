
nums=[36,45,32,31,15,41,9,46,36,6,15,16,33,26,27,31,44,34]
eve=sorted(nums[0::2])
odd=sorted(nums[1::2],reverse=True)
for i in range(len(nums)):
    if i%2==0:
        nums[i]=eve.pop(0)
        continue
    nums[i]=odd.pop(0)
        
print(nums)

