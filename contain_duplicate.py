nums=[1,2,3,4,7,8,9,7,6,3]

#way1
# found=False

# for i in range (len(nums)):
#     for j in range(i+1,len(nums)):
#         if(nums[i]==nums[j]):
#            found=True
#            break
#     if found:
#         print("true")   
#         break
# else:
#      print("false")   
    
#way2

nums = [1, 2, 3, 4, 7]

index_map = {}  # To store the numbers we've already seen
founds = False   # To track if a duplicate is found

for i, v in enumerate(nums):
    if v in index_map:  # If the number has already been seen
        founds = True    # Mark that a duplicate is found
        print("true")    # Print "true" for the duplicate
        break            # Exit the loop as we found the duplicate

    index_map[v] = i  # Store the number and its index in the dictionary

# If no duplicate is found after the loop finishes, print "false"
else:
    print("false")
