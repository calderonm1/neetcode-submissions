class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while not lp >= rp:
            while not s[lp].isalnum():
                lp += 1
            while not s[rp].isalnum():
                rp -= 1

            if s[lp].lower() != s[rp].lower():
                return False
            lp += 1
            rp -= 1
        return True
