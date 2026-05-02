class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        result = []

        for i in range (len(nums)):
            
            if nums[i] > 0:
                break
            
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            j, k = i + 1, (len(nums) - 1)
            tgt = -1 * nums[i]

            while j < k:
                if (nums[j] + nums[k] == tgt):
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1
                    while nums[j] == nums[j - 1] and j < k:
                        j += 1
                elif (nums[j] + nums[k] < tgt):
                    j += 1
                else:
                    k -= 1
        
        return result