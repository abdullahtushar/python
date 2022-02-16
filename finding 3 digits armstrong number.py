a=int(input('Enter 3 digits number: '))
b=a%10
c=a//10
d=c%10
e=c//10
# print(e,d,b)
if e**3+d**3+b**3==a:
    print('An armstrong number')
else:
    print('not an armstrong number')

