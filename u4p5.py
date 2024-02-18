#binary search
def Binary_Search(lst, n, l, r):
    while r >= l:
        mid = (l + r) // 2
        if lst[mid] == n:
            return mid
        elif lst[mid] > n:
            return Binary_Search(lst, n, l, mid - 1)
        else:
            return Binary_Search(lst, n, mid + 1, r)
    return -1
#code testing
a = [1, 2, 3, 4, 5, 6, 7, 9, 20, 21, 24, 34]
n = 4
print(Binary_Search(a, n, 0, len(a) - 1))
