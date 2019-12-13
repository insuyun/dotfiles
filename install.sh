#!/bin/bash

# Install packages
PKGS=(zsh autojump gdb)
sudo apt update

for pkg in "${PKGS[@]}"
do
  sudo apt install $pkg
done

# TODO: Support Mac OS
