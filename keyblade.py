from PIL import Image,ImageFont,ImageDraw
from random import randint

# GUI Tool
import tkinter as tk

# To get all png files in dir
import glob, os

def random_color():
    r=randint(50,255)
    g=randint(50,255)
    b=randint(50,255)
    return r,g,b
def choice(png):
    choicePage = tk.Tk()
    width = choicePage.winfo_screenwidth()
    height = choicePage.winfo_screenheight()
    choicePage.geometry(str(width)+ "x" + str(height)) #Sets resolution
    label1 = tk.Label(text="Enter the word you would like to use?")
    label.grid(row = 0,column = 0)
    entry1 = tk.Entry(choicePage)
    entry1.grid(row = 1,column = 0)

    # Bad implementation (need to fix)
    def confirm():
        wordart(png,entry1.get().upper())
    confirm_button = tk.Button(choicePage,text='Confirm',command = confirm)
    confirm_button.grid(row = 2,column = 0)

    choicePage.mainloop()
def wordart(png,word):
    print(word)
    text = word * 100 #Number of times to repeat word

    img = Image.open(png, "r").convert("RGB")
    img_h,img_w = img.size
    pixel = img.load()

    # Establish a black screen for base
    base =Image.new('RGBA',(img_h,img_w),'black')
    text_size = int(img_w / 50) #Making text size according to dimension
    font=ImageFont.truetype("arial.ttf",text_size)
    width, height= font.getsize(text)
    draw=ImageDraw.Draw(base)

    r, g, b = random_color()
    height_counter= height
    # Sets silhoutte text
    silhoutte = 'Keyblade'

    # Makes all lines of text
    while (height_counter < base.size[1]):
        r, g, b = random_color()
        start= randint(0,len(word)-1) # Staggers the text
        draw.text((0,height_counter),word[start:len(word)]+text, font=font, fill=(r,g,b))
        height_counter += height

    hor = []
    vert = []
    # Formats text into white space of image
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            if (pixel[i,j] != (255,255,255)):
                hor.append(i)
                vert.append(j)

    # Gets rid of outline of image
    final_art =Image.new('RGBA',(img_h,img_w),'black')
    for i,j in zip(hor,vert):
            final_art.putpixel((i,j),base.getpixel((i,j)))

    final_art.show()
    final_art.save("wordart.png")

window = tk.Tk()
width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(str(width)+ "x" + str(height)) #Sets resolution
window.columnconfigure(0,weight=1)
label = tk.Label(text="Select an image that you would like to use: ")
label.grid(row=0,column=0)

#Gets all png files in the dir and makes them into buttons
for i,file in enumerate(glob.glob(os.getcwd()+ "/**/*.png",recursive=True),start = 1):
    png = os.path.basename(file) #Gets file name from path
    b = tk.Button(window,text=png)
    b.grid(row=i, column=0)
    b.config(command = lambda b= b: choice(b['text']))

window.mainloop()
