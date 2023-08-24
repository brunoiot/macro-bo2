# *******************************************
# *                                         *
# *            MACRO FOR COD BO2            *
# *                                         *
# *******************************************

# Author: Bruno de Lima Marques
# GitHub: https://github.com/brunoiot
# Description: This program provides an automatic shooting macro for Call of Duty: Black Ops II, allowing the player to automate mouse clicks for semi-automatic or burst-fire weapons.
# Date: 2023-08-20

# Import libraries
import keyboard
from pynput import keyboard as kb
import time
from pynput.mouse import Button as BT, Controller
from interface import *

# Create an instance of the InterfaceManager class
manager = InterfaceManager()

# Create the window using the manager
manager.create_window()

# Retrieve the selected weapon choice from the manager
choosed_weapon = manager.choosed_weapon

# Create an instance of the mouse controller
mouse = Controller()

# Monitor and handle keyboard events using a context manager
with kb.Events() as events:

    # Iterate through keyboard events using the events context manager
    for event in events:
        # Configure the delay time based on the chosen weapon's fire rate
        match choosed_weapon:
            case "M8A1":
                delay = 0.0479  # Adjusted delay for M8A1 fire rate
            case "FAL":
                delay = 0.0949    # Adjusted delay for FAL fire rate
            case "SWAT":
                delay = 0.01  # Adjusted delay for SWAT fire rate
            case "Chicom":
                delay = 0.05  # Adjusted delay for Chicom fire rate
            case "Five Seven":
                delay = 0.08   # Adjusted delay for Five Seven fire rate
            case _:
                print("Error: Invalid weapon selection")

        # Reopen the menu window if the 'Esc' key is pressed
        if keyboard.is_pressed('esc'):
            manager.create_window()

        else:
            print('Received event {}'.format(event))

        # While the 'Alt' key is pressed, perform shooting actions by clicking the left mouse button
        while keyboard.is_pressed('alt'):
            print(delay)
            mouse.click(BT.left)
            time.sleep(delay)
