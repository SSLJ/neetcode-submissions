class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        k=1
        p=[]
        left=0
        while(left<n):
            for right in range(n):
                if right==left:
                    continue
                else:
                    k*=nums[right]
            p.append(k)
            k=1
            left+=1
        return p   