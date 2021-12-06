# You are given two integer arrays nums1 and nums2, sorted in non-decreasing
# order, and two integers m and n, representing the number of elements in nums1
# and nums2 respectively.
# 
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# 
# The final sorted array should not be returned by the function, but instead be
# stored inside the array nums1. To accommodate this, nums1 has a length of
# m + n, where the first m elements denote the elements that should be merged,
# and the last n elements are set to 0 and should be ignored. nums2 has a length
# of n.

class Solution:
    """
    >>> s = Solution()
    >>> num1 = [1, 2, 3, 0, 0]
    >>> num2 = [2, 2]
    >>> s.merge(num1, 3, num2, 2)
    >>> num1
    [1, 2, 2, 2, 3]
    >>> s = Solution()
    >>> num1 = [1, 2, 3, 9, 0, 0, 0, 0]
    >>> num2 = [2, 2, 10, 20]
    >>> s.merge(num1, 4, num2, 4)
    >>> num1
    [1, 2, 2, 2, 3, 9, 10, 20]
    >>> s = Solution()
    >>> num1 = [1, 2, 4, 5, 6, 0]
    >>> num2 = [3]
    >>> s.merge(num1, 5, num2, 1)
    >>> num1
    [1, 2, 3, 4, 5, 6]
    """

    def merge(self, nums1, m, nums2, n):
        """
        O(m+2n)
        use two queues
        """
        class Queue:
            def __init__(self, nums, shift = 0):
                self.max_size = len(nums[shift:])
                self.data = nums
                self.head = 0
                self.size = 0
                self.shift = shift
            def put(self, x):
                assert self.size < self.max_size, 'the queue is full'
                self.data[(self.head + self.size)%self.max_size + self.shift] = x
                self.size = self.size + 1
            def pop(self):
                assert self.size > 0, 'the queue is empty'
                num = self.data[self.head + self.shift]
                self.head = (self.head+1)%self.max_size
                self.size = self.size - 1
                return num
            def get(self):
                assert self.size > 0, 'the queue is empty'
                return self.data[self.head + self.shift]
            def get_size(self):
                return self.size

        # two queue that use existing storage in nums1 and nums2
        q1 = Queue(nums1, shift = m) # when i < m, move data to q2
        q2 = Queue(nums2) 

        next2 = 0
        for i in range(m+n):
            if i < m: # compare q1, nums1, nums2
                if next2 < n:
                    if q1.get_size() > 0: # compare q1 and nums2
                        if q1.get() > nums2[next2]:
                            temp = nums1[i]
                            nums1[i] = nums2[next2]
                            q1.put(temp)
                            next2 += 1
                        else:
                            q1.put(nums1[i])
                            nums1[i] = q1.pop()
                    else: # compare nums1 and nums2
                        if nums1[i] > nums2[next2]:
                            temp = nums1[i]
                            nums1[i] = nums2[next2]
                            q1.put(temp)
                            next2 += 1
                else: # q1 size must be positive => swap q1 and nums1
                    temp = nums1[i]
                    nums1[i] = q1.pop()
                    q1.put(temp)

            else: # compare q2, nums2
                # move all elements in q1 to q2
                while q1.get_size() > 0:
                    q2.put(q1.pop())

                if next2 < n: # compare q2 and nums2
                    if q2.get_size() > 0:
                        if q2.get() > nums2[next2]:
                            nums1[i] = nums2[next2]
                            next2 += 1
                        else:
                            nums1[i] = q2.pop()
                    else:
                        nums1[i] = nums2[next2]
                        next2 += 1

                else: # pop q2 to nums1
                    nums1[i] = q2.pop()

    def mergeV2(self, nums1, m, nums2, n):
        """
        O(m+n)

        """
        class Queue:
            def __init__(self, nums):
                self.max_size = len(nums)
                self.data = nums
                self.size, self.head, self.tail = 0, 0, -1
            def put(self, x):
                assert self.size < self.max_size, 'the queue is full'
                self.data[(self.tail+1)%self.max_size] = x
                self.size, self.tail = self.size+1, (self.tail+1)%self.max_size
            def pop(self):
                assert self.size > 0, 'the queue is empty'
                num = self.data[self.head%self.max_size]
                self.head, self.size = (self.head+1)%self.max_size, self.size-1
                return num
            def get(self):
                assert self.size > 0, 'the queue is empty'
                return self.data[self.head%self.max_size]
            def get_size(self):
                return self.size
                
        queue = Queue(nums2)

        next2 = 0
        for i in range(m + n):
            if queue.get_size() > 0:
                if next2 < n:
                    if queue.get() > nums2[next2]:
                        temp = nums1[i]
                        nums1[i] = nums2[next2]
                        if i < m:
                            queue.put(temp)
                        next2 += 1
                    else:
                        if i < m:
                            queue.put(nums1[i])
                        nums1[i] = queue.pop()
                else:
                    temp = nums1[i]
                    nums1[i] = queue.pop()
                    if i < m:
                        queue.put(temp)

            else: # queue.size() ==0, i.e. nums2 is not used up
                if i < m:
                    if nums1[i] > nums2[next2]:
                        temp = nums1[i]
                        nums1[i] = nums2[next2]
                        queue.put(temp)
                        next2 += 1
                else:
                    nums1[i] = nums2[next2]
                    next2 += 1

    def mergeV1(self, nums1, m, nums2, n):
        """
	runtime O(mn)
        """
        if n == 0:
            return

        def swap(nums):
            if len(nums) == 1:
                return
            for i in range(len(nums)-1):
                if nums[i] > nums[i+1]:
                    nums[i], nums[i+1] = nums[i+1], nums[i]
                else:
                    break

        for i in range(m + n):
            if i < m:
                if nums1[i] >= nums2[0]:
                    nums1[i], nums2[0] = nums2[0], nums1[i]
                    swap(nums2)
            else:
                nums1[i] = nums2[i-m]

if __name__ == '__main__':
    s = Solution()
    num1 = [1, 2, 3, 9, 0, 0, 0, 0]
    num2 = [2, 2, 10, 20]
    s.merge(num1, 4, num2, 4)
