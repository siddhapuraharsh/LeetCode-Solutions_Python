# Leetcode: https://leetcode.com/problems/trapping-rain-water/

class Solution:
    def trap(self, height: List[int]) -> int:

        '''
        Approach:
        1. For a particular element i, find its max left and max right element.
        2. Consider the min(maxLeft, maxRight) and subtract the height of element
        3. Keep adding them
        '''

        output = 0
        length = len(height)

        left_max_arr = [0] * length
        right_max_arr = [0] * length

        left_max_arr[0] = height[0]
        right_max_arr[-1] = height[-1]

        for i in range(1, length):
            # Forward direction for left_max_arr
            left_max_arr[i] = max(left_max_arr[i-1], height[i])

            # Backward direction for right_max_arr
            j = length - 1 - i
            right_max_arr[j] = max(right_max_arr[j+1], height[j])

        for i in range(1, length-1):
            output += min(left_max_arr[i], right_max_arr[i]) - height[i]

        return output
