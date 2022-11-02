"""
This program will create a divine language a funny language from english
And recite it.
"""
# Dependencies
import pyttsx3


def reverse(string):
    string_return = string[::-1]
    return string_return


f = open('String_characters.py')
text = f.read()
divine_text = ""
texts = text.split(" ")
for i in texts:
    divine_text += reverse(i) + " "

print(divine_text)
pyttsx3.speak(divine_text)
