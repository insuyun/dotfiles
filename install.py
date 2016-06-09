#!/usr/bin/env python2
import os
import sys
import glob

ROOT = os.path.abspath(os.path.dirname(__file__))

def exec_cmds(*cmds):
    for cmd in cmds:
        os.system(cmd)

def mkdir(dn):
    if not os.path.exists(dn):
        os.makedirs(dn)

def init_submodules():
    exec_cmds("git submodule init",
                "git submodule update")

def git_clone(addr, dirp):
    path = os.path.join(os.environ['HOME'], dirp)
    if not os.path.exists(path):
        os.system("git clone %s %s" % (addr, path))
    else:
        print("~/%s already exists" % dirp)


def replace_file(src, dest = None):
    if not dest:
        dest = ".%s" % src
    # make as full path
    dest = os.path.join(os.environ['HOME'], dest)
    src = os.path.join(ROOT, src)

    if os.path.islink(dest):
        os.unlink(dest)
    elif os.path.exists(dest):
        old = os.path.join(os.environ['HOME'], dest + ".old")
        os.rename(dest, old)
    os.symlink(src, dest)

def create_bin_dir():
    bin_d = os.path.join(os.environ['HOME'], 'bin')
    mkdir(bin_d)

def handle_link():
    init_submodules()
    create_bin_dir()
    files = ['antigen',
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
                'bash_profile']

    for fn in files:
        replace_file(fn)

    # setup peda gdb
    os.system('echo "source $DIR/peda/peda.py " > ~/.gdbinit')
    os.system('echo "source ~/.gdbinit.local" >> ~/.gdbinit')

    for fn in glob.glob("bin/*"):
        replace_file(fn, fn)
    print('Done.')

def usage():
    print("usage : %s <command>\n"
            "\n"
            "Available commands\n"
            "   link        Install symbolic links\n" % sys.argv[0])
    sys.exit(-1)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        usage()

    if sys.argv[1] == "link":
        handle_link()
    else:
        usage()
