

import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk





class PageOne(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent, bg="white")
        self.controller = controller  # Store the controller reference
        self.grid(row=0, column=0, pady=20, padx=10)
        self.input_screen()  # Start with the input screen

    def browse_file(self):
        """Opens a file dialog and updates the entry field."""
        self.filename = filedialog.askopenfilename(title="Select a File")
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, self.filename)

    def run_command(self):
        """Simulate running a command and switch to completion screen."""
        print("Running Command")
        self.complete_screen()

    def setup_page(self):
        """Clears the current page before adding new widgets."""
        for widget in self.winfo_children():
            widget.destroy()

    def input_screen(self):
        """Shows the input form with file selection, text input, and submit button."""
        self.setup_page()  # Clear any previous screen

        grid_row = 0
        self.label = ttk.Label(self, text="Page One", font=("Arial", 16, "bold"), background="white")
        self.label.grid(row=grid_row, column=0, sticky="w", pady=5)

        grid_row += 1
        self.file_label = ttk.Label(self, text="Select File:", background="white")
        self.file_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        self.file_entry = ttk.Entry(self, width=40)
        self.file_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        browse_button = ttk.Button(self, text="Browse", command=self.browse_file, style="TButton")
        browse_button.grid(row=grid_row, column=2, padx=5, pady=5)

        grid_row += 1
        text_label = ttk.Label(self, text="Enter Text:", background="white")
        text_label.grid(row=grid_row, column=0, sticky="w", pady=5)

        text_entry = ttk.Entry(self, width=40)
        text_entry.grid(row=grid_row, column=1, padx=5, pady=5)

        grid_row += 1
        submit_button = ttk.Button(self, text="Submit", command=self.run_command, style="TButton")
        submit_button.grid(row=grid_row, column=1, pady=10)

    def complete_screen(self):
        """Shows the completion screen after form submission."""
        self.setup_page()  # Clear previous widgets

        done_label = ttk.Label(self, text="✅ Done.", font=("Arial", 14, "bold"), background="white")
        done_label.grid(row=0, column=0, pady=20, padx=10)

        back_button = ttk.Button(self, text="Back", command=self.input_screen)
        back_button.grid(row=1, column=0, pady=10)


