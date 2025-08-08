

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext, font
from tkinter import filedialog
from .fileio import browse_and_read_file
import tkinter.font as tkfont


class VideoPathEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VideoPath: VideoPad Projects Editor")
        self.root.geometry("500x500")

        # Monospaced font for text area
        mono_font = tkfont.Font(family="Courier", size=10)
        
        # Label Step 1.
        self.label = tk.Label(self.root,
                         text="1. Pick a VideoPad Project",
                         anchor="w",       # anchor text to left
                         justify="left",   # justify multi-line text to left
                         font=("Helvetica", 11, "bold"),
                         width=40,         # label width to see alignment
                         bg="lightgrey")   # background color to visualize

        self.label.pack(fill="x", padx=10, pady=10)  # fill horizontally

        # Button to browse and open file
        self.load_button = tk.Button(
            self.root, text="Select a VideoPad project",
            command=lambda: browse_and_read_file(self.text_area)
        )
        self.load_button.pack(pady=10)
        
        # Smaller scrollable and read-only text area with gray background
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.NONE, width=60, height=8,
                                                   font=mono_font, bg='#f0f0f0', fg='black')
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        # Make text widget read-only initially
        self.text_area.config(state='disabled')

        # Label Step 2.
        self.label = tk.Label(self.root,
                         text="2. Choose the folder where resources are",
                         anchor="w",       # anchor text to left
                         justify="left",   # justify multi-line text to left
                         font=("Helvetica", 11, "bold"),
                         width=40,         # label width to see alignment
                         bg="lightgrey")   # background color to visualize

        self.label.pack(fill="x", padx=10, pady=10)  # fill horizontally

        # Create and place the Entry widget to display folder path
        self.path_entry = tk.Entry(self.root, width=60)
        self.path_entry.pack(padx=10, pady=10)

        # Create and place the Browse button
        self.browse_button = tk.Button(self.root, text="Browse Folder", command=self.browse_folder)
        self.browse_button.pack(pady=5)

        # Label Step 3.
        self.label = tk.Label(self.root,
                 text="3. Try to migrate references in the project",
                 anchor="w",       # anchor text to left
                 justify="left",   # justify multi-line text to left
                 font=("Helvetica", 11, "bold"),
                 width=40,         # label width to see alignment
                 bg="lightgrey")   # background color to visualize

        self.label.pack(fill="x", padx=10, pady=10)  # fill horizontally


    def browse_folder(self):
        folder_path = filedialog.askdirectory(title="VideoPath: VideoPad projects editor")
        if folder_path:
            # Clear any previous content in the Entry widget
            self.path_entry.delete(0, tk.END)
            # Insert the selected folder path into the Entry widget
            self.path_entry.insert(0, folder_path)


    def run(self):
        self.root.mainloop()