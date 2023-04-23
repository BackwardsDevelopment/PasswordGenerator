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


def generateString(length, spec):
    out = ""
    for pos in range(length):
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

def str2bool(v):
    if isinstance(v, bool):
        return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise argparse.ArgumentTypeError('Boolean value expected.')

parser = argparse.ArgumentParser(description="Generate a Randomly generated password")
parser.add_argument('-l', '--length', type=int, help='The Length the Password should be.')
parser.add_argument('-s', '--specialChars', type=str2bool, default=False, help='Whether to include special characters.')

args = parser.parse_args()

print(args)

print(generateString(args.length, args.specialChars))