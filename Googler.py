""" Excel Searcher v1.1 """
import time
import xlwings as xw
import webbrowser
import pyautogui
from selenium import webdriver

name = "sample.xlsx"
file_location = "C:\Users\DRicchi\Deskstop\\" + name
x = 0
y = 0
z = 0

print file_location

print("Welcome to Googler v1.1")
print("Press Y to continue or N to stop")
time.sleep(0.5)
user = raw_input("Begin? Press Any Keys")
print("Opening Excel")
wb = xw.Book(name)

while True:
    user = raw_input("Continue Process? Y|N ")
    
    if user == "Y" or user == "y":

        "pyautogui.press(['ctrl' + 'w','ctrl' + 'w'])"
        x += 1
        range1 = "A" + str(x)
        range2 = "C" + str(x)
        tab1 = str(wb.sheets[y].range(range1).value)
        tab2 = str(wb.sheets[y].range(range2).value)
        tab3 = tab1 + ' ' + tab2
        tab4 = tab3 + ' ' + 'price'
        tab5 = tab1 + ' ' + 'price'
        
        if tab1 == False and tab2 == False:
            print("Continue to next Sheet? Press Y to continue, Press N to stay, or Press Any keys to abort")
            check_user = raw_input()
            if check_user == "Y" or check_user == "y":
                y += 1
                x = 0
                print("Moving to next Sheet")
            elif check_user == "N" or check_user == "n":
                print("Continuing")
            else:
                print("Okay, Aborting in 3 sec")
                time.sleep(3)
                print("Aborted")
                break
        else:
            print("Opening Browser")
            webbrowser.open('chrome')
            webbrowser.get().open_new_tab('http://bing.com/?q=%s'%tab3)
            webbrowser.get().open_new_tab('http://google.com/?q=%s'%tab3)
            time.sleep(2)
            pyautogui.press('enter')
            print("Process Finished")

    elif user == "N" or user == "n":
        print("Aborting in 3 sec")
        time.sleep(3)
        print("Aborted")
        break

    else:
        print("Please try again, Use Y to continue or N to stop")
        


