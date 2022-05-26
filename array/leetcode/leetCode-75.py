from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # One pass solution 
        left, i, right = 0, 0, len(nums)-1
        def swap(i,j):
            nums[i], nums[j] = nums[j], nums[i]
        while i <= right:
            # if we encounter 0 
            if nums[i] == 0:
                swap(i, left)
                left += 1
            # If we encounter 2   
            elif nums[i] == 2:
                swap(i, right)
                right -= 1
                i-=1
            i+=1
           
            
if __name__ == "__main__":

    '''
        Expected - 
        Input: nums = [2,0,2,1,1,0]
        Output: [0,0,1,1,2,2]       
    '''
    obj = Solution()
    nums = [2,0,2,1,1,0]
    obj.sortColors(nums)
    print(nums)            