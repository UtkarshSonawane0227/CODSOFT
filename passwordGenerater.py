import random, string
from tkinter import *
import pyperclip

root =Tk()
root.geometry("600x600+400+500")
root.title("Random Password Generator")
root.configure(bg="#17161b")
task_list = []

#icon
Image_icon = PhotoImage(file = "password.png")
root.iconphoto(False,Image_icon)


output_pass = StringVar()

characters = [string.punctuation, string.ascii_uppercase, string.digits, string.ascii_lowercase]  

def randPassGen():
    password = "" 
    for y in range(password_len.get()):
        char_type = random.choice(characters)  
        password+= random.choice(char_type)
    
    output_pass.set(password)

def copyPass():
    pyperclip.copy(output_pass.get())
def reset():
    name.set("")             
    output_pass.set("")      
    pyperclip.copy("")
    password_len.set("")

username= Label(root,text='Username',font= "Century 12 bold").place(x=100,y=20)
 
name= StringVar()
Entry(root , textvariable = name, width = 24, font='Century 18').place(x=100,y=50)

Button(root, text = "Enter username", font= "Century 10 ", 
          bg='#F0F8FF', fg='black', activebackground="teal", padx=5, pady=5 ).place(x=450,y=48)

pass_head = Label(root, text = 'Password Length', font = 'Century 12 bold').place(x=100,y=100)

password_len = IntVar() 
length = Spinbox(root, from_ = 8, to_ = 20, textvariable = password_len , width = 24, font= "Century 18").place(x=100,y=130)


Button(root, command = randPassGen, text = "Generate Password", font="Century 10", 
          bg='#F0F8FF', fg='black', activebackground="teal", padx=5, pady=5 ).place(x=450,y=128)

pass_label = Label(root, text = 'Random Generated Password', font = 'Century 12 bold').place(x=100,y=200)

Entry(root , textvariable = output_pass, width = 24, font= "Century 19").place(x=100,y=250)

Button(root, text = 'Copy to Clipboard', command = copyPass, font= "Century 10", 
          bg='#F0F8FF', fg='black', activebackground="teal", padx=5, pady=5 ).place(x=450,y=250)


Button(root, command=reset, text = "Reset", font="Century 10", 
          bg='#F0F8FF', fg='black', activebackground="teal", padx=5, pady=5 ).place(x=250,y=430)
root.mainloop()  
