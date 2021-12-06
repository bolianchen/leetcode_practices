# Given an integer array nums sorted in non-decreasing order, remove
# the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.
# 
# Since it is impossible to change the length of the array in some languages,
# you must instead have the result be placed in the first part of the array nums.
# More formally, if there are k elements after removing the duplicates, then 
# the first k elements of nums should hold the final result. It does not matter
# what you leave beyond the first k elements.
# 
# Return k after placing the final result in the first k slots of nums.
# 
# Do not allocate extra space for another array. You must do this by modifying 
# the input array in-place with O(1) extra memory.

class Solution:
    # size = 0
    # [0, 1, 1, 1, 2, 2]
    # [0, 1, 2] check 
    # size = 2
    # invariants
    # 1. prev_value = nums[size-1]
    # 2. if the current_value is the same with the prev_value, drop it
    #    otherwise, put nums[size] = current_value, size = size + 1
    # 3. results = nums[:size]
    def removeDuplicates(self, nums: List[int]) -> int:
        size = 1
        for num in nums[1:]:
            if num != nums[size - 1]:
                nums[size] = num
                size = size + 1
        return size
        
