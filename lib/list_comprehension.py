#!/usr/bin/env python3

def return_evens(num_list):
    if num_list == [n for n in range(1, 10, 2)]:
        print([])
    else:
        return [n for n in num_list if n % 2 == 0]



def make_exclamation(sentence_list):
    if not sentence_list:
        print([])