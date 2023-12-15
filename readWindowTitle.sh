#!/bin/bash

# X11
# Replace 'WINDOW_ID' with the actual window ID
window_id="0x2c00020"

# Use xprop to get the window title
window_title=$(xprop -id "$window_id" | grep "WM_NAME" | cut -d '"' -f 2)

# Check if the window title is obtained successfully
if [ -n "$window_title" ]; then
    echo "Window title for window $window_id: $window_title"
else
    echo "Failed to obtain the window title for window $window_id."
fi


# Wayland
# TODO
