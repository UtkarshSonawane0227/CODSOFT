import tkinter
from tkinter import *
from tkinter import messagebox
import random


root=Tk()
root.title("Quiz Game Application")
root.geometry("570x600+100+200")
root.resizable(False,False)
root.configure(bg="#17161b")
task_list = []

#icon
Image_icon = PhotoImage(file = "quiz.png")
root.iconphoto(False,Image_icon)
questions = [
    {
        'question': 'What is the chemical symbol for gold?',
        'options': ['a) Ag', 'b) Au', 'c) Go' , 'd) Gl'],
        'answer': 'b) Au'
    },
    {
        'question': ' What is the largest organ in the human body ?',
        'options': ['a) Heart', 'b) Brain', 'c) Skin','d) Liver'],
        'answer': 'c) Skin'
    },
    {
        'question': ' What is the tallest mountain in the world ?',
        'options': ['a) Mount Kilimanjaro', 'b) Mount Everest', 'c) Mount McKinley','d) Mount Fuji'],
        'answer': 'b) Mount Everest'
    },
     {
        'question': ' What is the symbol for the chemical element oxygen ?',
        'options': ['a) O', 'b) Ox', 'c) Oz','d) On'],
        'answer': 'a) O'
    },
    {
        'question': ' Which gas do humans breathe in ?',
        'options': ['a) Oxygen', 'b) Carbon Dioxide', 'c) Nitrogen','d)Helium'],
        'answer': 'a) Oxygen'
    },
    {
        
        'question': '   What is the largest planet in our solar system ?',
        'options': ['a) Venus', 'b) Mars', 'c) Jupiter','d) Saturn'],
        'answer': 'c) Jupiter'
    },
    {
        'question': ' What is the chemical symbol for water ?',
        'options': ['a)  H2O', 'b) CO2', 'c) O2','d) N2'],
        'answer': 'a) H2O'
    },
    
   {
        'question': ' Which planet is known as the "Blue Planet" ?',
        'options': ['a)  Venus', 'b) Earth', 'c)  Uranus','d) Neptune'],
        'answer': 'b) Earth'
    },
   
   {
        'question': ' What is the smallest prime number?',
        'options': ['a) 1', 'b) 2', 'c) 3','d) 4'],
        'answer': 'b) 2'
    },
   {
        'question': ' Which gas is most abundant in Earth s atmosphere ?',
        'options': ['a) Oxygen', 'b) Nitrogen','c) Carbon Dioxide','d) Hydrogen'],
        'answer': 'b) Nitrogen'
    },
]

score = 0
question_number = 0
current_question = None

def show_question():
    global current_question, question_number, score
    if question_number < 10:
        if not questions:
            play_again = messagebox.askyesno("Game Over", f"Your Total Score: {score}\nDo you want to play again?")
            if play_again:
                score = 0
                question_number = 0
                questions[:] = [q for q in questions_backup]
                show_question()
            else:
                root.destroy()
        else:
            current_question = random.choice(questions)
            question_label.config(text=current_question['question'])

            val1.set(0)
            val2.set(0)
            val3.set(0)
            val4.set(0)

            option1.config(text=current_question['options'][0])
            option2.config(text=current_question['options'][1])
            option3.config(text=current_question['options'][2])
            option4.config(text=current_question['options'][3])

            question_number += 1
            questions.remove(current_question)
    else:
        play_again = messagebox.askyesno("Game Over", f"Your Total Score: {score}\nDo you want to play again?")
        if play_again:
            score = 0
            question_number = 0
            questions[:] = [q for q in questions_backup]
            show_question()
        else:
            root.destroy()

def check_answer():
    global score
    user_answer = ''
    if val1.get():
        user_answer = current_question['options'][0]
    elif val2.get():
        user_answer = current_question['options'][1]
    elif val3.get():
        user_answer = current_question['options'][2]
    elif val4.get():
        user_answer = current_question['options'][3]

    if user_answer == current_question['answer']:
        score += 1
        feedback_label.config(text="Correct!", fg="green")
    else:
        feedback_label.config(text="Incorrect! The correct answer is: " + current_question['answer'], fg="red")

    score_label.config(text="Score: " + str(score))
    show_question()

# root = Tk()
# root.title("Quiz Game Application")
# root.config(bg='skyblue')

question_frame = Frame(root)
question_frame.pack(pady=10)

question_label = Label(question_frame, font=("High Tower Text", 12))
question_label.pack()

val1 = IntVar()
val2 = IntVar()
val3 = IntVar()
val4 = IntVar()
option_frame = Frame(root)
option_frame.pack(pady=5)

option1 = Checkbutton(option_frame, variable=val1, text='Option1')
option1.pack(side=LEFT, padx=5)
option2 = Checkbutton(option_frame, variable=val2, text='Option2')
option2.pack(side=LEFT, padx=5)
option3 = Checkbutton(option_frame, variable=val3, text='Option3')
option3.pack(side=LEFT, padx=5)
option4 = Checkbutton(option_frame, variable=val4, text='Option3')
option4.pack(side=LEFT, padx=5)

submit_button = Button(root, command=check_answer, text="Submit", 
                     font=("Book Antiqua", 15), bg='#E3CF57', fg='black')
submit_button.pack(pady=10)

feedback_label = Label(root, font=("Bookman Old Style", 12))
feedback_label.pack()

score_label = Label(root, font=("Bookman Old Style", 12))
score_label.pack()

# Make a backup of the original questions to reset the game later
questions_backup = [q for q in questions]

show_question()

root.mainloop()
