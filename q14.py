a=int(input('enter the first number:'))
b=int(input('enter the second number:'))
c=int(input('enter the third number:'))
s=min(a,b,c)
l=max(a,b,c)
m=a+b+c-s-l
print('the sorted order is :',s,m,l)
