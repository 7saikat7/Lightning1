# using recursion
# def binarysearch(t, l, r, x):
#     if r >= l:
#         mid = l + (r - l)
#         if t[mid] == x:
#             return mid
#         elif t[mid] > x:
#             return binarysearch(t,l, mid - 1, x)
#         else:
#             return binarysearch(t, mid + 1, r, x)
#     else:
#         return -1

# using iterative return

#kichu kori ni bhai just comment pull kore ne

def search(n, t, low, up):
    m = int((low + up) / 2)
    i = 0
    while low <= up:
        if n != t[m]:
            if n > t[m]:
                low = m
                search(n, t, low, up)
            else:
                up = m
                search(n, t, low, up)
        else:
            return m, i
        i += 1
        m = int((low + up) / 2)


arr = [2, 3, 4, 10, 40, 77]
x = 3
# result = binarysearch(arr, 0, len(arr) - 1, x)
lower = 0
upper = len(arr)
result, loops = search(x, arr, lower, upper)
print(f"Found in index: {result}, number of loops: {loops}")
# time complexity=O(log(n))
# space complexity=O(log(n)) for recursive approach, O(1) for iterative approach
