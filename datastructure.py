//create a list and pass in function

>>> list = [1,2,3,4,5]
>>> def myfunc(n):
...     print(n)
...
>>> myfunc(list)
[1, 2, 3, 4, 5]
>>>
 names = {'name' :'navi', 'age': 23}
>>> names
{'name': 'navi', 'age': 23}

/////tuple

>>> t = 12345,hello,hii
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'hello' is not defined
>>> t = 123,456,'hello'
>>> t[0]
123
>>> t[2]
'hello'
>>> v ([1,2,3],[1,2,3])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'v' is not defined
>>> v= ([1,2,3],[1,2,3])
>>> v
([1, 2, 3], [1, 2, 3])
>>> t = 'n','a','v'
>>> t1= 'e','e','n'
>>> t3 = t+t1
>>> t3
('n', 'a', 'v', 'e', 'e', 'n')
>>>
//range
>>> list(range(15))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
>>> 
//sorted
>>> fruit = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
>>> for f in sorted(set(fruit)):
...     print(f)
...
apple
banana
orange
pear
>>>
///dictionary
>>> name = {'name1': 12, 'name2': 13}
>>> name
{'name1': 12, 'name2': 13}
>>> name['hello'] = 123
>>> name
{'name1': 12, 'name2': 13, 'hello': 123}

///delete 
>>> del name['name1']
>>> name
{'name2': 13, 'hello': 123}
