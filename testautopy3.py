import autopy

screen = autopy.bitmap.capture_screen()
# debug = autopy.bitmap.Bitmap.open("bug.png")
# pos = screen.find_bitmap(debug)

while True:
    mousePos = autopy.mouse.location()
    color = screen.get_color(mousePos[0],mousePos[1])
    print(mousePos)


# colorPos = screen.find_color((89,90,182),0.1)
# print(colorPos)
# autopy.mouse.move(colorPos[0],colorPos[1])
