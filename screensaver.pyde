#resolution
def setup():
    size(800,600)
    background(0)
    squid = loadImage("squid.png")
    imageMode(CENTER)
    x = 300
    y = 400
    o = 2
    p = 2
    global x,y,o,p,squid

    
def draw():

    background(0)
    image(squid,x,y,200,200)
    global x,y,o,p
    x = x + o
    y = y + p
    if x > 710:
        o = -2
    if x < 90:
        o = 2
    if y < 30:
        p = 2 
    if y > 570:
        p = -2
    
    
    
