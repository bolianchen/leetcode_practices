class Solution:
    def search(self, nums, target):
        """
        O(log n)
	>>> nums = [-1, 0, 3, 5, 9, 12]
	>>> target = 9
        >>> s = Solution()
	>>> s.search(nums, target)
        4
	>>> nums = [-1, 0, 3, 5, 9, 12]
	>>> target = 2
        >>> s = Solution()
	>>> s.search(nums, target)
        -1
        """
        start, end = 0, len(nums)-1

        while start <= end:
            i = start + (end - start)//2
            if nums[i] == target:
                return i
            elif nums[i] > target:
                end = i-1
            else:
                start=i+1
        return -1

        

if __name__ == '__main__':
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    s = Solution()
    r = s.search(nums, target)
