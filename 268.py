def missingNumber(nums):
    nums.sort()
    prev = nums[0]
    
    for index, _ in enumerate(nums, 1):
        if nums[index] > prev:
            if nums[index] - prev == 1:
                prev = nums[index]
            else:
                return prev + 1
        else:
            prev = nums[index]

print(missingNumber([9,6,4,2,3,5,7,0,1]))
