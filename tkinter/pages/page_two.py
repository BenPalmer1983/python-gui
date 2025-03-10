


import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
import json
from ui import DropDown

class PageTwo(tk.Frame):

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
        self.label = ttk.Label(self, text="Page Two", font=("Arial", 16, "bold"), background="white")
        self.label.grid(row=grid_row, column=0, sticky="w", pady=5)


        grid_row += 1

        self.dropdown_var = tk.StringVar()
        dropdown_options = DropDown.load("data/dropdown_page2.json")  # Load from JSON
        self.dropdown = ttk.Combobox(self, textvariable=self.dropdown_var, values=dropdown_options, state="readonly", width=38)
        self.dropdown.grid(row=grid_row, column=1, padx=10, pady=5)
        self.dropdown.current(0)  # Set default option


    def complete_screen(self):
        self.setup_page()  # Clear previous widgets

        done_label = ttk.Label(self, text="✅ Done.", font=("Arial", 14, "bold"), background="white")
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