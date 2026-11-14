class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups ={}
        for word in strs: 
            copy_word=word
            sorted_word = "".join(sorted(copy_word))
            if sorted_word not in groups:
                groups[sorted_word]=[word]
            else:
                groups[sorted_word].append(word)
            #print(groups)
        return list(groups.values())
        