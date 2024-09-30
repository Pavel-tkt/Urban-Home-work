from time import process_time_ns

immutable_var=(10, "lime",True)
print(immutable_var)
#immutable_var[1]=2
#не поддерживает изменение- внутри кортежа
#task4
mutable_list=[2,5,9,'Palace','normal',50.5]
mutable_list[0]=20
mutable_list.remove(5)
mutable_list.extend('777')
print(mutable_list)