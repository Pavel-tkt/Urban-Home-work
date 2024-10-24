#Задача "Распаковка"
def print_params(a = 1, b = 'строка', c = True):
    print(a,b,c)

print_params(b=25)
print_params(c = [1,2,3]) #работает
print_params("q")
print_params(' *', 'два')
print_params(0, b=3,c=3+1)
print('---------------------------')
# 2.Распаковка параметров:
values_list = [5, 'Master', False]
values_dict = {'a':11, 'b':False, 'c':55}
print_params(*values_list)
print_params(**values_dict)
print('---------------------------')
values_list_2 = [54.32, 'Строка' ]
print_params(*values_list_2, 42)
print('----------------___________---------')

def append_to_list(item, values_list = None):
    if values_list is None:
        values_list = []
        values_list.append(item)
print(values_list)
print(*values_list)