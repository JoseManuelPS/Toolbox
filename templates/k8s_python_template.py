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

#from <(package)> import <(module)>
from rich import print
from rich.progress import Progress
from rich.prompt import Prompt
from rich.table import Table
# import <(package)>
import argparse as argp
import os
import subprocess as sp
import time



###############################################################################
## Args. ######################################################################
###############################################################################

# parser = argp.ArgumentParser(description = '<(script_description)>')
# parser.add_argument('<(arg | --arg)>', metavar = '<(ARG)>', type = <(bool | int | str)>, help = '<(arg_description)>', default = <(True or False | some_number | some_text)>)
# args = parser.parse_args()



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


  def execCommand_local(self, command):
    command_exec = sp.run([command], shell=True, universal_newlines=True, stdout=sp.PIPE, stderr=sp.PIPE)
    return command_exec


  def execCommand_remote(self, command, node_connection):
    command_format = 'ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i ' + args.ssh_key + ' ' + node_connection + ' ' + command
    command_exec = sp.run([command_format], shell=True, universal_newlines=True, stdout=sp.PIPE, stderr=sp.PIPE)
    return command_exec


  def getNodesInfo_names(self):
    
    get_nodes_exec = self.execCommand_local('kubectl get nodes')
    get_nodes_exec_split_row = get_nodes_exec.stdout.splitlines()

    nodes_info_names = []
    for x in range(1, len(get_nodes_exec_split_row)):
      if args.node_group == 'all':
        get_nodes_exec_split_colum = get_nodes_exec_split_row[x].split()
        nodes_info_names.append(get_nodes_exec_split_colum[0])
      else:
        get_nodes_exec_split_colum = get_nodes_exec_split_row[x].split()
        if args.node_group in get_nodes_exec_split_colum[0]:
          nodes_info_names.append(get_nodes_exec_split_colum[0])

    return nodes_info_names


  def getNodesInfo_ips(self):

    get_nodes_exec = self.execCommand_local('kubectl get nodes -o wide')
    get_nodes_exec_split_row = get_nodes_exec.stdout.splitlines()

    nodes_info_ips = []
    for x in range(1, len(get_nodes_exec_split_row)):
      if args.node_group == 'all':
        get_nodes_exec_split_colum = get_nodes_exec_split_row[x].split()
        nodes_info_ips.append(get_nodes_exec_split_colum[5])
      else:
        get_nodes_exec_split_colum = get_nodes_exec_split_row[x].split()
        if args.node_group in get_nodes_exec_split_colum[0]:
          nodes_info_ips.append(get_nodes_exec_split_colum[5])

    return nodes_info_ips



###############################################################################
## Verbose & UI. ##############################################################
###############################################################################

## Colors:
### [green]     Oks, Nodes_ips, Network_interfaces_names, Network_interfaces_ips, systemservices
### [red]       Errors, 
### [yellow]    Warnings, 
### [blue]      Nodes_names,
### [magent]    Paths

## Emojis:
### :white_heavy_check_mark:    Checks, Oks, 
### :heavy_exclamation_mark:    Errors, 
### :warning:                   Warnings, 
### :person_running:            Skips, 
### :grey_question:             Asks, Questions, 



###############################################################################
## Execution. #################################################################
###############################################################################

Main()


