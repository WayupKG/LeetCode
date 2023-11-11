# 231. Power of Two

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        degree = 0
        while True:
            res = 2**degree
            if res == n:
                return True
            elif res > n:
                return False
            degree += 1


solutionObj = Solution()
print(solutionObj.isPowerOfTwo(129))


