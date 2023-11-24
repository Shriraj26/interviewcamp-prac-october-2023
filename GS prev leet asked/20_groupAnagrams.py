def groupAnagrams(self, arr: List[str]) -> List[List[str]]:
        myDict = {}

        for s in arr:
            
            # Create a 26 letter array
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            
            count = tuple(count)
            if count in myDict:
                myDict[count].append(s)
            else:
                myDict[count] = [s]
        
        return list(myDict.values())