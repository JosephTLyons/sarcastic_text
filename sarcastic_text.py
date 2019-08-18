#!/usr/bin/env python3

new_text = ""
position = 0

for character in input("\nInput:  "):
    if position % 2 == 0:
        new_text += character.upper()

    else:
        new_text += character.lower()

    if character.isalpha():
        position += 1

print("\nOutput: " + new_text + "\n")
