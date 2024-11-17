class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
            To achieve an O(n) time complexity, we loop through the nums array twice:

                Prefix Pass:

                In the first pass, we calculate the product of all elements before the current element.
                We maintain a running product (prefix) and assign it to the result array at each step.
                This ensures that each position in result initially holds the product of all elements to the left of the 
                current index.

                Postfix Pass:

                In the second pass, we calculate the product of all elements after the current element.
                Starting from the end of the array, we maintain a running product (postfix) and multiply it with the 
                existing value in the result array.
                This effectively combines the prefix and postfix products for each element.

                Complexity:
                Time Complexity: O(n), as we traverse the array twice (once for prefix and once for postfix).
                Space Complexity: O(n) for the output array, but no additional space is used for intermediate 
                calculations.
                
                By combining the prefix and postfix products, the result array contains the desired product for each 
                index without including the element at that index.
        """
        nums_length = len(nums)
        result = [1] * nums_length

        prefix = 1
        for i in range(nums_length):
            result[i] = prefix
            prefix *= nums[i]
        
        postfix = 1
        for i in range(nums_length - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        
        return result