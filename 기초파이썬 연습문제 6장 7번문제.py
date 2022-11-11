Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shpae("turtle")
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    t.shpae("turtle")
AttributeError: 'Turtle' object has no attribute 'shpae'
>>> t.shape("turtle")
>>> 
>>> count = 0
>>> t.lt(30)
>>> for i in range(7):
	t.fd(100); t.fd(-30); t.lt(60); t.fd(30); t.fd(-30);
	t.rt(120); t.fd(30); t.fd(-30); t.lt(60); t.fd(-70); t.lt(60);

>>> 
