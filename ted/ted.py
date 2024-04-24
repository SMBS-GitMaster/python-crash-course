# TED basically loads snippets of code from a file and assigns them to a number. 0-9
# When you type that number, TED will type the code snippet.

# You can pause and unpause TED typing by pressing 0. By default, TED waits two seconds per newline.

# You can enable and disable TED by pressing F5. When disabled, it doesn't listen to any keypresses and doesn't type anything.

# You can change the speed of TED by pressing F6. Speeds from 1 to 9 are available. 1 is the fastest (1 character per 0.1 seconds) and 9 is the slowest (1 character per 0.9 seconds).

import time
import keyboard

import os

# We're gonna get the code snippets from a file called "ted.txt"
# We need to parse everything between ``` and ``` and assign them to a number from 1 to 9.
# If there are more than 9 snippets, we'll ignore the rest and print a warning.

time.sleep(5)
with open("ted.txt", "r") as f:
    text = "\n".join(f.readlines())
    print("Writing:", text)
    try:
        keyboard.write(text, delay=0.01)
    except:
        print("Error writing text")

exit(0)
with open("ted.txt", "r") as f:
    lines = f.readlines()

    snippets = []
    snippet = ""

    capturing = False

    # For each line, check if it starts with ```, in which case we start capturing at the next line, until we find another ```
    for line in lines:
        if line.startswith("```"):
            if capturing:
                snippets.append(snippet)
                snippet = ""
            capturing = not capturing
        elif capturing:
            snippet += line

    snippets = snippets[:9]

# We need to create a class to store the TED settings and data.
class TED:
    def __init__(self):
        self.enabled = True
        self.speed = 5
        self.pause = False

        self.data = []

        for snippet in snippets:
            self.data.append(snippet)

        self.current = 0

    def type(self, text):
        for line in text.split("\n"):
            print("writing: ", line)
            if not self.enabled:
                return

            if keyboard.is_pressed("0"):
                self.pause = not self.pause

            if self.pause:
                time.sleep(0.1)
                continue

            try:
                keyboard.write(line + "\n", delay=0.01 * self.speed)
            except StopIteration:
                time.sleep(2 * self.speed / 10)

    def listen(self):
        print("Listening...")
        while True:
            if keyboard.is_pressed("esc"):
                print("We're goner")
                break

            if keyboard.is_pressed("0"):
                print("This works")
                self.pause = not self.pause

            key = keyboard.read_event()
            if key.event_type == keyboard.KEY_DOWN:
                # Check if key is a number and which
                keyname = key.name
                if keyname.isdigit():
                    self.type(self.data[int(keyname) - 1])

            elif keyname == "f5":
                self.enabled = not self.enabled
            elif keyname == "f6":
                self.speed = (self.speed + 1) % 10
                print(f"Speed: {self.speed}")

ted = TED()
ted.listen()
