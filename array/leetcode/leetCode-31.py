# Next permutation 
# time - O(n)
# space - O(1)

from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Just reverse the nums in case it is too small
        if len(nums)<=2:
            return nums.reverse()
        # element before the last element 
        ptr = len(nums) - 2
        
        while ptr >= 0 and nums[ptr] >= nums[ptr + 1]:
            ptr -= 1
        
        # Incase it is the last permutation 
        if ptr == -1 :
            return nums.reverse()
        
        # find the next big number after ptr 
        for index in range(len(nums)-1, ptr , -1):
            if nums[index] > nums[ptr]:
                nums[ptr], nums[index] = nums[index] , nums[ptr]
                break 
        
        # Now reverse the nums starting from ptr
        nums[ptr + 1:] = reversed(nums[ptr + 1:])
        
        
if __name__ == "__main__":
    '''
        Test Case :
            Input: nums = [1,2,3]
            Output: [1,3,2]
    '''
    obj = Solution()
    nums = [1,2,3]
    obj.nextPermutation(nums)
    print(nums)       
        
        