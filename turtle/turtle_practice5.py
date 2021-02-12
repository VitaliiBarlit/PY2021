import turtle

turtle.hideturtle()
turtle.speed(0)
turtle.tracer(1000)
turtle.penup()
turtle.setposition(-200, -100)
turtle.pendown()
turtle.pensize(2)

axiom = 'F+F+F+F'
axiom_temp= ''
iteration_deep = 3

dl = 30
angl  = 90

translate = {'+':'+', '-':'-', 
             'F':'F+F-F-FF+F+F-F'}
             #'F':'F-G+F+G-F', 'G': 'GG'}


for i in range(iteration_deep):
    for ch in axiom:
        axiom_temp += translate[ch]
    axiom = axiom_temp
    axiom_temp = ''


turtle.fillcolor('#99BBFF')
turtle.begin_fill()
for ch in axiom:
    if ch == '-':
        turtle.right(90)
#        turtle.forward(8)
#        turtle.right(45)
#        turtle.right(angl)
    elif ch == '+':
        turtle.left(90)
#        turtle.forward(8)
#        turtle.left(45)
#        turtle.left(angl)       
    else:
        turtle.forward(8)
turtle.end_fill()


turtle.update()
turtle.mainloop()
        
        
