#일반적인 프로그램
color=""
speed=0

def upspeed():
    global speed
    speed+=10

def downspeed():
    global speed
    speed-=10

color ="white"
print("색상: ",color)
print("속도: ",speed)

upspeed()
print("속도: ",speed)


color2=""
speed2=0

def upspeed2():
    global speed2
    speed2+=10

def downspeed2():
    global speed2
    speed2-=10

color ="yellow"
print("색상: ",color)
print("속도: ",speed2)

upspeed2()
print("속도: ",speed2)