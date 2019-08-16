import autopy
import time

def findgamearea():
    for i in range(50):
        screen = autopy.bitmap.capture_screen()
        s = autopy.bitmap.Bitmap.open("s.png")
        gamepos = screen.find_bitmap(s)
        if gamepos:
            print("find at",gamepos)
            return gamepos
        else:
            print("cannot find game area "+ str(i+1) + "/50")
    exit()

def grabAndSave(gamepos):
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,True)
    autopy.mouse.move(gamepos[0]+602,gamepos[1]+149)
    autopy.mouse.toggle(autopy.mouse.Button.LEFT,False)
    


def findfish(gamepos):
    screen = autopy.bitmap.capture_screen()
    print(gamepos)
    fisPos = screen.find_color((254,57,11),0.05,((gamepos[0]+18,gamepos[1]+139),(430,251)))
    if not fisPos:
        fisPos = screen.find_color((252,114,22),0.05,((gamepos[0]+18,gamepos[1]+139),(430,251)))
    print("fish at : "+ str(fisPos))
    if fisPos:
        autopy.mouse.move(fisPos[0],fisPos[1])
        grabAndSave(gamepos)
        return True
    else:
        return False

# def endgame(gamepos):
#     screen = autopy.bitmap.capture_screen()
#     ok = autopy.bitmap.Bitmap.open("endgame.png")
#     okpos = screen.find_bitmap(ok,0.05,((gamepos[0]+18,gamepos[1]+139),(430,500)))
#     if okpos:
#         print("endgame")
#         exit()

def startgame():
    gamepos = findgamearea()
    while True:
        findfish(gamepos)
        # endgame(gamepos)
startgame()


# 400.203

# 392.342
# 822.593

# 1002.352

# 8.139
# 430.251
# 602.149