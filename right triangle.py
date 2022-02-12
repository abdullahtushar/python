a=int(input('Input value 1:'))
b=int(input('b '))
c=int(input('c '))
if a**2==b**2+c**2:
  print('right triangle')
elif b**2==a**2+c**2:
  print('right triangle')
elif c**2==b**2+a**2:
  print('right triangle')
else:
  print('not a right triangle')
