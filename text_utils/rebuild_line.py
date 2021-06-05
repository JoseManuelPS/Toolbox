#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
##        Name: rebuild_line.py                                               #
##        Date: 05/06/2021                                                    #
## Description: The program reads one by one each of the lines of a file,     #
##              if in any line it finds a match with the text entered as      #
##              "old", it replaces it with the text entered as "new".         #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



###############################################################################
## Imports.  ##################################################################
###############################################################################

import re
import os
import argparse



###############################################################################
## Args. ######################################################################
###############################################################################

parser = argparse.ArgumentParser(description = 'The program reads one by one each of the lines of a file, if in any line it finds a match with the text entered as "old", it replaces it with the text entered as "new".')
parser.add_argument('path', metavar = 'PATH', type = str, help = 'Path to the folder or the file to process.')
parser.add_argument('--new', type = str, help = 'The NEW text that you want to replace.', default = None)
parser.add_argument('--old', type = str, help = 'The OLD text that you want to replace.', default = None)
parser.add_argument('--replace', help = 'Replace the original file with the new content.', action = 'store_true')
parser.add_argument('--verbose', help = 'Show more information during execution.', action = 'store_true')
args = parser.parse_args()



###############################################################################
## Main code. #################################################################
###############################################################################

# Test the <(old)> argument.
if args.old is None:
  args.old = input('Please enter the OLD text you want to replace: ')

# Test the <(new)> argument.
if args.new is None:
  args.new = input('Please enter the NEW text you want to replace: ')

class Processor:

  def processFile(self, originalFile):

    # Open tmpFile.
    tmpFileName = originalFile + '_tmp'
    with open(tmpFileName, mode="w") as tmpFile, open(originalFile, mode="r") as realFile:    
      for line in realFile.readlines():
        processedLine = self.processLine(line)
        tmpFile.write(processedLine)
        if args.verbose and line != processedLine:
          print('Line before being processed: ' + line)
          print('Line after being processed:  ' + processedLine)

      # Close files.
      realFile.close()
      tmpFile.close()

    if args.replace:
      os.rename(originalFile, originalFile + "_old")
      os.rename(tmpFileName, originalFile)


  def processLine(self, line):

    if line.find(args.old) != -1:
      processedLine = ''
      processedLineSplit = re.split(args.old, line)

      for x in range(0, len(processedLineSplit)):
        if len(processedLineSplit) > (x+1):
          processedLine = processedLine + processedLineSplit[x] + args.new
        else:
          processedLine = processedLine + processedLineSplit[x]

      return processedLine
    else:
      return line


def checkPattern (pattern, fileToCheckName):

  with open(fileToCheckName, mode="r") as fileToCheck:

    for line in fileToCheck.readlines():
      if pattern in line:
        fileToCheck.close()
        return True

    fileToCheck.close()

  return False


def classifyPath (processPath):

  if args.verbose:
    print('Selected folder/file: ' + processPath)

  if os.path.isfile(processPath) and checkPattern(args.old, processPath):
    processor.processFile(processPath)
  elif os.path.isdir(processPath):
    with os.scandir(processPath) as newElementsFound:
      newElementsFound = [processPath + '/' + element.name for element in newElementsFound]

    for newElement in newElementsFound:
      if os.path.isfile(newElement) and checkPattern(args.old, newElement):
        processor.processFile(newElement)
      elif os.path.isdir(processPath):
        classifyPath(newElement)



###############################################################################
## Execution. #################################################################
###############################################################################

processor = Processor ()
args.path = os.path.abspath(args.path)
classifyPath(args.path)


