# Config

Configuration files for [@yous](https://github.com/yous)

## Requirements

* [Git][]
* [Vundle][]

[Git]: http://git-scm.com
[Vundle]: https://github.com/gmarik/vundle

## Install

1. Clone this repository:

    ``` sh
    $ git clone git@github.com:yous/config.git
    $ cd config
    $ git submodule init
    $ git submodule update
    ```

2. Copy configuration files to home directory:

    ``` sh
    $ ./install.sh
    $ git config --global core.excludesfile ~/.gitignore
    ```

3. Install dependencies:

    If you are using [RVM][],

    ``` sh
    $ rvm use current@global
    $ gem install what_methods wirble
    ```

    Otherwise just install gems:

    ``` sh
    $ gem install what_methods wirble
    ```

    In [Vim][],

    ```
    :BundleInstall
    ```

    To use [Zsh][] as default shell,

    ``` sh
    $ chsh -s /bin/zsh
    ```

[RVM]: http://rvm.io
[Vim]: http://www.vim.org
[Zsh]: http://www.zsh.org
