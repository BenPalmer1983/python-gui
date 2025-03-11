

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk





class PageOne(ttk.Frame):

    page_title = "Page One"
    button_text = "Page One"

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
        
        self.setup_page()  # Clear any previous screen

        grid_row = 0
        self.label = ttk.Label(self, text=self.page_title, style="Title.Page.TLabel")
        self.label.grid(row=grid_row, column=0, sticky="w", pady=5)

        grid_row += 1
        self.file_label = ttk.Label(self, text="Select File:", style="Page.TLabel")
        self.file_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        self.file_entry = ttk.Entry(self, width=40, style="Page.TEntry")
        self.file_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        browse_button = ttk.Button(self, text="Browse", command=self.browse_file, style="Page.TButton")
        browse_button.grid(row=grid_row, column=2, padx=5, pady=5)

        grid_row += 1
        text_label = ttk.Label(self, text="Enter Text:", style="Page.TLabel")
        text_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        text_entry = ttk.Entry(self, width=40, style="Page.TEntry")
        text_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        grid_row += 1
        submit_button = ttk.Button(self, text="Submit", command=self.run_command, style="Page.TButton")
        submit_button.grid(row=grid_row, column=1, pady=10)


    def complete_screen(self):
        """Shows the completion screen after form submission."""
        self.setup_page()  # Clear previous widgets

        done_label = ttk.Label(self, text="Done.", style="Page.TButton")
        done_label.grid(row=0, column=0, pady=20, padx=10)

        back_button = ttk.Button(self, text="Back", command=self.input_screen, style="Page.TButton")
        back_button.grid(row=1, column=0, pady=10)


