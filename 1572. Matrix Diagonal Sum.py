#Question Link: https://leetcode.com/problems/matrix-diagonal-sum/

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:

        n = len(mat)
        primaryDiagonalSum = 0
        secondaryDiagonalSum = 0

        for i in range(n):
            for j in range(n):
                if i == j:
                    primaryDiagonalSum += mat[i][j]
                elif (i+j) == (n-1):
                    secondaryDiagonalSum += mat[i][j]

        return primaryDiagonalSum + secondaryDiagonalSum
			
