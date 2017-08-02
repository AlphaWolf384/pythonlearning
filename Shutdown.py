import pyautogui, time

print('Shut Down Procedure will start in 5 sec')
pyautogui.moveTo(27, 870, duration = 0.25)
pyautogui.click()
pyautogui.moveTo(372, 815, duration = 0.25)

time.sleep(5)

print('Shutting Down now')
pyautogui.click()

