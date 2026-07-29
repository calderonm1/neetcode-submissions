class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for word in strs:
            # Count frequency of each character
            char_count = [0] * 26
            for letter in word:
                index = ord(letter) - ord('a')
                char_count[index] += 1  # Fixed: was using ++alphabet_list[index]
            
            # Convert to string key
            key = tuple(char_count)  # Using tuple is more efficient than string join
            
            # Add word to the group
            if key not in res:
                res[key] = []
            res[key].append(word)
        
        return list(res.values())