#!/usr/bin/env python

new_text = ""
position = 0

for character in raw_input("Non-sarcastic text: "):
    if position % 2 == 0:
        new_text += character.upper()

    else:
        new_text += character.lower()

    if character != ' ':
        position += 1

print("Sarcastic text: " + new_text)
