from typing import List, Set, Dict, Tuple, Optional
class Solution:
    """
    >>> s = Solution()
    >>> nums = [-1, 0, 1, 2, -1, -4]
    >>> s.threeSum(nums)
    [[-1, -1, 2], [-1, 0, 1]]
    >>> s = Solution()
    >>> nums = []
    >>> s.threeSum(nums)
    []
    >>> s = Solution()
    >>> nums = [0]
    >>> s.threeSum(nums)
    []
    """
    def __init__(self):
        self.threeSum = self.threeSum
    def threeSumBF(self, nums: List[int]) -> List[List[int]]:
        """ Brute-force solution
        Theta(n^3) => time limit exceeded while being submitted
        """
        result = []
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp = sorted([nums[i], nums[j], nums[k]])
                        if temp not in result:
                            result.append(temp)
        return result

    def threeSumImpBF(self, nums: List[int]) -> List[List[int]]:
        """ Do early stopping at the last loop
	O(n^3) => still time limit exceeded
        """
        result = []
        known_pairs = set() # a set of tuples
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                for k in range(j+1, length):
                    if (nums[i], nums[j]) in known_pairs:
                        continue
                    if nums[i] + nums[j] + nums[k] == 0:
                        known_pairs.update({
                            (nums[i], nums[j]), (nums[j], nums[i]),
                            (nums[i], nums[k]), (nums[k], nums[i]),
                            (nums[j], nums[k]), (nums[k], nums[j])
                            })

                        result.append([nums[i], nums[j], nums[k]])
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """ Improved Solution after checking the hint 1 and 2
        O(n^2*log(n))
        """
        result = []
        nums.sort() # O(nlog(n))
        seen_firsts = set()
        length = len(nums)
        for i in range(length):
            first = nums[i]
            if first in seen_firsts:
                continue
            seen_firsts.add(first)
            seen_seconds = set()
            for j in range(i+1, length):
                second = nums[j]
                if second in seen_seconds:
                    continue
                seen_seconds.add(second)
                target = -first -second
                try:
                    target_idx = j+1 + nums[j+1:].index(target)
                    temp = [first, second, nums[target_idx]]
                    if temp not in result:
                        result.append(temp)
                except:
                    pass
        return result

if __name__ == '__main__':
    s = Solution()
    r = s.threeSum([-1, 0, 1, 2, -1, -4])
    import pdb; pdb.set_trace()
