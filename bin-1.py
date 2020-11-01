found =False
def binsearch(a,num,n,m):
    mid = int((n+m)/2)
    print(mid)
    if a[mid]==num:
        print("Found")
    elif a[mid]<num:
        binsearch(a,num,mid+1,m)
    elif a[mid]>num:
        binsearch(a,num,n,mid-1)

    


a = [1,2,3,4,5]
num=5
binsearch(a,num,0,len(a)-1)

