import tkinter as tk
import tkinter.ttk as ttk


class TestApp:
    def __init__(self, master=None):
        # build ui
        self.toplevel_4 = tk.Tk() if master is None else tk.Toplevel(master)
        self.label_3 = tk.Label(self.toplevel_4)
        self.label_3.configure(cursor='arrow', font='{Arial} 36 {bold}', state='normal', text='Mask Detect')
        self.label_3.pack(side='top')
        self.labelframe_4 = tk.LabelFrame(self.toplevel_4)
        self.label_4 = tk.Label(self.labelframe_4)
        self.label_4.configure(text='label_4')
        self.label_4.pack(side='top')
        self.entry_2 = tk.Entry(self.labelframe_4)
        _text_ = '''entry_2'''
        self.entry_2.delete('0', 'end')
        self.entry_2.insert('0', _text_)
        self.entry_2.pack(side='top')
        self.button_2 = tk.Button(self.labelframe_4)
        self.button_2.configure(text='button_2')
        self.button_2.pack(side='top')
        self.labelframe_4.configure(font='{Arial} 14 {italic}', height='200', padx='20', text='Local Webcam')
        self.labelframe_4.configure(width='600')
        self.labelframe_4.pack(side='top')
        self.toplevel_4.configure(height='200', width='200')

        # Main widget
        self.mainwindow = self.toplevel_4


    def run(self):
        self.mainwindow.mainloop()

if __name__ == '__main__':
    app = TestApp()
    app.run()

