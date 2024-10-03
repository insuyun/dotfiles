# dotfiles

[@jakkdu](https://github.com/jakkdu)' dotfiles.

## Installation

- Clone this repository:
``` sh
git clone https://github.com/jakkdu/dotfiles.git
cd dotfiles
```

- Install dependencies with a root privilege
``` sh
./install.sh
```

- Setup environment

```sh
./setup.sh
```

## Installation (with docker)
```sh
docker build -t pwn_docker .
docker run --privileged -v $(pwd):/mnt -it pwn_docker
```
