#!/bin/bash

# X11
# Get the window ID (replace 'WINDOW_TITLE' with the actual window title)
window_id=$(xprop -root | grep '_NET_ACTIVE_WINDOW(WINDOW)' | sed -n 's/.*\(0x[0-9a-f]\+\).*/\1/p')

# Check if the window ID is obtained successfully
if [ -n "$window_id" ]; then
    # Use xprop to get the value of _NET_WM_WINDOW_OPACITY for the window
    opacity_value=$(xprop -id "$window_id" _NET_WM_WINDOW_OPACITY | awk '{print $NF}')

    # Print the opacity value
    echo "Opacity value for window $window_id: $opacity_value"
else
    echo "Failed to obtain the window ID."
fi


# wayland
# TODO
