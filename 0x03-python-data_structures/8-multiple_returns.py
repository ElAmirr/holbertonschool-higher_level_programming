#!/usr/bin/python3
def multiple_returns(sentence):
    lenth = len(sentence)
    if lenth == 0:
        return None
    return sentence(lenth, sentence[0])
