#!/usr/bin/python

import random
import string

def RandomPasswordGenerator(passLen=10):
     letters = string.ascii_lowercase
     pw = ''

     for i in range(passLen):
        pw += random.choice(letters)

     return pw

RandomPasswordGenerator()
