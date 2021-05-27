#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary:
        best_s = 0
        best_n = ""
        for i, j in (a_dictionary.items()):
            if j > best_s:
                best_n = i
                best_s = j
        return best_n
    else:
        return None
