import threading
import asyncio
import discord

noGod = False

def term_commands():
    global noGod
    responce = input("").lower()
    if responce == "help":
        print("*help ------- View terminal commands")
        print("*togs ------- Toggle voteskip command")
    elif responce == "togs":
        noGod = not noGod
        print("Disable voteskip has been set to {}".format(noGod))
    else:
        print("Not a valid option.")
    term_commands()

def start_term():
    user = threading.Thread(target=term_commands)
    user.daemon = True
    user.start()
    user.join(2)
