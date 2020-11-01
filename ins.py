def insertionSort(a):
    for i in range (1,len(a)):
        item=a[i]
        j=i-1
        while j>=0 and item<a[j]:
            a[j+1]=a[j]
            j=j-1
            a[j+1]=item
a=[33,6,9,22,4,5,17]
insertionSort(a)
print(a)
