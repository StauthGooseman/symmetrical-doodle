from turtle import *

TurtleScreen._RUNNING = True
setup(1., 1.)
tracer(False)
ht()
pu()
setpos(0,0)
pd()
speed(10)
width(1)

b=10000

def space(N, a=0, b=1):
    return [i/N*abs(b-a)+min(b,a) for i in range(N+1)]

intT = space(b, 100, 100.1)
intD = space(b, 0, b*0.3)
intA = [i**(1/2) for i in intD[::3]]

for i in range(b):
    fd(intD[i])
    # bk(d*0.1)
    lt(intT[i])
    d += 1
    # t *= 1.001
    

update()
exitonclick()
# setpos(0,0)
# for i in range(100):
#     fd(d)
#     lt(10)
#     d *= 0.9