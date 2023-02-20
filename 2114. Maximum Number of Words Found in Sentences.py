#Question Link: https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        maxWordsCount = 0
        for i in sentences:
            tempWordsCount = len(i.split())
            if tempWordsCount>maxWordsCount:
                maxWordsCount = tempWordsCount 
        return maxWordsCount
      
