def insertionSortRecursive(arr,n):
    if n<=1:
        return
    insertionSortRecursive(a,n-1)
    last=a[n-1]
    j=n-2
    while (j>=0 and a[j]>last):
        a[j+1]=a[j]
        j=j-1
    a[j+1]=last
def printArray(a,n):
    for i in range(n):
        print(a[i])
a=[12,13,11,5,6]
n=len(arr)
insertionSortRecursive(arr,n)
printArray(a,n)
        
