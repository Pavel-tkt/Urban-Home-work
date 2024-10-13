my_dict={'Павел':1980, 'Егор':1999, 'Михаил':1890, 'Мария':1939}
print('Dict:', my_dict)
print(my_dict['Егор'])
print(my_dict.get('Павел'))
my_dict.update({'Larisa':2001,
                'Lili':2020})
s=my_dict.pop('Мария')
print(my_dict)
print(s)

#task2
my_set={5,9,'i',3,7,5,'i',7,True,1,1,'rrr'}
my_set.add('rer')
my_set.add(14)
print('Set:', my_set)
print(my_set.remove(3))
my_set.remove('i')
print('New_set:',my_set)



