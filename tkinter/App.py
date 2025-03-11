import tkinter as tk
from tkinter import ttk, filedialog
from pages import PageOne, PageTwo, PageThree
from ui import UIStyle

# ------------------ Main App Class ------------------
class App(tk.Tk):

    page_list = [PageOne, PageTwo, PageThree]

    def __init__(self):
        super().__init__()
        
        UIStyle.set_style()

        self.configure(bg=UIStyle.background)

        self.title("Tkinter Multi-Page UI")
        self.geometry("1000x650")
        self.resizable(False, False)

        

        # ------------------ Header ------------------
        header = ttk.Frame(self, height=50, style="TFrame")
        header.pack(side="top", fill="x")

        header_label = ttk.Label(header, text="My Generic App", style="Header.TLabel")
        header_label.pack(pady=10)

        self.sidebar = ttk.Frame(self, width=150, style="Sidebar.TFrame")
        self.sidebar.pack(side="left", fill="y", pady=20)

        # Container for Pages
        self.container = ttk.Frame(self, style="PageContainer.TFrame")
        self.container.pack(side="right", fill="both", expand=True, padx=0, pady=0)

        # Dictionary to store pages
        self.pages = {}
        for page in self.page_list:
            page_instance = page(self.container, self)
            self.pages[page] = page_instance
            page_instance.grid(row=0, column=0, sticky="nsew")

        # Sidebar Buttons
        self.create_sidebar_buttons()
        self.show_page(PageOne)  # Show Home Page initially


   

    def create_sidebar_buttons(self):
        for page in self.page_list:
            btn = ttk.Button(self.sidebar, text=page.button_text, command=lambda p=page: self.show_page(p), style="Sidebar.TButton")
            btn.pack(pady=10, padx=10, fill="x")

    def show_page(self, page):
        """Display the selected page."""
        self.pages[page].tkraise()

