There exists several display servers (for example: Xorg and wayland) these haev their own compositor (the thing that 'composes' the final image (of the various application windows) that we see on the desktop)

Ubuntu made a switch to wayland system in their newer version but maintained a compatibility layer with xorg (probably not perfectly complete compatibiliy)

These two display servers xorg and waylang have different corresponding tool to configure them xtool and sway something respectively.

These is what will help me manipulate the opacity of a window.

Example
```bash
xprop -f _NET_WM_WINDOW_OPACITY 32c -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * 80 / 100)))
```

TODO: figure out the active window from where the shortcut command is issued from.

TODO: tie two above two components (the configurator and the active window identifier) with a driver interface (shortcut keys)
