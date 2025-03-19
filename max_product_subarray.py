nums=[4,3,5,-2,4,9,2]
max_product=nums[0]
current_product=nums[0]

for i in range(1,len(nums)):
    current_product=max(nums[i],current_product*nums[i])
    max_product=max(max_product,current_product)

print(max_product)    


#way2
class Solution(object):
    def maxProduct(self, nums):
        if not nums:
            return 0  # Edge case: empty array

        max_product_so_far = nums[0]
        min_product = nums[0]
        max_product = nums[0]

        for i in range(1, len(nums)):
            num = nums[i]

            if num < 0:  # Swap max and min when a negative number appears
                min_product, max_product = max_product, min_product

            max_product = max(num, max_product * num)
            min_product = min(num, min_product * num)

            max_product_so_far = max(max_product_so_far, max_product)

        return max_product_so_far
