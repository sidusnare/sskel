sskel
=====

sidusnare's skeleton

WIP
==
This is a massive work in progress. It reflects the way I do things with a UNIX style ./usr/ folder in my home directory. It is an effort to separate the generic and environment specific components of my custom environment. Hopefully you will find something here that can be of use to you, perhaps a new way of managing your $HOME folder. I have tried to make these scripts platform independent, as I myself move across Linux, MacOS, and Solaris.

Reason for the madness
==
The goals here are:
1) Not to have a cluttered $HOME folder
2) Not modify or add to the system-wide path, to maintain your own setup in a shared environment and to maintain portability.
3) Have things arranged so that having your common custom scripts in a git repository
4) Workstation and platform agnosticism.

The idea is that all your workstations have this same layout, you use a git repo to replicate and sync, and you can just use all the scripts you have written without trying to think what computer you wrote whatever script on and will it work on this one.

Example of usefulness
==
Sometimes I need to run specific versions of software, such as firefox or java. Changing this system wide is a pain, and can affect other software or users. I can extract my desired version in $HOME/usr/local/opt, symlink the bin to "$HOME/usr/local/bin/ and since everything has that, even my X11 environment because of the custom .xinitrc, I get everything using that version of firefox/java/whatever like nothing changed.
I can write custom scripts, that I want to use on any of my workstations, and keep it in $HOME/usr/bin. Since I use git to keep everything outside /local/ in sync I dont have to think about what I wrote where and when. I just do a git pull and everything is there. If I can even merge multiple changes I make, so I am not duplicating my work.
Warnings
==
If you follow the instructions, this will overwrite .bashrc .profile and .gnupg in your home directory.
If you follow the instructions, this will overwrite .bashrc .profile and .gnupg in your home directory.
If you follow the instructions, this will overwrite .bashrc .profile and .gnupg in your home directory.
If you follow the instructions, this will overwrite .bashrc .profile and .gnupg in your home directory.
If you follow the instructions, this will overwrite .bashrc .profile and .gnupg in your home directory.

If you follow the instructions, this will overwrite .bashrc .profile and .gnupg in your home directory.


Use
==
Run these commands and you will get started, however this will overwrite .bashrc .profile and .gnupg in your home directory.
cd $HOME
git clone https://github.com/sidusnare/sskel.git usr
bash -x $HOME/usr/sanity.quick

Notes
==
You will see a folder, ./etc/loc.d , which has no apparent use. I have a personal web server that uses a .php script and array and known IPs / subnets to return a short one word name for my current location, like "work", "home", "moms", or "coffehouse". I have scripts to include with these names in that folder. There are many ways to implement this same functionality depending on your situation so I lect this code out, but the directory in place. Implementing this idea I leave as an exercise for the reader
