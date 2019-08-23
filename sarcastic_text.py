#!/usr/bin/env python3

new_text = ""
should_be_upper = True

for character in input("\nInput:  "):
    if should_be_upper:
        new_text += character.upper()

    else:
        new_text += character.lower()

    if character.isalpha():
        should_be_upper = not should_be_upper

print("\nOutput: " + new_text + "\n")
