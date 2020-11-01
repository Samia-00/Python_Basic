a=[5,4,4,3,1,-2,-3,-5]
total2=0
i=0
while True:
    total2=total2+a[i]
    i=i+1
    if a[i]<= 0:
        break
print(total2)

total3=0
for element in a:
    if element <= 0:
        break
    total3 +=element
print(total3)


g=['apple','orange','banana','water melon','jack-fruit','mango','blue-berry']
for e in range(len(g)):
    for j in range(e+1):
        print(g[e])


total0=0
for d in range(1,100):
    if d%3==0:
        total0 +=d
        print(d)
    elif d%5==0:
        total0 +=d
        print(d)
print(total0)






total=0
j=1
while j<5:
    total +=j
    j=j+1
print(total)
