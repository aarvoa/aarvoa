from tkinter import *
from tkinter.filedialog import asksaveasfilename, askopenfilename
import subprocess
compiler = Tk()
compiler.title("ARmaxIDE")
file_path = ''



def set_file_path(path):
    global file_path
    file_path = path


def save_as():
    if file_path == '':
        path = asksaveasfilename(filetypes=[('Python Files', "*.py")])
    else:
        path = file_path
    with open(path, 'w') as file:
        code = editor.get("1.0", END)
        file.write(code)
        set_file_path(path)

def open_file():
    path = askopenfilename(filetypes=[('Python Files', "*.py")])
    with open(path, 'r') as file:
        code = file.read()
        editor.delete('1.0', END)
        editor.insert(1.0, code)
        set_file_path(path)

def run():
    if file_path == '':
        save_prompt = Toplevel()
        text = Label(save_prompt, text='Please save your code')
        text.pack()
        return 	
    command = f'python {file_path}'
    print(file_path)
    print(command)
    process =  subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    code_output.insert('1.0', output)
    code_output.insert('1.0', error)

def about():
    # make this window same background color as black
    about_prompt = Toplevel()
    about_prompt.title("About")
    about_prompt.configure(bg='gray11')
    text = Message(about_prompt, text='ARmaxIDE was created by aarvoa or also known as ItzAtlasGG\nThis IDE is still in development\nThis IDE is good for low end pc and laptops because it is light weight\nThis IDE is open source\nThis IDE is free to use\nHope you like it and have fun coding', bg='gray11', fg='white')
    text.pack()
    button = Button(about_prompt, text="Close", command=about_prompt.destroy, bg='white', fg='gray11')
    button.pack()    
menu_bar = Menu(compiler)

file_menu = Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_as)
file_menu.add_command(label="Save as", command=save_as)
file_menu.add_command(label="Exit", command=exit)
file_menu.add_command(label="About", command=about)
menu_bar.add_cascade(label="File", menu=file_menu)

run_bar = Menu(menu_bar, tearoff=0)
run_bar.add_command(label="Run", command=run)
menu_bar.add_cascade(label="Run", menu=run_bar)

compiler.config(menu=menu_bar)
# add a sidebar to the editor
sidebar = Frame(compiler, width=200, bg='gray20')
sidebar.pack_propagate(False)
sidebar.pack(side=LEFT, fill=Y)
# add a scrollbar to the editor
scrollbar = Scrollbar(compiler)
scrollbar.pack(side=RIGHT, fill=Y)
compiler.configure(bg='gray11')
editor = Text(bg='gray11', fg='white')
editor.pack(expand=True, fill=BOTH)
#
code_output = Text(height=10, bg='gray11', fg='white')
code_output.pack(expand=True, fill=BOTH)

compiler.mainloop()

# make the fontsize 16
compiler.option_add('*Font', '16')