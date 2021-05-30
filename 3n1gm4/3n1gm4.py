#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
##        Name: 3n1gm4.py                                                     #
##        Date: 30/05/2021                                                    #
## Description: Create a secret box to store a key.                           #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



###############################################################################
## Imports.  ##################################################################
###############################################################################

import argparse
import random
import string



###############################################################################
## Args. ######################################################################
###############################################################################

parser = argparse.ArgumentParser(description = 'Create a secret box to store a key.')
parser.add_argument('rows', type = int, help = 'Type number of rows')
parser.add_argument('columns', type = int, help = 'Type number of columns')
args = parser.parse_args()



###############################################################################
## Main code. #################################################################
###############################################################################

vars_list = list(string.ascii_letters) + list(string.digits)
vars_list += ['$', '%', '*', '!', '&', '^', '@', '#']

box = ''
for x in range(0, args.rows):
  row = ''
  for y in range(0, args.columns):
    val = random.randint(0, len(vars_list) - 1)
    row += vars_list [val]
  box += row + '\n'
print(box)

exit(0)


