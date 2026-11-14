class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nonDuplicates = {}
        for num in nums : 
            if num in nonDuplicates : 
                return True
            else:
                nonDuplicates[num]=1
        return False
        