class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        """
            To determine if two strings are anagrams, we use a hashmap to count character 
            occurrences.

            1. Create an empty hashmap where keys are characters and values are their counts.
            2. Loop through the first string `s`, incrementing the count for each character.
            3. Loop through the second string `t`, decrementing the count for each character.
            4. Finally, check if all values in the hashmap are 0:
            - If true, the strings are anagrams.
            - If false, the strings are not anagrams.

            Time Complexity:
            - O(n + m), where `n` is the length of `s` and `m` is the length of `t`.

            Space Complexity:
            - O(1) for fixed-size character sets (e.g., lowercase English letters or ASCII).
            - O(u) for generic strings, where `u` is the number of unique characters.
        """
        character_hashmap = defaultdict(int)

        for c in s:
            character_hashmap[c] += 1

        for c in t:
            character_hashmap[c] -= 1

        for counter in character_hashmap.values():
            if counter != 0:
                return False

        return True 