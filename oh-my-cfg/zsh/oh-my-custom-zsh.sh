#!/bin/bash
###############################################################################
##        Name: oh-my-custom-zsh.sh                                           #
##        Date: 11/12/2021                                                    #
## Description: Custom configuration of oh-my-zsh.                            #
##----------------------------------------------------------------------------#
##      Editor: José Manuel Plana Santos                                      #
##     Contact: dev.josemanuelps@gmail.com                                    #
###############################################################################



# Script information.
scriptName="oh-my-custom-zsh"
scriptVersion="v1.0"

# Script directories.
scriptPath=$(cd $(dirname $0) ; pwd -P)/
srcPath=$scriptPath"src/"

# Common strings.
tab="--> "
title="Loading $scriptName $scriptVersion...\n\n"

# Checking binary of package manager.
checkBinary=$(which apt | wc -l)
if [ $(which apt | wc -l) -eq 1 ]; then
  installerMedia="sudo apt"
elif [ $(which dnf | wc -l) -eq 1 ]; then
  installerMedia="sudo dnf"
elif [ $(which yum | wc -l) -eq 1 ]; then
  installerMedia="sudo yum"
fi

# User information.
execUser=$(echo $USER)
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

  # Installing oh-my-zsh
  OhMyZsh-Config

  if [ "$errors" != "" ]; then
    Catch
  fi

  exit 0
}

OhMyZsh () {

  sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
  ZSH_CUSTOM=$execUser_Home'/.oh-my-zsh/custom'
}

OhMyZsh-Config () {

  aliasFile="/tmp/.oh-my-custom-zsh.alias"
  if [ -f $aliasFile ]; then
    rm -f $aliasFile
  fi

  plugins="git"

  read -p "Do you want to install powerlevel10k theme? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    
    git clone --depth=1 https://github.com/romkatv/powerlevel10k.git $ZSH_CUSTOM/themes/powerlevel10k
    
    read -p "Do you want to load custom powerlevel10k theme? [y/n]: " selectedOption
    if [ "$selectedOption" == "y" ]; then
      cp ./.p10k.zsh $execUser_Home
      sed -i 's|ZSH_THEME.*|ZSH_THEME=\"powerlevel10k/powerlevel10k\"|' $execUser_Home/.zshrc
    fi
  fi

  read -p "Do you want to install zsh-syntax-highlighting plugin? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    git clone https://github.com/zsh-users/zsh-syntax-highlighting.git $ZSH_CUSTOM/plugins/zsh-syntax-highlighting
    plugins=$plugins" zsh-syntax-highlighting"
  fi

  read -p "Do you want to install zsh-completions plugin? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    git clone https://github.com/zsh-users/zsh-completions $ZSH_CUSTOM/plugins/zsh-completions
    plugins=$plugins" zsh-completions"
  fi

  read -p "Do you want to install zsh-autosuggestions plugin? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    git clone https://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions
    plugins=$plugins" zsh-autosuggestions"
  fi

  read -p "Do you want to install custom k => z plugin? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    git clone https://github.com/supercrabtree/k $ZSH_CUSTOM/plugins/k; sed -i 's/^k[[:space:]]/z /g' ${ZSH_CUSTOM}/plugins/k/k.sh
    plugins=$plugins" k"
    echo "alias f=\"z -ha\"" >> $aliasFile
  fi

  read -p "Do you want to install custom kubectl plugin? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    plugins=$plugins" kubectl"
    echo "alias k=\"kubectl\"" >> $aliasFile
    echo "alias ka=\"kubectl apply\"" >> $aliasFile
    echo "alias kd=\"kubectl describe\"" >> $aliasFile
    echo "alias ke=\"kubectl exec\"" >> $aliasFile
    echo "alias kg=\"kubectl get\"" >> $aliasFile
    echo "alias kga=\"kubectl get all\"" >> $aliasFile
    echo "alias kl=\"kubectl logs\"" >> $aliasFile
    echo "alias kr=\"kubectl run\"" >> $aliasFile
    echo "alias krm=\"kubectl delete\"" >> $aliasFile
  fi

  read -p "Do you want to install custom minikube plugin? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    plugins=$plugins" minikube"
  fi

  read -p "Do you want to install custom docker plugin? [y/n]: " selectedOption
  if [ "$selectedOption" == "y" ]; then
    plugins=$plugins" docker"
    echo "alias d=\"docker\"" >> $aliasFile
  fi

  sed -i "s|plugins.*|plugins=($plugins)|" $execUser_Home/.zshrc

  cat $aliasFile >> $execUser_Home/.zshrc
  if [ -f $aliasFile ]; then
    rm -f $aliasFile
  fi

  echo "# To customize prompt, run \'p10k configure\' or edit ~/.p10k.zsh." >> $execUser_Home/.zshrc
  echo "[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh" >> $execUser_Home/.zshrc
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

  # Checking binary of the git dependency.
  checkBinary=$(which git | wc -l)

  # Actions in case of not finding it.
  if [ $checkBinary -eq 0 ]; then

    echo "Trying to install git..."
    $installerMedia -y install git

    checkBinary=$(which git | wc -l)
    if [ $checkBinary -eq 0 ]; then
      errors=$errors$tab"[ERROR] Not git binary found. Please install it and try again.\n"
      Catch
    fi
  fi

  # Checking binary of the zsh dependency.
  checkBinary=$(which zsh | wc -l)

  # Actions in case of not finding it.
  if [ $checkBinary -eq 0 ]; then

    echo "Trying to install zsh..."
    $installerMedia -y install zsh
    echo "Configuring zsh as default shell..."
    chsh -s $(which zsh)

    checkBinary=$(which zsh | wc -l)
    if [ $checkBinary -eq 0 ]; then
      errors=$errors$tab"[ERROR] Not zsh binary found. Please install it and try again.\n"
      Catch
    fi
  fi

  # Checking binary of the curl dependency.
  checkBinary=$(which curl | wc -l)

  # Actions in case of not finding it.
  if [ $checkBinary -eq 0 ]; then

    echo "Trying to install curl..."
    $installerMedia -y install curl

    checkBinary=$(which curl | wc -l)
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


