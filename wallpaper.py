from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import pylab as plt
import numpy as np
import ctypes
import os
import random
import time

def new_wallpaper(txt):
    name   = "assets/pics/wallpaper.jpg"
    text   = txt
    width  = 1920
    height = 1080

    random.seed(time.time())
    rand_cmap = random.randint(1, 5)
    if( rand_cmap == 1 ):
        cmap = "flag"
    elif(rand_cmap == 2):
        cmap = "cool"
    elif(rand_cmap == 3):
        cmap = "hsv"
    elif(rand_cmap == 4):
        cmap = "Purples"
    elif(rand_cmap == 5):
        cmap = "prism"

    rand = np.random.random((int(height), int(width)))

    fig = plt.imshow(rand, interpolation='nearest')
    fig.axes.get_xaxis().set_visible(False)
    fig.axes.get_yaxis().set_visible(False)
    plt.axis('off')

    plt.set_cmap(cmap)
    plt.savefig(name, bbox_inches='tight', pad_inches=0)

    img  = Image.open(name)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assets/fonts/comic-sans.ttf", 30)
    draw.text((25, 25), "@" + text, (0, 0, 0), font=font)
    draw.text((450, 250), "Love, \nShenbot", (0, 0, 0), font=font)
    img.save(name)
