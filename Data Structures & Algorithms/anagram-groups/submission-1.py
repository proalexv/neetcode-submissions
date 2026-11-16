from collections import defaultdict, Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # MYIDEA: 
        # # Loop through the arrary and sort, put them in a has table with value as index
        # sortedStrDict = defaultdict(list)
        # answer= []
        
        # for i in range(len(strs)):
        #     key = "".join(sorted(strs[i]))
        #     value = strs[i]
            
        #     sortedStrDict[key].append(value)
        # #Loop through dict and Generate new arrary with the indexs and return
        # for key,value in sortedStrDict.items(): 
        #         answer.append(value)
        # return answer
# __________________________

        # 1. We could loop through arrary, use a counter to track our 
        # keys then words as our values
        answer = []
        string_dict = defaultdict(list)
        
        for i in range(len(strs)):
            char_count = [0] * 26 
            for char in strs[i]:
                char_count[ord(char) - ord("a")] += 1
            
            string_dict[tuple(char_count)].append(strs[i])
        # 2.loop through dict and grab list values and append to answer arrary      
        for key,value in string_dict.items(): 
            answer.append(value)

        return answer

