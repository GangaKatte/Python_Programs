nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
current_sum=nums[0]
max_sum=nums[0]

for i in range (1,len(nums)):
    current_sum=max(nums[i],current_sum+nums[i])
    max_sum=max(max_sum,current_sum)
  

print(max_sum)    