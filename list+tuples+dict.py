Python 2.7.11 (v2.7.11:6d1b6a68f775, Dec  5 2015, 20:32:19) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> [1, 3] + [4, 5]
[1, 3, 4, 5]
>>> [[1, 3]] + [[4, 5]]
[[1, 3], [4, 5]]
>>> (1, 3) + (4, 5)
(1, 3, 4, 5)
>>> ((1, 3)) + ((4, 5))
(1, 3, 4, 5)
>>> [[1, 3] + [4, 5]]
[[1, 3, 4, 5]]
>>> (1, 3), + (4, 5),

Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    (1, 3), + (4, 5),
TypeError: bad operand type for unary +: 'tuple'
>>> ((1, 3),) + ((4, 5),)
((1, 3), (4, 5))
>>> [1, 4] + (1, 3)

Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    [1, 4] + (1, 3)
TypeError: can only concatenate list (not "tuple") to list
>>> {1: 3} + {1: 4}

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    {1: 3} + {1: 4}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> {1: 3} + {2: 4}

Traceback (most recent call last):
  File "<pyshell#9>", line 1, in <module>
    {1: 3} + {2: 4}
TypeError: unsupported operand type(s) for +: 'dict' and 'dict'
>>> 
