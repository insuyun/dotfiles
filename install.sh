#!/bin/bash

if [[ "$(uname)" = 'Linux' ]]; then
  sudo apt update
  sudo apt install -y zsh autojump gdb
  sudo chsh -s $(which zsh) $USER

elif [[ "$(uname)" = 'Darwin' ]]; then

  echo "TODO: Support Mac OS"

fi

