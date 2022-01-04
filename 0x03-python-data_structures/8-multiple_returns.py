#!/usr/bin/python3
def multiple_returns(sentence):
    new_sentence = ()
    if not sentence == "":
        new_sentence = len(sentence), sentence[0]
    else:
        new_sentence = 0, "None"
    return (new_sentence)
