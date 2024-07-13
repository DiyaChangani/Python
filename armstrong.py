n=153
temp=n
sum=0
while n>=0:
    r=n%10
    r=r*r*r
    sum=sum+r
    n=n//10

if temp==sum:
    print(temp," is an armstrong number")
else:
    print(temp," is not an armstrong number")