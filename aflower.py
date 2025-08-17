import turtle
t = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('#262626')
t.fillcolor('#7c909c')
t.speed(50)
col = ('#ED7864','#7a3d46', '#6E544F', '#592F2F', '#6E382E')
for n in range(5):
    for x in range(8):
        t.speed(x + 50)
        for i in range(2):
            t.pensize(2)
            t.circle(80 + n * 20, 90)
            t.lt(90)
        t.lt(50)
    t.pencolor(col[n % 4])
# Move exitonclick outside the loops
s.exitonclick()