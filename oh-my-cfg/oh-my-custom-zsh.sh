#!/bin/bash
###############################################################################
##        Name: oh-my-custom-zsh.sh                                           #
##        Date: 09/11/2021                                                    #
## Description: Custom configuration of oh-my-zsh.                            #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



# Script information.
scriptName="oh-my-custom-zsh"
scriptVersion="b1.0"

# Script directories.
scriptPath=$(cd $(dirname $0) ; pwd -P)/
srcPath=$scriptPath"src/"

# Common strings.
tab="--> "
title="Loading $scriptName $scriptVersion...\n\n"

# Package-manager.
installerMedia="apt"

# User information.
#logUser=$(logname)
logUser="user"
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

  # Checking script dependencies.
  Check_Dependencies

  # Installing oh-my-zsh
  OhMyZsh

  if [ "$errors" != "" ]; then
    Catch
  fi

  exit 0
}

OhMyZsh () {

  echo Hello
  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended

}



###############################################################################
## Auxiliary methods. #########################################################
###############################################################################

# Process interrupt or <(CTRL + C)> combination captured.
Catch () {

  clear -x

  if [ "$errors" != "" ]; then
    echo -e "[ERROR LOG]\n\n$errors"
    exit 1
  fi

  echo "The script $scriptName has been forced to close..."
  exit 1
}

# Checking script dependencies.
Check_Dependencies () {

  # Checking binary of the dependency.
  checkBinary=$(which git | wc -l)

  # Actions in case of not finding it.
  if [ $checkBinary -eq 0 ]; then

    echo "Trying to install git..."
    $installerMedia -y install git

    if [ $checkBinary -eq 0 ]; then
      errors=$errors$tab"[ERROR] Not git binary found. Please install it and try again.\n"
      Catch
    fi
  fi

  # Checking binary of the dependency.
  checkBinary=$(which zsh | wc -l)

  # Actions in case of not finding it.
  if [ $checkBinary -eq 0 ]; then

    echo "Trying to install zsh..."
    $installerMedia -y install zsh
    chsh -s $(which zsh)

    if [ $checkBinary -eq 0 ]; then
      errors=$errors$tab"[ERROR] Not zsh binary found. Please install it and try again.\n"
      Catch
    fi
  fi

  # Checking binary of the dependency.
  checkBinary=$(which curl | wc -l)

  # Actions in case of not finding it.
  if [ $checkBinary -eq 0 ]; then

    echo "Trying to install curl..."
    $installerMedia -y install curl

    if [ $checkBinary -eq 0 ]; then
      errors=$errors$tab"[ERROR] Not curl binary found. Please install it and try again.\n"
      Catch
    fi
  fi
}



###############################################################################
## Execution. #################################################################
###############################################################################

# Script execution start.
Main


