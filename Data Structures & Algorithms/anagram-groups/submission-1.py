class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # brute force 
        '''
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
        '''
        res = defaultdict(list)

        for s in strs : 
            count = [0]*26 

            for c in s : 
                count[ord(c)-ord('a')] += 1

            res[tuple(count)].append(s)
        return list(res.values())


