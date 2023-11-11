# res = [1, 2, 1, 3, 0, 1, 2]
# # [0, 4, 8, 10]
# # [4, 0, 3, 1, 4]
# # [3, 1, 2, 0, 4]
#
# print(res[5])

def jump(nums):
    res = []
    n = 0
    while True:
        n = nums[n] + n
        res.append(n)
        if n >= len(nums) or n == 0 or nums[n] == 0:
            break
    return len(res)


print(jump([4, 0, 3, 1, 4]))