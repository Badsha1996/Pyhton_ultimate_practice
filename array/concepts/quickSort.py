# This is a code explaining the quick sort 
# Time complexity - O(nlogn)
# Space complexity - O(1) --> this is an advantage ove the merge sort
'''
ALGORITHM BREAKDOWN 
* Divide and Conqure Algorihtm
* take a pivot, compare i and j and swap them after that swap with pivot  
* recursively do quick sort 
'''
from cmath import pi
from operator import le


class sort:
    def __init__(self):
        pass
    def quick_sort(self,arr, low, high):
        if low < high:
            pivot = self.partition(arr, low , high)
            self.quick_sort(arr,pivot + 1, high )
            self.quick_sort(arr,low, pivot - 1 )
        return arr
            
    def partition(self, arr, low, high):
        left = low 
        right = high - 1
        pivot_element = arr[high]

        while left < right:
            while left < high and arr[left] < pivot_element:
                left+=1
            while right > low and arr[right] >= pivot_element:
                right-=1
            if left < right :
                arr[left], arr[right] = arr[right], arr[left]

        
        if arr[left] > pivot_element:
            arr[left] , arr[high] = arr[high], arr[left]
        return left

if __name__=="__main__":
    arr = [90,80,68,21,18,26,30]
    obj = sort()
    ans = obj.quick_sort(arr, 0, len(arr)-1)
    print(ans)


