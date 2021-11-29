def setup():
    size(800,600)
    attackpicker = 0
    buffpicker = 0
    mouseX = 0
    mouseY= 0
    x= 0
    buffpicker = random(7)
    frameRate(10)
    att1 = loadImage("AttackCard1.png")
    att2 = loadImage("AttackCard2.png")
    att3 = loadImage("AttackCard3.png")
    att4 = loadImage("AttackCard4.png")
    att5 = loadImage("AttackCard5.png")
    att6 = loadImage("AttackCard6.png")
    att7 = loadImage("AttackCard7.png")
    buf1 = loadImage("BuffCard1.png")
    buf2 = loadImage("BuffCard2.png")
    buf3 = loadImage("BuffCard3.png")
    buf4 = loadImage("BuffCard4.png")
    buf5 = loadImage("BuffCard5.png")
    buf6 = loadImage("BuffCard6.png")
    global attackpicker, att1, att2, att3, att4, att5, att6, att7, buf1, buf2, buf3, buf4, buf5, buf6
def draw():
    #attack cardbox
    global attackpicker, att1, att2, att3, att4, att5, att6, att7
    fill(256)
    rect(90,50,200,100)
    textSize(15)
    fill(0)
    text("click here ONCE for\n a random ATTACK card.",100,110)
    
    if mouseX>= 90 and mouseX <= 290 and mouseY >=50 and mouseY <= 150 and mousePressed:
        global attackpicker, att1, att2, att3, att4, att5, att6, att7
        attackpicker = int(random(1,8))  
        print(attackpicker)  
        if attackpicker == 1:
            image(att1,100 ,200)
        if attackpicker == 2:
            image(att2,100 ,200)
        if attackpicker == 3:
            image(att3,100 ,200)
        if attackpicker == 4:
            image(att4,100 ,200)
        if attackpicker == 5:
            image(att5,100 ,200)
        if attackpicker == 6:
            image(att6,100 ,200)
        if attackpicker == 7:
            image(att7,100 ,200)
            
    global attackpicker, att1, att2, att3, att4, att5, att6, att7, buf1, buf2, buf3, buf4, buf5, buf6
    #buff cardbox
    fill(256)
    rect(440,50,200,100)
    textSize(15)
    fill(0)
    text("click here ONCE \nfor a random BUFF card.",450,110)
    
    if mouseX>= 440 and mouseX <= 690 and mouseY >=50 and mouseY <= 150 and mousePressed:
        global buffpicker, buf1, buf2, buf3, buf4, buf5, buf6
        buffpicker = int(random(1,7))  
        print(buffpicker)  
        if buffpicker == 1:
            image(buf1,450,200)
        if buffpicker == 2:
            image(buf2,450,200)
        if buffpicker == 3:
            image(buf3,450,200)
        if buffpicker == 4:
            image(buf4,450,200)
        if buffpicker == 5:
            image(buf5,450,200)
        if buffpicker == 6:
            image(buf6,450,200)
            
            
