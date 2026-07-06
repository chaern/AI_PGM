import tkinter as tk
from tkinter import filedialog, messagebox
import os

current_file = None
dark_mode = False


# -------------------------
# 파일 기능
# -------------------------
def new_file():
    global current_file
    text.delete("1.0", tk.END)
    current_file = None
    status.set("새 문서")


def open_file():
    global current_file

    filename = filedialog.askopenfilename(
        filetypes=[("텍스트 파일", "*.txt"), ("모든 파일", "*.*")]
    )

    if not filename:
        return

    with open(filename, "r", encoding="utf-8") as f:
        text.delete("1.0", tk.END)
        text.insert(tk.END, f.read())

    current_file = filename
    status.set(f"열림: {os.path.basename(filename)}")


def save_file():
    global current_file

    if current_file is None:
        save_as()
        return

    with open(current_file, "w", encoding="utf-8") as f:
        f.write(text.get("1.0", tk.END))

    status.set("저장됨")


def save_as():
    global current_file

    filename = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("텍스트 파일", "*.txt")]
    )

    if not filename:
        return

    current_file = filename
    save_file()


# -------------------------
# 편집 기능
# -------------------------
def find_text():
    target = find_entry.get()
    text.tag_remove("highlight", "1.0", tk.END)

    if target:
        idx = "1.0"
        while True:
            idx = text.search(target, idx, nocase=1, stopindex=tk.END)
            if not idx:
                break
            end = f"{idx}+{len(target)}c"
            text.tag_add("highlight", idx, end)
            idx = end

        text.tag_config("highlight", background="yellow")


def replace_text():
    find = find_entry.get()
    replace = replace_entry.get()

    content = text.get("1.0", tk.END)
    new_content = content.replace(find, replace)

    text.delete("1.0", tk.END)
    text.insert("1.0", new_content)


# -------------------------
# UI 기능
# -------------------------
def update_status(event=None):
    content = text.get("1.0", tk.END)
    chars = len(content) - 1
    status.set(f"글자 수: {chars}")


def toggle_theme():
    global dark_mode

    dark_mode = not dark_mode

    if dark_mode:
        bg = "#1e1e1e"
        fg = "white"
    else:
        bg = "white"
        fg = "black"

    text.config(bg=bg, fg=fg, insertbackground=fg)


# -------------------------
# 자동 저장
# -------------------------
def auto_save():
    if current_file:
        try:
            with open(current_file, "w", encoding="utf-8") as f:
                f.write(text.get("1.0", tk.END))
        except:
            pass

    root.after(3000, auto_save)  # 3초마다 저장


# -------------------------
# 메인 창
# -------------------------
root = tk.Tk()
root.title("강화된 메모장")
root.geometry("900x600")

# 메뉴
menu = tk.Menu(root)
file_menu = tk.Menu(menu, tearoff=0)

file_menu.add_command(label="새 파일", command=new_file)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_command(label="다른 이름으로 저장", command=save_as)

menu.add_cascade(label="파일", menu=file_menu)
menu.add_command(label="다크모드", command=toggle_theme)

root.config(menu=menu)


# -------------------------
# 상단 찾기/바꾸기
# -------------------------
top_frame = tk.Frame(root)
top_frame.pack(fill="x")

find_entry = tk.Entry(top_frame)
find_entry.pack(side="left", fill="x", expand=True, padx=5, pady=5)
find_entry.insert(0, "찾기")

replace_entry = tk.Entry(top_frame)
replace_entry.pack(side="left", fill="x", expand=True, padx=5)
replace_entry.insert(0, "바꾸기")

tk.Button(top_frame, text="찾기", command=find_text).pack(side="left")
tk.Button(top_frame, text="바꾸기", command=replace_text).pack(side="left")


# -------------------------
# 텍스트 영역
# -------------------------
text = tk.Text(root, undo=True, wrap="word")
text.pack(fill="both", expand=True)

text.bind("<KeyRelease>", update_status)


scroll = tk.Scrollbar(text)
scroll.pack(side="right", fill="y")
text.config(yscrollcommand=scroll.set)
scroll.config(command=text.yview)


# -------------------------
# 상태바
# -------------------------
status = tk.StringVar()
status.set("글자 수: 0")

status_bar = tk.Label(root, textvariable=status, anchor="w")
status_bar.pack(fill="x")


# -------------------------
# 시작
# -------------------------
auto_save()
root.mainloop()