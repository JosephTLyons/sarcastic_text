#!/usr/bin/env python

new_text = ""
position = 0

for character in raw_input("\nInput:  "):
    if position % 2 == 0:
        new_text += character.upper()

    else:
        new_text += character.lower()

    if character.isalpha():
        position += 1

print("\nOutput: " + new_text + "\n")
