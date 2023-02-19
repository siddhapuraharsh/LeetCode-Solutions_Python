#Link: https://leetcode.com/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        answerArray = []
        for i in range(1,n+1):
            if i%3 == 0 and i%5 == 0:
                answerArray.append("FizzBuzz")
            elif i%3 == 0:
                answerArray.append("Fizz")
            elif i%5 == 0:
                answerArray.append("Buzz")
            else:
                answerArray.append(str(i))
        return answerArray
      
