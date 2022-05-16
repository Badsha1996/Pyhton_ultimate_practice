# This is a problem of maximum total value in a sub array 
# This problem can be solved using kadane algorithm 
"""_Algorithm breakdown_
* keep track of maximum sum and last saved maximum sum 
* any point value gets to neg, reset that to 0
* comapre between max to the point and total max 
"""
class solution:
    def __init__(self) -> None:
        pass
    def maxSubArraySum(self, arr):
        curMax = 0
        totalMax = -float("inf")
        for value in arr:
            curMax += value
            if curMax > totalMax :
                totalMax = curMax
            if curMax < 0:
                curMax = 0
        return totalMax 

if __name__=="__main__":
    arr = [-9,4,5,-3,-3,9,9,-3,9,0]
    obj = solution()
    res = obj.maxSubArraySum(arr)
    print(res)