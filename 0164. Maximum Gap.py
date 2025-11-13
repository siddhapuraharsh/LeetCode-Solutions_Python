# Leetcode: https://leetcode.com/problems/maximum-gap/

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        """
        Approach:
        1. Handle edge case: if array has < 2 elements, return 0.
        2. Compute bucket_size = ceil((max - min) / (length - 1)):
           - Ensures bucket index (x - min) / bucket_size ≤ length-1
        3. Calculate number of buckets = ceil((max - min) / bucket_size) + 1:
           - This equals the array length (n) in practice due to pigeonhole principle
           - Prevents index out of bounds (e.g., [1,2,3,4] needs 4 buckets)
        4. Initialize bucket arrays (max_bucket/min_bucket) with size = number_of_buckets.
        5. Assign each element to a bucket:
           - Bucket index = floor((x - min) / bucket_size)
           - Update bucket's min/max values
        6. Find maximum gap between consecutive non-empty buckets:
           - Track previous bucket's max value
           - Skip empty buckets (min_bucket[i] == inf)
        """
        length = len(nums)
        if length < 2: 
            return 0

        maximum = max(nums)
        minimum = min(nums)
        bucket_size = math.ceil((maximum - minimum) / (length - 1))
        if bucket_size == 0:  # Handles all equal elements
            return 0

        # Calculate buckets as ceil((max-min)/bucket_size) + 1 (always = length)
        number_of_buckets = math.ceil((maximum - minimum) / bucket_size) + 1
        max_bucket = [float('-inf')] * number_of_buckets
        min_bucket = [float('inf')] * number_of_buckets

        # Distribute elements into buckets
        for num in nums:
            bucket_index = int((num - minimum) / bucket_size)
            max_bucket[bucket_index] = max(max_bucket[bucket_index], num)
            min_bucket[bucket_index] = min(min_bucket[bucket_index], num)

        # Find max gap between consecutive non-empty buckets
        output = 0
        previous_max = max_bucket[0]  # Start with first non-empty bucket
        for i in range(1, number_of_buckets):
            if min_bucket[i] == float('inf'):  # Skip empty bucket
                continue
            output = max(output, min_bucket[i] - previous_max)
            previous_max = max_bucket[i]  # Update to current bucket's max

        return output
