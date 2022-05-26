# Pascal's Triangle
# Algorithm :
    # start by assuming u have first arr = [1] inside your result 
    # make a new array for each row by adding 0
    # to both sides then loop through it and add 
    # pre + cur and append it to result 

# time - O(n^2)
# space - O(n)
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Base Case 
        if numRows == 1:
            return [[1]]
        res = [[1]]
        
        for i in range(numRows-1):
            # making a new array by adding 0 to both side 
            pre_arr = [0] + res[-1] + [0]
            ans = []
            for j in range(1,len(pre_arr)):
                # adding two adjecent element
                ans.append(pre_arr[j-1]+pre_arr[j])
            res.append(ans)
        
        return res
if __name__ == "__main__":
    '''
        Test Case :
            Input: numRows = 5
            Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
    '''
    obj = Solution()
    numRows = 5
    res = obj.generate(numRows)
    print(res)