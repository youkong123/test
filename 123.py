Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:14:34) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import random
>>> y=[]
>>> for x in range(1000):import random
>>> y=[]
>>> for x in range(/;\1000):
	y.append(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))

	
>>> dic={}
>>> for i in y:
	if i in dic:
		continue
	else:
		dic[i]=y.count(i)

	y.append(random.choice('abcdefghijklmnopqrstuvwxyz!@#$%^&*()'))

	
>>> dic={}
>>> for i in y:
	if i in dic:
		continue
	else:
		dic[i]=y.count(i)

		
>>> dic
{'y': 27, '^': 29, 'p': 27, 't': 31, 'a': 30, '*': 24, 'g': 28, 's': 29, 'u': 23, 'e': 19, 'j': 32, '&': 29, 'z': 27, 'n': 27, 'm': 30, ')': 32, 'd': 21, '@': 18, 'q': 23, '%': 21, 'k': 27, 'c': 33, '(': 31, 'x': 24, '#': 24, 'f': 34, 'h': 22, 'l': 42, '$': 32, 'r': 25, 'i': 28, 'b': 36, '!': 25, 'o': 32, 'w': 31, 'v': 27}
>>> z=dic.sort
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    z=dic.sort
AttributeError: 'dict' object has no attribute 'sort'
>>> z=[dic]
>>> z
[{'y': 27, '^': 29, 'p': 27, 't': 31, 'a': 30, '*': 24, 'g': 28, 's': 29, 'u': 23, 'e': 19, 'j': 32, '&': 29, 'z': 27, 'n': 27, 'm': 30, ')': 32, 'd': 21, '@': 18, 'q': 23, '%': 21, 'k': 27, 'c': 33, '(': 31, 'x': 24, '#': 24, 'f': 34, 'h': 22, 'l': 42, '$': 32, 'r': 25, 'i': 28, 'b': 36, '!': 25, 'o': 32, 'w': 31, 'v': 27}]
>>> z.sort
<built-in method sort of list object at 0x03C881E8>
>>> z.sorted
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    z.sorted
AttributeError: 'list' object has no attribute 'sorted'
>>> for k,v in dic.items():
        print(k,':',v)
        break











        


        
        
