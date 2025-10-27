from tkinter import *
from PIL import Image, ImageDraw, ImageTk

if not hasattr(Image, "Resampling"): # Pillow<9.0
    Image.Resampling = Image
from random import randint
from math import sin, cos, pi

scaleFactor = 4
appWidth = 400
appHeight = 400

app = Tk()
app.geometry("400x400")

canvas = Canvas(app, bg = "green")
canvas.pack(fill=BOTH, expand = 1)

myImage = Image.new(
    "RGB",
    (appWidth * scaleFactor, appHeight * scaleFactor),
    color = "green",
)

drawingContext = ImageDraw.Draw(
    myImage, "RGBA"
)

def drawShaun(x, y):
    #195*115
    #legs
    for l in range(2):
        drawingContext.rectangle(((x+30+50*l), y+60, (x+30+50*l)+10, y+115), fill='black')
        drawingContext.rectangle(((x+30+50*l)+20, y+60, (x+30+50*l)+30, y+115), fill='black')
    #body
    for i in range(3):
        drawingContext.ellipse([(x+40*i, y), (x+60+40*i, y+60)], fill="white")
    for j in range(2):
        drawingContext.ellipse([((x+20)+40*j, y+30), ((x+20)+60+40*j, y+90)], fill="white")
    #tail
    drawingContext.ellipse([(x+125, y+35), (x+155, y+85)],fill="white") 
    #face
    drawingContext.ellipse([(x-20, y+10), (x+20, y+70)],fill="black")    
    #ears
    drawingContext.ellipse([(x-40, y+20), (x-10, y+30)],fill="black")
    drawingContext.ellipse([(x+10, y+20), (x+40, y+30)],fill="black")
    #hair
    for h in range(2):
        drawingContext.ellipse([((x-17)+15*h, y+5), ((x-17)+20+15*h, y+25)], fill="white")

def drawGrass(x, y):
    #120*50
    drawingContext.line([(x-20, y), (x, y+50)], fill="lightgreen" , width=2)
    drawingContext.line([(x+20, y), (x+20, y+50)], fill="lightgreen" , width=2)
    drawingContext.line([(x+60, y), (x+40, y+50)], fill="lightgreen" , width=2)

for _ in range(10):
    grassX = randint(30, appWidth * scaleFactor - 150)
    grassY = randint(30, appHeight * scaleFactor - 80)
    drawGrass(grassX, grassY)

for _ in range(7):
    shaunX = randint(30, appWidth * scaleFactor - 200)
    shaunY = randint(30, appHeight * scaleFactor - 130)
    drawShaun(shaunX, shaunY)

myImage = myImage.resize((appWidth, appHeight), Image.Resampling.LANCZOS)
myImage.save("myImage.png", bitmap_format = "png")
myImage = ImageTk.PhotoImage(myImage)
canvas.create_image(0,0,image=myImage, anchor="nw")

app.mainloop()