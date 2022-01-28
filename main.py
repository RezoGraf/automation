# This is a sample Python script.
import time
import keyboard
# from time import sleep
import pyautogui

def zdvh():
    time.sleep(5.5)
    pyautogui.click(370, 480)
    pyautogui.click()
    pyautogui.press('tab')
    # pyautogui.click(650, 470)
    # pyautogui.click()
    # def paste(text: str):
    #     buffer = pyperclip.paste()
    #     pyperclip.copy(text)
    #     keyboard.press_and_release('ctrl + v')
    #     pyperclip.copy(buffer)
    # def type(text: str, interval=0.0):
    #     if interval == 0.0:
    #         paste(text)
    #         return
    #     buffer = pyperclip.paste()
    #     for char in text:
    #         pyperclip.copy(char)
    #         keyboard.press_and_release('ctrl + v')
    #         time.sleep(interval)
    #     pyperclip.copy(buffer)
    # def paste(text: str):
    #     buffer = pyperclip.paste()
    #     pyperclip.copy(text)
    #     keyboard.press_and_release('ctrl + v')
    #     pyperclip.copy(buffer)
    keyboard.write('Услуга1')
    pyautogui.press('tab')
    pyautogui.write('525', interval=0.1)
    pyautogui.press('enter')
    print('finished')
    # Press ⌃R to execute it or replace it with your code.
    # Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    zdvh()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
