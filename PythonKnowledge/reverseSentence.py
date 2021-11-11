#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  2 11:03:02 2021
Finding the reverse of sentenceword by word
@author: nyarbasi
"""

#sentence = "we are reversing this sentence"
#word_list = sentence.split()
#reversed_list = word_list[:: -1]
#reversed_sentence = " ".join(reversed_list)
#print(reversed_sentence)
#



####### or ########

sentence = "dread it run from it destiny still arrives"
word_list = sentence.split()
reversed_list = reversed(word_list)
reversed_sentence = " ".join(reversed_list)
print(reversed_sentence)



## reversing a word's letters#######

#word = 'reversing'
#reversedWord=list(reversed(word))
#print(reversedWord)
#
#


#########
#class Vowels:
#    vowels = ['a', 'e', 'i', 'o', 'u']
#
#    def __reversed__(self):
#        return reversed(self.vowels)
# 
#v = Vowels()
#print(list(reversed(v)))