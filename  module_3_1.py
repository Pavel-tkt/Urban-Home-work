calls = 0
def count_calls (): #Создать функцию count_calls и изменять в ней значение переменной calls.
    # Эта функция должна вызываться в остальных двух функциях.
    global calls
    calls += 1
    return calls
def string_info (string):  #Создать функцию string_info с параметром string
    count_calls()
    return (len(string), string.upper(), string.lower())
    # Создать функцию is_contains с двумя параметрами string и list_to_search
def is_contains(string, list_to_search):
    count_calls()
    list_to_search = [s.lower() for s in list_to_search] #преобр списка в нижний регистр
    #print(list_to_search)
    return (string.lower() in list_to_search)

print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBan
print(is_contains('cycle', ['recycle', 'cyclic'])) # No matches
print(calls)