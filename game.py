import turtle as t


win=t.Screen()
win.tracer(0)
win.setup(800,600)
win.bgcolor("blue")
win.title("Pong Game")


# Score 
score_a=0
score_b=0

#score_board
pen=t.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A:0 Player B:0",align="center",font= ("Ariel",24))

#Paddle
def pad_setting(pad,x):
    pad.speed(0)
    pad.shape("square")
    pad.color("white")
    pad.shapesize(stretch_wid=5,stretch_len=1)
    pad.penup()
    if(x=="left"):
        pad.goto(-380,0)
    else:
        pad.goto(380,0)

left_pad=t.Turtle()
pad_setting(left_pad,"left")
right_pad=t.Turtle()
pad_setting(right_pad,"right")







#moving paddles function
def left_up():
    left_pad.sety(left_pad.ycor()+20) 
def left_down():
    left_pad.sety(left_pad.ycor()-20)
def right_up():
    right_pad.sety(right_pad.ycor()+20)
def right_down():
    right_pad.sety(right_pad.ycor()-20)

win.listen()
win.onkeypress(left_up,'w')
win.onkeypress(left_down,'s')
win.onkeypress(right_up,'Up')
win.onkeypress(right_down,'Down') 

#ball

ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.dx=0.1
ball.dy=0.1

while(True):
    win.update() 
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    # up wall

    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1
    
    # down wall
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    #right wall
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx*=-1
        score_a+=1
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font= ("Ariel",24,"normal"))


    #left wall
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx*=-1
        score_b+=1  
        pen.clear()
        pen.write("Player A:{} Player B:{}".format(score_a,score_b),align="center",font= ("Ariel",24,"normal"))


    #Collision with paddle
    if ball.xcor()>370 and right_pad.ycor()-50 < ball.ycor() <right_pad.ycor()+50:
        ball.setx(360)
        ball.dx*=-1
    
    if ball.xcor()<-370 and left_pad.ycor()-50 < ball.ycor()<left_pad.ycor()+50:
        ball.setx(-360)
        ball.dx*=-1
