#!/usr/bin/python
import sys
import operator

hist = []
letters = {}
for i in range(ord('A'), ord('Z')+1):
    letters[chr(i)] = 0
    
if len(sys.argv) == 1:
    sys.exit("No file given!")
    
text = sys.argv[1]
all_lines = []
number_of_chars = 0
try:
    with open(text) as file:
        for line in file:
            for char in line:
                if char in letters:
                    number_of_chars += 1
                    letters[char] += 1
    with open(text) as file:
        all_lines = file.readlines()
        first_line = all_lines[0]
        for char in first_line.strip():
            hist.append(char)

                
except FileNotFoundError:
    print('Error')

letters = dict(sorted(letters.items(), key=operator.itemgetter(1), reverse=True))
for k,v in (letters.items()):
    print('{0:<8}{1:<8}{2:.2f}%'.format(k,v,v/number_of_chars))

print(f'Number of letters in text: {number_of_chars}')
first_letter = list(letters.keys())[0]
shift = ((ord(first_letter) - ord(hist[0])) % len(hist))
print('key:{0}'.format(shift))

def decipher(letter, shift, limit):
    output = (ord(letter) + shift) % limit
    if(output < 65):
        return output+ord('A')
    else:
        return output
    
try:
    with open(text) as file:
        for line in file:
            for char in line:
                if char in letters:
                    print(chr(decipher(char,shift,91)),end='')
                else:
                    print(char,end='')
except FileNotFoundError:
    print('Error')
