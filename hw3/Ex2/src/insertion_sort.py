def insertion_sort(A):
    comparisons = 0
    swaps = 0
    n = len(A)
    for j in range(1, n):
        key = A[j]
        i = j - 1
        while i >= 0 and A[i] > key:
            comparisons += 1
            A[i + 1] = A[i]
            i -= 1
            swaps += 1
        A[i + 1] = key
        if i >= 0:
            comparisons += 1
    return comparisons, swaps
