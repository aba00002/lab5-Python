#a program that displays a simple menu to the user to test each of the function created in my library file
def simpleMenu():
    print("1. Display a vertical line on the gfx hat")
    print("2. Display a horizontal line on the gfx hat")
    print("3. Display a staircase on the gfx hat")
    print("4. Display random pixels on the gfx hat")
    print("5. Clear backlight on the gfx hat")
selection = int(input("Enter your choice: "))
if selection ==1:
    from aba00002 import displayVertical
elif selection==2:
    from aba00002 import displayHorizontal
elif selection==3:
    from aba00002 import staircase
elif selection==4:
    from aba00002 import displayRandom
elif selection==5:
    from aba00002 import clearBacklight


