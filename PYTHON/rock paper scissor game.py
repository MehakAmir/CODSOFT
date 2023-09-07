from tkinter import *
import tkinter.font as font
import random

player_score = 0
computer_score = 0
options = [('rock',0), ('paper',1), ('scissors',2)]

def choice(player_input):
    global player_score, computer_score

    computer_input = get_computer_choice()

    player_choice_label.config(text = 'Your Selected : ' + player_input[0])
    computer_choice_label.config(text = 'Computer Selected : ' + computer_input[0])

    if(player_input == computer_input):
        winner_label.config(text = "Tie")
    elif((player_input[1] - computer_input[1]) % 3 == 1):
        player_score += 1
        winner_label.config(text="You Won!!!")
        player_score_label.config(text = 'Your Score : ' + str(player_score))
    else:
        computer_score += 1
        winner_label.config(text="Computer Won!!!")
        computer_score_label.config(text='Your Score : ' + str(computer_score))

def get_computer_choice():
    return random.choice(options)


game_window = Tk()
game_window.title("Rock Paper Scissors Game")
app_font = font.Font(size = 12)

game_title = Label(text = 'ROCK PAPER SCISSOR', font = font.Font(size = 22), fg = 'blue',pady=10)
game_title.pack()

winner_label = Label(text = "Let's Start the Game", fg = 'blue', font = font.Font(size = 18), pady = 10)
winner_label.pack()

input_frame = Frame(game_window)
input_frame.pack()

player_options = Label(input_frame, text = "Your Options : ", font = app_font, fg = 'blue')
player_options.grid(row = 0, column = 0, pady = 8)

rock_btn = Button(input_frame, text = 'Rock',font = font.Font(size = 15), width = 15, bd = 5, bg = 'light pink', pady = 10, command = lambda: choice(options[0]))
rock_btn.grid(row = 1, column = 1, padx = 8, pady = 10)

paper_btn = Button(input_frame, text = 'Paper',font = font.Font(size = 15), width = 15, bd = 5, bg = 'light green', pady = 10, command = lambda: choice(options[1]))
paper_btn.grid(row = 2, column = 1, padx = 8, pady = 10)

scissors_btn = Button(input_frame, text = 'Scissors',font = font.Font(size = 15) ,width = 15, bd = 5, bg = 'light yellow', pady = 10, command = lambda: choice(options[2]))
scissors_btn.grid(row = 3, column = 1, padx = 8, pady = 10)

score_label = Label(input_frame, text = 'Score : ', font = app_font,fg='blue')
score_label.grid(row = 4, column = 0)

player_choice_label = Label(input_frame, text = 'Your Selected : ---', font = app_font)
player_choice_label.grid(row = 4, column = 1, pady = 10)

player_score_label = Label(input_frame, text = 'Your Score : -', font = app_font)
player_score_label.grid(row = 5, column = 1, pady = 10)

computer_choice_label = Label(input_frame, text = 'Computer Selected : ---', font = app_font, fg = 'black')
computer_choice_label.grid(row = 6, column = 1, pady = 6)

computer_score_label = Label(input_frame, text = 'Computer Score : -', font = app_font, fg = 'black')
computer_score_label.grid(row = 7, column = 1, padx = (10,0), pady = 6)

game_window.geometry('800x600')
game_window.mainloop()

