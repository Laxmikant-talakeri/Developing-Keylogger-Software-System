from PIL import ImageGrab
import time
import keyboard

# Function to take a screenshot and save it
def screenshot(file_path, extend, screenshot_counter):
    im = ImageGrab.grab()  # Capture the screen
    screenshot_name = f"screenshot_{screenshot_counter}.png"
    im.save(file_path + extend + screenshot_name)  # Save the captured screenshot

# Provide the appropriate values for these variables
file_path = r"C:\Users\Dell\OneDrive\Desktop\logger\screenashots\\"  # Replace with the desired directory
extend = ""  # You can add a subdirectory here if needed

screenshot_counter = 1  # Initialize the screenshot counter

# Loop to capture screenshots when Enter key is pressed
while True:
    if keyboard.is_pressed('enter'):
        screenshot(file_path, extend, screenshot_counter)
        print(f"Screenshot {screenshot_counter} taken and saved.")
        screenshot_counter += 1
        time.sleep(0.2)  # Sleep to avoid multiple rapid screenshots

    time.sleep(0.1)  # Sleep to avoid continuous checking and reduce CPU usage
