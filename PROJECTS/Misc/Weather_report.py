import tkinter as tk

root = tk.Tk()


class weather_pane:

    design={"bg": "#013243", "fg": "orange", 'font': ("Helvetica", 30)}

    def __init__(self, master):
        self.root = master
        # Create widgets
        self.header()
        self.top_grid()

    def header(self):
        header = tk.Frame(bg="#013243")
        tk.Label(header, text="Live Weather Report", cnf={"bg": "#013243", "fg": "orange", 'font':("Helvetica", 30)}).grid(row=0, column=0)
        tk.Label(header, cnf=self.design).grid(row=1, column=0)
        header.pack()

    def top_grid(self):
        print(self.root)

        top = tk.Frame(bg="#013243")
        tk.Label(top, text="City: ", cnf={"bg": "#013243", "fg": "White"}).grid(row=0, column=0)
        tk.Entry(top,  cnf={"bg": "#013243", "fg": "White"}).grid(row=0, column=1)
        tk.Label(top, cnf=self.design).grid(row=1, column=0)
        # Button
        print(tk.Button.keys(self))
        tk.Button(top, text="Find weather", cnf={'width':'25', 'highlightbackground':'#013243', 'activebackground':'#013243'}).grid(row=1, column=0, columnspan=2)
        top.pack()

    def footer(self):
        footer = tk.Frame(bg="#013243")
        tk.Label(footer, text="Live Weather Report", cnf={"bg": "#013243", "fg": "orange", 'font':("Helvetica", 30)}).grid(row=0, column=0)
        tk.Label(footer, cnf=self.design).grid(row=1, column=0)
        footer.pack()


# Window configuration
root.config(bg="#013243")
root.title("Weather now")
root.minsize(500, 500)
root.maxsize(500, 500)
weather_pane(root)
tk.mainloop()
