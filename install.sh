#!/bin/bash

if [[ "$(uname)" = 'Linux' ]]; then
  sudo apt update
  sudo apt install -y zsh autojump gdb

  chsh -s $(which zsh)

elif [[ "$(uname)" = 'Darwin' ]]; then

  echo "TODO: Support Mac OS"

fi

