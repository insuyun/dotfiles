#!/usr/bin/env python3
import glob
import os
import platform
import subprocess
import sys

def replace_file(src, dest=None):
    # make as full path
    dest = os.path.join(os.environ['HOME'], dest)
    src = os.path.join(os.path.abspath(os.path.dirname(__file__)), src)
    if os.path.islink(dest):
        os.unlink(dest)
    elif os.path.exists(dest):
        old = os.path.join(os.environ['HOME'], dest + ".old")
        os.rename(dest, old)
    os.symlink(src, dest)

def install():
    # Install submodule
    for cmd in ["git submodule init", "git submodule update"]:
        subprocess.check_call(cmd, shell=True)
    
    pkgs = [
        "zsh",
        "mosh"
    ]
    
    # Set up for Linux
    if platform.system() == 'Linux':
        subprocess.check_call(
                "sudo apt-get install -y %s" % ' '.join(pkgs),
                shell=True)

        # Install zsh
        subprocess.check_call("chsh -s $(which zsh)", shell=True)

    # Install configuration files
    files = [
            'antigen',
            'gemrc',
            'gitconfig',
            'gitignore_global',
            'ideavimrc',
            'irbrc',
            'profile',
            'screenrc',
            'tmux.conf',
            'vimrc',
            'zprofile',
            'zshrc',
            'gdbinit.local',
            'bash_profile'
            ]

    for fn in files:
        replace_file(fn, ".%s" % fn)

    # Install peda
    os.system('echo "source %s/peda/peda.py " > ~/.gdbinit' 
            % os.path.abspath(os.path.dirname(__file__)))

    # Install user bin
    user_bin = os.path.join(os.environ['HOME'], 'bin')
    if not os.path.exists(user_bin):
        os.makedirs(user_bin)

    # Install inkscape for Mac OSX
    if platform.system() == "Darwin":
        replace_file("inkscape", "bin/inkscape") 

if __name__ == '__main__':
    install()
