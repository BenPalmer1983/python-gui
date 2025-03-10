import tkinter as tk
from tkinter import ttk, filedialog
from pages import PageOne, PageTwo

# ------------------ Main App Class ------------------
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="white", foreground="#333")
        style.configure("TButton", font=("Arial", 11, "bold"), padding=6, background="#34495E", foreground="white")
        style.configure("TEntry", font=("Arial", 11), padding=5)
        style.configure("TCombobox", font=("Arial", 11), padding=5)

        self.title("Tkinter Multi-Page UI")
        self.geometry("900x600")
        self.resizable(False, False)

        # ------------------ Header ------------------
        header = tk.Frame(self, bg="#34495E", height=50)
        header.pack(side="top", fill="x")

        header_label = tk.Label(header, text="My Generic App", fg="white", bg="#34495E", font=("Arial", 14, "bold"))
        header_label.pack(pady=10)

        # ------------------ Sidebar ------------------
        self.sidebar = tk.Frame(self, width=150, bg="#2C3E50")
        self.sidebar.pack(side="left", fill="y")

        # Container for Pages
        self.container = tk.Frame(self, bg="white")
        self.container.pack(side="right", fill="both", expand=True, padx=2, pady=2)

        # Dictionary to store pages
        self.pages = {}
        for Page in (PageOne, PageTwo):
            page_instance = Page(self.container, self)
            self.pages[Page] = page_instance
            page_instance.grid(row=0, column=0, sticky="nsew")

        # Sidebar Buttons
        self.create_sidebar_buttons()
        self.show_page(PageOne)  # Show Home Page initially

    def create_sidebar_buttons(self):
        buttons = [("Page One", PageOne), ("Page Two", PageTwo)]
        for text, page in buttons:
            btn = ttk.Button(self.sidebar, text=text, command=lambda p=page: self.show_page(p))
            btn.pack(pady=10, padx=10, fill="x")

    def show_page(self, page):
        """Display the selected page."""
        self.pages[page].tkraise()

