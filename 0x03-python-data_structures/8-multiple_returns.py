#!/usr/bin/python3
def multiple_returns(sentence):
    lenth = len(sentence)
    if lenth == 0:
        return 0, None
    return lenth, sentence[0]
