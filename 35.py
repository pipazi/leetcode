from typing import List
class Solution:

    # 暴力
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     for index, num in enumerate(nums):
    #         if num >= target:
    #             return index
    #     return len(nums)

    # dfs + 二分
    # def searchInsert(self, nums: List[int], target: int) -> int:
    #     l = len(nums)
    #     def dfs(start, end):
    #         if nums[start] >= target:
    #             return start
    #         if nums[end] == target:
    #             return end
    #         if  nums[end] < target:
    #             return end + 1     
    #         if end - start == 1 and nums[start] < target < nums[end]:
    #             return end
    #         half = (start + end) // 2
    #         if nums[half] < target:
    #             return dfs(half, end)
    #         elif nums[half] > target:
    #             return dfs(0, half)
    #         else:
    #             return half
    #     return dfs(0, l - 1)

    # loop + 二分
    def searchInsert(self, nums: List[int], target: int) -> int:
        start, end = 0, len(nums) - 1
        while start <= end:
            if nums[start] >= target:
                return start
            if nums[end] == target:
                return end
            if  nums[end] < target:
                return end + 1     
            if end - start == 1 and nums[start] < target < nums[end]:
                return end 
            
            half = (start + end) // 2
            if nums[half] < target:
                start = half
            elif nums[half] > target:
                end = half
            else:
                return half
        

s = Solution()
print(s.searchInsert([1,3,5,6], 2))
print(s.searchInsert([1,3,5,6], 5))
print(s.searchInsert([1,3,5,6], 7))
