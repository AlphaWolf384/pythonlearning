import pyautogui, time

print('Restart Procedure will start in 5 sec')
pyautogui.moveTo(27, 870, duration = 0.25)
pyautogui.click()
pyautogui.moveTo(430, 815, duration = 0.25)
pyautogui.click()
pyautogui.moveTo(526, 764)

time.sleep(5)

print('Restarting now')

