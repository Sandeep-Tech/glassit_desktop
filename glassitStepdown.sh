#!/bin/bash

# Set strict mode
set -euo pipefail
IFS=$'\n\t'

# Global variables
STEP=2

# Session specific handlers
function x11Handler() {

  # Use the 'xdotool' command to get the focused window ID in an X11 session
	focusedWindowId=$(xdotool getwindowfocus)
  echo "focused window id $focusedWindowId"

  # TODO: need to figure out the existing level of alpha for the given window inorder to base the next value upon

  # Lower the window opacity
  xprop \
    -id ${codeWindowId} \
    -f _NET_WM_WINDOW_OPACITY 32c \
    -set _NET_WM_WINDOW_OPACITY $(printf 0x%x $((0xffffffff * ${alpha} / 255)))

}
function waylandHandler() {
  # Use the 'swaymsg' command to get the focused window ID in a sway (Wayland) session
  focusedWindowId=$(swaymsg -t get_tree | jq -r '.. | select(.focused?).id')
  
  # TODO: COMPLETE ME
  echo "This feature is not yet implemented for wayland display server systems..."  # Placeholder msg
}


# Run session specific flow
if ( shopt -s nocasematch; [[ "$XDG_SESSION_TYPE" == 'x11' ]] ); then
  echo On X11 system
	x11Handler
elif [[ "$XDG_SESSION_TYPE" == 'wayland' ]]; then
	echo on Wayland system
  waylandHandler
fi
