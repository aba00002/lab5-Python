from gfxhat import lcd
from gfxhat import backlight

#a function that displays a vertical line at a given x coordinate 50 on the gfx hat using for loop.
lcd.clear()
def displayVertical():
    x = 50
    for y in range (0, 64):
        lcd.set_pixel(x,y,1)
        lcd.show()


#a function that displays a vertical line at a given x coordinate 122 on the gfx hat using while loop.
lcd.clear()
def displayVerticalWhile():
    x = 122
    y = 0
    while (y <= 63):
        lcd.set_pixel(x,y,1)
        y = y + 1
        lcd.show()



#a function that displays a horizontal line at a given y coordinate 40 using while loop
lcd.clear()
def displayHorizontal():
    y = 40
    x = 0
    while (x <= 127):
        lcd.set_pixel(x,y,1)
        x=x+1
        lcd.show()

#a function that displays a horizontal line at a given y coordinate 3 using for loop
lcd.clear()
def displayHorizontalFor():
    y = 3
    for x in range (0, 128):
        lcd.set_pixel(x,y,1)
        lcd.show()


#A  function that creates a staircase starting at a specific coordinate. One stair has a width of w and a height of h.
def oneStair(x,y,w=12,h=5,SW=127,SH=63):
    for a in range(h):
        if y >= 0:
            lcd.set_pixel(x,y-a,1)
        else:
            h = a
    for b in range (0,w):
        if x+b<=SW:
            lcd.set_pixel(x+b,y-h,1)
        else:
            w = b
    return (x+w,y-h)
def staircase(x=10, y = 63, w = 12, h = 12):
    while (x+w<127 and y-h >= 0):
        x, y = oneStair(x,y,w,h)
        lcd.show()

    

#to display random pixels continously all over the screen 
lcd.clear()
import random
import time
def displayRandom():
    for x in range (128):
        x = random.randint(0, 127)
        y = random.randint(0, 63)
        lcd.set_pixel(x,y,1)
        time.sleep(0.1)
        lcd.show()


#Function to clear backlight
def clearBacklight():
    backlight.set_all(0,0,0)
    backlight.show()





