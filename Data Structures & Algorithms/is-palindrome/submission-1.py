class Solution:
    def isPalindrome(self, s: str) -> bool:
        lp = 0
        rp = len(s) - 1

        while lp < rp:
            # check if lp is not alphanumeric
            if not s[lp].isalnum():
                lp += 1

            # check if rp is not alphamumeric
            if not s[rp].isalnum():
                rp -= 1

            # check if both are alphanumeric
            if not (s[lp].isalnum() and s[rp].isalnum()):
                continue

            # check if they are equal
            if s[lp].lower() != s[rp].lower():
                return False
            
            lp += 1
            rp -= 1
        return True
