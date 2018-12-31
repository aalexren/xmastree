#!/Library/Frameworks/Python.framework/Versions/3.7/bin/python3
# -*- coding: utf-8 -*-

from termcolor import colored
import random
import time
import curses

def sign(std, x, y):
  text = 'made by 4ernitsa (kot_mapku3)©'
  std.addstr(y, x, text)

def xmas(std, x, y):
  colors = [47, 197, 227]
  # Текст написан с помощью figlet (можно установить через brew для mac)
  text = [
  ' __  __ _____ ____  ______   __',
  '|  \/  | ____|  _ \|  _ \ \ / /',
  '| |\/| |  _| | |_) | |_) \ V / ',
  '| |  | | |___|  _ <|  _ < | |  ',
  '|_|  |_|_____|_| \_\_| \_\|_|  ',
  '  ____ _   _ ____  ___ ____ _____ __  __    _    ____  ',
  '/  ___| | | |  _ \|_ _/ ___|_   _|  \/  |  / \  / ___| ',
  '| |   | |_| | |_) || |\___ \ | | | |\/| | / _ \ \___ \ ',
  '| |___|  _  |  _ < | | ___) || | | |  | |/ ___ \ ___) |',
  '\ ____|_| |_|_| \_\___|____/ |_| |_|  |_/_/   \_\____/ ',
  ]

  # Для каждой строки свой цвет из трёх
  for i in range(0, len(text)):
    color = random.choice(colors)
    for j in range(0, len(text[i])):
      std.addstr(y+i, x+j, text[i][j], curses.color_pair(color))


x, y = 0, 0
foot = 5 # ширина ствола ёлки
long = 4 # высота ствола
stdscr = curses.initscr() # берём управление терминалом
height, width = stdscr.getmaxyx()
curses.start_color()
curses.use_default_colors()
#Добавляем цвета в палитру (цвета берутся из цветовой схемы терминала)
for i in range(0, 255): 
  curses.init_pair(i + 1, i, -1)

while True:
  temp = 1
  xmas(stdscr, width//3, 0)  # текст figlet
  sign(stdscr, width//3 + 4, height//2 + 3) # подпись
  for level in range(0, height//2):          # проще говоря, это высота ёлки
    for _ in range(0, (width//3-temp)//2 + height//(height//10)//2):
      x += 1
    for _ in range(0, temp):
      stdscr.addstr(y, x, '*', curses.color_pair(random.randint(20, 230)))
      x += 1
    for _ in range(0, (width//3-temp)//2 + height//(height//10)//2):
      x += 1
    temp += 2
    y += 1
    x = 0

  for i in range(0, long): # высота ножки
    for space in range(0, (width//3-foot)//2 + height//(height//10)//2):
      x += 1
    for stick in range(0, foot): # ну с шириной ножки можно играться
      stdscr.addstr(y, x, '|')
      x += 1
    for space in range(0, (width//3-foot)//2 + height//(height//10)//2):
      x += 1
    y += 1
    x = 0
  stdscr.refresh()
  x, y = 0, 0
  time.sleep(0.5)