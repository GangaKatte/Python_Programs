# nums = [1, 2, 3, 4, 1, 5]
# found = False
# k = 2

# for i in range(len(nums)):
#     for j in range(i + 1, len(nums)):  # Compare nums[i] with nums[j]
#         if nums[i] == nums[j] and abs(i - j) <= k:  # Check for duplicate and valid distance
#             found = True
#             print("true")  # Print true when found
#             break  # Exit the inner loop when duplicate is found
#     if found:
#         break  # Exit the outer loop once we have found a valid duplicate

# if not found:  # If no valid duplicates found, print false
#     print("false")


#way2

nums = [1, 2, 3, 4, 1, 5]
found = False
index_map={}
k = 2

for i,v in enumerate(nums):
    if v in index_map and abs(i-index_map[v]) <=k:
        found = True
        print ("true")
        break
    index_map[v]=i
else:
    print("false")        


    