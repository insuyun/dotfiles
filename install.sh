#!/bin/bash

if [[ "$(uname)" = 'Linux' ]]; then
  pkgs=(zsh autojump gdb)
  sudo apt update

  for pkg in "${pkgs[@]}"
  do
    sudo apt install $pkg
  done

  chsh -s $(which zsh)

elif [[ "$(uname)" = 'Darwin' ]]; then

  echo "TODO: Support Mac OS"

fi

