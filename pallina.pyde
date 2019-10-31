width=500
x=100
y=120
x2=1
y2=1
lrect=(width/2)-25
lrect2=(width/2)+25
punti1=0
punti2=0
aggpunti=10
def setup():
    size(500,440)
    background(0,0,255)
    stroke(0,255,0)
def draw():
    global x,y,x2,y2,lrect,lrect2,punti1,punti2,aggpunti
    background(0,0,0)
    ellipse(x,y,50,50)
    x+=2*(x2)
    y+=2*(y2)
    fill(255,0,140)
    if x>=width or x<0:
        x2*= -1
    rect(lrect,height-25,80,25)
    if y+25>height-25 and x>=lrect and x<=lrect+80 :              #controlla se la pallina si trova all altezza della racchetta e compresa nella sua lunghezza
        y2*= -1                                                   #cambia la direzione decrementando la y
    rect(lrect2,0,80,25)
    if y<=40 and x>=lrect2 and x<=lrect2+80 :                     #fa la stessa cosa ma con l altra racchetta
        y2*= -1
    text(punti1, 420, height-80); 
    text(punti2, 20, 80);       
    textSize(40);
    if y>=width :                                                 #incrementa lo score quando la pallina tocca il foglio sia in alto che in basso
        punti2=punti2+aggpunti
        y=height/2
    if y<=0 :
        punti1=punti1+aggpunti
        y=height/2
    if punti1>=30 :                                              #limite di punti a 30 poi crea una nuova pagina con scritto il player vincitore
        aggpunti=0
        rect(0,0,width,height)
        fill(0,0,0)
        textSize(60);
        text("PLAYER 1 WIN", width/2-200 , height/2);
    if punti2>=30 :
        aggpunti=0
        rect(0,0,width,height)
        fill(0,0,0)
        textSize(60);
        text("PLAYER 2 WIN", width/2-200 , height/2);
    
def keyPressed():                                                #funzioni per riconoscere il tasto con cui far muovere la racchetta
    global lrect,lrect2
    if keyCode == RIGHT:
        print("right")
        lrect=lrect+25
        if lrect>=width-80:
            lrect=500-80
        
    if keyCode == LEFT:
        print("left")
        lrect=lrect-25
        if lrect<=0:
            lrect=0
    if key == "a" and lrect2>0:
        print("a")
        lrect2=lrect2-25
    
    if key == "d" and lrect2<=width-80:
        print("d")
        lrect2=lrect2+25

        
         
        
