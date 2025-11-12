class Solution:
    def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
      
        '''
        Pseudocode:
        
        1. Consider i > j
        2. Case 1: arr1[i] > arr1[j] & arr2[i] > arr2[j] 
            = arr1[i] - arr1[j] + arr2[i] - arr2[j] + i - j
            = (arr1[i] + arr2[i] + i) - (arr1[j] + arr2[j] + j)
            

        3. Case 2: arr1[i] < arr1[j] & arr2[i] > arr2[j] 
            = arr1[j] - arr1[i] + arr2[i] - arr2[j] + i - j
            = (arr2[i] - arr1[i] + i) - (arr2[j] - arr1[j] + j)

        4. Case 3: arr1[i] > arr1[j] & arr2[i] < arr2[j] 
            = arr1[i] - arr1[j] + arr2[j] - arr2[i] + i - j
            = (arr1[i] - arr2[i] + i) - (arr1[j] - arr2[j] + j)

        5. Case 4: arr1[i] < arr1[j] & arr2[i] < arr2[j] 
            = arr1[j] - arr1[i] + arr2[j] - arr2[i] + i - j
            = (arr1[j] + arr2[j] - j) - (arr1[i] + arr2[i] - i)

        6. Calculate Max for all cases
        '''

        arr_case_1 = []
        arr_case_2 = []
        arr_case_3 = []
        arr_case_4 = []

        for i in range(len(arr1)):
            arr_case_1.append(arr1[i] + arr2[i] + i)
            arr_case_2.append(arr2[i] - arr1[i] + i)
            arr_case_3.append(arr1[i] - arr2[i] + i)
            arr_case_4.append(arr1[i] + arr2[i] - i)

        case_1 = max(arr_case_1) - min(arr_case_1)
        case_2 = max(arr_case_2) - min(arr_case_2)
        case_3 = max(arr_case_3) - min(arr_case_3)
        case_4 = max(arr_case_4) - min(arr_case_4)

        output = max(case_1, case_2, case_3, case_4)

        return output


        '''
        Better Approach:
        
        class Solution:
            def maxAbsValExpr(self, arr1: List[int], arr2: List[int]) -> int:
                minA = minB = minC = minD = math.inf
                maxA = maxB = maxC = maxD = -math.inf

                for i, (num1, num2) in enumerate(zip(arr1, arr2)):
                    minA = min(minA, i + num1 + num2)
                    maxA = max(maxA, i + num1 + num2)
                    minB = min(minB, i + num1 - num2)
                    maxB = max(maxB, i + num1 - num2)
                    minC = min(minC, i - num1 + num2)
                    maxC = max(maxC, i - num1 + num2)
                    minD = min(minD, i - num1 - num2)
                    maxD = max(maxD, i - num1 - num2)
                
                return max(maxA - minA, maxB - minB,
                        maxC - minC, maxD - minD)
        '''
        
