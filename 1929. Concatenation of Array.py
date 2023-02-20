#Question Link: https://leetcode.com/problems/concatenation-of-array/ 

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        n = len(nums)
        for i in range(n):
            ans.insert(i,nums[i])
            ans.append(nums[i])
        return ans
