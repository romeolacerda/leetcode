from bisect import bisect_left

class Solution:
    def LIS(self, nums):
        n = len(nums)
        lis = []
        lis_len = [1] * n
        
        for i in range(n):
            pos = bisect_left(lis, nums[i])
            if pos == len(lis):
                lis.append(nums[i])
            else:
                lis[pos] = nums[i]
            lis_len[i] = len(lis)
            
        return lis_len
    
    def minimumMountainRemovals(self, nums):
        n = len(nums)
        lis_lr = self.LIS(nums)
        lis_rl = self.LIS(nums[::-1])[::-1]
        
        max_mountain_size = 0
        for i in range(n):
            if lis_lr[i] > 1 and lis_rl[i] > 1:
                max_mountain_size = max(max_mountain_size, lis_lr[i] + lis_rl[i] - 1)
        
        return n - max_mountain_size
    
arr = [2,1,1,5,6,2,3,1]
solution = Solution()
result = solution.minimumMountainRemovals(arr)
print(result)