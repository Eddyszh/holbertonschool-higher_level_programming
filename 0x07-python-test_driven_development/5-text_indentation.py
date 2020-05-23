#!/usr/bin/python3
"""
    Text_identation
    Function:
        text_identtion: prints a text with 2 new lines
        after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Args:
        text: given text
    Raise:
        TypeError
    """
    if text is None or not isinstance(text, str) or len(text) < 0:
        raise TypeError("text must be a string")
    ident = "".join([s if s not in ".?:" else s + "\n\n" for s in text])
    print("\n".join([i.strip() for i in ident.split("\n")]), end='')
