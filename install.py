#!/usr/bin/env python3
import os
import sys
import glob

ROOT = os.path.abspath(os.path.dirname(__file__))
BIN_DIR = os.path.join(os.environ['HOME'], 'bin')

def install_peda():
    # setup peda gdb
    os.system('echo "source $DIR/peda/peda.py " > ~/.gdbinit')

def mkdir(dn):
    if not os.path.exists(dn):
        os.makedirs(dn)

def init_submodules():
    cmds = (
            "git submodule init",
            "git submodule update"
            )

    for cmd in cmds:
        os.system(cmd)

def install_bin():
    # install inkscape for Mac OSX
    if sys.platform == "darwin":
        replace_file("inkscape", "bin/inkscape") 

    # install make-loop
    replace_file("make-loop", "bin/make-loop")

def replace_file(src, dest=None):
    # make as full path
    dest = os.path.join(os.environ['HOME'], dest)
    src = os.path.join(ROOT, src)
    if os.path.islink(dest):
        os.unlink(dest)
    elif os.path.exists(dest):
        old = os.path.join(os.environ['HOME'], dest + ".old")
        os.rename(dest, old)
    os.symlink(src, dest)

def handle_link():
    init_submodules()
    mkdir(BIN_DIR)
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

    install_peda()
    install_bin()

    print('Done.')

def usage():
    print("usage : %s <command>\n"
            "\n"
            "Available commands\n"
            "\tlink\t\tInstall symbolic links\n" % sys.argv[0])
    sys.exit(-1)

def main():
    if sys.argv[1] == "link":
        handle_link()
    else:
        usage()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()
    main()
