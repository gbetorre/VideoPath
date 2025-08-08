# Replace some text in an input file saving changes in an output file
# Usage example:
# replace_text_in_file('original.txt', 'modified.txt', 'old_word', 'new_word')

import tkinter as tk

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
        

def replace_text_in_file(input_filepath, output_filepath, old_text, new_text):
    with open(input_filepath, 'r', encoding='utf-8') as infile, \
         open(output_filepath, 'w', encoding='utf-8') as outfile:

        for line in infile:
            # Replace old_text with new_text in each line
            new_line = line.replace(old_text, new_text)
            outfile.write(new_line)

#old_path = input("Digita il percorso dove VideoPad non trova le risorse: ")
#print(f"Il vecchio percorso è: {old_path}")
#new_path = input("Digita il percorso dove si trovano ora le risorse")