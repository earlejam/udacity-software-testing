# Fuzz Testing
# ------------
# Write a random fuzzer, based on Charlie Miller's example
# from Problem Set 4, for a text viewer application.
#
# For multiple iterations, the procedure, fuzzit, should take in the content
# of a text file, pass the content into a byte array, randomly modify bytes
# of the "file", and add the resulting byte array (as a String) to a list. 
# The return value of the fuzzit procedure should be a list of 
# byte-modified strings.

ENCODING = 'utf-8'
FUZZ_FACTOR = 150
NUM_TIMES = 1000

import array
import math
import random

content = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Phasellus sollicitudin condimentum libero,
sit amet ultrices lacus faucibus nec.
Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Cras nulla nisi, accumsan gravida commodo et,
venenatis dignissim quam. Mauris rutrum ullamcorper consectetur.
Nunc luctus dui eu libero fringilla tempor. Integer vitae libero purus.
Fusce est dui, suscipit mollis pellentesque vel, cursus sed sapien.
Duis quam nibh, dictum ut dictum eget, ultrices in tortor.
In hac habitasse platea dictumst. Morbi et leo enim.
Aenean ipsum ipsum, laoreet vel cursus a, tincidunt ultrices augue.
Aliquam ac erat eget nunc lacinia imperdiet vel id nulla."""


def fuzzit(content):
# Write a random fuzzer for a simulated text viewer application

    modified_texts = []

    for i in range(NUM_TIMES):

        buf = list(content)

        # begin Charlie Miller fuzzing code
        numwrites = random.randrange(math.ceil((float(len(buf)) / FUZZ_FACTOR))) + 1

        for j in range(numwrites * 100):
            rand_byte = random.randrange(256)
            rand_loc = random.randrange(len(buf))
            buf[rand_loc] = '%c'%(rand_byte)
        # end Charlie Miller fuzzing code

        modified_texts.append(''.join(buf))
        print(''.join(buf))


    return modified_texts


if __name__ == "__main__":
    fuzzit(content)