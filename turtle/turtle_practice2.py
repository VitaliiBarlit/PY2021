import turtle as t


axiom = 'a'
axmTemp = ''
itr = 9
dl = 3
angl = 60

t.hideturtle()
t.penup()
t.setx(-400)
t.sety(-400)
t.pendown()
t.tracer(0)

translate = {'+':'+',
             '-':'-',
             'a':'b-a-b',
             'b':'a+b+a'}

for k in range(itr):
    for ch in axiom:
        axmTemp += translate[ch]
        axiom = axmTemp
        axmTemp = ''
        
for ch in axiom:
    if ch == '+':
        t.right(angl)
    elif ch == '-':
        t.left(angl)
    else:
        t.forward(dl)