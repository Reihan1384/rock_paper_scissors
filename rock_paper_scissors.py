import random
import tkinter as tk

# ================= colors =====================
backgr = "#4CC9F0"
actions = "#7209B7"
scores = "#FFD166"
texts = "#000000"

# ================= game variables =====================
player1Score = 0
player2Score = 0
winningScore = 5

# ================= game logic =====================
def computer_move():
    return random.choice(["سنگ", "کاغذ", "قیچی"])
    
def rounds(player1):
    global player1Score ,player2Score
    
    player2 = computer_move()
    
    if player1 == player2:
       result = "!تساوی"
    
    elif player1 == "سنگ":
        if player2 == "قیچی":
            player1Score += 1
            result = "!بازیکن 1 این راند رو برد"
        elif player2 == "کاغذ":
            player2Score += 1
            result = "!بازیکن 2 این راند رو برد"
            
    elif player1 == "قیچی":
        if player2 == "کاغذ":
            player1Score += 1
            result = "!بازیکن 1 این راند رو برد"
        elif player2 == "سنگ":
            player2Score += 1
            result = "!بازیکن 2 این راند رو برد"
            
    elif player1 == "کاغذ":
        if player2 == "سنگ":
            player1Score += 1
            result = "!بازیکن 1 این راند رو برد"
        elif player2 == "قیچی":
            player2Score += 1 
            result = "!بازیکن 2 این راند رو برد"
    return result, player2
            

# ================= window =====================
root = tk.Tk()
root.title("Rock-Paper-Scissors")
root.geometry("800x750")
root.configure(bg=backgr)
root.resizable(False, False)

def show_frame(frame):
    frame.tkraise()

# ================= frames =====================       
main_frame = tk.Frame(root, bg=backgr)
game_frame = tk.Frame(root, bg=backgr)

for frame in (main_frame, game_frame):
    frame.place(x=0, y=0, width=800, height=750)

show_frame(main_frame)

# ================= main frame =====================  
title_lable = tk.Label(main_frame, 
                       text="سنگ کاغذ قیچی", 
                       bg=backgr, 
                       fg=texts, 
                       font=("Tahoma", 24, "bold"))
title_lable.place(relx=0.5, rely=0.2, anchor="center")

prompt_lable = tk.Label(main_frame, 
                        text=":امتیاز برنده شدن را وارد کنید", 
                        bg=backgr, 
                        fg=texts, 
                        font=("Tahoma", 24, "bold"))
prompt_lable.place(relx=0.5, rely=0.35, anchor="center")

score_entry = tk.Entry(main_frame, 
                       font=("Tahoma", 16), 
                       justify="center")
score_entry.place(relx=0.5, rely=0.45, anchor="center")

def start_game():
    global winningScore
    val = score_entry.get()
    if val.isdigit() and int(val) > 0:
        winningScore = int(val)
        reset_game()
        show_frame(game_frame)
    else:
        prompt_lable.config("!عدد معتبر وارد کنید", fg="red")

start_btn = tk.Button(main_frame, 
                      text="شروع بازی", 
                      font=("Tahoma", 16, "bold"), 
                      width=12, 
                      height=2, 
                      bg=actions, 
                      fg=texts, 
                      command=start_game)
start_btn.place(relx=0.5, rely=0.6, anchor="center")
        
# ================= game frame =================

# عنوان
game_lable = tk.Label(
    game_frame,
    text="سنگ کاغذ قیچی",
    bg=backgr,
    fg=texts,
    font=("Tahoma", 24, "bold")
)
game_lable.place(relx=0.5, rely=0.08, anchor="center")

# امتیاز
score_label = tk.Label(
    game_frame,
    text="بازیکن 1: 0 | بازیکن 2: 0",
    bg=scores,
    fg=texts,
    font=("Tahoma", 16, "bold"),
    padx=20,
    pady=8
)
score_label.place(relx=0.5, rely=0.18, anchor="center")

# نتیجه راند
result_label = tk.Label(
    game_frame,
    text=" 👇حرکت خود را انتخاب کن",
    bg=backgr,
    fg=texts,
    font=("Tahoma", 18)
)
result_label.place(relx=0.5, rely=0.32, anchor="center")

# حرکت کامپیوتر
cpu_move_label = tk.Label(
    game_frame,
    text="",
    bg=backgr,
    fg=texts,
    font=("Tahoma", 16)
)
cpu_move_label.place(relx=0.5, rely=0.40, anchor="center")


# ================= update score =================
def update_score():
    score_label.config(
        text=f"بازیکن 1: {player1Score} | بازیکن 2: {player2Score}"
    )

    if player1Score >= winningScore:
        result_label.config(text="🎉 !بازیکن 1 برنده کل بازی شد")
    elif player2Score >= winningScore:
        result_label.config(text="💻 !بازیکن 2 برنده کل بازی شد")


# ================= play function =================
def play(choice):
    if player1Score >= winningScore or player2Score >= winningScore:
        return

    result, cpu = rounds(choice)

    result_label.config(text=result)
    cpu_move_label.config(text=f"حرکت کامپیوتر: {cpu}")
    update_score()


# ================= buttons =================
btn_frame = tk.Frame(game_frame, bg=backgr)
btn_frame.place(relx=0.5, rely=0.6, anchor="center")

rock_btn = tk.Button(
    btn_frame, text="سنگ\n🪨",
    font=("Arial", 28),
    width=4, height=2,
    bg=actions, fg="white",
    command=lambda: play("سنگ")
)
rock_btn.grid(row=0, column=0, padx=20)

paper_btn = tk.Button(
    btn_frame, text="کاغذ\n📄",
    font=("Arial", 28),
    width=4, height=2,
    bg=actions, fg="white",
    command=lambda: play("کاغذ")
)
paper_btn.grid(row=0, column=1, padx=20)

scissors_btn = tk.Button(
    btn_frame, text="قیچی\n✂️",
    font=("Arial", 28),
    width=4, height=2,
    bg=actions, fg="white",
    command=lambda: play("قیچی")
)
scissors_btn.grid(row=0, column=2, padx=20)

# ================= reset function =================
def reset_game():
    global player1Score,player2Score
    player1Score = 0
    player2Score = 0
    score_label.config(text="بازیکن 1: 0 | بازیکن 2: 0")
    result_label.config(text=" 👇حرکت خود را انتخاب کن")
    cpu_move_label.config(text="")
    score_entry.delete(0, tk.END)
    prompt_lable.config(text=":امتیاز برنده شدن را وارد کنید", fg=texts)

# ================= back buttons =================
back_btn = tk.Button(
    game_frame,
    text="بازگشت",
    bg=actions,
    fg=texts,
    font=("Tahoma", 18, "bold"),
    command=lambda: show_frame(main_frame)
)
back_btn.place(relx=0.5, rely=0.85, anchor="center")



root.mainloop()