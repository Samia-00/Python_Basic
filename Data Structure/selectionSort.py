def selectionSort(a):
    for i in range (0,len(a)-1):
        min= i
        for j in range (i+1,len(a)):
            if a[j]<a[min]:
                min=j
        if min != i:
            a[i],a[min]=a[min],a[i]
        
a=[44,77,9,60,23,100]
selectionSort(a)
#a=[44,77,9,60,23,100]
print(a)
