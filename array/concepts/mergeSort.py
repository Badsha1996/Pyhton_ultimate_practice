# Merge sort alghorithm 
# time complexity - O(nlogn)
# space complexity - O(n) --> as it required an extra array to store data
'''
ALGORITHM BREAKDOWN 
* Divide and Conqure Algorihtm
* divide the array into two equal parts after that divide them till get to just one element 
* merge them toghter using extra array 
* it slower for smaller input 
* if the array is sorted it still go through the whole array
'''
import sys
sys.setrecursionlimit(2**10)

class sort:
    
    def __init__(self):
        pass
    # sorting method 
    def merge_sort(self, arr):
        # base condition 
        if len(arr)<=1:
            return arr
        mid = (0 + len(arr))//2
        left_arr = self.merge_sort(arr[:mid])
        right_arr = self.merge_sort(arr[mid:])
        return self._merge(left_arr, right_arr)

    # utility function 
    def _merge(self,arr1, arr2):
        index1 = index2 = 0
        arr = []
        while index1 < len(arr1) and index2 < len(arr2):
            if arr1[index1] <= arr2[index2]:
                arr.append(arr1[index1])
                index1+=1
            else:
                arr.append(arr2[index2])
                index2+=1
        if index1 == len(arr1):
            arr.extend(arr2[index2:])
        else:
            arr.extend(arr1[index1:])
        return arr
if __name__=="__main__":
    arr = [float("inf"), 0, 9, 40, 100, 90,float("-inf")]
    obj = sort()
    ans = obj.merge_sort(arr)
    print(ans)
