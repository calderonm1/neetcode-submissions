class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        myDict = {}
        for letter in s:
            myDict[letter] = myDict.get(letter, 0) + 1
        for letter in t:
            myDict[letter] = myDict.get(letter, 0) - 1
        for key in myDict:
            if myDict[key] != 0:
                return False
        return True
        