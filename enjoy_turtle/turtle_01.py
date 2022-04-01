#
import turtle

# s = turtle.getscreen()
#
# turtle.done()

t = turtle.Turtle()
# t.right(90)
# t.forward(100)
# t.left(90)
# t.backward(100)

# t.goto(100, 100)
# t.home()

# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)
# t.rt(90)
# t.fd(100)

# t.circle(60)

t.dot(60)

# t.bgcolor("blue")

t.begin_fill()
t.fd(100)
t.lt(120)
t.fd(100)
t.lt(120)
t.fd(100)
t.end_fill()

t.speed(1)
t.forward(100)
t.speed(10)
t.forward(100)

t.clear()

turtle.bgcolor("blue")

t.reset()

turtle.done()