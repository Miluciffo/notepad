from tkinter import *

ui = Tk()
ui.title('Notepad')
# ui.iconbitmap('')
ui.geometry('800x800')
ui_menu = Menu(ui)

# ---------------------[File]-------------------------------
fl_menu = Menu(ui_menu, tearoff=0)
fl_menu.add_command(label='Open')
fl_menu.add_command(label='Save')
fl_menu.add_command(label='Close')
ui.config(menu=fl_menu)

# ---------------------[View]-------------------------------
vm_menu = Menu(ui_menu, tearoff=0)
vm_menu_sb = Menu(vm_menu, tearoff=0)
ft_menu_sb = Menu(vm_menu, tearoff=0)
# vm_menu.add_command(label='')
vm_menu_sb.add_command(label='Dark Theme')
vm_menu_sb.add_command(label='Light Theme')
vm_menu.add_cascade( label='Theme', menu=vm_menu_sb)

ui_menu.add_cascade(label='File', menu=fl_menu)
ui_menu.add_cascade(label='View', menu=vm_menu)
ui.config(menu=ui_menu)


fr_text = Frame(ui)
fr_text.pack(fill=BOTH, expand=1)
text_fd = Text(fr_text, bg='white', fg='black', padx=9, pady=9, wrap=WORD, insertbackground='black' , spacing3=10 , width=30)
text_fd.pack(expand=1, fill=BOTH, side=LEFT)

scr_bar=Scrollbar(fr_text, command=text_fd.yview)
scr_bar.pack(side=LEFT, fill=Y)
text_fd.config(yscrollcommand=scr_bar.set)

ui.mainloop()
