class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        """
        This function checks if a given string is a palindrome without creating a new string.
        It uses the two-pointer technique and processes characters in-place to achieve optimal space complexity.

        Steps:
        1. Initialize two pointers:
           - `start_pointer` starts at the beginning of the string.
           - `end_pointer` starts at the end of the string.
        2. While `start_pointer` is less than or equal to `end_pointer`:
           - Skip non-alphanumeric characters using `char.isalnum()` for both pointers.
           - Compare the characters at both pointers after converting them to lowercase.
           - If the characters do not match, return `False`.
           - Otherwise, move the `start_pointer` forward and the `end_pointer` backward.
        3. If all characters match and the pointers cross, return `True`.

        Advantages of this approach:
        - It avoids creating a new string, reducing space complexity to O(1).
        - The input string is processed directly, making the algorithm memory-efficient.

        Time Complexity: O(n), where `n` is the length of the input string.
        Space Complexity: O(1), as no additional space is allocated for preprocessing.
        """
        start_pointer = 0
        end_pointer = len(s) - 1

        while start_pointer <= end_pointer:
            # Skip non-alphanumeric characters
            while start_pointer < end_pointer and not s[start_pointer].isalnum():
                start_pointer += 1
            while start_pointer < end_pointer and not s[end_pointer].isalnum():
                end_pointer -= 1

            # Compare characters after converting to lowercase
            if s[start_pointer].lower() != s[end_pointer].lower():
                return False

            # Move pointers
            start_pointer += 1
            end_pointer -= 1

        return True