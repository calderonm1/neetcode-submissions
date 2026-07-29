class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = {}
        longest = 0
        l = 0
        max_count = 0

        for r in range(len(s)):
            # Add the new character to our window
            counts[s[r]] = counts.get(s[r], 0) + 1
            max_count = max(max_count, counts[s[r]])

            # If the window is invalid, shrink it from the left
            if (r - l + 1) - max_count > k:
                counts[s[l]] -= 1
                l += 1

            # Update longest valid window seen so far
            longest = max(longest, r - l + 1)

        return longest
