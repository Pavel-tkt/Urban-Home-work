first=int(input('Введите первое целое число:'))
second=int(input('Введите второе целое число:'))
third=int(input('Введите третье целое число:'))
if first - second==0 and first - third==0:
    print('3')
elif first-second==0 or first-third==0 or second-third==0:
    print('2')
else:
    print(0)