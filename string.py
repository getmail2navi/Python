Python 3.6.4 (v3.6.4:d48eceb, Dec 19 2017, 06:04:45) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> x = 'naveen'
>>> x
'naveen'
>>> x + "is a bad"
'naveenis a bad'
>>> 
>>> X + "good"
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    X + "good"
NameError: name 'X' is not defined
>>> y = "ihavegoodhabits"
>>> y
'ihavegoodhabits'
>>>  y = "ihavegood'habits"
SyntaxError: unexpected indent
>>>  y = "ihavegood'habits'"
SyntaxError: unexpected indent
>>> x[0]
'n'
>>> x=[0-2]
>>> x
[-2]
>>> x[3]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    x[3]
IndexError: list index out of range
>>> x == [2]
False
>>> x=[-3]
>>> x
[-3]
>>> x=[0]
>>> x[0]
0
>>> x = 'naveen'
>>> x
'naveen'
>>> x[0]
'n'
>>> x[-3]
'e'
>>> s[0:3]
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    s[0:3]
NameError: name 's' is not defined
>>> x[0:3]
'nav'
>>> x[3:]
'een'
>>> 
