# Given an array of integers nums and an integer target, return indices of the
# two numbers such that they add up to target. You may assume that each input 
# would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.

class Solution:
    """
    >>> s = Solution()
    >>> s.twoSumV1([2, 7, 11, 15], 9)
    [0, 1]
    >>> s = Solution()
    >>> s.twoSumV1([3, 2, 4], 6)
    [1, 2]
    >>> s = Solution()
    >>> s.twoSumV1([3, 3], 6)
    [0, 1]
    """
    def twoSumV4(self, nums, target):
        """
        O(n)

        """
        table = {} # key: num; value: index
        i = 0
        for num in nums:
            # look up first, the case of two equal numbers can be found
            if table.get(target - num) is not None:
                return [i, table.get(target - num)]
            table[num] = i
            i = i + 1

    def twoSumV3(self, nums, target):
        """
        O(n)
        """
        table = {} # key: num; value: index
        for i, num in enumerate(nums):
            # look up first, the case of two equal numbers can be found
            if table.get(target - num) is not None:
                return [i, table.get(target - num)]
            table[num] = i

    def twoSumV2(self, nums, target):
        """
        A brute-force solution
        Its worst case happens when the two numers are at the last of the list
        (n-1) + (n-2) + ... + 1 = (n-1)*(n/2) ~ O(n^2)
        """
        for i, num1 in enumerate(nums):
            for j, num2 in enumerate(nums[i+1:]):
                if (num1 + num2) == target:
                    # invariants
                    # absolute index for j is i+1+j
                    return [i, i+1+j]

    def twoSumV1(self, nums, target):
        """
        Results: 
        """
        lookup_table = {}
        for idx, num in enumerate(nums):
            if lookup_table.get(num) is None:
                lookup_table[num] = idx
            # discard num after its value has become a list (not int) 
            elif isinstance( lookup_table.get(num), int):
                lookup_table[num] = [ lookup_table.get(num), idx ]
        
        for idx, num in enumerate(nums):
            new_target = target - num
            if new_target != num:
                if isinstance(lookup_table.get(new_target), int):
                    return [idx, lookup_table.get(new_target)]
                elif isinstance(lookup_table.get(new_target), list):
                    return [idx, lookup_table.get(new_target)[0]]
            else:
                if isinstance(lookup_table.get(new_target), list):
                    return [idx, lookup_table.get(new_target)[-1]]

