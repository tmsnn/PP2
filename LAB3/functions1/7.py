def has_33(nums):
    for j in  range (len(nums) - 1): 
        if nums[j] == 3 and nums[j + 1] == 3:
            return True
    return False
    
nums = list(map(int, input().split()))
if (has_33(nums)):
    print("True")
else:
    print("False")
