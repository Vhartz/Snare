#!/bin/usr/python
"""author : Vitor Amorim 'Vhartz' <vhartzamorimg2@gmail.com>
   version : 0.1
   license : Mit License
"""
from tkinter import *
from time import strftime as time
import os

# função de janela de seleção
def selection_modules():
    select = Tk()
    select.title("Home")
    select.geometry("300x300")
    select.resizable(False,False)
    #select.configure(background='')

    # função exit da tela de seleção
    def logout_exit():
        select.destroy()

    lbl_welcome =Label(select, text="Bem-Vindo Vitor Amorim",  font='Times 20 bold italic')
    lbl_welcome.pack(side=TOP)

    #setando atualização do relogio
    def tictac():
        new = time("%H:%M:%S")
        if rlg['text'] != new:
            rlg['text'] = new
        rlg.after(100,tictac)

    #  label do relogio
    rlg = Label(select, text=time("%H:%M:%S"), font='Times 15 bold')
    rlg.pack(side=TOP)

    # inicializção do pkg helper 
    def pkg_h():
        import pkg_helper

    pkg_helper = Button(select, text="Pkg Helper", font=('arial',9,'bold'), command = pkg_h)
    pkg_helper.pack(side=TOP, padx=10, pady=10)

    def arch_time():
        os.system("")

    set_time = Button(select, text="Time Arch Update", font=('arial',9,'bold'), command = arch_time)
    set_time.pack(side=TOP, padx=10, pady=10)

    logout = Button(select, text="Logout", font=('arial',9,'bold'), command = logout_exit)
    logout.pack(side=BOTTOM, padx=10, pady=10)

    tictac()
    select.mainloop()
###################################------------------------########################################         

# função de login
def iniciar():
    login_base = Tk()
    login_base.title('Login Snake')
    login_base.geometry("200x180")
    login_base.resizable(False,False)
    #login_base.configure(background='#858585')
    #login_base.iconbitmap(r':C:\Users\Vitor Amorim\Google Drive\Python\Snare\icon\icon_login_base.ico')
   
    # função exit do login
    def exit():
        login_base.destroy()
    #verification user and passwd
    def ent():
        usr = str(user.get())
        pswd = str(passwd.get())
        if usr == 'admin' and pswd == 'admin':
            print("Started Sucessfull")
            selection_modules()
            login_base.destroy()

    lb1 = Label(text='Login', font='Times 15 bold italic' )
    lb1.pack(side=TOP)

    lb2 = Label(text='Usurario')
    lb2.pack(side=TOP)

    user = Entry()
    user.pack(side=TOP)

    lb3 = Label(text='Senha')
    lb3.pack(side=TOP)

    passwd = Entry(show='*')
    passwd.pack(side=TOP)

    enter = Button(text='Entrar', command = ent)
    enter.pack(side=LEFT, pady=10, padx=30)
    
    exi = Button(text='Sair', command = exit)
    exi.pack(side=RIGHT, pady=10 ,padx=30)

    login_base.mainloop()
########################################---------------------------------#####################################

iniciar()