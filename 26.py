# Remove Duplicates from Sorted Array(L26)

def removeDuplicates(nums):
    i, j = 0, 0

    while j < len(nums):

        if nums[i] != nums[j]:
            # Copy j to i + 1
            # print("Swap count ", i+1)
            i += 1
            nums[i] = nums[j]        
        j += 1
        # print("i j")
        # print(i, j, nums)
        # print("==================================")

    
    return nums[:i + 1]

print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 6, 5]))
# print(removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4]))
