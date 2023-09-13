# Сложность O(n^2) / не прошел тест
def maxArea1(height: list) -> int:
    res = []
    for il, l in enumerate(height):
        for ir, r in enumerate(reversed(height[il:])):
            sum_l_r = l * r
            sum_index = sum(height[il:(len(height) - ir)])
            print(f'l = {l}: r = {r} == {sum_l_r + sum_index}')
            res.append(sum_l_r + sum_index)
    return max(res)


# Сложность O(n^2) / вышел Time limit Exceeded
def maxArea2(height: list) -> int:
    res = []
    for il, l in enumerate(height):
        for ir, r in enumerate(reversed(height[il:])):
            min_border = min([l, r])
            res_height = len(height[il:(len(height) - ir - 1)])
            res.append(min_border * res_height)
    return max(res)


# Сложность O(n) / линейный сложность / Задача решено
def maxArea3(height: list) -> int:
    res, left, right = 0, 0, len(height) - 1
    while left < right:
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res


print(maxArea3([1, 8, 6, 2, 5, 4, 8, 3, 7]))
