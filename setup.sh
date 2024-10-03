#!/bin/bash

DIRNAME="$(dirname "$0")"
DIR="$(cd "$DIRNAME" && pwd)"

function replace_file() {
  if [[ "$#" -ne 2 ]]; then
    echo "Illegal number of parameters"
    exit -1
  fi

  local dst=$2
  local src=$DIR/$1

  if [[ -L "$dst" ]]; then
    rm $dst
  elif [[ -f "$dst" ]]; then
    mv $dst $dst.old
  fi

  echo "Replace $src -> $dst"
  ln -s $src $dst
}

function append_if_not_exist() {
  if [[ "$#" -ne 2 ]]; then
    echo "Illegal number of parameters"
    exit -1
  fi

  grep -qF -- "$1" "$2" || echo "$1" >> "$2"
}

# Initialize submodules
git submodule init
git submodule update

configs=(bash_profile bashrc gitconfig gitignore_global ideavimrc profile tmux.conf vimrc zprofile zshrc)

# Install configs
for config in "${configs[@]}"
do
  replace_file config/$config ~/.$config
done

replace_file 3rd/antigen ~/.antigen

# Install pwndbg
pushd 3rd/pwndbg
./setup.sh
popd


# Install bin
mkdir -p ~/bin

if [ "$(uname)" = 'Darwin' ]; then
  replace_file bin/inkscape ~/bin
fi

# Install pyenv
if [ "$(uname)" = 'Linux' ]; then
  if [[ ! -e ~/.pyenv ]]; then
    git clone https://github.com/pyenv/pyenv.git ~/.pyenv
    git clone https://github.com/pyenv/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
  fi
fi


# Install rust + ropr
if ! command -v rustc &> /dev/null
then
  curl https://sh.rustup.rs -sSf | sh -s -- -y
fi
export PATH=$PATH:$HOME/.cargo/bin
cargo install ropr

