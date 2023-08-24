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
import sys
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font
from tkinter import *

class InterfaceManager:
    def __init__(self):
        self.window = None
        self.choosed_weapon = None


    def create_window(self):
        # Define the action when the window is closed
        def on_closing():
            if messagebox.askokcancel("Quit", "Do you want to quit?"):
                window.destroy()
                sys.exit()

        # Define the action when the 'Activate' button is clicked
        def active():
            self.choosed_weapon = weapon_cb.get()  # Store the selected weapon
            print(self.choosed_weapon)
            window.destroy()  # Close the window after selecting the weapon

        # Create a new Tkinter window
        window = tk.Tk()
        window.title("Macro BO2")
        window.geometry("380x410+450+100")
        window.resizable(False, False)

        # Define the file paths for the icon and image
        icon_path = "images/icon_macro.png"
        image_path = "images/Black Ops II.png"

        # Load the icon and image using PhotoImage
        icon = PhotoImage(file= icon_path)
        image = PhotoImage(file=image_path)

        # Set the window icon
        window.iconphoto(True, icon)

        # Create a label with the same dimensions as the image and place it on the window
        label = tk.Label(window, image=image)
        label.place(x=0, y=0, relwidth=1, relheight=1)

        # List of available weapon options
        weapon_list = ['M8A1', 'FAL', 'SWAT', 'Chicom', 'Five Seven']

        # Create a bold font for labels
        label_font = font.Font(weight="bold")

        # Create and display labels with specific text and font settings
        label0 = Label(window, text= "MACRO FOR BO2 BY @brunoiot", font=label_font)
        label0.pack(pady= 10)
        label1 = Label(window, text="Choose your weapon: ", font=(18))
        label1.pack(pady=5)

        # Create a combobox for weapon selection using the provided weapon list
        weapon_cb = ttk.Combobox(window, values= weapon_list)

        # Set the default value of the combobox to the first weapon in the list
        weapon_cb.set(weapon_list[0])

        # Set the combobox state to 'readonly' to prevent manual text input
        weapon_cb['state'] = 'readonly'

        # Display the combobox and add some vertical padding
        weapon_cb.pack(pady=10)

        # Create an 'Activate' button with specified text, font, and command
        btn_active = Button(window, text="Activate", font=(18), command=active)

        # Display the button with vertical padding
        btn_active.pack(pady=100)

        # Create a label to display a warning message
        text_warning = Label(window, text="⚠️ This window will close once you click to activate the macro.\n"
                                         "🎮 Hold down the 'Alt' key on your keyboard to fire automatically.\n"
                                         "❌ Press 'ESC' to deactivate the macro and return to this window.")

        # Display the warning message
        text_warning.pack()

        # Set up a protocol to handle window closing using the on_closing function
        window.protocol("WM_DELETE_WINDOW", on_closing)

        # Start the main event loop to display the window
        window.mainloop()


