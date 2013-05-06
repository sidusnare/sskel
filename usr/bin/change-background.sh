#!/bin/bash
#Wrapper for python script to import env from flat files
#Fred Dinkler IV


source "$HOME"/usr/local/var/env
GSPID=`pidof gnome-session`
PIC=`"$HOME"/usr/bin/change-background.py`
echo New picture is $PIC
if [ -n "$GSPID"  ] ; then
	echo with gnome
	gconftool-2 -t str -s /desktop/gnome/background/picture_filename "$PIC"
fi
if [ -n "$WMAKER_BIN_NAME" ];then
	echo with windowmaker
	wmsetbg "$PIC"
fi
