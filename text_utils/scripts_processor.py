#!/usr/bin/env python3
# -*- coding: utf-8 -*-
###############################################################################
##        Name: scripts_processor.py                                          #
##        Date: 03/06/2021                                                    #
## Description: Simple application for code processing in shell scripts.      #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



###############################################################################
## Imports.  ##################################################################
###############################################################################

import re
import argparse
import os



###############################################################################
## Args. ######################################################################
###############################################################################

parser = argparse.ArgumentParser(description = 'Simple application for code processing in shell scripts.')
parser.add_argument('path', metavar = 'PATH', type = str, help = 'Path to shell script.')
parser.add_argument('--advanced_on', help = 'Turn on advanced mode.', action = 'store_true')
parser.add_argument('--advanced_off', help = 'Turn off advanced mode.', action = 'store_true')
parser.add_argument('--verbose_on', help = 'Turn on verbose mode.', action = 'store_true')
parser.add_argument('--verbose_off', help = 'Turn off verbose mode.', action = 'store_true')
parser.add_argument('--verbose', help = 'Show more information during execution.', action = 'store_true')
args = parser.parse_args()



###############################################################################
## Main code. #################################################################
###############################################################################

class Main:

  def __init__(self):

    args.path = os.path.abspath(args.path)

    if not os.path.isfile(args.path):
      print ('[ERROR] The selected ' + args.path + 'is not a file.')
      exit (1)

    if args.verbose:
      print('Selected file: ' + args.path)

    self.checkArgs()
    Processor()
    exit(0)

  def checkArgs(self):

    if args.verbose_on and args.verbose_off:
      print ('[ERROR] Please choose only one tipe of verbose.')
      exit (1)

    if args.advanced_on and args.advanced_off:
      print ('[ERROR] Please choose only one tipe of advanced.')
      exit (1)

class Processor:

  def __init__(self):

    # Open tmpFile.
    tmpFilePath = args.path + '_tmp'
    tmpFile = open(tmpFilePath, 'w')

    # Open originalFile.
    originalFile = open(args.path, 'r')

    if args.verbose_on:
      self.mode = 0
      for line in originalFile.readlines():
        processedLine = self.processVerboseOn(line)
        tmpFile.write(processedLine)
        if args.verbose:
          self.printChanges(line, processedLine)

    if args.verbose_off:
      self.mode = 0
      for line in originalFile.readlines():
        processedLine = self.processVerboseOff(line)
        tmpFile.write(processedLine)
        if args.verbose:
          self.printChanges(line, processedLine)

    if args.advanced_on:
      self.mode = 0
      for line in originalFile.readlines():
        processedLine = self.processAdvancedOn(line)
        tmpFile.write(processedLine)
        if args.verbose:
          self.printChanges(line, processedLine)

    if args.advanced_off:
      self.mode = 0
      for line in originalFile.readlines():
        processedLine = self.processAdvancedOff(line)
        tmpFile.write(processedLine)
        if args.verbose:
          self.printChanges(line, processedLine)

    # Close files.
    tmpFile.write('\n')
    originalFile.close()
    tmpFile.close()
    print('Done!')

  def printChanges (self, line, processedLine):
    if line != processedLine:
      print('Line before being processed: ' + line)
      print('Line after being processed:  ' + processedLine)

  def processLine (self, line):

    if self.mode == 1:
      # Uncomment mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + processedLine[1]
      return processedLine

    if self.mode == 2:
      # Comment mode.
      if re.search('^\s+', line):
        # Comment line with blank spaces before code.
        preSpace = re.findall('^\s*', line)
        processedLine = re.split('^\s+', line)
        processedLine = preSpace[0] + '# ' + processedLine[1]
      else:
        # Comment line without blank spaces before code.
        processedLine = '# ' + line
      return processedLine

    return line

  def processVerboseOn(self, line):

    if line.strip() == '':
      return line

    if line.find('# Process') != -1 and line.strip() != '# Process-Start: Verbose-Off' and line.strip() != '# Process-End: Verbose-Off':
      return line

    if line.strip() == '# Process-Start: Verbose-Off':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-Start: Verbose-On\n'
      self.mode = 1
      return processedLine

    if line.strip() == '# Process-End: Verbose-Off':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-End: Verbose-On\n'
      self.mode = 0
      return processedLine

    if self.mode == 1:
      return self.processLine(line)

    return line

  def processVerboseOff(self, line):

    if line.strip() == '':
      return line

    if line.find('# Process') != -1 and line.strip() != '# Process-Start: Verbose-On' and line.strip() != '# Process-End: Verbose-On':
      return line

    if line.strip() == '# Process-Start: Verbose-On':
      # Change from Verbose-On mode to Verbose-Off mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-Start: Verbose-Off\n'
      self.mode = 2
      return processedLine

    if line.strip() == '# Process-End: Verbose-On':
      # Change from Verbose-On mode to Verbose-Off mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-End: Verbose-Off\n'
      self.mode = 0
      return processedLine

    if self.mode == 2:
      return self.processLine(line)

    return line

  def processAdvancedOn(self, line):

    if line.strip() == '':
      return line

    if (line.find('# Process') != -1 and 
      line.strip() != '# Process-Start: Advanced-Off' and 
      line.strip() != '# Process-End: Advanced-Off'and 
      line.strip() != '# Process-Start: Simple-On'and 
      line.strip() != '# Process-End: Simple-On'):
      return line

    if line.strip() == '# Process-Start: Advanced-Off':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-Start: Advanced-On\n'
      self.mode = 1
      return processedLine

    if line.strip() == '# Process-End: Advanced-Off':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-End: Advanced-On\n'
      self.mode = 0
      return processedLine

    if line.strip() == '# Process-Start: Simple-On':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-Start: Simple-Off\n'
      self.mode = 2
      return processedLine

    if line.strip() == '# Process-End: Simple-On':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-End: Simple-Off\n'
      self.mode = 0
      return processedLine

    if self.mode == 1:
      return self.processLine(line)

    if self.mode == 2:
      return self.processLine(line)

    return line

  def processAdvancedOff(self, line):

    if line.strip() == '':
      return line

    if (line.find('# Process') != -1 and 
      line.strip() != '# Process-Start: Advanced-On' and 
      line.strip() != '# Process-End: Advanced-On'and 
      line.strip() != '# Process-Start: Simple-Off'and 
      line.strip() != '# Process-End: Simple-Off'):
      return line

    if line.strip() == '# Process-Start: Advanced-On':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-Start: Advanced-Off\n'
      self.mode = 2
      return processedLine

    if line.strip() == '# Process-End: Advanced-On':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-End: Advanced-Off\n'
      self.mode = 0
      return processedLine

    if line.strip() == '# Process-Start: Simple-Off':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-Start: Simple-On\n'
      self.mode = 1
      return processedLine

    if line.strip() == '# Process-End: Simple-Off':
      # Change from Verbose-Off mode to Verbose-On mode.
      processedLine = line.split('# ', 1)
      processedLine = processedLine [0] + '# Process-End: Simple-On\n'
      self.mode = 0
      return processedLine

    if self.mode == 1:
      return self.processLine(line)

    if self.mode == 2:
      return self.processLine(line)

    return line



###############################################################################
## Execution. #################################################################
###############################################################################

Main()


