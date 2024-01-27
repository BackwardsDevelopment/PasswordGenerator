# Command
# gen-password

# Arguments
# Length             [integer] (-l) default: 16
# Special Characters [boolean] (-s) default: false

# Example command

# gen-password -l 20 -s true

import math
import random
import argparse


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# List of all digits
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# List of some common special characters
special_chars = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', "'", '"', ',', '<', '.', '>', '/', '?']


def depreciatedGenerateString(length, spec):
    out = ""
    for _ in range(length):
        if random.random() > .75 and spec:
            out += special_chars[math.floor(random.random()*len(special_chars))]
        else:
            if random.random() > .625:
                out += numbers[math.floor(random.random()*len(numbers))]
            else:
                if random.random() > .5:
                    out += letters[math.floor(random.random()*len(letters))].upper()
                else:
                    out += letters[math.floor(random.random()*len(letters))].lower()
    return out

def generateString(length, spec):
    out = ""
    for _ in range(length):
        charType = random.random()
        if spec:
            if charType < .25:
                out += special_chars[math.floor(random.random()*len(special_chars))]
            elif charType < .5:
                out += numbers[math.floor(random.random()*len(numbers))]
            elif charType < .75:
                out += letters[math.floor(random.random()*len(letters))].lower()
            elif charType < 1:
                out += letters[math.floor(random.random()*len(letters))].upper()
        else:
            if charType < .33:
                out += numbers[math.floor(random.random()*len(numbers))]
            elif charType < .66:
                out += letters[math.floor(random.random()*len(letters))].lower()
            elif charType < 1:
                out += letters[math.floor(random.random()*len(letters))].upper()
    return out

def main(total, length, spec, useOld):
    out = []
    for _ in range(total):
        if (useOld):
            print("Depreciation Warning.\nWhile using the old generation process is possible, it isn't recommended.")
            out.append(depreciatedGenerateString(length, spec))
        else:
            out.append(generateString(length, spec))
    return out

parser = argparse.ArgumentParser(description="Generate a Randomly generated password")
parser.add_argument('-l', '--length', type=int, default=16, help='The Length the Password should be.')
parser.add_argument('-s', '--specialChars', action="store_true", help='Whether to include special characters.')
parser.add_argument('-t', '--totalPasswords', type=int, default=1, help="The number of passwords to generate")
parser.add_argument('-o', '--old', action="store_true", help="Use the old method to generate a string")

args = parser.parse_args()

passwords = main(args.totalPasswords, args.length, args.specialChars, args.old)

if len(passwords) > 1:
    for index, passwd in enumerate(passwords):
        print(f"{index+1}: {passwd}")
else:
    print(passwords[0])
