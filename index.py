import os, time
from tkinter.tix import InputOnly
import pyautogui

time.sleep(1)
dir = str(input("Digite o diretorio que deseja atualizar: "))
print("Abrindo CMD!")
print("Abrindo CMD!")
print("Abrindo CMD!")
time.sleep(0.1)
pyautogui.hotkey("ctrl", "alt" , "t")
time.sleep(4)
pyautogui.write(f"cd {dir}")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write("git add *")
time.sleep(1)
pyautogui.press("enter")
time.sleep(1)
pyautogui.write('git commit -m "Atualizacao"')
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.write("git push")
time.sleep(1)
pyautogui.press("enter")
time.sleep(5)
pyautogui.hotkey("alt","f4")
print("Atualizado com sucesso!")