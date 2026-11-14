class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt ={}
        for i in range(len(nums)):
            dictt[nums[i]]=i
        answer=[]
        for i in range(len(nums)):
            if target-nums[i] in dictt and  dictt[target-nums[i]] != i : 
                answer.append(i)
                answer.append(dictt[target-nums[i]])
                if answer != None : 
                    return answer
        return answer

        