from tkinter import *
import os

def pkg_base():
    pkg_window = Tk()
    pkg_window.title("PKG-HELPER")
    pkg_window.geometry("100x150")
    pkg_window.resizable(False,False)
    
    def pkg_arch():
        arch_pkg_window = Tk()
        arch_pkg_window.title("PKG HELPER")
        arch_pkg_window.geometry("250x200")
        arch_pkg_window.resizable(False,False)

        pkg_la = Label(arch_pkg_window, text='Pacote')
        pkg_la.pack(side=TOP)

        pkg_entrada = Entry(arch_pkg_window,)
        pkg_entrada.pack(side=TOP)

        def install():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo pacman -S %s'%(pct_enter))

        pkg_arch_buton = Button(arch_pkg_window, text='Instalar', command = install)
        pkg_arch_buton.pack(side=TOP, padx=10, pady=10)


        def remove():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo pacman -R %s -y'%(pct_enter))

        pkg_arch_buton2 = Button(arch_pkg_window, text='Remover', command = remove)
        pkg_arch_buton2.pack(side=TOP, padx=10, pady=10)

        def search():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo pacman -Ss %s'%(pct_enter))

        pkg_arch_buton3 = Button(arch_pkg_window, text='Procurar', command = search)
        pkg_arch_buton3.pack(side=TOP, padx=10, pady=10)

    bt_arch = Button(text='Arch', command = pkg_arch)
    bt_arch.pack(side=TOP, padx=10, pady=10)

    def pkg_debian():
        arch_pkg_window = Tk()
        arch_pkg_window.title("PKG HELPER")
        arch_pkg_window.geometry("250x200")
        arch_pkg_window.resizable(False,False)

        pkg_la = Label(arch_pkg_window, text='Pacote')
        pkg_la.pack(side=TOP)

        pkg_entrada = Entry(arch_pkg_window,)
        pkg_entrada.pack(side=TOP)

        def install():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo apt install %s'%(pct_enter))

        pkg_arch_buton = Button(arch_pkg_window, text='Instalar', command = install)
        pkg_arch_buton.pack(side=TOP, padx=10, pady=10)


        def remove():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo apt remove %s -y'%(pct_enter))

        pkg_arch_buton2 = Button(arch_pkg_window, text='Remover', command = remove)
        pkg_arch_buton2.pack(side=TOP, padx=10, pady=10)

        def search():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo cache search %s'%(pct_enter))

        pkg_arch_buton3 = Button(arch_pkg_window, text='Procurar', command = search)
        pkg_arch_buton3.pack(side=TOP, padx=10, pady=10)

    bt_debian = Button(text='Debian', command = pkg_debian)
    bt_debian.pack(side=TOP, padx=10, pady=10)

    def pkg_fedora():
        arch_pkg_window = Tk()
        arch_pkg_window.title("PKG HELPER")
        arch_pkg_window.geometry("250x200")
        arch_pkg_window.resizable(False,False)

        pkg_la = Label(arch_pkg_window, text='Pacote')
        pkg_la.pack(side=TOP)

        pkg_entrada = Entry(arch_pkg_window,)
        pkg_entrada.pack(side=TOP)

        def install():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo dnf install %s'%(pct_enter))

        pkg_arch_buton = Button(arch_pkg_window, text='Instalar', command = install)
        pkg_arch_buton.pack(side=TOP, padx=10, pady=10)


        def remove():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo dnf remove %s -y'%(pct_enter))

        pkg_arch_buton2 = Button(arch_pkg_window, text='Remover', command = remove)
        pkg_arch_buton2.pack(side=TOP, padx=10, pady=10)

        def search():
            pct_enter = str(pkg_entrada.get())
            os.system('sudo dnf search %s'%(pct_enter))

        pkg_arch_buton3 = Button(arch_pkg_window, text='Procurar', command = search)
        pkg_arch_buton3.pack(side=TOP, padx=10, pady=10)
    
    
    bt_fedora = Button(text='Fedora', command = pkg_fedora)
    bt_fedora.pack(side=TOP, padx=10, pady=10)

    pkg_window.mainloop()
    
pkg_base()

