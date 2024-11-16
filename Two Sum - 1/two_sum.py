class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        """
            We solve the problem in a single pass using a hashmap (dictionary).

            1. During each iteration:
            - We check if the complement (target - nums[i]) already exists in the hashmap.
            - If it exists, we return the indices of the current element and the complement.

            2. Time Complexity:
            - The algorithm runs in O(n) time because we loop through the array once.
            - Hashmap operations (get and set) have an average time complexity of O(1).

            3. Space Complexity:
            - The space complexity is O(n) because we store up to n elements in the hashmap
                in the worst case (when no solution is found until the last iteration).
        """

        hashmap = {}

        for i in range(len(nums)):
            second = hashmap.get(target-nums[i])
            if second is not None:
                return [i, second]
            else:
                hashmap[nums[i]] = i