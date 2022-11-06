from tkinter import *
import math
import winsound
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
GRIN = "#395144"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
reps = 5
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_mark.config(text="✓")
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    check_mark.config(text="")
    if reps % 8 == 0:
        count_down(long_break_secs)
        title_label.config(text="Break", fg=RED)
    if reps % 2 == 0:
        count_down(short_break_secs)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        title_label.config(text="Work", fg=GREEN)
    winsound.Beep(500, 1000)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    minutes = math.floor(count / 60)
    seconds = int(count % 60)
    if seconds < 10:
        seconds = f'0{seconds}'
    if seconds == 0:
        seconds = "00"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✓"
            check_mark.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
tomato = PhotoImage(file="tomato.png")
window.config(padx=100, pady=50, bg=YELLOW)

window.iconbitmap('icon.ico')
title_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW,  highlightthickness=0)
canvas.create_image(100, 112, image=tomato)


timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="start", bg=YELLOW, fg=GRIN, command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

reset_button = Button(text="reset", bg=YELLOW, fg=GRIN, command=reset, highlightthickness=0)
reset_button.grid(column=2, row=2)

check_mark = Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30))
check_mark.grid(column=1, row=3)






window.mainloop()
