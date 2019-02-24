import pyautogui, sys
print('Press Ctrl-C to quit.')
try:
    while True:
        x, y = pyautogui.position()
        im = pyautogui.screenshot()
        colour = str(im.getpixel((x, y)))
        positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4) + " Colour: " + colour
        print(positionStr, end='')
        print('\b' * len(positionStr), end='', flush=True)
except KeyboardInterrupt:
    print('\n')
