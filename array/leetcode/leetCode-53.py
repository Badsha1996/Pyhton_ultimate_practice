# Maximum Subarray
# time - O(n)
# space - O(1)

import numbers
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Concept of kadanes Algorithm 
        total_max = nums[0]
        cur_max   = 0
        
        for num in nums:
            cur_max = cur_max + num
            if cur_max > total_max :
                total_max = cur_max
            if cur_max < 0:
                cur_max = 0
        return total_max

if __name__ == "__main__":

    '''
        Expected - 
        Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
        Output: 6
        Explanation: [4,-1,2,1] has the largest sum = 6.
    '''
    obj = Solution()
    nums = [-2,1,-3,4,-1,2,1,-5,4]
    res = obj.maxSubArray(nums)
    print(res)