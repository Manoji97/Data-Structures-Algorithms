def binary(l,x):            #binary search using iteration method
    start = 0
    end = len(l) -1
    mid = (start + end)//2
    while start <= end:
        if l[mid] == x:
            return mid
        elif l[mid] > x:
            end = mid - 1
        elif l[mid] < x:
            start = mid + 1
        mid = (start + end)//2
    return -1

def binrecur(l,start,end,x):            # binary search using recursion
    if start >= end:
        return -1
    mid = (start + end)//2
    if x == l[mid]:
        return mid
    elif x > l[mid]:
        return binrecur(l,mid +1,end,x)
    elif x < l[mid]:
        return binrecur(l,start,mid -1,x)




def selection_sort(l):              #selection sort using min function
    for i in range(0,len(l)-1):
        print(l[i], l[i+1:])
        minnindex = l[i+1:].index(min(l[i+1:]))
        if l[i] > l[minnindex+i+1]:
            l[i],l[minnindex+i+1] = l[minnindex+i+1],l[i]
        print(l)
    return l

def selectionwithoutmin(l):             #selection sort without using min function
    for i in range(0,len(l)-1):
        minind = i
        for j in range(i+1,len(l)):
            if l[j] < l[minind]:
                minind = j
        l[i],l[minind] = l[minind],l[i]
    return l


def bubblesort(l):                  #opimised bubble sort
    for k in range(0,len(l)-1):
        f = 0
        for i in range(0,len(l)-1-k):
            if l[i] > l[i+1]:
                l[i],l[i+1] = l[i+1],l[i]
                f = 1
        if f == 1:
            break
    return l        


def insertionsort(l):               # normal case O(n) and for dec sorted array its O(n^2)
    for i in range(1,len(l)):
        val = l[i]
        hole = i
        while hole > 0 and l[hole -1] > val:
            l[hole],l[hole - 1] = l[hole -1],l[hole]
            hole -= 1
        l[hole] = val
    return l




def merge(left,right,old):          # merge function used in the mergesort function (next)
    i,j,k = 0,0,0                   # that is to combine the two sorted array into a single sorted array
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            old[k] = left[i]
            i += 1
            k += 1
        else:
            old[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        old[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        old[k] = right[j]
        k += 1
        j += 1
    return old

def merge1(left,right,old):      #for removing the duplicates and replace with the 1000000
    i,j,k = 0,0,0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            old[k] = left[i]
            i += 1
            k += 1
        elif left[i] == right[j]:
            old[k] = left[i]
            i += 1
            j += 1
            k += 1
        else:
            old[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        old[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        old[k] = right[j]
        k += 1
        j += 1
    while k < len(old):
        old[k] = 1000000
        k += 1
    return old
    

def mergesort(l):           # merge the recursed the list (half)
    if len(l) < 2:
        return l
    a = len(l)//2
    l1 = mergesort(l[:a])
    l2 = mergesort(l[a:])
    l = merge(l1,l2,l)
    return l
    


