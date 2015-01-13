
def quicksort(A):
    quicksort_impl(A, 0, len(A) - 1)

def quicksort_impl(A, p, r):
    if p >= r:
        return
    
    pivot = A[r]

    next_swap = p
    
    for i in range(p, r):
        if A[i] < A[r]:
            A[next_swap],A[i] = A[i], A[next_swap]
            next_swap += 1

    A[next_swap],A[r] = A[r], A[next_swap]

    quicksort_impl(A, p, next_swap - 1)
    quicksort_impl(A, next_swap + 1, r)
