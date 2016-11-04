#!/bin/python

import sys
s = raw_input().strip()
counter  = 1
for letter in s:
   if letter and letter.isupper():
	counter = counter + 1
