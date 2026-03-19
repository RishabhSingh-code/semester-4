'''Given an array arr[] denoting heights of n towers and a positive integer k.
 For each tower, you must perform exactly one of the following operations exactly once.
   Increase the height of the tower by k Decrease the height of the tower by k Find out 
   the minimum possible difference between the height of the shortest and tallest towers after 
   you have modified each tower. You can find a slight modification of the problem here. Note:
     It is compulsory to increase or decrease the height by k for each tower. After the operation,
       the resultant array should not contain any negative integers.'''

def minimize_height_difference(arr, k):
    n = len(arr)
    
    if n == 1:
        return 0
    
    arr.sort()
    
    ans = arr[-1] - arr[0]
    
    small = arr[0] + k
    big = arr[-1] - k
    
    if small > big:
        small, big = big, small
    
    for i in range(n - 1):
        
        subtract = arr[i + 1] - k
        add = arr[i] + k
        
        if subtract < 0:
            continue
        
        new_min = min(small, subtract)
        new_max = max(big, add)
        
        ans = min(ans, new_max - new_min)
    
    return ans


# Example usage
arr = [1, 5, 8, 10]
k = 2

print(minimize_height_difference(arr, k))