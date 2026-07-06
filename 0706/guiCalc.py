import tkinter as tk
from tkinter import messagebox

expression = ""


def press(value):
    global expression
    expression += str(value)
    display_var.set(expression)


def clear():
    global expression
    expression = ""
    display_var.set("")


def backspace():
    global expression
    expression = expression[:-1]
    display_var.set(expression)


def calculate():
    global expression
    try:
        result = str(eval(expression))
        display_var.set(result)
        expression = result
    except ZeroDivisionError:
        messagebox.showerror("오류", "0으로 나눌 수 없습니다.")
        clear()
    except Exception:
        messagebox.showerror("오류", "잘못된 수식입니다.")
        clear()


# -------------------------
# 메인 창
# -------------------------
root = tk.Tk()
root.title("계산기")
root.geometry("350x500")
root.minsize(300, 400)     # 최소 크기
# root.resizable(False, False)  ← 삭제

display_var = tk.StringVar()

# 화면
display = tk.Entry(
    root,
    textvariable=display_var,
    font=("Arial", 22),
    justify="right",
)
display.pack(fill="x", padx=10, pady=10, ipady=15)

# 버튼 프레임
frame = tk.Frame(root)
frame.pack(fill="both", expand=True, padx=5, pady=5)

buttons = [
    ["C", "←", "/", "*"],
    ["7", "8", "9", "-"],
    ["4", "5", "6", "+"],
    ["1", "2", "3", "="],
    ["0", ".", "(", ")"],
]

for r, row in enumerate(buttons):
    for c, text in enumerate(row):

        if text == "C":
            command = clear
        elif text == "←":
            command = backspace
        elif text == "=":
            command = calculate
        else:
            command = lambda t=text: press(t)

        btn = tk.Button(
            frame,
            text=text,
            font=("Arial", 18),
            command=command
        )

        btn.grid(
            row=r,
            column=c,
            sticky="nsew",
            padx=2,
            pady=2
        )

# 행과 열이 창 크기에 맞게 같이 늘어남
for i in range(len(buttons)):
    frame.rowconfigure(i, weight=1)

for i in range(4):
    frame.columnconfigure(i, weight=1)

root.mainloop()