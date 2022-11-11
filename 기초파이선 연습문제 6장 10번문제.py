Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
SyntaxError: invalid syntax
>>> 
>>> count = 0
>>> 
>>> while True:
	t.fd(100); t.rt(90); t.fd(20); t.rt(90); t.fd(100); t.lt(90); t.fd(20);
	t.lt(90);

	
count += 1
if(count == 7):
break;
