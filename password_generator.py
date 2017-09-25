#!/usr/bin/env python
from random import randint
import string
import os
import urllib.request

# http://preshing.com/20110811/xkcd-password-generator/

word_file = os.path.abspath(__file__)[:-21] + 'google-10000-english.txt'
words = []

# check for and create the word file if needed
try:
    with open(word_file, 'r') as f:
        print ("Words file exists, starting")
except IOError:
    print ("Words file does not exist, starting")
    urllib.request.urlretrieve("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt", filename=word_file)
        
with open(word_file, 'r') as f:
    words = f.readlines()

num_needed = input('Do you need a number? (y or n): ')
need_punc = input('Do you need punctuation? (y or n): ')
need_mixed_case = input('Do you need mixed case? (y or n): ')

num_needed = True if num_needed.lower() == 'y' else False
need_punc = True if need_punc.lower() == 'y' else False
need_mixed_case = True if need_mixed_case.lower() == 'y' else False

password = ''
current_word = ''

for i in (range(0,4)):
    current_word = words[randint(0,len(words))].rstrip()
    
    print('Using: {}'.format(current_word.title()))
    
    if need_mixed_case:
        password+=current_word.title()
    else:
        password+=current_word
    
if num_needed:
    password+=str(randint(1,10))
    
if need_punc:
    punc_list = list(string.punctuation)
    my_punc = punc_list[randint(0,len(punc_list))]
    password+=str(my_punc)
    
print('Your password is:\n{} \nLength is {}'.format(password, len(password)))
    
