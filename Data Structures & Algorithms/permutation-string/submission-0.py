class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len1, len2 = len(s1), len(s2)

        # substring cannot be greater than the string it is derived from
        if len1 > len2: return False

        s1_counts, s2_counts = {}, {}
        matches = 0

        for c in s1:
            s1_counts[c] = s1_counts.get(c, 0) + 1

        l, r = 0, 0

        # we should iterate until the window is out of scope or a match has been found
        for l in range(len2):
            # window only needs to be as big as the substring itself
            while r < len(s2) and r - l < len1:
                # increment the counter for the current character
                s2_counts[s2[r]] = s2_counts.get(s2[r], 0) + 1

                # check if there is a match whenever there is a change to the counter
                if s2_counts.get(s2[r]) == s1_counts.get(s2[r]): matches += 1

                # increment r (loop condition)
                r += 1

            # if the number of matches is equal to the number of elements in the counts hash, return true
            if len(s1_counts) == matches:
                return True
            
            # otherwise, we must decrement matches if one exists and update the value of the counter
            if s2_counts.get(s2[l]) == s1_counts.get(s2[l]): matches -= 1
            s2_counts[s2[l]] -= 1

        
        # if no match has been found at this point, return False
        return False




        