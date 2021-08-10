nums = [0,0,1,1,1,2,2,3,3,4]


i = 0
check = 0
while i < len(nums):
    
    try:
     if nums[i] == nums[i + 1]:
        ii = i + 1
        while ii < len(nums):
            
            try:
             nums[ii] = nums[ii + 1]
            except:
             pass
            ii += 1
        i -= 1
    except:
        pass
    i += 1
    check += 1

    if check > i + 3:
        check = i
        i += 1

print(nums)