import tkinter as tk
import time
import math
import random

lYRICS = [  
    (0,  "I want one ticket out of your heavy gaze"),
    (4,  "I want one ticket off of your carousel"),
    (9,  "But you should know that i die slow"),
    (13, "Running through the halls of your haunted house"),
    (18, "And the toughest part is that we both know"),
    (22, "What happened to you"),
    (24, "Why you're out on your own"),    
    (26, "Merry chrismast, please don't call"),
    (31, "Merry chrismast, i'm not yours at all"),
    (36, "Merry chrismast, please don't call me"),
    (41, "Please don't call me"),
    (45, "Please don't call me"),
    (49, "Please don't call me"),
]    

BOX_W, BOX_H = 600, 350
FONT = ("Arial", 22, "bold")
BG_COLOR = "#840000"
FG_COLOR = "#FFFFFF"

root = tk.Tk()
root.title("Merry Chrismast - Bleachers")
root.geometry(f"{BOX_W}x{BOX_H}")
root.configure(bg=BG_COLOR)

canvas = tk.Canvas(root, width=BOX_W, height=BOX_H, bg=BG_COLOR, highlightthickness=0)
canvas.pack()

# partikel salju / debu yang melayang
particles = []
for _ in range(60):
    x = random.randint(0, BOX_W)
    y = random.randint(0, BOX_H)
    r = random.randint(1,4)
    speed = random.uniform(0.3, 1.2)
    p = canvas.create_oval(x, y, x+r*2, y+r*2, fill="white", outline="")
    particles.append([p, speed])

lyric_text = canvas.create_text(BOX_W//2, BOX_H//2, text="", fill=FG_COLOR, font=FONT, width=600, justify="center")

start = time.time()

def update():
    global last_text
    elapsed = time.time() - start
    text = ""
    for t, line in lYRICS:
        if elapsed >= t:
            text = line
        else:
            break

    # efek melayang naik - turun
    float_y = BOX_H//2 + math.sin(elapsed * 2) * 8
    canvas.coords(lyric_text, BOX_W//2, float_y)
    canvas.itemconfig(lyric_text, text=text)

    # gerakin partikel
    for p, speed in particles:
        canvas.move(p, 0, -speed)
        x1, y1, x2, y2 = canvas.coords(p)
        if y2 < 0:
            canvas.move(p, 0, BOX_H)
        if x1 < 0:
            canvas.move(p,  BOX_W, 0)

    root.after(30, update)

update()
root.mainloop()
