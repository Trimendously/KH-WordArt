from PIL import Image,ImageFont,ImageDraw
from random import randint

def random_color():
    r=randint(50,255)
    g=randint(50,255)
    b=randint(50,255)
    return r,g,b
def choice():
    while True:
        choices = ['DARKNESS','LIGHT','FRIENDS','HEART'] #Most used words in KH
        print("Your options are : ", choices)
        word =input("Enter word:  ") #Word to make art
        word = word.upper()
        if word in choices:
            break

    return word
def wordart():
    word = choice()

    text = word * 100 #Number of times to repeat word

    # Establish a black screen for base
    base =Image.new('RGBA',(900,900),'black')

    font=ImageFont.truetype("arial.ttf",10)
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
        height_counter = height_counter + height

    art = Image.new('RGBA',(900,900),'black')
    font1 = ImageFont.truetype("arial.ttf",200)
    width, height = font1.getsize(silhoutte)
    draw1=ImageDraw.Draw(art)
    draw1.text(((art.size[0]-width)/2,(art.size[1]-height)/2),silhoutte, font=font1, fill='white')

    hor = []
    vert = []
    # Formats text into white space of image
    for i in range(art.size[0]):
        for j in range(art.size[1]):
            pixel=art.getpixel((i,j))
            if (pixel == (255,255,255,255)):
                hor.append(i)
                vert.append(j)
                #art.putpixel((i,j),base.getpixel((i,j)))

    # Gets rid of outline of image
    final_art =Image.new('RGBA',(900,900),'black')
    for i,j in zip(hor,vert):
            final_art.putpixel((i,j),base.getpixel((i,j)))

    final_art.show()
    final_art.save("wordart.png")

wordart()
