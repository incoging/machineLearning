
# -*- coding:utf-8 -*-
class Solution:
    def GetUglyNumber_Solution(self, index):
        if index <= 0:
            return 0
        ugly_numbers = [0 for _ in range(index)]
        ugly_numbers[0] = 1
        next_ugly_index = 1

        multiply_2, multiply_3, multiply_5 = 0, 0, 0
        while next_ugly_index < index:
            min_value = min(ugly_numbers[multiply_2] * 2, ugly_numbers[multiply_3] * 3, ugly_numbers[multiply_5] * 5)
            ugly_numbers[next_ugly_index] = min_value

            while ugly_numbers[multiply_2] * 2 <= ugly_numbers[next_ugly_index]:
                multiply_2 += 1
            while ugly_numbers[multiply_3] * 3 <= ugly_numbers[next_ugly_index]:
                multiply_3 += 1
            while ugly_numbers[multiply_5] * 5 <= ugly_numbers[next_ugly_index]:
                multiply_5 += 1
            next_ugly_index += 1
        return ugly_numbers[next_ugly_index - 1]
    pass

