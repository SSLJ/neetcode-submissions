class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        map = dict()
        for i in range(n):
          comp = target-nums[i]
          if comp in map:
            return [map[comp],i]
          map[nums[i]]=i  
                