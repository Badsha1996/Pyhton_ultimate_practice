# this is an easier version of quick sort 
from operator import eq
import random


def quick_sort(arr):
    # base code 
    if len(arr) <=1 :
        return arr
    small, equal, large = [], [], []
    
    pivot = random.randint(0,len(arr)-1)
    pivot_ele = arr[pivot]
    for ele in arr:
        if ele < pivot_ele:
            small.append(ele)
        elif ele > pivot_ele:
            large.append(ele)
        else:
            equal.append(ele)
    
    return quick_sort(small) + equal + quick_sort(large)

if __name__ == "__main__":
    arr = [0,float("-inf"),float("inf"),7,8,10,3,2]
    ans = quick_sort(arr)
    print(ans)


