Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> import random
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> 
>>> for i in range(10):
	x = random.randint(1, 100)
	y = random.randint(1, 100)
	z = random.randint(-180, 180)
	t.up()
	t.goto(x, y)
	t.down()
	t.circle(z);

>>> 
