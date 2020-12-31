import tkinter
top = tkinter.Tk()
import random

def new_password():
    character_array = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','!','£','$','/',1,2,3,4,5,6,7,8,9,0,]

    array_length = len(character_array)
    pass_length = 8

    password = []

    for i in range(0,8):
        value = random.randint(0,array_length-1)
        character = str(character_array[value])
        password.append(character)

    password_str = "".join(password)

    print(password_str)
B = tkinter.Button(top, text ="New Password", command = new_password)
B.pack()
top.mainloop()
