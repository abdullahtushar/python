x=float(input('x: '))
y=float(input('y: '))
if x<0 and y<0:
    print('3rd Quardant')
elif x<0 and y==0:
    print('X-axis')
elif x==0 and y==0:
    print('Origin')
elif x==0 and y>0:
    print('Y-axis')
else:
    print('1st quardrant')