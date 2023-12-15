"""
A simple POC
This script is invoked by the xbindkeys program with appropriate args
"""
import sys
import os
import subprocess
import re
import json







# class CompositorUtils:
#     def __init__(self):
#         # Determine the compositor type
#         self.compositor_type = self._detect_compositor()

#     def _detect_compositor(self):
#         session_type = os.environ.get('XDG_SESSION_TYPE')

#         if session_type == 'x11':
#             return 'x11'
#         elif session_type == 'wayland':
#             return 'wayland'
#         else:
#             print(f"Unsupported compositor type: {session_type}")
#             return None

#     def _get_focused_window_id_x11(self):
#         try:
#             result = subprocess.run(['xdotool', 'getactivewindow'], capture_output=True, text=True, check=True)
#             return int(result.stdout.strip())
#         except subprocess.CalledProcessError as e:
#             print(f"Error getting focused window ID: {e}")
#             return None

#     def _get_window_opacity_x11(self, window_id):
#         try:
#             result = subprocess.run(['xprop', '-id', str(window_id), '_NET_WM_WINDOW_OPACITY'], capture_output=True, text=True, check=True)
#             opacity_match = re.search(r'CARDINAL\s*=\s*(\d+)', result.stdout)
#             return int(opacity_match.group(1)) if opacity_match else 100
#         except subprocess.CalledProcessError as e:
#             print(f"Error getting window opacity: {e}")
#             return None

#     def _set_window_opacity_x11(self, window_id, opacity):
#         try:
#             subprocess.run(['xprop', '-id', str(window_id), '-f', '_NET_WM_WINDOW_OPACITY', '32c', '-set', '_NET_WM_WINDOW_OPACITY', str(opacity)], check=True)
#         except subprocess.CalledProcessError as e:
#             print(f"Error setting window opacity: {e}")

#     def _get_focused_window_id_wayland(self):
#         try:
#             result = subprocess.run(['swaymsg', '-t', 'get_tree'], capture_output=True, text=True, check=True)
#             tree = json.loads(result.stdout)
            
#             def find_focused_window(node):
#                 if node.get('focused') and 'id' in node:
#                     return node['id']
#                 if 'nodes' in node:
#                     for child in node['nodes']:
#                         window_id = find_focused_window(child)
#                         if window_id:
#                             return window_id
#                 return None

#             return find_focused_window(tree)
#         except subprocess.CalledProcessError as e:
#             print(f"Error getting focused window ID: {e}")
#             return None

#     def _get_window_opacity_wayland(self, window_id):
#         try:
#             result = subprocess.run(['swaymsg', '-t', 'get_tree'], capture_output=True, text=True, check=True)
#             tree = json.loads(result.stdout)
            
#             def find_window_opacity(node):
#                 if 'id' in node and node['id'] == window_id:
#                     return node.get('opacity', 1) * 100
#                 if 'nodes' in node:
#                     for child in node['nodes']:
#                         opacity = find_window_opacity(child)
#                         if opacity:
#                             return opacity
#                 return None

#             return find_window_opacity(tree)
#         except subprocess.CalledProcessError as e:
#             print(f"Error getting window opacity: {e}")
#             return None

#     def _set_window_opacity_wayland(self, window_id, opacity):
#         try:
#             subprocess.run(['swaymsg', f'floating enable; opacity {opacity}', '-w', f'id={window_id}'], check=True)
#         except subprocess.CalledProcessError as e:
#             print(f"Error setting window opacity: {e}")

#     def _get_focused_window_id(self):
#         if self.compositor_type == 'x11':
#             return self._get_focused_window_id_x11()
#         elif self.compositor_type == 'wayland':
#             return self._get_focused_window_id_wayland()
#         else:
#             return None

#     def _get_window_opacity(self, window_id):
#         if self.compositor_type == 'x11':
#             return self._get_window_opacity_x11(window_id)
#         elif self.compositor_type == 'wayland':
#             return self._get_window_opacity_wayland(window_id)
#         else:
#             return None

#     def _set_window_opacity(self, window_id, opacity):
#         if self.compositor_type == 'x11':
#             self._set_window_opacity_x11(window_id, opacity)
#         elif self.compositor_type == 'wayland':
#             self._set_window_opacity_wayland(window_id, opacity)

#     def stepup(self):
#         window_id = self._get_focused_window_id()
#         if window_id is not None:
#             current_opacity = self._get_window_opacity(window_id)
#             new_opacity = min(100, current_opacity + 1)
#             self._set_window_opacity(window_id, new_opacity)

#     def stepdown(self):
#         window_id = self._get_focused_window_id()
#         if window_id is not None:
#             current_opacity = self._get_window_opacity(window_id)
#             new_opacity = max(0, current_opacity - 1)
#             self._set_window_opacity(window_id, new_opacity)

#     def reset(self):
#         window_id = self._get_focused_window_id()
#         if window_id is not None:
#             self._set_window_opacity(window_id, 100)





# class CompositorUtils:
#     def __init__(self):
#         # Determine the compositor type
#         self.compositor_type = self._detect_compositor()

#     def _detect_compositor(self):
#         session_type = os.environ.get('XDG_SESSION_TYPE')

#         if session_type == 'x11':
#             return 'x11'
#         elif session_type == 'wayland':
#             return 'wayland'
#         else:
#             print(f"Unsupported compositor type: {session_type}")
#             return None

#     def _get_focused_window_id_x11(self):
#         try:
#             result = subprocess.run(['xdotool', 'getactivewindow'], capture_output=True, text=True, check=True)
#             return int(result.stdout.strip())
#         except subprocess.CalledProcessError as e:
#             print(f"Error getting focused window ID: {e}")
#             return None

#     def _read_opacity_from_file(self, window_id):
#         opacity_file_path = f"glassit_opacity_{window_id}.txt"
#         if os.path.exists(opacity_file_path):
#             with open(opacity_file_path, 'r') as file:
#                 try:
#                     return int(file.read())
#                 except ValueError:
#                     print(f"Error reading opacity from file for window {window_id}")
#         return None

#     def _write_opacity_to_file(self, window_id, opacity):
#         opacity_file_path = f"glassit_opacity_{window_id}.txt"
#         with open(opacity_file_path, 'w') as file:
#             file.write(str(opacity))

#     # Modify the _get_window_opacity and _set_window_opacity methods
#     def _get_window_opacity_x11(self, window_id):
#         # Read opacity from file
#         stored_opacity = self._read_opacity_from_file(window_id)
#         return stored_opacity if stored_opacity is not None else 100

#     def _set_window_opacity_x11(self, window_id, opacity):
#         # Write opacity to file
#         self._write_opacity_to_file(window_id, opacity)
#         try:
#             subprocess.run(['xprop', '-id', str(window_id), '-f', '_NET_WM_WINDOW_OPACITY', '32c', '-set', '_NET_WM_WINDOW_OPACITY', str(opacity)], check=True)
#         except subprocess.CalledProcessError as e:
#             print(f"Error setting window opacity: {e}")

#     def _get_focused_window_id_wayland(self):
#         try:
#             result = subprocess.run(['swaymsg', '-t', 'get_tree'], capture_output=True, text=True, check=True)
#             tree = json.loads(result.stdout)
            
#             def find_focused_window(node):
#                 if node.get('focused') and 'id' in node:
#                     return node['id']
#                 if 'nodes' in node:
#                     for child in node['nodes']:
#                         window_id = find_focused_window(child)
#                         if window_id:
#                             return window_id
#                 return None

#             return find_focused_window(tree)
#         except subprocess.CalledProcessError as e:
#             print(f"Error getting focused window ID: {e}")
#             return None

#     def _get_window_opacity_wayland(self, window_id):
#         try:
#             result = subprocess.run(['swaymsg', '-t', 'get_tree'], capture_output=True, text=True, check=True)
#             tree = json.loads(result.stdout)
            
#             def find_window_opacity(node):
#                 if 'id' in node and node['id'] == window_id:
#                     return node.get('opacity', 1) * 100
#                 if 'nodes' in node:
#                     for child in node['nodes']:
#                         opacity = find_window_opacity(child)
#                         if opacity:
#                             return opacity
#                 return None

#             return find_window_opacity(tree)
#         except subprocess.CalledProcessError as e:
#             print(f"Error getting window opacity: {e}")
#             return None

#     def _set_window_opacity_wayland(self, window_id, opacity):
#         try:
#             subprocess.run(['swaymsg', f'opacity {opacity / 100}', '-w', f'id={window_id}'], check=True)
#         except subprocess.CalledProcessError as e:
#             print(f"Error setting window opacity: {e}")

#     def _get_focused_window_id(self):
#         if self.compositor_type == 'x11':
#             return self._get_focused_window_id_x11()
#         elif self.compositor_type == 'wayland':
#             return self._get_focused_window_id_wayland()
#         else:
#             return None

#     def _get_window_opacity(self, window_id):
#         if self.compositor_type == 'x11':
#             return self._get_window_opacity_x11(window_id)
#         elif self.compositor_type == 'wayland':
#             return self._get_window_opacity_wayland(window_id)
#         else:
#             return None

#     def _set_window_opacity(self, window_id, opacity):
#         if self.compositor_type == 'x11':
#             self._set_window_opacity_x11(window_id, opacity)
#         elif self.compositor_type == 'wayland':
#             self._set_window_opacity_wayland(window_id, opacity)

#     def stepup(self):
#         window_id = self._get_focused_window_id()
#         if window_id is not None:
#             current_opacity = self._get_window_opacity(window_id)
#             new_opacity = min(100, current_opacity + 1)
#             self._set_window_opacity(window_id, new_opacity)

#     def stepdown(self):
#         window_id = self._get_focused_window_id()
#         if window_id is not None:
#             current_opacity = self._get_window_opacity(window_id)
#             new_opacity = max(0, current_opacity - 1)
#             self._set_window_opacity(window_id, new_opacity)

#     def reset(self):
#         window_id = self._get_focused_window_id()
#         if window_id is not None:
#             self._set_window_opacity(window_id, 100)





import os
import subprocess

class CompositorUtils:
    def __init__(self):
        pass

    def _get_focused_window_id_x11(self):
        try:
            result = subprocess.run(['xdotool', 'getactivewindow'], capture_output=True, text=True, check=True)
            return int(result.stdout.strip())
        except subprocess.CalledProcessError as e:
            print(f"Error getting focused window ID: {e}")
            return None

    def _read_opacity_from_file(self, window_id):
        opacity_file_path = f"glassit_opacity_{window_id}.txt"
        if os.path.exists(opacity_file_path):
            with open(opacity_file_path, 'r') as file:
                try:
                    return float(file.read())
                except ValueError:
                    print(f"Error reading opacity from file for window {window_id}")
        return None

    def _write_opacity_to_file(self, window_id, opacity):
        opacity_file_path = f"glassit_opacity_{window_id}.txt"
        with open(opacity_file_path, 'w') as file:
            file.write(str(opacity))

    def _get_window_opacity_x11(self, window_id):
        stored_opacity = self._read_opacity_from_file(window_id)
        return stored_opacity if stored_opacity is not None else 100.0

    def _set_window_opacity_x11(self, window_id, opacity):
        # Scale opacity from [0, 100] to [0, 42949672.95]
        scaled_opacity = int(opacity * 42949672.95)  # 0xFFFFFFFF / 100

        self._write_opacity_to_file(window_id, opacity)
        try:
            subprocess.run(['xprop', '-id', str(window_id), '-f', '_NET_WM_WINDOW_OPACITY', '32c', '-set', '_NET_WM_WINDOW_OPACITY', str(scaled_opacity)], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error setting window opacity: {e}")

    def _get_focused_window_id(self):
        return self._get_focused_window_id_x11()

    def _get_window_opacity(self, window_id):
        return self._get_window_opacity_x11(window_id)

    def _set_window_opacity(self, window_id, opacity):
        self._set_window_opacity_x11(window_id, opacity)

    def stepup(self):
        window_id = self._get_focused_window_id()
        if window_id is not None:
            current_opacity = self._get_window_opacity(window_id)
            new_opacity = min(100.0, current_opacity + 1.0)
            self._set_window_opacity(window_id, new_opacity)

    def stepdown(self):
        window_id = self._get_focused_window_id()
        if window_id is not None:
            current_opacity = self._get_window_opacity(window_id)
            new_opacity = max(0.0, current_opacity - 1.0)
            self._set_window_opacity(window_id, new_opacity)

    def reset(self):
        window_id = self._get_focused_window_id()
        if window_id is not None:
            self._set_window_opacity(window_id, 100.0)



class GlassIt:
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    # Handle actions
    def dispatch(self, action):
        compositor_utils = CompositorUtils()
        if action == 'stepup':
            compositor_utils.stepup()
        elif action == 'stepdown':
            compositor_utils.stepdown()
        elif action == 'reset':
            compositor_utils.reset()



def main():
    # Ensure thes presence of appropriate 'action' on script invocation
    if len(sys.argv) != 2 or sys.argv[1] not in ["stepup", "stepdown", "reset"]:
        print("Usage: python script.py [stepup|stepdown|reset]")
        sys.exit(1)

    # Parse the action
    action = sys.argv[1]

    # 'glass' the current window based on current action
    glassit = GlassIt()
    glassit.dispatch(action)


if __name__ == "__main__":
    main()
