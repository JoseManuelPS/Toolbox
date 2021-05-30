#!/bin/bash
###############################################################################
##        Name: <(script_name)>                                               #
##        Date: <(script_date)>                                               #
## Description: <(script_description)>                                        #
##----------------------------------------------------------------------------#
##     <(Extra: -> Content)>                                                  #
##              -> <(Content)>                                                #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



# Script information.
scriptName="<(script_name)>"
scriptVersion="<(script_version)>"

# Script directories.
scriptPath=$(cd $(dirname $0) ; pwd -P)/
srcPath=$scriptPath"src/"

# Common strings.
tab="--> "
title="Loading $scriptName $scriptVersion...\n\n"

# Package-manager.
installerMedia="<(package_manager)>"

# User information.
logUser=$(logname)
if ["$logUser" == "root"]; then
  logUser_Home="/root/"
else
  logUser_Home="/home/$logUser/"
fi
execUser=$(whoami)
execUser_Home="$(echo $HOME)"



###############################################################################
## Main code. #################################################################
###############################################################################

Main () {

  clear -x
  echo -e $title

  # Directory change to the directory where the script is executed.
  cd $scriptPath

  # Process interrupt or <(CTRL + C)> combination captured.
  trap 'Catch' SIGINT

  # Checking the script execution as root user.
  Check_Root

  # Checking script dependencies.
  Check_Dependencies

  # Print shell custom menu.
  Print_SMenu

  # Print dialog custom menu.
  Print_DMenu

  # Switch-Case of selected option.
  case "$selectedOption" in
    1)
      Option
    ;;
    *)
      clear
    ;;
  esac

  # Process-Start: Verbose-Off
  # # Comment on the block
  # Command on the block
  # Process-End: Verbose-Off

  # Process-Start: Verbose-On
  # Comment on the bock
  <(command_on_the_block)>
  # Process-End: Verbose-On

  if ["$errors" != ""]; then
    Catch
  fi

  exit 0
}



###############################################################################
## Auxiliary methods. #########################################################
###############################################################################

# Process interrupt or <(CTRL + C)> combination captured.
Catch () {

  if ["$errors" != ""]; then
    echo -e $errors
    exit 1
  fi

  clear -x
  echo "The script $scriptName has been forced to close..."
  exit 1
}

# Checking the script execution as root user.
Check_Root () {

  if ["$execUser" != "root"]; then
    error=$error$tab"The $scriptName must be run as root, please try again.\n"
    Catch
  fi
}

# Checking script dependencies.
Check_Dependencies () {

  # Checking binary of the dependency.
  checkBinary=$(which <(dependency)> | wc -l)

  # Actions in case of not finding it.
  if [$checkBinary -eq 0]; then
    <(command_to_resolve_this_dependency)>
    # or
    error=$error$tab"<(actions_to_resolve_this_dependency)>.\n"
    Catch
  fi
}



###############################################################################
## Verbose & UI. ##############################################################
###############################################################################

# Print shell custom menu.
Print_SMenu () {

  possibleOptions=2

  clear -x
  echo -e " _________________________________________________________________ "
  echo -e "|                                                                 |"
  echo -e "| Please select one of the following options:                     |"
  echo -e "|                                                                 |"
  echo -e "| 1)  Option 1.                                                   |"
  echo -e "| 2)  Option 2.                                                   |"
  echo -e "|-----------------------------------------------------------------|"
  echo -e "| 0)  Exit.                                                       |"
  echo -e "|_________________________________________________________________|\n"
  read -p "Selected option: " selectedOption

  # Captured of user selected option.
  whileExit=0
  while [$whileExit -eq 0]; do
    for ((x=0; x<=$possibleOptions; x++)); do
      if ["$selectedOption" == "$x"]; then
        whileExit=1
      fi
    done
    if [$whileExit -eq 0]; then
      read -p "Invalid option, please try again: " selectedOption
    fi
  done
}

# Print dialog custom menu.
Print_DMenu () {

  possibleOptions=2

  selectedOption=$(dialog --stdout --backtitle "$title" --title "Main menu" \
    --menu "Please select one of the following options:" 15 60 \
    $possibleOptions \
    1- "Option_1." \
    2- "Option_2.")

  # Captured of user selected option.
  for ((x=1; x<=$possibleOptions; x++)); do
    if ["$possibleOptions" = "$x-"]; then
      selectedOption=$x
    elif ["$possibleOptions" = ""]; then
      selectedOption=0
    fi
  done
}



###############################################################################
## Execution. #################################################################
###############################################################################

# Script execution start.
Main


