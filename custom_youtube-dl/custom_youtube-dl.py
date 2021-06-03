#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
##        Name: custom_youtube-dl.py                                          #
##        Date: 02/06/2021                                                    #
## Description: Assistant to use the youtube-dl tool.                         #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



###############################################################################
## Imports.  ##################################################################
###############################################################################

import re
import argparse
import subprocess
from os import path
from os import listdir



###############################################################################
## Args. ######################################################################
###############################################################################

parser = argparse.ArgumentParser(description = 'Assistant to use the youtube-dl tool.')
parser.add_argument('path', metavar = 'PATH', type = str, help = 'Set the path to the directory where the download is saved.')
parser.add_argument('--name', type = str, help = 'Set the name under which the download is saved.')
args = parser.parse_args()



###############################################################################
## Main code. #################################################################
###############################################################################

# Checking if the application youtube-dl exists and update it.
try:
  p = subprocess.Popen(['youtube-dl', "-U"])
  p.wait()
except:
  print ('\n\n[ERROR] The application youtube-dl is not installed.')
  exit(1)

# Fixing possible incorrect path.
args.path = path.abspath(args.path)
if not path.isdir(args.path):
  print ('\n\n[ERROR] <(' + args.path + ')> is not a directory.')
  exit(1)
if args.path[len(args.path) - 1] != '/':
  args.path += '/'

# Printing instructions.
p = subprocess.Popen(['clear', '-x'])
p.wait()
print('Type <(exit)> to quit this program')

# Load the number of episodes if the name is written.
if args.name is not None:
  episode_list = []
  for x in listdir(args.path):
    if path.isfile(args.path + x):
      regular_expression = re.search('(?<=' + args.name + '_)\\w+', x)
      if regular_expression is not None:
        number_of_episode = regular_expression.group(0)
        episode_list.append(int(number_of_episode))

  # Checking for new episode number.
  if not episode_list:
    episode_num = 0
  else:
    episode_num = max(episode_list)

while 1:
  url = input('\n\nURL: ')
  if url == 'exit':
    exit(0)

  if args.name is not None:
    episode_num += 1
    episode_num_str = str(episode_num)

    if episode_num < 10:
      episode_num_str = '0' + episode_num_str

    full_name = args.path + args.name + "_" + episode_num_str + '.%(ext)s'

  # Executing youtube-dl
  if not args.name:
    p = subprocess.Popen(['youtube-dl', url])
    p.wait()
    print('\n\nDownload complete!')
  else:
    p = subprocess.Popen(['youtube-dl', '-o', full_name, url])
    p.wait()
    print('\n\n' + args.name + "_" + episode_num_str + ' download complete!')


