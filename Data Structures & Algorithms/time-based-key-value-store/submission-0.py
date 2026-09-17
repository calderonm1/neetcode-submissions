class TimeMap:

    def __init__(self):
        # a dict containing arrays
        self.keyToValueList = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if the array does not exist, we must create it
        # otherwise, we will add to it and sort it
        valueList = self.keyToValueList.get(key, [])
        valueList.append((timestamp, value))
        valueList.sort()
        self.keyToValueList[key] = valueList

    def get(self, key: str, timestamp: int) -> str:
        valueList = self.keyToValueList.get(key, [])

        l = 0
        r = len(valueList) - 1
        retVal = ""

        while l <= r:
            m = (l + r) // 2

            if valueList[m][0] == timestamp:
                return valueList[m][1]
            elif valueList[m][0] > timestamp:
                r = m - 1
            else:
                retVal = valueList[m][1]
                l = m + 1

        return retVal

    
