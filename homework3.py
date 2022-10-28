"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:

    characters = "cbacba"
    phrase = "aabbccc"

    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters, capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""

from collections import Counter


def generate_phrase(characters, phrase):
    phrase_count = Counter(phrase.lower())
    characters_count = Counter(characters.lower())

    if not phrase_count and not characters_count:      # empy string
        return True

    if len(phrase) > len(characters):
        return False

    for char, count in phrase_count.items():
        if char in characters_count and count <= characters_count.get(count):
            continue
        else:
            return False

    return True

print(generate_phrase('cbacba', 'aabbccc'))
