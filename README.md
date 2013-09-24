sting-launcher
==============

Simple and minimal GTK+Cairo application launcher written in Python.

For example, you want to open a terminal, so you...

> `Super-space`, `term`, `Enter` & voilà

Menuless, mouseless, iconless.

features
--------

-   launches programs
-   config files to customize aliases and colors ;D
-   before you ask yes, it is inspired on long defunct Enso Launcher
-   before you complain yes, it is way simpler than Enso Launcher

ingredients
-----------

- Linux (I think);
- Python (I'm sure);
- Googling powers.

installation
------------

-   git clone this repo to a path (here it is in `~/bin/sting`, or you 
    may prefer `/opt/sting`, or any other path meets your taste);
    
-   `mkdir -p ~/.config/sting`
-   `cp your/sting/path/aliases ~/.config/sting/`
-   `cp your/sting/path/colors ~/.config/sting`
-   edit both files to your taste
-   you can test it running `python your/sting/path/sting.py` on a 
    terminal
-   bind a keystroke to sting acording to your system
-   sting's lightness and freshness is ready for your finger tips

Keybind hint for crunchbang users:
-   open `~/.config/openbox/rc.xml`
-   find the line with `<keybind key="W-space">`
-   change this tag's command to `python your/sting/path/sting.py`

instructions
------------

-   when the 'type it' screen apears, start typing the name of the
    alias you want to run; when the autocompletion shows what you expect
    press `Enter`;
-   press `Backspace` to remove the last entered character;
-   press `Escape` to clear what you typed, and again to close the 
    window;
-   that's it.

license
-------

Use it as you wish, do not blame me.
