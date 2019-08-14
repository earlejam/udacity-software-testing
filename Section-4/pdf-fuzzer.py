#!/usr/bin/python

seed_files = [
    "seed_files/JamesEarleyStat312HW3.pdf",
    "seed_files/JEMorphology2.pdf",
    "seed_files/cap-gown-rental.pdf",
    "seed_files/conda-cheatsheet.pdf",
    "seed_files/calorieAssessment.pdf"
]

apps = [
    "/Applications/Adobe Acrobat Reader DC.app/Contents/MacOS/AdobeReader"
]

fuzzing_out = "fuzz.pdf"

FUZZ_FACTOR = 249
NUM_TIMES = 10000
ONE_SECOND = 1


# end config #


import math
import random
import subprocess
import time

for i in range(NUM_TIMES):
    tgt_file = random.choice(seed_files)
    tgt_app = random.choice(apps)

    buffer = bytearray(open(file_choice, 'rb').read())

    # begin Charlie Miller fuzzing code
    numwrites = random.randrange(math.ceil((float(len(buffer)) / FUZZ_FACTOR))) + 1

    for j in range(numwrites):
        rand_byte = random.randrange(256)
        rn = random.randrange(len(buf))
        buf[rn] = "%c"%(rbyte)
    # end Charlie Miller fuzzing code

    open(fuzz_output, 'wb').write(buf)

    process = subprocess.Popen([app, fuzz_output])

    time.sleep(ONE_SECOND)
    crashed = process.poll()
    if not crashed:
        process.terminate()

