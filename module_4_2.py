def test_function():

     def inner_function():
         global a
         a = 'Я в области видимости функции test_function'
         return a
     inner_function()
     print(a)

test_function()
#inner_function() - функция не видна, так как она нахоится внутри test_function
# print(globals())




