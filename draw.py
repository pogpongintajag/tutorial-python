import turtle
tao=turtle.Pen()
tao.shape('turtle')
tao.left (45)
tao.forward(100)
for i in range(4):
    tao.left(40)
    tao.forward(30)


tao.right(40)
tao.forward(30)
for i in range(4):
    tao.left(40)
    tao.forward(30)


tao.right(20)
tao.forward(50)
tao.penup()
tao.goto(50,0)
tao.pendown()
for i in range(5):
    tao.left(80)
    tao.forward(50)




