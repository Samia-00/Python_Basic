x=int(input())
choice=input('1 or 2:')
if choice =='1':
    for i in range (1,x):
        sum1=(x*(x+1))/2
    print(sum1)
elif choice == '2' :
        fact =1
        for i in range (1,x+1):
            fact= fact*i
        print(fact)
            
