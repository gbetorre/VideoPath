

import tkinter as tk
from tkinter import filedialog
import re
from urllib.parse import unquote

def browse_and_read_file(text_widget):
    # Open file dialog limited to .vpj files
    vpj_file_path = filedialog.askopenfilename(
        title="Select a .vpj file",
        filetypes=[("VideoPad Project files", "*.vpj"), ("All files", "*.*")]
    )
    if vpj_file_path:
        try:
            with open(vpj_file_path, 'r', encoding='utf-8') as file:
                content = file.read()
            # Enable text widget temporarily so we can modify content
            text_widget.config(state='normal')
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, content)
            # Set to read-only again
            text_widget.config(state='disabled')
        except Exception as e:
            text_widget.config(state='normal')
            text_widget.delete('1.0', tk.END)
            text_widget.insert(tk.END, f"Error reading file:\n{e}")
            text_widget.config(state='disabled')
    else:
        text_widget.config(state='normal')
        text_widget.delete('1.0', tk.END)
        text_widget.insert(tk.END, "No file selected.")
        text_widget.config(state='disabled')
        

def split_path_filename(full_path):
    # Split by last URL-encoded backslash %5C
    if '%5C' in full_path:
        path_part, filename_ext = full_path.rsplit('%5C', 1)  # split once from right
    else:
        # no %5C found: treat entire string as filename
        path_part, filename_ext = '', full_path
    # Extract file extension from filename
    if '.' in filename_ext:
        filename, extension = filename_ext.rsplit('.', 1)
    else:
        filename, extension = filename_ext, ''

    return path_part, filename_ext, filename, extension


def get_resources(s):
    p = re.compile(r'path=([^&]+)&creationtime=')
    matches = p.findall(s)
    count = 0
    D = {}
    for match in matches:
        count += 1
        path, filename_ext, filename, extension = split_path_filename(match)
        D["RISORSA " + str(count)] = [unquote(match), unquote(path), unquote(filename_ext)]
    return D


# Replace some text in an input file saving changes in an output file
# Usage example:
# replace_text_in_file('original.txt', 'modified.txt', 'old_word', 'new_word')
def replace_text_in_file(input_filepath, output_filepath, old_text, new_text):
    with open(input_filepath, 'r', encoding='utf-8') as infile, \
         open(output_filepath, 'w', encoding='utf-8') as outfile:

        for line in infile:
            # Replace old_text with new_text in each line
            new_line = line.replace(old_text, new_text)
            outfile.write(new_line)


#def search(