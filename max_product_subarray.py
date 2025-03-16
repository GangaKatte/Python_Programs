nums=[4,3,5,-2,4,9,2]
max_product=nums[0]
current_product=nums[0]

for i in range(1,len(nums)):
    current_product=max(nums[i],current_product*nums[i])
    max_product=max(max_product,current_product)

print(max_product)    