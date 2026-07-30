class Solution:

    def encode(self, strs: List[str]) -> str:
        retVal = ""
        for s in strs:
            retVal += str(len(s)) + "#" + s
        return retVal


    def decode(self, s: str) -> List[str]:
        retVal = []
        while (True):
            idx = 0

            for c in s:
                if c == "#":
                    break
                idx += 1
            num = int(s[0:idx])
            offset = idx + 1

            word = s[offset:(offset+num)]
            retVal.append(word)

            s = s[offset+num:]

            if s == "":
                break
            
        return retVal
            
            