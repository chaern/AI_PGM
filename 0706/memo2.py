# Memo Pro UI (2-toolbar version)
import tkinter as tk
from tkinter import ttk, filedialog, colorchooser

current_file=None

FONT_LIST=[
"Arial","Calibri","Times New Roman","Courier New","Verdana",
"Georgia","Comic Sans MS","Tahoma","Consolas","Impact"
]

def new_file():
    global current_file
    text.delete("1.0",tk.END)
    current_file=None

def open_file():
    global current_file
    f=filedialog.askopenfilename(filetypes=[("Text","*.txt")])
    if not f:return
    with open(f,"r",encoding="utf-8") as fp:
        text.delete("1.0",tk.END)
        text.insert("1.0",fp.read())
    current_file=f

def save_as():
    global current_file
    f=filedialog.asksaveasfilename(defaultextension=".txt")
    if f:
        current_file=f
        save_file()

def save_file():
    global current_file
    if not current_file:
        return save_as()
    with open(current_file,"w",encoding="utf-8") as fp:
        fp.write(text.get("1.0",tk.END))

def find_text():
    text.tag_remove("find","1.0",tk.END)
    word=find_entry.get()
    if not word:return
    idx="1.0"
    while True:
        idx=text.search(word,idx,nocase=1,stopindex=tk.END)
        if not idx:break
        end=f"{idx}+{len(word)}c"
        text.tag_add("find",idx,end)
        idx=end
    text.tag_config("find",background="yellow")

def replace_text():
    a = find_entry.get()
    b = replace_entry.get()

    content = text.get("1.0", tk.END)
    content = content.replace(a, b)

    text.delete("1.0", tk.END)
    text.insert("1.0", content)

def apply_font():
    text.configure(font=(font_var.get(),size_var.get()))

def pick_color():
    c=colorchooser.askcolor()[1]
    if c:
        try:
            text.tag_add("color","sel.first","sel.last")
            text.tag_config("color",foreground=c)
        except tk.TclError:
            pass

def align(j):
    text.tag_configure("align",justify=j)
    text.tag_add("align","1.0","end")

root=tk.Tk()
root.title("Memo Pro UI")
root.geometry("1000x650")
root.minsize(900,600)

toolbar1=tk.Frame(root,bg="#f0f0f0")
toolbar1.pack(fill="x")
toolbar2=tk.Frame(root,bg="#f0f0f0")
toolbar2.pack(fill="x")

ttk.Button(toolbar1,text="📄",command=new_file).pack(side="left",padx=2,pady=2)
ttk.Button(toolbar1,text="📂",command=open_file).pack(side="left",padx=2)
ttk.Button(toolbar1,text="💾",command=save_file).pack(side="left",padx=2)



ttk.Label(toolbar1, text="검색").pack(side="left", padx=(10, 2))
find_entry = ttk.Entry(toolbar1, width=15)
find_entry.pack(side="left")

ttk.Label(toolbar1, text="바꾸기").pack(side="left", padx=(10, 2))
replace_entry = ttk.Entry(toolbar1, width=15)
replace_entry.pack(side="left")

ttk.Button(
    toolbar1,
    text="🔍 검색",
    command=find_text
).pack(side="left", padx=5)

ttk.Button(
    toolbar1,
    text="🔁 바꾸기",
    command=replace_text
).pack(side="left", padx=2)


font_var=tk.StringVar(value="Arial")
size_var=tk.IntVar(value=12)
ttk.Combobox(toolbar2,textvariable=font_var,values=FONT_LIST,width=15,state="readonly").pack(side="left",padx=5,pady=2)
ttk.Combobox(toolbar2,textvariable=size_var,values=list(range(8,40)),width=5,state="readonly").pack(side="left",padx=5)
ttk.Button(toolbar2,text="A✓",command=apply_font).pack(side="left",padx=2)
ttk.Button(toolbar2,text="🎨",command=pick_color).pack(side="left",padx=5)
ttk.Button(
    toolbar2,
    text="⬅ 왼쪽",
    command=lambda: align("left")
).pack(side="left", padx=3)

ttk.Button(
    toolbar2,
    text="↔ 가운데",
    command=lambda: align("center")
).pack(side="left", padx=3)

ttk.Button(
    toolbar2,
    text="➡ 오른쪽",
    command=lambda: align("right")
).pack(side="left", padx=3)

text=tk.Text(root,wrap="word",undo=True,font=("Arial",12),padx=15,pady=15,borderwidth=0)
text.pack(fill="both",expand=True)

root.mainloop()
