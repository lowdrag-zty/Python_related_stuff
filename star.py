
import turtle as t


t.pensize(4)
t.hideturtle()


t.circle(50,steps =3)
t.circle(50)
t.pu()
t.goto(25 * (3 ** 0.5),25)
t.pd()
for i in range(0,3):
	t.lt(120)
	t.fd(50 * (3 ** 0.5))

t.pu()
t.goto(0,49)
t.pd()
t.pensize(4)
t.circle(1)
t.done()






'''
import turtle as t

t.pensize(4)
t.hideturtle()
t.speed(1)
t.fillcolor('red')
t.pencolor('red')
t.fill(True)

for i in range(0,5):
	t.fd(100)
	t.lt(72)
	t.fd(100)
	t.right(144)

t.fill(False)
'''