#!/bin/bash


# Set strict mode
set -euo pipefail
IFS=$'\n\t'







# # Function to display usage information
# function showUsage() {
#   echo "Usage: $0 [--stepup | --stepdown | --reset]"
# }

# # Initialize variables with default values
# stepUp=false
# stepDown=false
# reset=false
# flagProvided=false

# # Parse command-line options
# while getopts ":h-:" opt; do
#   case $opt in
#     -)
#       case "${OPTARG}" in
#         stepup)
#           stepUp=true
#           flagProvided=true
#           ;;
#         stepdown)
#           stepDown=true
#           flagProvided=true
#           ;;
#         reset)
#           reset=true
#           flagProvided=true
#           ;;
#         *)
#           echo "Invalid option: --$OPTARG"
#           showUsage
#           exit 1
#           ;;
#       esac
#       ;;
#     h)
#       showUsage
#       exit 0
#       ;;
#     *)
#       echo "Invalid option: -$opt"
#       showUsage
#       exit 1
#       ;;
#   esac
# done

# # Check if a flag is provided
# if [ "$flagProvided" == false ]; then
#   echo "Error: Please provide a flag."
#   showUsage
#   exit 1
# fi

# # Validate that only one flag is provided
# if [[ "$stepUp" == true && ("$stepDown" == true || "$reset" == true) ]] || \
#    [[ "$stepDown" == true && ("$stepUp" == true || "$reset" == true) ]] || \
#    [[ "$reset" == true && ("$stepUp" == true || "$stepDown" == true) ]]; then
#   echo "Error: Only one flag at a time is allowed."
#   showUsage
#   exit 1
# fi

# # Perform actions based on the provided flag
# if [ "$stepUp" == true ]; then
#   echo "Performing step up..."
# elif [ "$stepDown" == true ]; then
#   echo "Performing step down..."
# elif [ "$reset" == true ]; then
#   echo "Performing reset..."
# fi















# Session specific handlers
function x11Handler() {
  # Use the 'xdotool' command to get the focused window ID in an X11 session
	focused_window_id=$(xdotool getwindowfocus)


}
function waylandHandler() {
  # Use the 'swaymsg' command to get the focused window ID in a sway (Wayland) session
  focused_window_id=$(swaymsg -t get_tree | jq -r '.. | select(.focused?).id')

  # TODO: Perform the compositor config alteration
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


