Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
name = 'pogpong'
print(name)
pogpong
type(name)
<class 'str'>
name.lower()
'pogpong'
name.uper()
Traceback (most recent call last):
  File "<pyshell#4>", line 1, in <module>
    name.uper()
AttributeError: 'str' object has no attribute 'uper'. Did you mean: 'upper'?
name.upper()
'POGPONG'
friend='dan'
print('hellodan how are you')
hellodan how are you
print('hello'+friend+ 'how are you')
hellodanhow are you
monry = 10
print( 'dan can borrow your money 10 baht')
dan can borrow your money 10 baht
print(friend + 'can i borrow' + 'baht')
dancan i borrowbaht
print(friend + 'can i borrow'+money + 'baht')
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    print(friend + 'can i borrow'+money + 'baht')
NameError: name 'money' is not defined. Did you mean: 'monry'?
type(money)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    type(money)
NameError: name 'money' is not defined. Did you mean: 'monry'?
type(money)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    type(money)
NameError: name 'money' is not defined. Did you mean: 'monry'?
money=10
type(money)
<class 'int'>
print(friend + 'can i borrow'+ str(money) + 'baht')
dancan i borrow10baht
print('{} can i borrow {}  baht'.format(friend,money) )
dan can i borrow 10  baht
print(f'{friend}can i borrow {money} baht')
dancan i borrow 10 baht
money = 12368
print(f'{money:,}')
12,368
print(f'{money:,.2f}')
12,368.00
>>> print('{money:,}'.format(money))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    print('{money:,}'.format(money))
KeyError: 'money'
>>> print('{:,.2f}'.format(money))
12,368.00
>>> import maht
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import maht
ModuleNotFoundError: No module named 'maht'
>>> import maht
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    import maht
ModuleNotFoundError: No module named 'maht'
>>> import maht
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    import maht
ModuleNotFoundError: No module named 'maht'
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2023, 2, 14, 17, 43, 5, 525731)
>>> datetime.now().strftime('%y%m%d %h %m %s')
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    datetime.now().strftime('%y%m%d %h %m %s')
ValueError: Invalid format string
>>> datetime.now().strftime('%y%m%d %h %m %s')
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    datetime.now().strftime('%y%m%d %h %m %s')
ValueError: Invalid format string
]
>>> import random
>>> random.randint(1,7)
4
