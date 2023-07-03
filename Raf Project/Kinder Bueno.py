import tkinter as tk
from tkinter import messagebox


class GUI:
    def __init__(self):
        self.root = tk.Tk()

        self.label = tk.Label(self.root, text='O golis vromaei', font=('Arial', 18))
        self.label.pack(padx=10, pady=10)

        self.menubar = tk.Menu(self.root)
        self.filemenu = tk.Menu(self.menubar, tearoff=0)
        self.filemenu.add_command(label='close', command=exit)
        self.menubar.add_cascade(menu=self.filemenu, label='File')

        self.textbox = tk.Text(self.root, height=5, font=('Arial', 16))
        self.textbox.bind('<KeyPress>', self.shortcut)
        self.textbox.pack(padx=10, pady=10)

        self.root.protocol('WM_DELETE_WINDOW', self.close)

        self.check_state = tk.IntVar()  # <--

        self.check = tk.Checkbutton(self.root, text="Show Messagebox", font=('Arial', 16), variable=self.check_state)
        self.check.pack(padx=10, pady=10)

        self.button = tk.Button(self.root, text='Show Message', font=('Arial', 18), command=self.show_message)
        self.button.pack(padx=10, pady=10)

        self.root.mainloop()

    def show_message(self):
        if self.check_state.get() == 0:
            print(self.textbox.get('1.0', tk.END))
        else:
            messagebox.showinfo(title='Message', message=self.textbox.get('1.0', tk.END))

    def shortcut(self, event):
        if event.keysym == 'Return' and event.char == '\r':
            self.show_message()

    def close(self):
        if messagebox.askyesno(title='fugeis?', message='8a fugeis?'):
            self.root.destroy()


GUI()