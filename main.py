from tkinter import *
from functools import partial
import random

root = Tk()
root.title("Double Player Mode")  # Window title

dble_frame = Frame(root, width=700, height=500, bg="green")  # Window frame
dble_frame.grid()

dealer_side = Label(
    dble_frame,
    text="Dealer",
    font="Times 14 bold",  # Dealer's Side, 
    bg="#733f19",
    fg="white",
    padx=330,
    pady=12)  # of the table
dealer_side.place(x=-10, y=0)

dble_creds_1 = 500  # Intial value of credits for player one
dble_bets_1 = 5  # and their bets

dble_creds_2 = 500  # Intial value for credits for player two
dble_bets_2 = 5  # and their bets


def dble_add_creds_1():
    global dble_creds_1
    dble_creds_1 += dble_bets_1
    dble_creds_1_counter.set("Credits: ${:.2f}".format(dble_creds_1))


def dble_sub_creds_1():
    global dble_creds_1
    dble_creds_1 -= dble_bets_1
    dble_creds_1_counter.set("Credits: ${:.2f}".format(dble_creds_1))


def dble_add_creds_2():
    global dble_creds_2
    dble_creds_2 += dble_bets_2
    dble_creds_2_counter.set("Credits: ${:.2f}".format(dble_creds_2))


def dble_sub_creds_2():
    global dble_creds_2
    dble_creds_2 -= dble_bets_2
    dble_creds_2_counter.set("Credits: ${:.2f}".format(dble_creds_2))


def dble_bets_add_1():
    global dble_bets_1
    dble_bet_add_1 = dble_bet_add_sub_var.get()
    dble_bets_1 += dble_bet_add_1
    dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
    dble_bet_add_sub_var.set(5)


def dble_bets_sub_1():
    global dble_bets_1
    dble_bet_add_1 = dble_bet_add_sub_var.get()
    dble_bets_1 -= dble_bet_add_1
    dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
    dble_bet_add_sub_var.set(5)


def dble_bets_add_2():
    global dble_bets_2
    dble_bet_add_2 = dble_bet_add_sub_var.get()
    dble_bets_2 += dble_bet_add_2
    dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
    dble_bet_add_sub_var.set(5)


def dble_bets_sub_2():
    global dble_bets_2
    dble_bet_sub_2 = dble_bet_add_sub_var.get()
    dble_bets_2 -= dble_bet_sub_2
    dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
    dble_bet_add_sub_var.set(5)


dble_creds_1_counter = StringVar()  # Sets variable as a string variable
dble_creds_1_counter.set("Credits: $500.00")
dble_creds_1_display = Label(dble_frame,
                             textvariable=dble_creds_1_counter,
                             bg="orange",
                             font="Times 10")
dble_creds_1_display.place(x=25, y=70)

dble_bets_1_counter = StringVar()
dble_bets_1_counter.set("Bets: $5.00")
dble_bets_1_display = Label(dble_frame,
                            textvariable=dble_bets_1_counter,
                            bg="orange",
                            font="Times 10")
dble_bets_1_display.place(x=25, y=100)

dble_creds_2_counter = StringVar()
dble_creds_2_counter.set("Credits: $500.00")
dble_creds_2_display = Label(dble_frame,
                             textvariable=dble_creds_2_counter,
                             bg="orange",
                             font="Times 10")
dble_creds_2_display.place(x=557, y=70)

dble_bets_2_counter = StringVar()
dble_bets_2_counter.set("Bets: $5.00")
dble_bets_2_display = Label(dble_frame,
                            textvariable=dble_bets_2_counter,
                            bg="orange",
                            font="Times 10")
dble_bets_2_display.place(x=592, y=100)

dble_bet_add_sub_var = IntVar()
dble_bet_add_sub_var.set(5)
dble_bet_add_but_1 = Button(dble_frame,
                            text="Add bets",
                            bg="gold",
                            bd=1,
                            command=dble_bets_add_1)
dble_bet_add_but_1.place(x=20, y=150)
dble_bet_sub_but_1 = Button(dble_frame,
                            text="Remove bets",
                            bg="gold",
                            bd=1,
                            command=dble_bets_sub_1)
dble_bet_sub_but_1.place(x=20, y=180)

dble_bet_add_but_2 = Button(dble_frame,
                            text="Add bets",
                            bg="gold",
                            bd=1,
                            command=dble_bets_add_2)
dble_bet_add_but_2.place(x=604, y=150)
dble_bet_sub_but_2 = Button(dble_frame,
                            text="Remove bets",
                            bg="gold",
                            bd=1,
                            command=dble_bets_sub_2)
dble_bet_sub_but_2.place(x=580, y=180)


def dble_buttons_state_play():
    dble_bet_add_but_1.config(state=DISABLED)
    dble_bet_sub_but_1.config(state=DISABLED)
    dble_bet_add_but_2.config(state=DISABLED)
    dble_bet_sub_but_2.config(state=DISABLED)
    dble_confirm_bets.config(state=DISABLED)
    dble_cnfrm_bets()


def dble_cnfrm_bets():
    global dble_play_1_crd_1
    global dble_play_1_crd_2
    global dble_play_1_ttl
    global dble_play_2_crd_1
    global dble_play_2_crd_2
    global dble_play_2_ttl
    dble_play_1_crd_1 = random.randint(1, 11)
    dble_play_1_crd_2 = random.randint(1, 11)
    dble_play_1_ttl = (dble_play_1_crd_1 + dble_play_1_crd_2)
    dble_play_2_crd_1 = random.randint(1, 11)
    dble_play_2_crd_2 = random.randint(1, 11)
    dble_play_2_ttl = (dble_play_2_crd_1 + dble_play_2_crd_2)
    print("Player 1 cards: ", dble_play_1_crd_1, dble_play_1_crd_2)
    print(dble_play_1_ttl, "\n")
    print("Player 2 cards: ", dble_play_2_crd_1, dble_play_2_crd_2)
    print(dble_play_2_ttl, "\n")
    if dble_play_1_ttl == 21:
        print("Player 1 wins!!")
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL)
        dble_add_creds_1()
        dble_sub_creds_2()
    if dble_play_1_ttl > 21:
        print("Player 1 loses")
        dble_sub_creds_1()
        dble_play_2_v_deal()
    if dble_play_2_ttl == 21:
        print("Player 2 wins!!")
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL)
        dble_add_creds_2()
        dble_sub_creds_1()
    if dble_play_2_ttl > 21:
        print("Player 2 loses")
        dble_sub_creds_2()
        dble_play_1_crd_ttl_v_deal()
    if dble_play_1_ttl and dble_play_2_ttl < 21:
        print("Choose an action (player 1 goes first) \n")
        dble_hit_but_1.config(state=NORMAL)
        dble_stay_but_1.config(state=NORMAL)
        dble_double_but_1.config(state=NORMAL)


dble_confirm_bets = Button(dble_frame,
                           text="Confirm bets",
                           bg="orange",
                           bd=1,
                           command=dble_buttons_state_play)
dble_confirm_bets.place(x=300, y=450)


def dble_crd_check():
    dble_hit_but_2.config(state=DISABLED)
    dble_stay_but_2.config(state=DISABLED)
    dble_double_but_2.config(state=DISABLED)
    global dble_play_1_ttl
    global dble_play_2_ttl
    if dble_play_1_ttl > dble_play_2_ttl:
        print("Player 2 is out \n")
        dble_sub_creds_2()
        dble_play_1_v_deal()
    if dble_play_1_ttl < dble_play_2_ttl:
        print("Player 1 is out \n")
        dble_sub_creds_1()
        dble_play_2_v_deal()
    if dble_play_1_ttl == dble_play_2_ttl:
        print("Its a draw \n")
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL) 
        


def dble_play_1_v_deal():
    dble_crd_1_deal = random.randint(1, 11)
    dble_crd_2_deal = random.randint(1, 11)
    dble_deal_crd_ttl = (dble_crd_1_deal + dble_crd_2_deal)
    print("Dealer cards", dble_crd_1_deal, dble_crd_2_deal, "\n")
    if dble_deal_crd_ttl == 21:
        print("Dealer wins \n")
        dble_sub_creds_1()
    if dble_deal_crd_ttl > 21:
        print("Player 1 wins \n")
        dble_add_creds_1()
    if dble_deal_crd_ttl > dble_play_1_ttl:
        print("Dealer wins \n")
        dble_sub_creds_1()
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL)
    if dble_deal_crd_ttl < dble_play_1_ttl:
        print("Player 1 wins \n")
        dble_add_creds_1()
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL)
    if dble_deal_crd_ttl == dble_play_1_ttl:
          print("Its a draw")
          dble_bet_add_but_1.config(state=NORMAL)
          dble_bet_sub_but_1.config(state=NORMAL)
          dble_bet_add_but_2.config(state=NORMAL)
          dble_bet_sub_but_2.config(state=NORMAL)
          dble_confirm_bets.config(state=NORMAL)


def dble_play_2_v_deal():
    dble_crd_1_deal = random.randint(1, 11)
    dble_crd_2_deal = random.randint(1, 11)
    dble_deal_crd_ttl = (dble_crd_1_deal + dble_crd_2_deal)
    dble_crd_hit_1 = random.randint(1, 11)
    dble_crd_hit_2 = random.randint(1, 11)
    print("Dealer cards", dble_crd_1_deal, dble_crd_2_deal, "\n")
    if dble_deal_crd_ttl == 21:
        print("Dealer wins \n")
        dble_sub_creds_2()
    if dble_deal_crd_ttl > 21:
        print("Player 2 wins \n")
        dble_add_creds_2()
    if dble_deal_crd_ttl > dble_play_2_ttl:
        print("Dealer wins \n")
        dble_sub_creds_2()
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL)
    if dble_deal_crd_ttl < dble_play_2_ttl:
        print("Player 2 wins \n")
        dble_add_creds_2()
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL)
    if dble_deal_crd_ttl == dble_play_2_ttl:
        print("Its a draw")
        dble_bet_add_but_1.config(state=NORMAL)
        dble_bet_sub_but_1.config(state=NORMAL)
        dble_bet_add_but_2.config(state=NORMAL)
        dble_bet_sub_but_2.config(state=NORMAL)
        dble_confirm_bets.config(state=NORMAL)


def dble_hit_1():
    global dble_play_1_ttl
    global dble_crd_hit_1
    dble_crd_hit_1 = random.randint(1, 11)
    dble_play_1_ttl += dble_crd_hit_1
    print("Player 1 hit card: ", dble_crd_hit_1)
    print(dble_play_1_ttl, "\n")
    if dble_play_1_ttl == 21:
        print("Player 1 wins")
        dble_add_creds_1()
    if dble_play_1_ttl > 21:
        print("Player 1 is busted")
        dble_sub_creds_1()
        dble_play_2_v_deal()
    if dble_play_1_ttl < 21:
        print("Play on \n")
        dble_hit_but_1.config(state=DISABLED)
        dble_stay_but_1.config(state=DISABLED)
        dble_double_but_1.config(state=DISABLED)
        dble_hit_but_2.config(state=NORMAL)
        dble_stay_but_2.config(state=NORMAL)
        dble_double_but_2.config(state=NORMAL)


def dble_double_1():
    global dble_bets_1
    dble_bets_1 *= 2
    dble_bets_1_counter.set("Bets: ${:.2f}".format(dble_bets_1))
    dble_hit_but_1.config(state=DISABLED)
    dble_stay_but_1.config(state=DISABLED)
    dble_double_but_1.config(state=DISABLED)
    dble_hit_but_2.config(state=NORMAL)
    dble_stay_but_2.config(state=NORMAL)
    dble_double_but_2.config(state=NORMAL)


def dble_stay_1():
    print("Play on \n")
    dble_hit_but_1.config(state=DISABLED)
    dble_stay_but_1.config(state=DISABLED)
    dble_double_but_1.config(state=DISABLED)
    dble_hit_but_2.config(state=NORMAL)
    dble_stay_but_2.config(state=NORMAL)
    dble_double_but_2.config(state=NORMAL)


dble_hit_but_1 = Button(dble_frame,
                        text="Hit",
                        bg="white",
                        bd=1,
                        command=dble_hit_1)
dble_hit_but_1.place(x=62, y=340)

dble_stay_but_1 = Button(dble_frame,
                         text="Stay",
                         bg="white",
                         bd=1,
                         command=dble_stay_1)
dble_stay_but_1.place(x=20, y=380)

dble_double_but_1 = Button(dble_frame,
                           text="Double",
                           bg="white",
                           bd=1,
                           command=dble_double_1)
dble_double_but_1.place(x=90, y=380)


def dble_hit_2():
    global dble_play_2_ttl
    global dble_crd_hit_2
    dble_crd_hit_2 = random.randint(1,11)
    dble_play_2_ttl += dble_crd_hit_2
    print("Player 2 hit card: ", dble_crd_hit_2)
    print(dble_play_2_ttl, "\n")
    if dble_play_2_ttl == 21:
        print("Player 2 wins")
        dble_add_creds_2()
    if dble_play_2_ttl > 21:
        print("Player 2 is busted")
        dble_sub_creds_2()
        dble_play_1_v_deal()
    if dble_play_2_ttl < 21:
        print("Play on \n")
        dble_crd_check()


def dble_double_2():
    global dble_bets_2
    dble_bets_2 *= 2
    dble_bets_2_counter.set("Bets: ${:.2f}".format(dble_bets_2))
    dble_crd_check()


dble_hit_but_2 = Button(dble_frame,
                        text="Hit",
                        bg="white",
                        bd=1,
                        command=dble_hit_2)
dble_hit_but_2.place(x=583, y=340)

dble_stay_but_2 = Button(dble_frame,
                         text="Stay",
                         bg="white",
                         bd=1,
                         command=dble_crd_check)
dble_stay_but_2.place(x=540, y=380)

dble_double_but_2 = Button(dble_frame,
                           text="Double",
                           bg="white",
                           bd=1,
                           command=dble_double_2)
dble_double_but_2.place(x=610, y=380)

dble_hit_but_1.config(state=DISABLED)
dble_stay_but_1.config(state=DISABLED)
dble_double_but_1.config(state=DISABLED)
dble_hit_but_2.config(state=DISABLED)
dble_stay_but_2.config(state=DISABLED)
dble_double_but_2.config(state=DISABLED)


dble_rules_but = Button(dble_frame, text="Rules", bg="orange", bd=1)
dble_rules_but.place(x=580, y=430)


def dble_exit():
    dble_exit_win = Toplevel(root)

    dble_exit_but.config(state=DISABLED)

    def close_dble_exit():  # If either the back button or window is closed
        dble_exit_but.config(
            state=NORMAL)  # revert the single player button back to normal
        sngle_exit_win.destroy()

    dble_exit_win.protocol("WM_DELETE_WINDOW", partial(close_dble_exit))

    dble_exit_frame = Frame(dble_exit_win,
                             width=200,
                             height=100,
                             bg="lawngreen")
    dble_exit_frame.grid()

    dble_exit_text = Label(dble_exit_frame,
                            text="Are you sure?",
                            font="Times 14",
                            justify=CENTER,
                            bg="lawngreen")
    dble_exit_text.place(x=10, y=0)

    def dble_exit_y():
        sys.exit()

    dble_ext_y_but = Button(dble_exit_frame,
                             text="Yes",
                             font="Times 10",
                             bd=1,
                             command=dble_exit_y)
    dble_ext_y_but.place(x=20, y=50)

    dble_ext_n_but = Button(dble_exit_frame,
                             text="No",
                             font="Times 10",
                             bd=1,
                             command=close_dble_exit)
    dble_ext_n_but.place(x=130, y=50)


dble_exit_but = Button(dble_frame,
                        text="Exit",
                        bg="orange",
                        bd=1,
                        command=dble_exit)
dble_exit_but.place(x=589, y=460)


root.mainloop()  # Loops the program until stopped/exited
