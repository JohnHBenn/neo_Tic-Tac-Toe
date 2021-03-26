import time
import adafruit_trellism4

trellis = adafruit_trellism4.TrellisM4Express()
def setup():
    global red
    global blue
    global nowin
    global color
    global colour

    trellis.pixels.fill(clear)
    
    for y in range (4):
        trellis.pixels[6,y] = color
    for x in range (6,1,-1):
            trellis.pixels[x,3] = color
    for y in range (3,-1,-1):
            trellis.pixels[2,y] = color
time.sleep(0.35)
red = (10,0,0)
blue = (0,0,10)
nowin = (10,0,10)
clear = (0,0,0)
color = red
colour = blue

a = (5,2)
b = (4,2)
c = (3,2)
d = (5,1)
e = (4,1)
f = (3,1)
g = (5,0)
h = (4,0)
i = (3,0)

soln = [[a,b,c],[d,e,f],[g,h,i],[a,d,g],[b,e,h],[c,f,i],[a,e,i],[c,e,g]]
setup()
for y in range (4):
        trellis.pixels[6,y] = color
for x in range (6,1,-1):
        trellis.pixels[x,3] = color
for y in range (3,-1,-1):
        trellis.pixels[2,y] = color

while True:
    pressed = set(trellis.pressed_keys)

    for press in pressed:
        if press:
            x, y = press

            if x<=5 and x>=3 and y<=2:      #sets parameters for buttons that can be pressed
                if trellis.pixels[x,y] == (0,0,0):
                    trellis.pixels[x,y] = color
                    for y in range (4):
                        trellis.pixels[6,y] = colour
                    for x in range (6,1,-1):
                        trellis.pixels[x,3] = colour
                    for y in range (3,-1,-1):
                        trellis.pixels[2,y] = colour
                
                    if color == red:
                        color = blue
                        colour = red
                    elif color == blue:
                        color = red
                        colour = blue
    for i in range(8):
        if trellis.pixels[soln[i][0]] == red and trellis.pixels[soln[i][1]] == red and trellis.pixels[soln[i][2]] == red:
            trellis.pixels.fill(red)
            time.sleep(1)
            setup()
        if trellis.pixels[soln[i][0]] == blue and trellis.pixels[soln[i][1]] == blue and trellis.pixels[soln[i][2]] == blue:
            trellis.pixels.fill(blue)
            time.sleep(1)
            setup()
    if trellis.pixels[5,2] != clear and trellis.pixels[4,2] != clear and trellis.pixels[3,2] != clear and trellis.pixels[5,1] != clear and trellis.pixels[4,1] != clear and trellis.pixels[3,1] != clear and trellis.pixels[5,0] != clear and trellis.pixels[4,0] != clear and trellis.pixels[3,0] != clear:
        trellis.pixels.fill(nowin)
        time.sleep(1)
        setup()
