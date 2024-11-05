def test_function():


    def inner_function():
        print("Я в области видимости функции test_function")

        #Вызовите функцию inner_function внутри функции test_function
    inner_function() # ничего не показывает



test_function() # показывает print из inner_function
#inner_function() #  ошибка, не видит в пространстве имен