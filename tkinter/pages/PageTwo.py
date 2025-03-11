


import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from tkinter import ttk
from tkinter import scrolledtext
import json
from ui import DropDown
from ui import UIStyle

class PageTwo(ttk.Frame):

    page_title = "Page Two"
    button_text = "Page Two"


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

        self.dropdown_var = tk.StringVar()
        dropdown_options = DropDown.load("data/dropdown_page2.json")  # Load from JSON
        self.dropdown = ttk.Combobox(self, textvariable=self.dropdown_var, values=dropdown_options, state="readonly", width=38, style="Page.TCombobox")
        self.dropdown.grid(row=grid_row, column=1, padx=10, pady=5)
        self.dropdown.current(0)  # Set default option

        grid_row += 1
        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5, font=("Arial", 12), bg=UIStyle.surface, fg=UIStyle.text)
        self.text_box.grid(row=grid_row, column=1, padx=10, pady=5)

        # Insert some example text
        self.text_box.insert(tk.END, "This is a scrollable text box. You can add long text here, and it will be scrollable!")

        grid_row += 1
        self.text_box = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=50, height=5, font=("Arial", 12), bg=UIStyle.surface, fg=UIStyle.text)
        self.text_box.grid(row=grid_row, column=1, padx=10, pady=5)

        self.text_box.insert(tk.END, "This is a scrollable text box. You can add long text here, and it will be scrollable!")
        self.text_box.config(state="disabled")

        grid_row += 1

        frame = ttk.Frame(self, style="Page.TFrame")
        frame.grid(row=grid_row, column=1, padx=10, pady=5, sticky="nsew")

        columns = ("ID", "Name", "Age", "City")
        self.tree = ttk.Treeview(frame, columns=columns, show="headings", height=5, style="Page.Treeview")

        # Define column headings
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center", width=100)

        # Insert sample data
        data = [
            (1, "A", 25, "AA"),
            (2, "B", 30, "BB"),
            (3, "C", 22, "CC"),
            (4, "D", 35, "DD"),
            (5, "E", 28, "EE"),
            (6, "F", 40, "FF"),
            (7, "G", 29, "GG"),
            (8, "H", 33, "HH"),
            (9, "I", 24, "II"),
            (10, "J", 27, "JJ"),
        ]

        for row in data:
            self.tree.insert("", tk.END, values=row)

        # Make it read-only (disable column separator clicks)
        self.tree.bind("<Button-1>", lambda e: "break" if self.tree.identify_region(e.x, e.y) == "separator" else None)

        # Add a vertical scrollbar
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        # Place widgets
        self.tree.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")



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