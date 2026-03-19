'''Given an array arr[] of positive integers. Return true if all the array elements are palindrome otherwise, return false.py'''
def is_palindrome(num):
    return str(num) == str(num)[::-1]


def all_palindromes(arr):
    for num in arr:
        if not is_palindrome(num):
            return False
    return True


# Example usage
arr = [121, 131, 222, 444]
print(all_palindromes(arr))