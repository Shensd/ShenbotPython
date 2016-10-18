from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random
import time

def new_inspire(txt):
    name   = "assets/pics/wallpapers/temp.jpg"
    text   = txt
    quote  = ""

    random.seed(time.time())
    rand_quote = random.randint(1, 16)
    if( rand_quote == 1 ):
        quote = "Go Fuck Yourself."
    elif(rand_quote == 2):
        quote = "The Universe Don't Seem Like It Be, But It Do."
    elif(rand_quote == 3):
        quote = "Waterboarding at Guantanamo Bay sounds super rad if you don't know what either of those things are."
    elif(rand_quote == 4):
        quote = "There should be confetti in tires so when there is a blow out it's still kind of an okay day"
    elif(rand_quote == 5):
        quote = "Of all the bodily functions that could be contagious, thank god it's the yawn."
    elif(rand_quote == 6):
        quote = "'DO NOT TOUCH' would probably be a really unsettling thing to read in braille."
    elif(rand_quote == 7):
        quote = "The best item to protect you from sasquatch attacks is a camera."
    elif(rand_quote == 8):
        quote = "Bushing your teeth is the only time you clean your skeleton"
    elif(rand_quote == 9):
        quote = "Making fun of a fat person at the gym is like making fun of a homeless person at a job fair."
    elif(rand_quote == 10):
        quote = "Dogs probably destroy shoes because they see humans put them on before they leave the house."
    elif(rand_quote == 11):
        quote = "The sinking of the Titanic must have been a miracle to the lobsters in the kitchen."
    elif(rand_quote == 12):
        quote = "If Goldilocks tried three beds, then Momma Bear and Daddy Bear slept seperately. Baby Bear is probably the \nonly thing keeping the family together."
    elif(rand_quote == 13):
        quote = "When you drink alcohol you are just borrowing happiness from tomorrow"
    elif(rand_quote == 14):
        quote = "What are snails even trying to do"
    elif(rand_quote == 15):
        quote = "Dog food could say it's any flavor it wants, you're not going to test it."
    elif(rand_quote == 16):
        quote = "Kissing just makes a big tube with assholes on either end."


    random.seed(time.time() + 839201)
    rand_wallpaper = random.randint(1, 5)
    wallpaper = "assets/pics/wallpapers/{}.jpg".format(rand_wallpaper)

    img  = Image.open(wallpaper)
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("assets/fonts/comic-sans.ttf", 35)
    draw.text((27, 23), "@" + text + "\n" + quote, (0, 0, 0), font=font)
    draw.text((25, 25), "@" + text + "\n" + quote, (255, 255, 255), font=font)
    img.save(name)
