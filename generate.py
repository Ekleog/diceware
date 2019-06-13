#!/usr/bin/env python

import math
import random
import sys

if len(sys.argv) != 3:
    print("Usage:", sys.argv[0], "[wordlist] [number of words to generate]")
    sys.exit(1)

filename = sys.argv[1]
nwords = int(sys.argv[2])

with open(filename, "r") as f:
    l = f.readlines()

words_in_list = len(l)
def word(i):
    return l[i].split()[1]

# This is a CSPRNG at least on linux, where /dev/urandom (and thus
# os.urandom) is a CSPRNG
rng = random.SystemRandom()

words = [word(rng.randrange(words_in_list)) for _ in range(nwords)]

word_entropy = math.log(words_in_list, 2)
print("One word is worth", word_entropy, "bits of entropy")

entropy_at = [str(int((i + 1) * word_entropy)) for i in range(nwords)]

print("Entropy:", end="")
for i in range(nwords):
    print(" " + entropy_at[i].rjust(len(words[i])), end="")
print()
print("Words  :", end="")
for i in range(nwords):
    print(" " + words[i].rjust(len(entropy_at[i])), end="")
print()
