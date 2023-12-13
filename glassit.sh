#!/bin/bash


# Set strict mode
set -euo pipefail
# IFS=$'\n\t'


# Util
# function getTargetWindowId() {
#   # Check if the session is Wayland
#   if [[ "$XDG_SESSION_TYPE" == 'wayland' ]]; then
#     # Use the 'swaymsg' command to get the focused window ID in a sway (Wayland) session
#     focused_window_id=$(swaymsg -t get_tree | jq -r '.. | select(.focused?).id')
#     echo "Focused Window ID in Wayland: $focused_window_id"
#   elif [[ "$XDG_SESSION_TYPE" == 'x11' ]]; then
#     # Use the 'xdotool' command to get the focused window ID in an X11 session
#     focused_window_id=$(xdotool getwindowfocus)
#     echo "Focused Window ID in X11: $focused_window_id"
#   else
#     echo "Unsupported session type: $XDG_SESSION_TYPE"
#   fi
# }
function getWaylandTargetWindowId() {
  # Use the 'swaymsg' command to get the focused window ID in a sway (Wayland) session
  focused_window_id=$(swaymsg -t get_tree | jq -r '.. | select(.focused?).id')
  echo "Focused Window ID in Wayland: $focused_window_id"
	# return focused_window_id
}
function getX11TargetWindowId() {
	# Use the 'xdotool' command to get the focused window ID in an X11 session
	focused_window_id=$(xdotool getwindowfocus)
  echo "Focused Window ID in X11: $focused_window_id"
	# return focused_window_id
}


# Session specific handlers
function x11Handler() {
  # echo "session is x11"
  getX11TargetWindowId
  # targetWindowId = $(getX11TargetWindowId)
  # echo "$targetWindowId"
  
}
function waylandHandler() {
  # echo "session is wayland"
  getWaylandTargetWindowId
  # targetWindowId = $(getWaylandTargetWindowId)
  # echo "$targetWindowId"
}


# Run session specific flow
if ( shopt -s nocasematch; [[ "$XDG_SESSION_TYPE" == 'x11' ]] ); then
	x11Handler
elif [[ "$XDG_SESSION_TYPE" == 'wayland' ]]; then
	waylandHandler
fi







# # !/bin/bash

# string1="Hello"
# string2="hello"

# # Perform case-insensitive string comparison in a subshell
# if (shopt -s nocasematch; [[ $string1 == $string2 ]] ); then
#     echo "Strings are equal (case-insensitive)"
# else
#     echo "Strings are not equal (case-insensitive)"
# fi





# # Read the instruction
# instr=$1

# # Check if instruction is not provided
# if [ -z "$instr" ]; then
#     echo "Please provide an instruction"
#     exit 1
# fi

# # Read the current active window in a Wayland environment
# # Assuming you have a tool like wdisplays that prints active Wayland surface
# active_window_info=$(wdisplays | grep "focused")

# # Extract window ID and name
# window_id=$(echo "$active_window_info" | awk '{print $1}')
# window_name=$(echo "$active_window_info" | awk '{print $2}')

# # Print the results to the console
# echo "Active Window ID: $window_id"
# echo "Active Window Name: $window_name"


