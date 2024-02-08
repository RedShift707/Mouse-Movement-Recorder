import tkinter as tk
from pynput import mouse
import time

# Global variables to store mouse movements
mouse_positions = []

# Callback function to be called on mouse movement
def on_move(x, y):
    mouse_positions.append((x, y))
    ball_canvas.coords(ball, x - BALL_RADIUS, y - BALL_RADIUS, x + BALL_RADIUS, y + BALL_RADIUS)
    status_label.config(text=f"Mouse moved to ({x}, {y})")

# Start listening to mouse movements
def start_listening():
    listener = mouse.Listener(on_move=on_move)
    listener.start()
    start_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)

# Stop listening to mouse movements
def stop_listening():
    listener.stop()
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)
    display_positions()

# Display recorded mouse positions
def display_positions():
    positions_label.config(text="Recorded Mouse Movements:")
    for position in mouse_positions:
        positions_label.config(text=positions_label.cget("text") + f"\n{position}")

# Close the CMD window when tkinter window is closed
def on_close():
    window.destroy()
    exit()

# Create the main window
window = tk.Tk()
window.title("Mouse Movement Recorder")

# Constants for the ball
BALL_RADIUS = 10

# Create UI components
status_label = tk.Label(window, text="Status: Not Recording", padx=10, pady=10)
start_button = tk.Button(window, text="Start Recording", command=start_listening)
stop_button = tk.Button(window, text="Stop Recording", command=stop_listening, state=tk.DISABLED)
positions_label = tk.Label(window, text="", padx=10, pady=10)

# Create a canvas for the ball
ball_canvas = tk.Canvas(window, width=2 * BALL_RADIUS, height=2 * BALL_RADIUS)
ball = ball_canvas.create_oval(0, 0, 2 * BALL_RADIUS, 2 * BALL_RADIUS, fill="red")

# Place UI components in the window
status_label.pack()
start_button.pack()
stop_button.pack()
positions_label.pack()
ball_canvas.pack()

# Set the close event handler
window.protocol("WM_DELETE_WINDOW", on_close)

# Run the main loop
window.mainloop()