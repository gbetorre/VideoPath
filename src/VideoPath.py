# Replace a path (a substring into a large string) with another

import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import scrolledtext
import tkinter.font as tkfont

def browse_and_read_file():
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
            text_area.config(state='normal')
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, content)
            # Set to read-only again
            text_area.config(state='disabled')
        except Exception as e:
            text_area.config(state='normal')
            text_area.delete('1.0', tk.END)
            text_area.insert(tk.END, f"Error reading file:\n{e}")
            text_area.config(state='disabled')
    else:
        text_area.config(state='normal')
        text_area.delete('1.0', tk.END)
        text_area.insert(tk.END, "No file selected.")
        text_area.config(state='disabled')



def browse_folder():
    folder_path = filedialog.askdirectory(title="VideoPath: VideoPad projects editor")
    if folder_path:
        # Clear any previous content in the Entry widget
        path_entry.delete(0, tk.END)
        # Insert the selected folder path into the Entry widget
        path_entry.insert(0, folder_path)


# Create the main window
root = tk.Tk()
root.title("VideoPath: VideoPad Projects Editor")
root.geometry("500x500")  

#root.withdraw()  # Hide the main window

#file_content = browse_and_read_file()
# Do something with file_content if needed
#label = tk.Label(root, text="This is bold text", font=("Helvetica", 11, "bold"))
#label.pack(pady=10)

label = tk.Label(root,
                 text="1. Pick a VideoPad Project",
                 anchor="w",       # anchor text to left
                 justify="left",   # justify multi-line text to left
                 font=("Helvetica", 11, "bold"),
                 width=40,         # label width to see alignment
                 bg="lightgrey")   # background color to visualize

label.pack(fill="x", padx=10, pady=10)  # fill horizontally

# Create button with command assigned to function name, no parentheses
load_button = tk.Button(root, text="Select a VideoPad project", command=browse_and_read_file)
load_button.pack(pady=10)


# Add other widgets for demonstration
#label_above = tk.Label(root, text="Above the line")
#label_above.pack()

#label_below = tk.Label(root, text="Below the line")
#label_below.pack()


# Define monospaced font
mono_font = tkfont.Font(family="Courier", size=10)

# Create a smaller scrollable readonly Text widget with gray background
text_area = scrolledtext.ScrolledText(root, wrap=tk.NONE, width=60, height=8,
                                      font=mono_font, bg='#f0f0f0', fg='black')
text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=False)

# Make text widget read-only initially
text_area.config(state='disabled')

# Create a horizontal separator (a thin dividing line)
#separator = ttk.Separator(root, orient='horizontal')
#separator.pack(fill='x', pady=10)  # fill horizontally and add vertical padding

label = tk.Label(root,
                 text="2. Choose the folder where resources are",
                 anchor="w",       # anchor text to left
                 justify="left",   # justify multi-line text to left
                 font=("Helvetica", 11, "bold"),
                 width=40,         # label width to see alignment
                 bg="lightgrey")   # background color to visualize

label.pack(fill="x", padx=10, pady=10)  # fill horizontally

# Create a horizontal separator (a thin dividing line)
#separator = ttk.Separator(root, orient='horizontal')
#separator.pack(fill='x', pady=10)  # fill horizontally and add vertical padding


# Create and place the Entry widget to display folder path
path_entry = tk.Entry(root, width=60)
path_entry.pack(padx=10, pady=10)

# Create and place the Browse button
browse_button = tk.Button(root, text="Browse Folder", command=browse_folder)
browse_button.pack(pady=5)


# Create a horizontal separator (a thin dividing line)
#separator = ttk.Separator(root, orient='horizontal')
#separator.pack(fill='x', pady=10)  # fill horizontally and add vertical padding

label = tk.Label(root,
                 text="3. Try to migrate references in the project",
                 anchor="w",       # anchor text to left
                 justify="left",   # justify multi-line text to left
                 font=("Helvetica", 11, "bold"),
                 width=40,         # label width to see alignment
                 bg="lightgrey")   # background color to visualize

label.pack(fill="x", padx=10, pady=10)  # fill horizontally


# Start the Tkinter event loop
root.mainloop()






'''
def browse_folder():
    # Open a folder browser dialog and return the selected path
    folder_path = filedialog.askdirectory(title="Select a Folder")
    if folder_path:
        print("Selected folder:", folder_path)
        use_folder_path(folder_path)  # Call your function with folder_path

def use_folder_path(path):
    # Replace this with your actual function that needs the folder path
    print(f"Function received folder path: {path}")
    # Your code here

# Setup minimal Tkinter window (it hides immediately after folder dialog)
root = tk.Tk()
root.withdraw()  # Hide the root window

browse_folder()
'''

old_path = input("Digita il percorso dove VideoPad non trova le risorse: ")
print(f"Il vecchio percorso è: {old_path}")
new_path = input("Digita il percorso dove si trovano ora le risorse")

def replace_text_in_file(input_filepath, output_filepath, old_text, new_text):
    with open(input_filepath, 'r', encoding='utf-8') as infile, \
         open(output_filepath, 'w', encoding='utf-8') as outfile:

        for line in infile:
            # Replace old_text with new_text in each line
            new_line = line.replace(old_text, new_text)
            outfile.write(new_line)

# Usage example:
replace_text_in_file('original.txt', 'modified.txt', 'old_word', 'new_word')

