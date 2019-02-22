from tkinter import *
from time import strftime as time

def selection_modules():
    select = Tk()
    select.title("Select")
    select.geometry("300x300")
    select.resizable(False,False)
    #select.configure(background='')
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

    rlg = Label(select, text=time("%H:%M:%S"), font='Times 15 bold')
    rlg.pack(side=TOP)

    logout = Button(select, text="Logout", font=('arial',9,'bold'), command = logout_exit)
    logout.pack(side=BOTTOM, padx=10, pady=10)

    tictac()
    select.mainloop()
         
def iniciar():
    login_base = Tk()
    login_base.title('Login Snake')
    login_base.geometry("200x180")
    login_base.resizable(False,False)
    #login_base.configure(background='####')
   
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

iniciar()