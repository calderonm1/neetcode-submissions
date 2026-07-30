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

            print(l, "counts:", counts)

            if r < 0: r = l

            while r < len_s and matches != len(counts):
                if s[r] in counts:
                    pre = counts[s[r]]
                    counts[s[r]] -= 1

                    if pre == 0:
                        matches -= 1
                    elif counts[s[r]] == 0:
                        matches += 1

                    # if counts[s[r]] == 0: matches += 1
                r += 1

            if matches == len(counts):
                substring = s[l:r]
                print(l, "substring", substring, "found between", l, r)

                if shortest == "" or len(substring) < len(shortest):
                    shortest = substring

            # remove the value at the left pointer from the counter
            print(l, "counts:", counts)
            pre = counts[s[l]]
            counts[s[l]] += 1
            if pre == 0:
                matches -= 1
            elif counts[s[l]] == 0:
                matches += 1

            print(l, "counts:", counts)
            print(l, "matches:", matches)
            print(l, "len(counts):", len(counts))
            print()


        return shortest


        # t = A B C
        # A  D  O  B  E  C  O  D  E  B  A  N  C
        # 0  1  2  3  4  5  6  7  8  9  10 11 12
        # 
        # _  _  _  l  _  _  _  _  _  _  r  _  _

        # l = 0, r = 5
        # A D O B E C