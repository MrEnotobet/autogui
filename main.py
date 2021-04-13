import pyautogui as pg
import time

time.sleep(20)

pg.hotkey("winleft")
pg.typewrite("chrome\n",1)
pg.moveTo(387, 46, 2)
pg.leftClick()
pg.typewrite("www.youtube.com\n", 0.5)