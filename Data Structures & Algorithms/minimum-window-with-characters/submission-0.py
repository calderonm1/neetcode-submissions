class Solution:
    def minWindow(self, s: str, t: str) -> str:
        shortest = ""
        len_s, len_t = len(s), len(t)

        if len_t > len_s:
            return shortest

        l, r = 0, -1

        counts = {}
        matches = 0
    
        for c in t:
            counts[c] = counts.get(c, 0) + 1

        for l in range(len_s):
            if s[l] not in counts:
                continue

            if r < 0: r = l

            # keep moving the right pointer until we find a matching substring
            while r < len_s and matches != len(counts):
                if s[r] in counts:
                    # we must update the counts dict whenever a relevant character is found
                    counts[s[r]] -= 1

                    # whenever we update the dict, we must check for matches
                    if counts[s[r]] == 0: matches += 1

                    print(l, "r:", r)
                    print(l, "counts:", counts)
                    print(l, "matches:", matches)

                # increment the right pointer
                r += 1

            # check for matches
            if matches == len(counts):
                # right pointer should be incremented by default
                # this is important so that we capture the inclusive substring
                substring = s[l:r]

                if shortest == "" or len(substring) < len(shortest):
                    shortest = substring

            # remove the value at the left pointer from the counter
            counts[s[l]] += 1
            matches -= 1
            print()


        return shortest


                
        # o u z o d y x a z v
        # 0 1 2 3 4 5 6 7 8 9
        # _ _ _ _ _ l r

        # l = 2, r = 6
        # z o d y x

        # update l = 5