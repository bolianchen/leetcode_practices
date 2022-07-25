class Solution:
    """
    >>> s = Solution()
    >>> s.reverse(123)
    321
    >>> s.reverse(-123)
    -321
    >>> s.reverse(120)
    21
    >>> s.reverse(0)
    0
    """
    def reverse(self, x: int) -> int:
        """
        O(number of x digits)
        """
        x = str(x)
        if x[0] == '-':
            x = x[0] + x[:0:-1]
        else:
            x = x[::-1]
        x = int(x)
        if x > 2**31-1 or x < -2**31:
            return 0
        return x


    def reverseV1(self, x: int) -> int:
        """
        O(number of x digits)
        """
        
        positive = x > 0
        if not positive:
            x = -x
            
        result = 0
        while x != 0:
            result = result * 10 + x%10
            x //= 10
        
        if not positive:
            result = -result

        if result > 2**31 - 1 or result < -2**31:
            return 0
            
        return result
