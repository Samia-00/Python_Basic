def searchSeq(x):
    #a=[5,4,3,1,10]
    for i in range(0,len(a)):
        if x==i:
            return True
        return False
a=[5,4,3,1,10]
k=int(input())
if searchSeq(k)==True:
    print("number found")
else:
    print("number not found")
