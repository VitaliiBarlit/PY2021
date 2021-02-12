import turtle


t = turtle.Turtle()
screen = turtle.Screen()
turtle.hideturtle()
turtle.speed(0)
turtle.tracer(1000)
turtle.penup()
turtle.setposition(-200, 200)
turtle.pendown()
turtle.pensize(2)
screen.screensize(3840,2160)
t.getscreen()
axiom = '-YF'
axiom_temp= ''
iteration_deep = 2

dl = 30
angl  = 90

translate = {'+':'+', '-':'-', 
             'X':'XFX-YF-YF+FX+FX-YF-YFFX+YF+FXFXYF-FX+YF+FXFX+YF-FXYF-YF-FX+FX+YFYF-',
             'Y':'+FXFX-YF-YF+FX+FXYF+FX-YFYF-FX-YF+FXYFYF-FX-YFFX+FX+YF-YF-FX+FX+YFY',
             'F':'F'}
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
        turtle.forward(15)
turtle.end_fill()


turtle.update()
turtle.mainloop()
        
        
