class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dictS = {}
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in dictS : 
                dictS[s[i]]+=1
            else:
                dictS[s[i]]=1
        print(dictS)
        for i in range(len(t)):
            if t[i] in dictS and dictS[t[i]] > 0: 
                dictS[t[i]]-=1
            else:
                return False 
        return True
        