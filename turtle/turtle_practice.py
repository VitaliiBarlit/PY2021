import turtle


turtle.hideturtle()
turtle.speed(0)
turtle.tracer(1)
turtle.penup()
turtle.setposition(0,10)
turtle.pendown()
turtle.pensize(2)

axiom = 'F+F+F+F+'
axiom_temp= ''
iteration_deep = 3

dl = 24
angl  = 90

translate = {'+':'+', '-':'-', 'F':'F+F-f-F+F', 'f':'f'}


for i in range(iteration_deep):
    for ch in axiom:
        axiom_temp += translate[ch]
    axiom = axiom_temp
    axm_tenp = ''


turtle.fillcolor('#99BBFF')
turtle.begin_fill()
for ch in axiom:
    if ch == '+':
        turtle.right(45)
        turtle.forward(8)
        turtle.right(45)
#        turtle.right(angl)
    elif ch == '-':
        turtle.left(45)
        turtle.forward(8)
        turtle.left(45)
#        turtle.left(angl)
    else:
        turtle.forward(dl)
turtle.end_fill()
        
turtle.update()
turtle.mainloop()
        
        
