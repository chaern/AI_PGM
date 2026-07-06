import tkinter as tk
from tkinter import colorchooser

# -------------------------
# 상태 변수
# -------------------------
tool = "pen"
pen_color = "black"
fill_color = ""
brush_size = 3

start_x = None
start_y = None

temp_item = None


# -------------------------
# 도구 선택
# -------------------------
def set_tool(t):
    global tool
    tool = t


def choose_color():
    global pen_color
    color = colorchooser.askcolor()[1]
    if color:
        pen_color = color


def choose_fill():
    global fill_color
    color = colorchooser.askcolor()[1]
    if color:
        fill_color = color


def clear():
    canvas.delete("all")


# -------------------------
# 마우스 이벤트
# -------------------------
def mouse_down(event):
    global start_x, start_y, temp_item
    start_x, start_y = event.x, event.y
    temp_item = None


def mouse_move(event):
    global temp_item

    if tool == "pen":
        canvas.create_line(
            start_x, start_y, event.x, event.y,
            fill=pen_color,
            width=brush_size,
            capstyle=tk.ROUND,
            smooth=True
        )
        start_x, start_y = event.x, event.y


def mouse_up(event):
    global start_x, start_y

    x1, y1 = start_x, start_y
    x2, y2 = event.x, event.y

    if tool == "line":
        canvas.create_line(x1, y1, x2, y2,
                           fill=pen_color,
                           width=brush_size)

    elif tool == "rect":
        canvas.create_rectangle(x1, y1, x2, y2,
                                outline=pen_color,
                                fill=fill_color)

    elif tool == "oval":
        canvas.create_oval(x1, y1, x2, y2,
                           outline=pen_color,
                           fill=fill_color)

    elif tool == "triangle":
        canvas.create_polygon(
            x1, y2,
            (x1 + x2) / 2, y1,
            x2, y2,
            outline=pen_color,
            fill=fill_color
        )


# -------------------------
# 메인 창
# -------------------------
root = tk.Tk()
root.title("확장 그림판")
root.geometry("900x650")

# 툴바
toolbar = tk.Frame(root)
toolbar.pack(fill="x")

tk.Button(toolbar, text="펜", command=lambda: set_tool("pen")).pack(side="left")
tk.Button(toolbar, text="직선", command=lambda: set_tool("line")).pack(side="left")
tk.Button(toolbar, text="사각형", command=lambda: set_tool("rect")).pack(side="left")
tk.Button(toolbar, text="원", command=lambda: set_tool("oval")).pack(side="left")
tk.Button(toolbar, text="삼각형", command=lambda: set_tool("triangle")).pack(side="left")

tk.Button(toolbar, text="선 색", command=choose_color).pack(side="left")
tk.Button(toolbar, text="채우기", command=choose_fill).pack(side="left")

tk.Button(toolbar, text="지우기", command=clear).pack(side="left")

tk.Label(toolbar, text="두께").pack(side="left")

tk.Button(toolbar, text="1", command=lambda: set_thickness(1)).pack(side="left")
tk.Button(toolbar, text="3", command=lambda: set_thickness(3)).pack(side="left")
tk.Button(toolbar, text="5", command=lambda: set_thickness(5)).pack(side="left")
tk.Button(toolbar, text="10", command=lambda: set_thickness(10)).pack(side="left")


def set_thickness(v):
    global brush_size
    brush_size = v


# 캔버스
canvas = tk.Canvas(root, bg="white")
canvas.pack(fill="both", expand=True)

canvas.bind("<Button-1>", mouse_down)
canvas.bind("<B1-Motion>", mouse_move)
canvas.bind("<ButtonRelease-1>", mouse_up)

root.mainloop()