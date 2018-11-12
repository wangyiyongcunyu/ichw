import turtle
import math
wn=turtle.Screen()
wn.bgcolor("black")

def format(turtle,size,k):
    colors=['yellow','blue','red','green','orange','white','brown']
    turtle.color(colors[k])
    turtle.shape('circle')
    turtle.shapesize(size,size,1)
    turtle.speed(0)

def orbit(turtle,x,y,z,t,d):
    if z==0:
        turtle.stamp()
    else:
        if t==0:
            turtle.up()
            turtle.goto(x*math.cos(math.radians(1/z))+d,y*math.sin(math.radians(1/z)))
            turtle.down()
            turtle.showturtle() 
        else:
            turtle.goto(x*math.cos(math.radians(t/z))+d,y*math.sin(math.radians(t/z)))

mer=turtle.Turtle() 
format(mer,0.2,1)
ven=turtle.Turtle()
format(ven,0.2,2)
ear=turtle.Turtle()
format(ear,0.3,3)
mar=turtle.Turtle()
format(mar,0.3,4)
jup=turtle.Turtle() 
format(jup,0.5,5)
sat=turtle.Turtle() 
format(sat,0.7,6)
sun=turtle.Turtle() 
format(sun,1,0)

    
for i in range(10000):
    orbit(sun,1,1,0,1,0)
    orbit(mer,25,24,0.1,i,-7)
    orbit(ven,61,60,0.2,i,-11)
    orbit(ear,91,84,0.3,i,-35)
    orbit(mar,123,120,0.4,i,-27)
    orbit(jup,175,168,0.5,i,-45)
    orbit(sat,290,286,0.6,i,-48)
