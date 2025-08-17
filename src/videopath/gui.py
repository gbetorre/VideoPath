# UI-related code: tkinter window creation and widgets

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from .fileio import browse_and_read_file, get_resources
import tkinter.font as tkfont


class VideoPathEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("VideoPath: VideoPad Projects Editor")
        self.root.geometry("500x800")
        # Monospaced FONT for text area
        mono_font = tkfont.Font(family="Courier", size=10)
        # LABEL Step 1.
        self.label = tk.Label(self.root,
                             text="1. Pick a VideoPad Project",
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Helvetica", 11, "bold"),
                             width=40,         		# label width to see alignment
                             bg="lightgrey")   		# background color to visualize
        self.label.pack(fill="x", padx=10, pady=10)	# fill horizontally
        # BUTTON to browse and open file
        self.load_button = tk.Button(self.root,
                                     text="Select a VideoPad project",
                                     command=self.load_file_content
        )
        self.load_button.pack(pady=10)
        # Smaller scrollable and read-only TEXTAREA with gray background
        self.text_area = scrolledtext.ScrolledText(self.root,
                                                   wrap=tk.NONE,
                                                   width=60,
                                                   height=8,
                                                   font=mono_font,
                                                   bg='#f0f0f0',
                                                   fg='black')
        self.text_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        # Make text widget read-only
        self.text_area.config(state='disabled')
        # LABEL Step 2.
        self.label = tk.Label(self.root,
                             text="2. Choose the folder where resources are",
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Helvetica", 11, "bold"),
                             width=40,         		# label width to see alignment
                             bg="lightgrey")   		# background color to visualize
        self.label.pack(fill="x", padx=10, pady=10) # fill horizontally
        # Create and place the ENTRY WIDGET to display folder path
        self.path_entry = tk.Entry(self.root, width=60)
        self.path_entry.pack(padx=10, pady=10)
        # Create and place the BROWSE BUTTON
        self.browse_button = tk.Button(self.root, text="Browse Folder", command=self.browse_folder)
        self.browse_button.pack(pady=5)
        # LABEL Step 3.
        self.label = tk.Label(self.root,
                             text="3. Try to migrate references in the project",
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Helvetica", 11, "bold"),
                             width=40,         		# label width to see alignment
                             bg="lightgrey")   		# background color to visualize
        self.label.pack(fill="x", padx=10, pady=10) # fill horizontally

        # Create a LISTBOX widget with multiple selection mode
        self.listbox = tk.Listbox(self.root, selectmode=tk.MULTIPLE, width=60, height=10)
        self.listbox.pack(padx=10, pady=10)
        # Create a Button widget with a command linked to the method to populate the listbox
        self.button = tk.Button(self.root, text="Load resources", command=self.on_button_click)
        self.button.pack(side=tk.LEFT)
            
        # Button to select all items
        btn_select_all = tk.Button(self.root, text="Select All", command=self.select_all)
        btn_select_all.pack(side=tk.LEFT, padx=5)  # Add some horizontal padding
        # Button to show selected items
        btn_show = tk.Button(self.root, text="Show Selected", command=self.show_selected)
        btn_show.pack(side=tk.LEFT, padx=5)



    def load_file_content(self):
        content = browse_and_read_file(self.text_area)


    def populate_listbox(self, items):
        # Clear existing items
        self.listbox.delete(0, tk.END)
        # Insert items into the listbox
        for item in items:
            self.listbox.insert(tk.END, item)
    
    
    def on_button_click(self):
        # This function is bound to the button and calls populate_listbox with specific items
        text_content = self.text_area.get("1.0", "end-1c")
        if not text_content:
            messagebox.showwarning("Don't know which VideoPad project", "Select a VideoPad project before")
            return
        # Suppose each item is separated by newlines in the text area
        items_to_add = text_content.splitlines()
        self.populate_listbox(items_to_add)


    def browse_folder(self):
        folder_path = filedialog.askdirectory(title="VideoPath: VideoPad projects editor")
        if folder_path:
            # Clear any previous content in the Entry widget
            self.path_entry.delete(0, tk.END)
            # Insert the selected folder path into the Entry widget
            self.path_entry.insert(0, folder_path)


    def show_selected(self):
        # Get selected indices from listbox
        selected_indices = self.listbox.curselection()
        # Get the selected items using indices
        selected_items = [self.listbox.get(i) for i in selected_indices]
        # Show selected items
        messagebox.showinfo("Selected Items", "\n".join(selected_items))


    def select_all(self):
        # Select all items in the listbox
        self.listbox.select_set(0, tk.END)

    def run(self):
        self.root.mainloop()
        