# dotfiles

[@jakkdu](https://github.com/jakkdu)' dotfiles.

- [Requirements](#requirements)
- [Install](#install)
    - [Git](#git)
    - [Homebrew](#homebrew)
    - [Ruby](#ruby)
    - [Zsh](#zsh)
    - [Vim](#vim)
    - [IntelliJ, Android Studio](#intellij-android-studio)
    - [iTerm2](#iterm2)
    - [Mac OS X](#mac-os-x)

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
./install.sh
```

Command option | Description
---------------|-----------------------------------------------
`link`         | Install symbolic links
`brew`         | Install Homebrew
`formulae`     | Install Homebrew formulae using Brewfile
`npm`          | Install global Node.js packages
`rbenv`        | Install rbenv
`rvm`          | Install RVM

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

### Homebrew

If you want to install [Homebrew](http://brew.sh),

``` sh
./install.sh brew
```

Then install Homebrew formulae with:

``` sh
rvm use system # To compile Vim with Ruby support
./install.sh formulae
```

### Ruby

If you want to install [RVM](http://rvm.io),

``` sh
./install.sh rvm
```

Update RVM with:

``` sh
rvm get stable
```

If you want to install [rbenv](https://github.com/sstephenson/rbenv),

``` sh
./install.sh rbenv
```

If you are using RVM,

``` sh
gem update --system
rvm use current@global
gem install rake rubocop wirble
```

Otherwise just install gems:

``` sh
gem update --system
gem install rake rubocop wirble
```

### Zsh

To use [Zsh](http://www.zsh.org) as default shell,

``` sh
chsh -s /bin/zsh
```

If you use custom Zsh like compiled one by [Homebrew](http://brew.sh),

``` sh
chsh -s /usr/local/bin/zsh
```

To update [Antigen](http://antigen.sharats.me):

``` sh
antigen selfupdate
```

To update Zsh plugins:

``` sh
antigen update
```

To make RVM works on Mac OS X Vim, move `/etc/zshenv` to `/etc/zshrc` as [Tim Pope mentioned](https://github.com/tpope/vim-rvm#faq).

``` sh
sudo mv /etc/zshenv /etc/zshrc
```

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

### IntelliJ, Android Studio

To use [Tomorrow Theme](https://github.com/ChrisKempson/Tomorrow-Theme):

1. Open File > Import Settings… in [IntelliJ](http://www.jetbrains.com/idea/) or [Android Studio](http://developer.android.com/sdk/installing/studio.html).
2. Select `tomorrow-theme/JetBrains/settings.jar`.
3. Open Settings > Editor > Colors & Fonts.
4. Select a scheme of Tomorrow Theme.

### iTerm2

To use [Solarized](https://github.com/altercation/solarized) on [iTerm2](http://www.iterm2.com):

1. Open Preferences… > Profiles > Colors.
2. Click 'Load Presets…' and select 'Import…'.
3. Select `*.itermcolors` files under `solarized/iterm2-colors-solarized/`.
4. Click 'Load Presets…' again and select one of Solarized.

To use [Tomorrow Theme](https://github.com/ChrisKempson/Tomorrow-Theme):

1. Open Preferences… > Profiles > Colors.
2. Click 'Load Presets…' and select 'Import…'.
3. Select `*.itermcolors` files under `tomorrow-theme/iTerm2/`.
4. Click 'Load Presets…' again and select one of Tomorrow Theme.

### Mac OS X

To write to NTFS external disk, be sure [FUSE for OS X](http://osxfuse.github.io) is installed already. After that,

``` sh
brew install ntfs-3g
```

If your Mac OS X version is 10.9 or earlier, you can install FUSE for OS X with brew command. See more information in [How to Write to NTFS External Disk Drives from OS X 10.9.2 Mavericks](http://coolestguidesontheplanet.com/how-to-write-to-a-ntfs-drive-from-os-x-mavericks/). The original `/sbin/mount_ntfs` links to `/System/Library/Filesystems/ntfs.fs/Contents/Resources/mount_ntfs`.
