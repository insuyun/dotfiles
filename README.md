# dotfiles

[@jakkdu](https://github.com/jakkdu)' dotfiles.

- [Requirements](#requirements)
- [Install](#install)
    - [Git](#git)
    - [Zsh](#zsh)
    - [Vim](#vim)

## Requirements

- [Git](http://git-scm.com)

## Install

Clone this repository:

``` sh
git clone https://github.com/jakkdu/dotfiles.git
cd dotfiles
```

For available install options:

``` sh
./install.py
```

Command option | Description
---------------|-----------------------------------------------
`link`         | Install symbolic links

### Git

Set user-specific configurations on `gitconfig`:

```
[user]
	name = Your Name
	email = you@example.com
```

If you are using [Keybase](https://keybase.io):

```
[user]
	signingkey = YOUR KEY
[commit]
	gpgsign = true
```

For more information about signing commits, see [A Git Horror Story: Repository Integrity With Signed Commits](http://mikegerwitz.com/papers/git-horror-story).

### Vim

To install [Vim](http://www.vim.org) plugins,

```
:PlugInstall
```

To update Vim plugins:

```
:PlugUpdate
```

To update [vim-plug](https://github.com/junegunn/vim-plug):

```
:PlugUpgrade
```

For additional syntax checkers for [Syntastic](https://github.com/scrooloose/syntastic):

- CSS (CSSLint): `./install npm`
- HTML (JSHint): `./install npm`
- JavaScript (JSHint, JSLint): `./install npm`
- JSON (JSONLint): `./install npm`
- Ruby (RuboCop, ruby-lint): `gem install rubocop ruby-lint`
- SASS: `gem install sass`
- SCSS: `gem install sass scss-lint`
- xHTML (JSHint): `./install npm`
