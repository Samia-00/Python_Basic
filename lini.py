
'''
def linearSearch(mylist,item):
    mylist=[3,7,5,9,11]
    for i in range(0,len(mylist)):
        if mylist[i]== item:
                   return True #print(item+"found"+str(i))
    return False #print("not found")

item=int(input())
if linearSearch(mylist,item)== True:
    print("found")
else:
    print("not found")


def linsearch(a,x):
    for i in range(a):
        if a[i]==x:
            return True
    return False

a=[5,3,9,77,4,66,90]
x=9
result=linsearch(a,x)
if result==True:
    print("found")
else:
    print("not found")
                   
                   
