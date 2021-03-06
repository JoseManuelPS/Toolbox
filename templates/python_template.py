#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
##        Name: <(script_name)>                                               #
##        Date: <(script_date)>                                               #
## Description: <(script_description)>                                        #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



###############################################################################
## Imports. ###################################################################
###############################################################################

import argparse
import <(import_name)>



###############################################################################
## Args. ######################################################################
###############################################################################

parser = argparse.ArgumentParser(description = '<(script_description)>')
parser.add_argument('<(arg)>', metavar = '<(ARG)>', type = bool, help = '<(arg_description)>')
parser.add_argument('<(arg)>', metavar = '<(ARG)>', type = int, help = '<(arg_description)>')
parser.add_argument('<(arg)>', metavar = '<(ARG)>', type = str, help = '<(arg_description)>')
parser.add_argument('--<(arg)>', type = bool, help = '<(arg_description)>', default = <(True or False)>)
parser.add_argument('--<(arg)>', type = int, help = '<(arg_description)>', default = <(some_number)>)
parser.add_argument('--<(arg)>', type = str, help = '<(arg_description)>', default = '<(some_text)>')
args = parser.parse_args()



###############################################################################
## Main code. #################################################################
###############################################################################

class Main:

  def __init__(self):

    some_custom_var = some_custom_method('some_custom_var')
    print(some_custom_var)
    exit(0)

  def some_custom_method(self, some_custom_var):

    some_custom_var = some_custom_var + ' plus some_text'
    return some_custom_var



###############################################################################
## Auxiliary methods. #########################################################
###############################################################################



###############################################################################
## Verbose & UI. ##############################################################
###############################################################################



###############################################################################
## Execution. #################################################################
###############################################################################

Main()


