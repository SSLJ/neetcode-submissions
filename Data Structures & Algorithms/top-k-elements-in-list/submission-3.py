from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        p=[]
        n=len(nums)
        c=Counter(nums)
        t=list(v for v,_ in c.most_common())
        for i in range(k):
            p.append(t[i])
        return p
        