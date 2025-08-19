# UI-related code: tkinter window creation and widgets

import tkinter as tk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import filedialog
from .fileio import browse_and_read_file, get_resources, migrate_resources, migrate_project
import tkinter.font as tkfont


class VideoPathEditor:
    def __init__(self):
        self.STEP_1 = "1. Pick a VideoPad Project"
        self.STEP_2 = "2. Choose the folder where you like to place the resources"
        self.STEP_3 = "3. Try to migrate references in a new project"
        self.root = tk.Tk()
        self.root.title("VideoPath: VideoPad Projects Editor")
        self.root.geometry("510x620")
        # Monospaced FONT for text area
        mono_font = tkfont.Font(family="Courier", size=10)
        # LABEL Step 1.
        self.label = tk.Label(self.root,
                             text=self.STEP_1,
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Helvetica", 11, "bold"),
                             width=40,         		# label width to see alignment
                             bg="lightgrey")   		# background color to visualize
        self.label.pack(fill="x", padx=10, pady=1)	# fill horizontally
        # BUTTON to browse and open file
        self.load_button = tk.Button(self.root,
                                     text="Select a VideoPad project",
                                     command=self.load_file_content
        )
        self.load_button.pack(pady=10)
        # TEXTAREA scrollable and read-only with gray background
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
                             text=self.STEP_2,
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Helvetica", 11, "bold"),
                             width=40,         		# label width to see alignment
                             bg="lightgrey")   		# background color to visualize
        self.label.pack(fill="x", padx=10, pady=10) # fill horizontally
        # ENTRY WIDGET to display folder path
        self.path_entry = tk.Entry(self.root, width=60)
        self.path_entry.pack(padx=10, pady=10)
        # BROWSE BUTTON
        self.browse_button = tk.Button(self.root, text="Browse Folder", command=self.browse_folder)
        self.browse_button.pack(pady=5)
        # LABEL Step 3.
        self.label = tk.Label(self.root,
                             text=self.STEP_3,
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Helvetica", 11, "bold"),
                             width=40,         		# label width to see alignment
                             bg="lightgrey")   		# background color to visualize
        self.label.pack(fill="x", padx=10, pady=10) # fill horizontally

        # LISTBOX widget with multiple selection mode
        frame = tk.Frame(self.root)
        frame.pack(padx=10, pady=10)
        self.listbox = tk.Listbox(frame, selectmode=tk.MULTIPLE, width=60, height=8)
        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.config(yscrollcommand=scrollbar.set)
        # BUTTON widget with a command linked to the method to populate the listbox
        self.button = tk.Button(self.root, text="Load Resources", command=self.on_button_click)
        self.button.pack(side=tk.LEFT, padx=5)
        # BUTTON to select all items
        btn_select_all = tk.Button(self.root, text="Select All", command=self.select_all)
        btn_select_all.pack(side=tk.LEFT, padx=5)  # Add some horizontal padding
        # BUTTON to de-select all items
        btn_select_none = tk.Button(self.root, text="Select None", command=self.deselect_all)
        btn_select_none.pack(side=tk.LEFT, padx=5)  # Add some horizontal padding
        # BUTTON to show selected items
        btn_show = tk.Button(self.root, text="Show Selected", command=self.show_selected)
        btn_show.pack(side=tk.LEFT, padx=5)
        # BUTTON to change paths
        btn_show = tk.Button(self.root, text="Migrate Paths", command=self.show_migrated)
        btn_show.pack(side=tk.LEFT, padx=5)
        # BUTTON to save the new VideoPad project
        btn_show = tk.Button(self.root, text="Save New", command=self.create_new_vpj)
        btn_show.pack(side=tk.LEFT, padx=5)


    def load_file_content(self):
        vpj_project = browse_and_read_file(self.text_area)
        # SHOW PATH AND NAME OF SELECTED vpj PROJECT
        self.label = tk.Label(self.root,
                             text=vpj_project,
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Consolas", 8),
                             width=78,         		# label width to see alignment
                             bg="lightyellow")   	# background color to visualize
        self.label.place(x=10, y=60)


    def browse_folder(self):
        folder_path = filedialog.askdirectory(title="VideoPath: VideoPad projects editor")
        if folder_path:
            # Clear any previous content in the Entry widget
            self.path_entry.delete(0, tk.END)
            # Insert the selected folder path into the Entry widget
            self.path_entry.insert(0, folder_path)
            

    def populate_listbox(self, D):
        # Clear existing items
        self.listbox.delete(0, tk.END)
        # Insert items into the listbox
        for (key, value) in D.items():
            self.listbox.insert(tk.END, value[0])
    
    
    def on_button_click(self):
        # This function is bound to the button and calls populate_listbox with specific items
        text_project = self.text_area.get("1.0", "end-1c")
        if not text_project:
            messagebox.showwarning("Don't know which VideoPad project", f"Select a VideoPad project before\n (See \"{self.STEP_1}\")")
            return
        # LABEL HELP Step 3.
        self.label = tk.Label(self.root,
                             text="TIP: If resources are truncated, select them then clic \"Show Selected\"",
                             anchor="w",       		# anchor text to left
                             justify="left",   		# justify multi-line text to left
                             font=("Helvetica", 9),
                             width=60         		# label width to see alignment
                             )
        # Place the label at absolute coordinates (x=50, y=100)
        self.label.place(x=55, y=434)
        #self.label.pack(fill="x", padx=1, pady=1)  # Show label
        self.populate_listbox(get_resources(text_project))


    def select_all(self):
        # Select all items in the listbox
        self.listbox.select_set(0, tk.END)
        
        
    def deselect_all(self):
        # Deselect all items in the listbox
        self.listbox.selection_clear(0, tk.END)


    def show_selected(self):
        # Get selected indices from listbox
        selected_indices = self.listbox.curselection()
        # Get the selected items using indices
        selected_items = [self.listbox.get(i) for i in selected_indices]
        # Make a set from list to avoid duplicates
        #selected_items_set = set(selected_items)
        # Show selected items
        if not selected_indices:
            messagebox.showwarning("Selected Items", "You haven't selected anything.\n TIP: Select some element in listbox or clic \"Select All\"")
        else:
            messagebox.showinfo("Selected Items", "\n".join(selected_items))


    def show_custom_messagebox(self, title, message):
        top = tk.Toplevel(self.root)
        top.title(title)
        top.geometry("800x400")  # Initial window size; can be resized by user
        top.transient(self.root)
        top.grab_set()
        # Create a frame to hold Text widget and scrollbar
        frame = tk.Frame(top)
        frame.pack(fill='both', expand=True, padx=10, pady=10)
        # Create vertical scrollbar
        scrollbar = tk.Scrollbar(frame)
        scrollbar.pack(side='right', fill='y')
        # Create Text widget
        mono_smaller = tkfont.Font(family="Courier", size=8)
        text_widget = tk.Text(frame, wrap='word', yscrollcommand=scrollbar.set, font=mono_smaller)
        text_widget.pack(side='left', fill='both', expand=True)
        # Insert your long message in text widget
        text_widget.insert('1.0', message)
        # Make text widget read-only
        text_widget.config(state='disabled')
        # Configure scrollbar
        scrollbar.config(command=text_widget.yview)
        # OK button to close the window
        btn = tk.Button(top, text="OK", command=top.destroy)
        btn.pack(pady=10)
        self.root.wait_window(top)


    def show_migrated(self):
        # Get selected indices from listbox
        selected_indices = self.listbox.curselection()
        # Get the selected items using indices
        selected_items = [self.listbox.get(i) for i in selected_indices]
        # Get the new paths
        migrated_items = migrate_resources(selected_items, self.path_entry.get().replace('/', '\\'))
        # Create strings combining each old item and the corresponding migrated item
        combined = [old + " -> " + new for old, new in zip(selected_items, migrated_items)]
        # Show items
        if not selected_indices:
            messagebox.showwarning("Selected Items", "You haven't selected anything.\n TIP: Select some element in listbox or clic \"Select All\"")
        else:
            #messagebox.showinfo("Selected Items", "\n".join(combined))
            self.show_custom_messagebox("Migrating Items", "\n".join(combined))


    def create_new_vpj(self):
        # Loaded content of vpj project as a string
        text_project = self.text_area.get("1.0", "end-1c")
        if not text_project:
            messagebox.showwarning("Don't know which VideoPad project", f"Select a VideoPad project before\n (See \"{self.STEP_1}\")")
            return

        # Get selected indices from listbox
        selected_indices = self.listbox.curselection()
        # Get the selected items using indices
        selected_items = [self.listbox.get(i) for i in selected_indices]
        # Get the new paths
        migrated_items = migrate_resources(selected_items, self.path_entry.get().replace('/', '\\'))

        new_text = migrate_project(text_project, selected_items, self.path_entry.get().replace('/', '\\'))
        f = open("new_project.vpj", 'w')
        f.write(new_text)
        f.close()
        

    def run(self):
        self.root.mainloop()
        