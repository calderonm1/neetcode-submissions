class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCharacterReplacement = 0

        for l in range(len(s)):
            r = l
            counts = {}
            maxCount = 0
            while (r - l + 1) - maxCount <= k:
                counts[s[r]] = counts.get(s[r], 0) + 1
                maxCount = max(counts[s[r]], maxCount)
                
                if r + 1 == len(s):
                    break
                r += 1

            print("l:", l, "r:", r, "maxCharacterReplacement:", r - l)
            print()
            maxCharacterReplacement = max(maxCharacterReplacement, r - l + 1)
        
        return maxCharacterReplacement


        # length window - most frequent char <= k
        


