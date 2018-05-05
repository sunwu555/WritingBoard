
from PIL import ImageTk, Image, ImageDraw
import PIL
import tkinter as tk
import numpy as np

width = 100
height = 100
center = height//2
white = (255, 255, 255)
green = (0,128,0)

def save():
    global Number
    global SaveName
    global k
    global image1
    global draw
    global cv
    global root

    filename = Number + '_' + str(k) + '.png'
    image2 = image1.resize((28, 28), Image.ANTIALIAS)
    image2.save('./dataset/' + filename)
    #image2 = image1.resize((50, 50), Image.ANTIALIAS)
    pix = np.array(image2)
    a = []
    for i in pix:
        for j in i:
            if j [0] > 100:
                a.append(0)
            else:
                a.append(1)
    f = open('./dataset/' + Number + '_' + str(k) + '.txt', "w")
    f.write(str(a))
    f.close()
    image1 = PIL.Image.new("RGB", (100, 100), (255,255,255))
    draw = ImageDraw.Draw(image1)
    cv = tk.Canvas(root, width = 100, height = 100, bg='gray90')
    cv.grid(row = 3, column = 1)
    cv.bind("<B1-Motion>", paint)
    k += 1
    SaveName.set('save as ' + Number + '_' + str(k))

def paint(event):
    # python_green = "#476042"
    x1, y1 = (event.x - 1), (event.y - 1)
    x2, y2 = (event.x + 1), (event.y + 1)
    cv.create_oval(x1, y1, x2, y2, fill="black",width=12)
    draw.line([x1, y1, x2, y2],fill="black",width=12)

def save_set():
    global SaveName
    global Number
    global k
    k = 0
    kk = str(k)
    Number = InputFile.get()
    SaveName.set('save as ' + Number + '_' + kk)

def clear_set():
    global draw
    global cv
    global root
    global image1

    image1 = PIL.Image.new("RGB", (100, 100), (255,255,255))
    draw = ImageDraw.Draw(image1)

    cv = tk.Canvas(root, width = 100, height = 100, bg='gray90')
    cv.grid(row = 3, column = 1)
    cv.bind("<B1-Motion>", paint)

root = tk.Tk()
k = 1
SaveName = tk.StringVar()

InputFile = tk.Entry(root, width = 20)
InputFile.grid(row = 1, column = 1, pady = 8)

button1 = tk.Button(text ='Get', width = 7, height = 2, command = save_set)
button1.grid(row = 2, column = 1, pady = 8)

# Tkinter create a canvas to draw on
cv = tk.Canvas(root, width=width, height=height, bg='gray90')
cv.grid(row = 3, column = 1)

# PIL create an empty image and draw object to draw on
# memory only, not visible
image1 = PIL.Image.new("RGB", (width, height), white)
draw = ImageDraw.Draw(image1)

# do the Tkinter canvas drawings (visible)
# cv.create_line([0, center, width, center], fill='green')
cv.bind("<B1-Motion>", paint)

# do the PIL image/draw (in memory) drawings
# draw.line([0, center, width, center], green)

# PIL image can be saved as .png .jpg .gif or .bmp file (among others)
# filename = "my_drawing.png"
# image1.save(filename)

button = tk.Button(textvariable = SaveName, width = 10, height = 2,command = save)
button.grid(row = 4, column = 1, pady = 8)

button2 = tk.Button(text = 'clear', width = 10, height = 2, command = clear_set)
button2.grid(row = 5, column = 1, pady = 8)

root.mainloop()
