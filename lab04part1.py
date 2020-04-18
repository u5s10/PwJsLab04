#!/usr/bin/python
import sys
import operator

letters = {}
for i in range(ord('A'), ord('Z')+1):
    letters[chr(i)] = 0
for i in range(ord('a'), ord('z')+1):
    letters[chr(i)] = 0

    
if len(sys.argv) == 1:
    sys.exit("No file given!")

text = sys.argv[1]

number_of_chars = 0
try:
    with open(text) as file:
        for line in file:
            for char in line:
                if char in letters:
                    number_of_chars += 1
                    letters[char.upper()] += 1
            
except FileNotFoundError:
    print('Error')
i = 0
for k,v in sorted(letters.items(), key=operator.itemgetter(1), reverse=True):
    if i > 25: break;
    i+=1;
    print('{0:<8}{1:<8}{2:.2f}%'.format(k,v,v/number_of_chars))

print(f'Number of letters in text: {number_of_chars}')
