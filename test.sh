#!/bin/bash

# # echo this is a string without quotes
# # echo this is a string with quotes


# # Initialize variables with default values
# flag_a=false
# flag_b=false
# flag_c=""
# positionals=()

# # Parse command-line options
# while getopts ":abc:" opt; do
#   case "$opt" in
#     a)
#       flag_a=true
#       ;;
#     b)
#       flag_b=true
#       ;;
#     c)
#       flag_c="$OPTARG"
#       ;;
#     \?)
#       echo "Invalid option: -$OPTARG" >&2
#       exit 1
#       ;;
#     :)
#       echo "Option -$OPTARG requires an argument." >&2
#       exit 1
#       ;;
#   esac
# done

# # Shift the processed options, so that $1, $2, etc. refer to the remaining arguments
# shift $((OPTIND-1))

# # Process the remaining positional arguments
# positionals=("$@")

# # Print the values of the flags and positional arguments
# echo "Flag A: $flag_a"
# echo "Flag B: $flag_b"
# echo "Flag C: $flag_c"
# echo "Positional Arguments: ${positionals[@]}"


while getopts "hvf:" flag; do
 case $flag in
   h) # Handle the -h flag
   # Display script help information
   echo h flag registered
   ;;
   v) # Handle the -v flag
   # Enable verbose mode
   echo v flag registered
   ;;
   f) # Handle the -f flag with an argument
   filename=$OPTARG
   # Process the specified file
   ;;
   \?)
   # Handle invalid options
   ;;
 esac
done