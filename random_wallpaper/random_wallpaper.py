#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
##        Name: random_wallpaper.py                                           #
##        Date: 30/05/2021                                                    #
## Description: Sets a wallpaper randomly, choosing from all the existing     #
##              images in a directory and its subdirectories.                 #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



###############################################################################
## Imports.  ##################################################################
###############################################################################

import sys
import time
import random
import argparse
import subprocess
from os import path
from os import listdir



###############################################################################
## Args. ######################################################################
###############################################################################

parser = argparse.ArgumentParser(description = 'Sets a wallpaper randomly, choosing from all the existing images in a directory and its subdirectories.')
parser.add_argument('folder_path', metavar = 'PATH', type = str, help = 'Path to the images directory.')
parser.add_argument('--time', type = int,  help = 'Set the time (in seconds) of each screen background. Default 60s.', default = 60)
parser.add_argument('--verbose', help = 'Show more information during execution.', action = 'store_true')
args = parser.parse_args()



###############################################################################
## Main code. #################################################################
###############################################################################

# Fixing possible incorrect path.
if args.folder_path[len(args.folder_path) - 1] != '/':
  args.folder_path += '/'

# Printing arguments.
if args.verbose:
  print('Selected path: ' + args.folder_path)
  print('Selected time: ', args.time)


# Selection of possible folders as categories.
category_list = []
for x in listdir(args.folder_path):
  if path.isdir(args.folder_path + x):
    category_list.append(x)

if not category_list:
  print('The path <(' + args.folder_path + ')> does not contain images or folders')
  sys.exit(1)

while 1:

  category_index = random.randint(0, len(category_list) - 1)
  if args.verbose:
    print('The selected category is: ' + category_list[category_index])

  # Adding images to the list <(image_list)>.
  image_list = []
  for x in listdir(args.folder_path + category_list[category_index]):
    if path.isfile(args.folder_path + category_list[category_index] + '/' + x):
      image_list.append(x)

  # Selecting the number of images used for the selected category.
  images_by_category = random.randint(0, len(image_list) - 1)
  if args.verbose:
    print('The number of images selected for this category is: ', images_by_category)

  # Change of wallpaper.
  while images_by_category != 0:

    image_index = random.randint(0, len(image_list) - 1)
    full_path = args.folder_path + category_list[category_index] + '/' + image_list[image_index]

    if args.verbose:
      print('The selected image is: ' + image_list[image_index])

    subprocess.Popen(['gsettings', 'set', 'org.gnome.desktop.background', 'picture-uri', full_path])
    time.sleep(args.time)
    image_list.remove(image_list[image_index])
    images_by_category -= 1


