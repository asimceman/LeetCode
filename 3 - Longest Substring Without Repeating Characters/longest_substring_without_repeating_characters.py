class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
            This function finds the length of the longest substring without repeating characters 
            using a variation of the sliding window technique.

            Approach:
            1. Sliding Window Technique:
            - Use two pointers (leading_pointer and trailing_pointer) to define a sliding window over the string.
            - The window represents the current substring without duplicate characters.
            - A hashmap (hashmap) is used to track the presence of characters in the current substring. 
                We use a boolean value (True) to indicate whether a character is in the substring.

            2. Steps:
            - Leading Pointer: Advances through the string to expand the window.
            - Trailing Pointer: Moves forward when a duplicate character is found, shrinking the window until the 
            duplicate is removed.
            - For every duplicate character encountered, remove characters from the hashmap and increment the 
            trailing_pointer to maintain a valid substring.
            - Once the duplicate is removed, add the current character to the hashmap, update the substring length 
            (leading_pointer - trailing_pointer), and compare it with max_substring to keep track of the longest valid 
            substring.

            3. Time Complexity: 
            - O(n): Each pointer moves forward at most n times, where n is the length of the string.

            4. Space Complexity:
            - O(n): The hashmap can contain up to n unique characters in the worst case (when all characters are 
            unique).

            5. Advantages of Boolean Hashmap:
            - Using a hashmap with boolean values (True) optimizes memory usage since bool is one of the lightest 
            datatypes in Python.
        """
        max_substring, leading_pointer, trailing_pointer = 0, 0, 0
        hashmap = defaultdict(bool)
        
        while leading_pointer <= len(s) - 1:
            if s[leading_pointer] in hashmap:
                del hashmap[s[trailing_pointer]]
                trailing_pointer += 1
            else:
                hashmap[s[leading_pointer]] = True
                leading_pointer += 1
                max_substring = max(leading_pointer - trailing_pointer, max_substring)

        return max_substring
