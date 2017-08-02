import pyautogui
print('Press Ctrl+C to quit.')

while True:
    if KeyboardInterrupt == True:
        KeyboardInterrupt
        print('\nDone')

    x, y = pyautogui.position()
    positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)

    print(positionStr)

