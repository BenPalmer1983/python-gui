
from tkinter import ttk

class UIStyle:

    background = "#181818"
    surface = "#202020"
    primary = "#8D99AE"
    secondary = "#EDF2F4"
    accent = "#D90429"
    text = "#FFFFFF"
    entry = "#363c47"

    @staticmethod
    def set_style():
            
        background = UIStyle.background
        surface = UIStyle.surface
        primary = UIStyle.primary
        secondary = UIStyle.secondary
        accent = UIStyle.accent
        text = UIStyle.text
        entry = UIStyle.entry

        style = ttk.Style()

        # Defaults
        style.configure("TLabel", font=("Arial", 11), background=background, foreground=text)
        style.configure("TButton", font=("Arial", 11, "bold"), padding=6, background=surface, foreground=text)
        style.configure("TEntry", font=("Arial", 11), padding=5, background=background, foreground=text)
        style.configure("TCombobox", font=("Arial", 11), padding=5, background=background, foreground=text)
        style.configure("TFrame", background=background, foreground=text) 

        # Header
        style.configure("Header.TLabel", font=("Arial", 16, "bold"), background=background, foreground=primary)

        # Side Bar
        style.configure("Sidebar.TFrame", font=("Arial", 12), background=background, foreground=background)
        style.configure("Sidebar.TButton", font=("Arial", 11, "bold"), padding=6, background=surface, foreground=primary)

        # Page Container
        style.configure("PageContainer.TFrame", font=("Arial", 12), background=surface, foreground=text)

        # Page 
        style.configure("Page.TFrame", font=("Arial", 12), background=surface, foreground=text)
        style.configure("Page.TLabel", font=("Arial", 11), background=surface, foreground=text)
        style.configure("Title.Page.TLabel", font=("Arial", 16, "bold"), background=surface, foreground=primary)
        style.configure("Page.TButton", font=("Arial", 11, "bold"), padding=6, background=surface, foreground=text)
        style.configure("Page.TEntry", font=("Arial", 11), padding=5, background=surface, foreground=text)
        style.configure("Page.TCombobox", font=("Arial", 11), padding=5, background=surface, foreground=text)
        style.configure("Page.Treeview", font=("Arial", 11), padding=5, background=surface, foreground=text)



        # Notebook (Tabs)
        style.configure("TNotebook", background=surface, foreground=text, tabposition="nw", padding=[0,0,0,0]) 
        style.configure("TNotebook.Tab", background=surface, foreground=text, padding=[10, 5], anchor="w") 
        style.configure("TNotebook.TFrame", background=surface, foreground=text, padding=[10,10,10,10])
        style.configure("TNotebook.TLabel", background=surface, foreground=text)
        style.configure("Title.TNotebook.TLabel", font=("Arial", 16, "bold"), background=surface, foreground=text)
        style.configure("TNotebook.TButton", font=("Arial", 11, "bold"), padding=6, background=surface, foreground=text)
        style.configure("TNotebook.TEntry", font=("Arial", 11), padding=5, background=surface, foreground=text)
        style.configure("TNotebook.TCombobox", font=("Arial", 11), padding=5, background=surface, foreground=text)


        # Override map
        style.map("TNotebook.Tab", background=[("selected", primary)])

        style.map("TEntry",
          background=[("active", entry), ("focus", entry)],
          fieldbackground=[("!disabled", background)],
          foreground=[("!disabled", primary)])
        

        style.map("TCombobox",
          fieldbackground=[("readonly", surface), ("!disabled", "lightyellow")], 
          background=[("readonly", surface)],
          foreground=[("!disabled", text)]) 




