import pyautogui
import keyboard  # using module keyboard
from collections import OrderedDict


# Cookie center position: X:  291 Y:  468
# Cursor white pixel X: 1694 Y:  295 Colour: (255, 255, 255)
# Grandma white pixel X: 1745 Y:  358 Colour: (255, 255, 255)
# Farm white pixel X: 1723 Y:  424 Colour: (255, 255, 255)
# Mine white pixel X: 1706 Y:  487 Colour: (255, 255, 255)
# Factory white pixel X: 1753 Y:  550 Colour: (255, 255, 255)
# Bank white pixel X: 1722 Y:  618 Colour: (255, 255, 255)
# Temple white pixel X: 1722 Y:  618 Colour: (255, 255, 255)
# Wizard white pixel X: 1747 Y:  743 Colour: (255, 255, 255)
# Shipment white pixel X: 1702 Y:  810 Colour: (255, 255, 255)
# Alchemy Lab white pixel X: 1696 Y:  866 Colour: (160, 172, 180)??
# Portal white pixel

# buildings = {
#     "Cursor":(1694, 295), # Colour: (255, 255, 255)
#     "Grandma" : (1745, 358), # Colour: (255, 255, 255)
#     "Farm" : (1723, 424), # Colour: (255, 255, 255)
#     "Mine" : (1706, 487), # Colour: (255, 255, 255)
#     "Factory" : (1753, 550), # Colour: (255, 255, 255)
#     "Bank" : (1722, 618), # Colour: (255, 255, 255)
#     "Temple" : (1712, 681), # Colour: (255, 255, 255)
#     "Wizard" : (1747, 743), # Colour: (255, 255, 255)
#     "Shipment" : (1702, 810), # Colour: (255, 255, 255)
#     "Alchemy_Lab" : (1696,866) # Colour: (160, 172, 180)??
#     }

buildings = OrderedDict([
    ("Alchemy_Lab",(1696,866)),
    ("Shipment",(1702, 810)),
    ("Wizard",(1747, 743)),
    ("Temple",(1712, 681)),
    ("Bank",(1722, 618)),
    ("Factory",(1753, 550)),
    ("Mine",(1706, 487)),
    ("Grandma",(1745, 358)),
    ("Cursor",(1694, 295)),
    ("Farm",(1723, 424))
    ])

white = (255,255,255)

run = True

# def isWhite(coordinates):
#     im = pyautogui.screenshot()
#     x = int(buildings[coordinates][0])
#     y = int(buildings[coordinates][1])
#     px_co = (x , y)
#     if im.getpixel(px_co) == white:
#         return True

def isWhite(coordinates,im):
    if im.getpixel(buildings.get(coordinates)) == white:
        return True

def stopRunning():
    if keyboard.is_pressed('q'):
        run = False

while run:  # making a loop
    stopRunning()
    while True:
        im = pyautogui.screenshot()
        for building in buildings.keys():
            if isWhite(building,im):
                pyautogui.click(buildings.get(building), button='left', clicks=1)
        for step in range(100):
            pyautogui.click(291, 468, button='left')
        stopRunning()
