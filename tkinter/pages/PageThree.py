


import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext
import json
from ui import DropDown

class PageThree(ttk.Frame):


    page_title = "Page Three"
    button_text = "Page Three"

    def __init__(self, parent, controller):
        super().__init__(parent, style="Page.TFrame")
        self.controller = controller  # Store the controller reference
        self.grid(row=0, column=0, pady=20, padx=10)
        self.input_screen()  # Start with the input screen

    def browse_file(self):
        
        self.filename = filedialog.askopenfilename(title="Select a File")
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, self.filename)

    def run_command(self):
        
        print("Running Command")
        self.complete_screen()

    def setup_page(self):
        
        for widget in self.winfo_children():
            widget.destroy()

    def input_screen(self):
        """Shows the input form with file selection, text input, and submit button."""
        self.setup_page()  # Clear any previous screen

        # ✅ Create Notebook
        self.notebook = ttk.Notebook(self, width=780, height=500, style="TNotebook")  
        self.notebook.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky="nsew")

        # ✅ Add Tabs
        self.create_tab_1()
        self.create_tab_2()


    def create_tab_1(self, title=None):

        if(title is None):
            title = self.page_title

        tab1 = ttk.Frame(self.notebook, width=780, height=500, style="TNotebook.TFrame")
        self.notebook.add(tab1, text="Main")

        # Grid for tab
        tab1.grid_propagate(False) 
        inner_frame = ttk.Frame(tab1, padding=10, style="TNotebook.TFrame")
        inner_frame.grid(row=0, column=0, padx=10, pady=2, sticky="nw")

        # Content
        grid_row = 0
        self.label = ttk.Label(inner_frame, text=title, style="Title.Page.TLabel")
        self.label.grid(row=grid_row, column=0, sticky="w", pady=5)

        grid_row += 1
        self.file_label = ttk.Label(inner_frame, text="Select File:", style="Page.TLabel")
        self.file_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        self.file_entry = ttk.Entry(inner_frame, width=40, style="Page.TEntry")
        self.file_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        browse_button = ttk.Button(inner_frame, text="Browse", style="Page.TButton")
        browse_button.grid(row=grid_row, column=2, padx=5, pady=5)

        grid_row += 1
        text_label = ttk.Label(inner_frame, text="Enter Text:", style="Page.TLabel")
        text_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        text_entry = ttk.Entry(inner_frame, width=40, style="Page.TEntry")
        text_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        grid_row += 1
        submit_button = ttk.Button(inner_frame, text="Submit", style="Page.TButton")
        submit_button.grid(row=grid_row, column=1, pady=10)


    def create_tab_2(self, title=None):

        if(title is None):
            title = self.page_title

        tab = ttk.Frame(self.notebook, width=780, height=500, style="TNotebook.TFrame")
        self.notebook.add(tab, text="Settings")

        # Grid for tab
        tab.grid_propagate(False)  
        inner_frame = ttk.Frame(tab, padding=10, style="TNotebook.TFrame")
        inner_frame.grid(row=0, column=0, padx=10, pady=2, sticky="nw")

        # Content
        grid_row = 0
        self.label = ttk.Label(inner_frame, text=title, style="Title.Page.TLabel")
        self.label.grid(row=grid_row, column=0, sticky="w", pady=5)

        grid_row += 1
        self.file_label = ttk.Label(inner_frame, text="Select File:", style="Page.TLabel")
        self.file_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        self.file_entry = ttk.Entry(inner_frame, width=40, style="Page.TEntry")
        self.file_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        browse_button = ttk.Button(inner_frame, text="Browse", style="Page.TButton")
        browse_button.grid(row=grid_row, column=2, padx=5, pady=5)

        grid_row += 1
        text_label = ttk.Label(inner_frame, text="Enter Text:", style="Page.TLabel")
        text_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        text_entry = ttk.Entry(inner_frame, width=40, style="Page.TEntry")
        text_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        grid_row += 1
        submit_button = ttk.Button(inner_frame, text="Submit", style="Page.TButton")
        submit_button.grid(row=grid_row, column=1, pady=10)




    def complete_screen(self):
        self.setup_page()  # Clear previous widgets

        done_label = ttk.Label(self, text="✅ Done.", style="TLabel")
        done_label.grid(row=0, column=0, pady=20, padx=10)

        back_button = ttk.Button(self, text="Back", command=self.input_screen, style="TButton")
        back_button.grid(row=1, column=0, pady=10)


    def load_dropdown_options(self):
        try:
            with open("data/dropdown_page2.json", "r") as file:
                data = json.load(file)
                return data.get("dropdown_options", [])  # Get list or return empty list if missing
        except (FileNotFoundError, json.JSONDecodeError):
            return ["Error: No Data"]  # Handle errors
        

