#!/usr/bin/python
"""
    author : Vitor Amorim 'Vhartz' <vhartzamorimg2@gmail.com>
    version : 0.1
    license : Mit License
"""
from tkinter import *
from time import strftime as time
import os
import subprocess

def selection_modules():
    select = Tk()
    select.title("Home")
    select.geometry("300x400")
    select.resizable(False,False)
    #select.configure(background='')

    # exit
    def logout_exit():
        select.destroy()

    lbl_welcome =Label(select, text="Bem-Vindo Vitor Amorim",  font='Times 20 bold italic')
    lbl_welcome.pack(side=TOP)

    #set update time
    def tictac():
        new = time("%H:%M:%S")
        if rlg['text'] != new:
            rlg['text'] = new
        rlg.after(100,tictac)

    #  label for time
    rlg = Label(select, text=time("%H:%M:%S"), font='Times 15 bold')
    rlg.pack(side=TOP)

    #  pkg helper
    def pkg_h():
        import pkg_helper

    pkg_helper = Button(select, text="Pkg Helper", font=('arial',9,'bold'), command = pkg_h)
    pkg_helper.pack(side=TOP, padx=10, pady=10)

    def arch_time():
        os.system("hwclock --systohc --localtime")

    set_time = Button(select, text="Time Arch Update", font=('arial',9,'bold'), command = arch_time)
    set_time.pack(side=TOP, padx=10, pady=10)

    #teste de internet
    def speed():
        os.system('speedtest')

    speed_test = Button(select, text='Speed Test', font=('arial',9,'bold'), command = speed)
    speed_test.pack(side=TOP, padx=10, pady=10)
    #open studio code
    def code():
        os.system("/opt/visual-studio-code/code '%f'")

    studio_code = Button(select, text='Studio Code', font=('arial',9,'bold'), command = code )
    studio_code.pack(side=TOP, padx=10, pady=10)
    # dd command

    def dd_comand():
        window_dd = Tk()
        window_dd.title('Criação de ISO Inicializavel')
        window_dd.geometry("300x200")
        window_dd.resizable(False,False)

        lbl0 = Label(window_dd, text='Insira o Caminho da ISO :', font='Times 11 bold ' )
        lbl0.pack(side=TOP, padx=10, pady=5)

        dd_insert = Entry(window_dd, width=40)
        dd_insert.pack(side=TOP, padx=10, pady=5)

        lblex1 = Label(window_dd, text='ex : /local/da/imagem.iso')
        lblex1.pack(side=TOP, padx=5, pady=0)

        lbl1 = Label(window_dd, text='Insira a Unidade a ser Gravada :', font='Times 11 bold ' )
        lbl1.pack(side=TOP, padx=10, pady=5)

        dd_insertt = Entry(window_dd, width=40)
        dd_insertt.pack(side=TOP, padx=10, pady=5)

        lblex2 = Label(window_dd, text='ex : /dev/sdX')
        lblex2.pack(side=TOP, padx=5, pady=0)

        def gravar():
            first = str(dd_insert.get())
            second = str(dd_insertt.get())

            window_sub = Tk()
            window_sub.title('Progresso')
            #window_sub.geometry("200x200")
            sub = subprocess.check_output('sudo dd if=%s of=%s bs=4M status=progress' %(first,second), shell = True)

            lb = Label(window_sub, text=sub)
            lb.pack(side=TOP, padx=10, pady=10)

            window_sub.mainloop()

        lbl2 = Button(window_dd, text='Gravar!', command = gravar)
        lbl2.pack(side=TOP, padx=10, pady=5)

        window_dd.mainloop()

    comand_dd = Button(select, text='DD', font=('arial',9,'bold'), command = dd_comand)
    comand_dd.pack(side=TOP, padx=10, pady=10)

    logout = Button(select, text="Logout", font=('arial',9,'bold'), command = logout_exit)
    logout.pack(side=BOTTOM, padx=10, pady=10)

    tictac()
    select.mainloop()

# login
def iniciar():
    login_base = Tk()
    login_base.title('Login Snake')
    login_base.geometry("200x180")
    login_base.resizable(False,False)
    #login_base.configure(background='#858585')
    #login_base.iconbitmap(r':')

    # exit
    def exit():
        login_base.destroy()
    #verification user and passwd
    def ent():
        usr = str(user.get())
        pswd = str(passwd.get())
        if usr == 'admin' and pswd == 'admin':
            print("Started Sucessfull")
            selection_modules()
            #login_base.destroy()
        else:
            print('User or passwd error')
        exit()

    lb1 = Label(text='Login', font='Times 15 bold italic' )
    lb1.pack(side=TOP)

    lb2 = Label(text='Usuario')
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
