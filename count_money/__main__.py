#!/usr/bin/env python3
# encoding: utf-8
import os
import webbrowser
import tkinter as tk
import gettext

from tkinter import font
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime


def init_language(lang_code='en'):
    global _
    localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'locale')
    translate = gettext.translation('count_money', localedir, fallback=True, languages=[lang_code])
    _ = translate.gettext


init_language('pt')


__app_name__ = _("Contar Dinheiro")
__author__ = "Victor Domingos"
__copyright__ = "Copyright 2019 Victor Domingos"
__license__ = "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)"
__status__ = "Beta"

ALL_BILLS = ["500", "200", "100", "50", "20", "10", "5"]
ALL_COINS = ["2.00", "1.00", "0.50", "0.20", "0.10", "0.05", "0.02", "0.01"]

DEFAULT_DIR = os.path.expanduser("~/")


class CalcWindow:
    def __init__(self, master):
        self.master = master
        jan_w = 230
        jan_h = 430
        min_w = 230
        min_h = 430
        self.notas = {n: 0 for n in ALL_BILLS}
        self.moedas = {n: 0 for n in ALL_COINS}
        self.soma_notas = 0
        self.soma_moedas = 0
        self.total = 0

        default_position_x = 0
        default_position_y = 0
        if __name__ == "__main__":
            position_x = 0
            position_y = 0
        else:
            position_x = default_position_x
            position_y = default_position_y

        self.str_soma_notas = tk.StringVar()
        self.str_soma_moedas = tk.StringVar()
        self.str_total = tk.StringVar()

        self.str_n500 = tk.StringVar()
        self.str_n200 = tk.StringVar()
        self.str_n100 = tk.StringVar()
        self.str_n50 = tk.StringVar()
        self.str_n20 = tk.StringVar()
        self.str_n10 = tk.StringVar()
        self.str_n5 = tk.StringVar()
        self.str_m200 = tk.StringVar()
        self.str_m100 = tk.StringVar()
        self.str_m50 = tk.StringVar()
        self.str_m20 = tk.StringVar()
        self.str_m10 = tk.StringVar()
        self.str_m5 = tk.StringVar()
        self.str_m2 = tk.StringVar()
        self.str_m1 = tk.StringVar()
        self.str_n500.trace("w", self.update_contas)
        self.str_n200.trace("w", self.update_contas)
        self.str_n100.trace("w", self.update_contas)
        self.str_n100.trace("w", self.update_contas)
        self.str_n50.trace("w", self.update_contas)
        self.str_n20.trace("w", self.update_contas)
        self.str_n10.trace("w", self.update_contas)
        self.str_n5.trace("w", self.update_contas)
        self.str_m200.trace("w", self.update_contas)
        self.str_m100.trace("w", self.update_contas)
        self.str_m50.trace("w", self.update_contas)
        self.str_m20.trace("w", self.update_contas)
        self.str_m10.trace("w", self.update_contas)
        self.str_m5.trace("w", self.update_contas)
        self.str_m2.trace("w", self.update_contas)
        self.str_m1.trace("w", self.update_contas)

        self.janelaCalc = tk.Toplevel()
        self.janelaCalc.title(__app_name__)

        self.janelaCalc.configure(background='grey92')

        self.janelaCalc.update_idletasks()
        self.janelaCalc.geometry("{}x{}+{}+{}".format(jan_w, jan_h, position_x, position_y))
        self.janelaCalc.minsize(min_w, min_h)
        self.janelaCalc.maxsize(min_w, min_h)
        pframe_topo = ttk.Frame(self.janelaCalc, padding="5 0 5 0")
        pframe_meio = ttk.Frame(self.janelaCalc, padding="0 5 0 0")
        pframe_fundo = ttk.Frame(self.janelaCalc, padding="0 0 5 5")
        pframe_limpar = ttk.Frame(self.janelaCalc, padding="5 10 5 10")
        lbl_frame1 = ttk.Labelframe(pframe_meio, pad="5", labelanchor="s")

        # appfont = font.Font(size=16, weight='bold')
        labelfont = font.Font(size=12)
        # copyfont = font.Font(size=10)
        titlefont = font.Font(size=14, weight='bold')
        totalfont = font.Font(size=24, weight='bold')

        # ---------- TOPO -----------
        #        app_lbl = ttk.Label(pframe_topo, font=appfont, text="Contar dinheiro")

        # ---------- MEIO -----------

        # ---Esquerda
        self.lbl_notas = ttk.Label(lbl_frame1, text=_("Notas:"), font=titlefont)
        self.lbl_notas.grid(row=1, column=1, columnspan=2)
        linha = 2
        for key in sorted(self.notas, key=int, reverse=True):
            ttk.Label(lbl_frame1, text=key + "€").grid(row=linha, column=1, sticky="e")
            linha += 1
        self.lbl_totn1 = ttk.Label(lbl_frame1, text=_("\nTotal notas: "))
        lbl_totn2 = ttk.Label(lbl_frame1, textvariable=self.str_soma_notas)
        self.lbl_totn1.grid(row=10, column=1, columnspan=2)
        lbl_totn2.grid(row=11, column=1, columnspan=2)

        lbl_n500 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_n500)
        lbl_n500.grid(row=2, column=2)
        lbl_n200 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_n200)
        lbl_n200.grid(row=3, column=2)
        lbl_n100 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_n100)
        lbl_n100.grid(row=4, column=2)
        lbl_n50 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_n50)
        lbl_n50.grid(row=5, column=2)
        lbl_n20 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_n20)
        lbl_n20.grid(row=6, column=2)
        lbl_n10 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_n10)
        lbl_n10.grid(row=7, column=2)
        lbl_n5 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_n5)
        lbl_n5.grid(row=8, column=2)

        lbl_espaco = ttk.Label(lbl_frame1, text=" ")
        lbl_espaco.grid(row=1, column=3)
        # ---Direita
        self.lbl_moedas = ttk.Label(lbl_frame1, text=_("Moedas:"), font=titlefont)
        self.lbl_moedas.grid(row=1, column=4, columnspan=2)
        linha = 2
        for key in sorted(self.moedas, key=float, reverse=True):
            ttk.Label(lbl_frame1, text=key + "€").grid(row=linha, column=4, sticky="e")
            linha += 1
        self.lbl_totm1 = ttk.Label(lbl_frame1, text=_("\nTotal moedas: "))
        lbl_totm2 = ttk.Label(lbl_frame1, textvariable=self.str_soma_moedas)
        self.lbl_totm1.grid(row=10, column=4, columnspan=2)
        lbl_totm2.grid(row=11, column=4, columnspan=2)

        lbl_m200 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m200)
        lbl_m200.grid(row=2, column=5)
        lbl_m100 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m100)
        lbl_m100.grid(row=3, column=5)
        lbl_m50 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m50)
        lbl_m50.grid(row=4, column=5)
        lbl_m20 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m20)
        lbl_m20.grid(row=5, column=5)
        lbl_m10 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m10)
        lbl_m10.grid(row=6, column=5)
        lbl_m5 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m5)
        lbl_m5.grid(row=7, column=5)
        lbl_m2 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m2)
        lbl_m2.grid(row=8, column=5)
        lbl_m1 = ttk.Entry(lbl_frame1, width=4, textvariable=self.str_m1)
        lbl_m1.grid(row=9, column=5)

        lbl_frame1.grid_columnconfigure(3, pad=5)
        lbl_frame1.grid_rowconfigure(1, pad=5)

        # ---------- FUNDO -----------
        # copyright_lbl = ttk.Label(pframe_fundo, font=copyfont, text="\n\n\n© 2016 Victor Domingos")
        tot_str1 = _("Total em numerário:")
        self.tot_lbl1 = ttk.Label(pframe_fundo, font=labelfont, text=tot_str1)
        tot_lbl2 = ttk.Label(pframe_fundo, font=totalfont, textvariable=self.str_total)
        self.limpar_btn = ttk.Button(pframe_limpar, text=_("Limpar"), command=self.limpar)
        self.guardar_btn = ttk.Button(pframe_limpar, text=_("Guardar…"), command=self.save_report)

        # app_lbl.pack()
        self.tot_lbl1.pack()
        tot_lbl2.pack()
        self.limpar_btn.pack(side="left", padx=4)
        self.guardar_btn.pack(side="right", padx=4)

        lbl_frame1.pack()
        # copyright_lbl.pack()
        pframe_topo.pack(side="top")
        pframe_meio.pack(side="top")
        pframe_limpar.pack(side="bottom")
        pframe_fundo.pack(side="bottom")
        lbl_n500.focus()

        pframe_topo.focus()
        self.update_contas()
        self.gerar_menu()
        self.janelaCalc.mainloop()

    @staticmethod
    def represents_int(s):
        try:
            int(s)
            return True
        except ValueError as e:
            print("represents_int():", e)
            messagebox.showwarning("", _("Por favor verifique se introduziu corretamente os valores."))
            return False

    def converter(self, arg):
        texto = arg.get()

        if texto == "":
            return 0
        elif self.represents_int(texto):
            return int(texto)
        else:
            return 0

    def limpar(self, *event):
        self.str_n500.set("")
        self.str_n200.set("")
        self.str_n100.set("")
        self.str_n50.set("")
        self.str_n20.set("")
        self.str_n10.set("")
        self.str_n5.set("")
        self.str_m200.set("")
        self.str_m100.set("")
        self.str_m50.set("")
        self.str_m20.set("")
        self.str_m10.set("")
        self.str_m5.set("")
        self.str_m2.set("")
        self.str_m1.set("")

    def update_contas(self, *event):
        self.notas["500"] = self.converter(self.str_n500)
        self.notas["200"] = self.converter(self.str_n200)
        self.notas["100"] = self.converter(self.str_n100)
        self.notas["50"] = self.converter(self.str_n50)
        self.notas["20"] = self.converter(self.str_n20)
        self.notas["10"] = self.converter(self.str_n10)
        self.notas["5"] = self.converter(self.str_n5)
        self.moedas["2.00"] = self.converter(self.str_m200)
        self.moedas["1.00"] = self.converter(self.str_m100)
        self.moedas["0.50"] = self.converter(self.str_m50)
        self.moedas["0.20"] = self.converter(self.str_m20)
        self.moedas["0.10"] = self.converter(self.str_m10)
        self.moedas["0.05"] = self.converter(self.str_m5)
        self.moedas["0.02"] = self.converter(self.str_m2)
        self.moedas["0.01"] = self.converter(self.str_m1)

        self.soma_notas = 0.0
        for key in self.notas:
            parcela = float(key) * float(self.notas[key])
            self.soma_notas += parcela

        self.soma_moedas = 0.0
        for key in self.moedas:
            parcela = float(key) * float(self.moedas[key])
            self.soma_moedas += parcela

        self.total = self.soma_notas + self.soma_moedas

        self.str_soma_notas.set("{:,.2f}€".format(float(self.soma_notas)).replace(',', ' '))
        self.str_soma_moedas.set("{:,.2f}€".format(float(self.soma_moedas)).replace(',', ' '))
        self.str_total.set(" {:,.2f}€".format(float(self.total)).replace(',', ' '))

    def save_report(self, *event):
        #try:
        with filedialog.asksaveasfile(initialdir=DEFAULT_DIR,
                                      mode="w",
                                      parent=self.janelaCalc) as f:
            txt = _("Contagem de Dinheiro\n")
            f.write(txt)
            f.write("=" * len(txt) + "\n")
            f.write("\n\n")
            f.write(_("Data: {}\n\n").format(str(datetime.now())[:-7]))
            f.write("\n")
            f.write(_("NOTAS:\n"))
            subtotal_notas = 0.0
            for bill_type in ALL_BILLS:
                face_value = float(bill_type)
                qtd = str(int(self.notas[bill_type]))
                line_total = float(face_value) * float(self.notas[bill_type])
                total = f"{line_total:.2f}€".rjust(10)
                f.write(f"{qtd.rjust(10)}  x {bill_type.rjust(4)}€  ={total}\n")
                subtotal_notas += line_total
            f.write(_("\nSubtotal: {:.2f}\n\n\n").format(subtotal_notas))

            f.write(_("MOEDAS:\n"))
            subtotal_moedas = 0.0
            #print(ALL_COINS)
            for coin_type in ALL_COINS:
                #print(coin_type, type(coin_type))
                face_value = float(coin_type)
                #print(face_value, type(face_value))
                qtd = str(int(self.moedas[coin_type]))
                line_total = float(face_value) * float(self.moedas[coin_type])
                total = f"{line_total:.2f}€".rjust(10)
                f.write(f"{qtd.rjust(10)}  x {coin_type.rjust(4)}€  ={total}\n")
                subtotal_moedas += line_total
            f.write(_("\nSubtotal: {:.2f}\n").format(subtotal_moedas))

            f.write("\n\n==========================\n\n")
            total_all = subtotal_notas + subtotal_moedas
            f.write(f"TOTAL: {total_all:.2f}\n")

        #except Exception as e:
        #    print(e)
        #    return

    def gerar_menu(self):
        # Menu da janela principal
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)

        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label=_("Ficheiro"), menu=self.filemenu)

        self.filemenu.add_separator()
        self.filemenu.add_command(label=_("Guardar relatório como…"),
                                  command=self.save_report,
                                  accelerator="Command+s")
        self.filemenu.add_command(label=_("Limpar todos os campos"),
                                  command=self.limpar,
                                  accelerator="Command+l")


        self.prefs_menu = tk.Menu(self.menu)
        self.menu.add_cascade(label=_("Preferências"), menu=self.prefs_menu)
        self.prefs_menu.add_command(label=_("English"),
                                  command=lambda: self.change_language('en'))
        self.prefs_menu.add_command(label=_("Português"),
                                  command=lambda: self.change_language('pt'))

        self.helpmenu = tk.Menu(self.menu)
        self.menu.add_cascade(label=_("Ajuda"), menu=self.helpmenu)
        self.helpmenu.add_command(label=_("Suporte da aplicação"),
                                  command=lambda: webbrowser.open("https://victordomingos.com/contactos/",
                                                                  new=1,
                                                                  autoraise=True))

        self.helpmenu.add_command(label=_("Visitar página do autor"),
                                  command=lambda: webbrowser.open("https://no-title.victordomingos.com",
                                                                  new=1,
                                                                  autoraise=True))


        self.master.bind_all("<Command-s>", self.save_report)
        self.master.bind_all("<Command-l>", self.limpar)


    def change_language(self, lang='en'):
        init_language(lang)
        self.menu.entryconfig(0, label=_("Ficheiro"))
        self.menu.entryconfig(1, label=_("Preferências"))
        self.menu.entryconfig(2, label=_("Ajuda"))

        self.filemenu.entryconfig(1, label=_("Guardar relatório como…"))
        self.filemenu.entryconfig(2, label=_("Limpar todos os campos"))

        self.helpmenu.entryconfig(0, label=_("Suporte da aplicação"))
        self.helpmenu.entryconfig(1, label=_("Visitar página do autor"))

        self.lbl_notas.config(text=_("Notas:"))
        self.lbl_totn1.config(text=_("\nTotal notas: "))
        self.lbl_moedas.config(text=_("Moedas:"))
        self.lbl_totm1.config(text=_("\nTotal moedas: "))
        self.tot_lbl1.config(text=_("Total em numerário:"))

        self.guardar_btn.config(text=_("Guardar…"))
        self.limpar_btn.config(text=_("Limpar"))


def main():
    root = tk.Tk()
    root.withdraw()
    janela_calculadora = CalcWindow(root)
    janela_calculadora.resizable(width=False, heigth=False)
    janela_calculadora.janelaCalc.focus()
    root.mainloop()


if __name__ == "__main__":
    main()

