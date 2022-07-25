class Solution:

    def isIdealPermutation(self, nums: List[int]) -> bool:
        """ an O(n^2) solution
        based on insertion sort to ensure shorter runtime for almost sorted
        array (ideal permutations)
        added early-stop mechanism for non-ideal permutations

        runtime is faster than 30 ~ 50% of online submissions
        memory usage less than 100% of online submissions
        """

        # count consecutive adjacent swaps during the insertion sort
        adj_swap = 0
    
        for i in range(len(nums)):
            j = i
            while j > 0:
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    if j == i:
                        adj_swap += 1

                    if adj_swap > 1 or i-j > 0:
                        return False

                    j-=1
                    
                else:
                    if j == i:
                        adj_swap = 0
                    break
                    
        return True

    def isIdealPermutation3(self, nums: List[int]) -> bool:
        """an O(n^2) solution
        discarded the variables explicitly count inversions
        added early-stop mechanism for negatives
        exceeded the time limit at the 161 test case
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] > nums[j]:
                    if i != j-1:
                        return False

        return True

    def isIdealPermutation2(self, nums: List[int]) -> bool:
        """a Theta(n^2) solution
        to update local and global inversions in the same loop
        no swaps of the insertion sort are conducted
        exceeded the time limit at the 156 test case
        """

        local_inversions = 0
        global_inversions = 0
        
        for i in range(len(nums)):
            j = i
            while j > 0:
                if nums[i] < nums[j-1]:
                    if j == i:
                        local_inversions += 1
                    global_inversions += 1
                j -= 1
        return local_inversions == global_inversions

    def isIdealPermutation1(self, nums: List[int]) -> bool:
        """an O(n^2) solution 
        exceeded the time limit at the 155 test case"""
        """
        local_inversions = 0
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                local_inversions += 1
        
        global_inversions = 0
        
        for i in range(len(nums)):
            j = i
            while j > 0:
                if nums[j] < nums[j-1]:
                    nums[j], nums[j-1] = nums[j-1], nums[j]
                    j-=1
                    global_inversions+=1
                else:
                    break
        return local_inversions == global_inversions
       
