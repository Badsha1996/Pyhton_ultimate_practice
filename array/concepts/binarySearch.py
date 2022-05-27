# Binary search 
# time - O(logn)
# space - O(1)
'''
    ALGORITHM BREAKDOWN
# Only works on sorted arr
# divide in two parts and search based on part 
'''
import sys
sys.setrecursionlimit(2**10)

class search:
    def __init__(self):
        pass
    def binary_search(self, arr, element, low , high):
        mid =  (high + low) // 2
        if arr[mid]==element:
            return mid
        elif arr[mid] < element:
             self.binary_search(arr, element, mid + 1, high)
        else:
             self.binary_search(arr, element, low, mid - 1)
if __name__=="__main__":
    arr = [2,4,5,6,7,10]
    low = 0
    high = len(arr) 
    key  = 6
    obj = search()
    res = obj.binary_search(arr, key, low, high)
    print(res)