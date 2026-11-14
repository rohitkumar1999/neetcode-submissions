class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictt = defaultdict(int)
        for num in nums:
            dictt[num]+=1
        return list(dict(sorted(dictt.items(), key=lambda x:x[1], reverse=True)[:k]).keys())
        

        