import tkinter as tk
import pygame
import keyboard

pygame.mixer.init()


# Play a sound
def play_sound(filename):
    pygame.mixer.Sound(filename).play()


# Create window
window = tk.Tk()
window.title("My Sound Deck")
window.geometry("400x350")


# Title
title = tk.Label(
    window,
    text="🎵 MY SOUND DECK",
    font=("Arial", 20)
)
title.pack(pady=20)


# Buttons
tk.Button(
    window,
    text="😂 Laugh [F1]",
    font=("Arial", 14),
    command=lambda: play_sound("sounds/laugh.mp3")
).pack(pady=5)

tk.Button(
    window,
    text="ඞ Sus [F2]",
    font=("Arial", 14),
    command=lambda: play_sound("sounds/sus.mp3")
).pack(pady=5)

tk.Button(
    window,
    text="💥 Vine Boom [F3]",
    font=("Arial", 14),
    command=lambda: play_sound("sounds/vine_boom.mp3")
).pack(pady=5)

tk.Button(
    window,
    text="✅ Yes [F4]",
    font=("Arial", 14),
    command=lambda: play_sound("sounds/yes.mp3")
).pack(pady=5)

tk.Button(
    window,
    text="❌ No [F5]",
    font=("Arial", 14),
    command=lambda: play_sound("sounds/no.mp3")
).pack(pady=5)


# Global numpad keybinds
keyboard.add_hotkey("num 1", lambda: play_sound("sounds/laugh.mp3"))
keyboard.add_hotkey("num 2", lambda: play_sound("sounds/sus.mp3"))
keyboard.add_hotkey("num 3", lambda: play_sound("sounds/vine_boom.mp3"))
keyboard.add_hotkey("num 4", lambda: play_sound("sounds/yes.mp3"))
keyboard.add_hotkey("num 5", lambda: play_sound("sounds/no.mp3"))


# Close program
def quit_program():
    keyboard.unhook_all()
    pygame.mixer.quit()
    window.destroy()


window.protocol("WM_DELETE_WINDOW", quit_program)

window.mainloop()