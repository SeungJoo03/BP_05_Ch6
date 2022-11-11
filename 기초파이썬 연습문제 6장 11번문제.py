Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 24 2015, 22:44:40) [MSC v.1600 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> import turtle
>>> t = turtle.Turtle()
>>> t.shape("turtle")
>>> t.color('red', 'yellow')
>>> t.begin_fill()
>>> while True:
	t.forward(200)
	t.left(170)
	if abs(t.pos()) < 1:
		break
	t.end_fill()

	
>>> 
