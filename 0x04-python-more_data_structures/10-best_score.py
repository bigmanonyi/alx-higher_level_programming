#!/usr/bin/python3
def best_score(a_dictionary):
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None
    row = list(a_dictionary.keys())[0]
    large = a_dictionary[row]
    for j, k in a_dictionary.items():
        if k > large:
            large = k
            row = j
            return (row)
