class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
            The algorithm maintains a running sum (`current_sum`) and resets it only when adding 
            the current element makes the sum smaller than the current element itself. 
            This ensures we start a new subarray when it's more beneficial than extending the 
            current one.

            For example:
            - In [4, -3, 1, 6], the subarray [4, -3] still contributes positively, so we extend 
            the sum to include subsequent elements.
            - In [4, -3, 1, 1], the subarray is not reset since subsequent elements can still 
            increase the sum. Although the sum (3) is less than the single element 4, the 
            algorithm waits for potentially larger values later.

            The global maximum (`maximum_sum`) is updated whenever the `current_sum` exceeds it, 
            ensuring we always track the largest subarray sum.

            Time complexity: O(n), as we iterate through the array once.
            Space complexity: O(1), as we use only a few variables.
        """
        current_sum, maximum_sum = 0, float('-inf')
        for i in range(len(nums)):
            if (current_sum + nums[i]) > nums[i]:
                current_sum += nums[i]
            else:
                current_sum = nums[i]

            if current_sum > maximum_sum:
                maximum_sum = current_sum
        
        return maximum_sum