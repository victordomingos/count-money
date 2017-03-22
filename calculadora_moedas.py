from tkinter import *
from tkinter import font
from tkinter import ttk
from tkinter import messagebox

__app_name__ = "Contar Dinheiro"
__author__ = "Victor Domingos"
__copyright__ = "Copyright 2016 Victor Domingos"
__license__ = "Attribution-ShareAlike 4.0 International (CC BY-SA 4.0)"
__version__ = "v.0.5 beta"
__status__ = "Beta"


class calc_window:
    def __init__(self, master):
        self.master = master
        jan_w = 230
        jan_h = 430
        min_w = 230
        min_h = 430
        default_position_x = 1050
        default_position_y = 0
        
        if __name__ == "__main__":
            position_x = 0
            position_y = 0
        else:
            position_x = default_position_x
            position_y = default_position_y

                
        self.notas = {"500": 1,
                 "200": 2,
                 "100": 3,
                 "50":  7,
                 "20":  24,
                 "10":  43,
                 "5":   9
                }
                
        self.moedas = {"2.00": 13,
                  "1.00": 9,
                  "0.50": 16,
                  "0.20": 14,
                  "0.10": 11,
                  "0.05": 9,
                  "0.02": 15,
                  "0.01": 9,
                 }
        self.soma_notas = 0
        self.soma_moedas = 0
        self.total = 0
        self.str_soma_notas = StringVar()
        self.str_soma_moedas = StringVar()
        self.str_total = StringVar()
        
        self.str_n500 = StringVar()
        self.str_n200 = StringVar()
        self.str_n100 = StringVar()
        self.str_n50 = StringVar()
        self.str_n20 = StringVar()
        self.str_n10 = StringVar()
        self.str_n5 = StringVar()
        self.str_m200 = StringVar()
        self.str_m100 = StringVar()
        self.str_m50 = StringVar()
        self.str_m20 = StringVar()
        self.str_m10 = StringVar()
        self.str_m5 = StringVar()
        self.str_m2 = StringVar()        
        self.str_m1 = StringVar()
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

        print("\n - A iniciar a calculadora de notas e moedas...")

        janelaCalc = Toplevel()
        janelaCalc.title("Contar dinheiro")

        janelaCalc.configure(background='grey92')

        janelaCalc.update_idletasks()
        janelaCalc.geometry("{}x{}+{}+{}".format(jan_w, jan_h, position_x, position_y))
        janelaCalc.minsize(min_w, min_h)
        janelaCalc.maxsize(min_w, min_h)
        pframe_topo = ttk.Frame(janelaCalc, padding="5 0 5 0")
        pframe_meio = ttk.Frame(janelaCalc, padding="0 5 0 0")
        pframe_fundo = ttk.Frame(janelaCalc, padding="0 0 5 5")
        pframe_limpar = ttk.Frame(janelaCalc, padding="5 10 5 10")
        lbl_frame1 = ttk.Labelframe(pframe_meio, pad="5", labelanchor="s")

        appfont = font.Font(size=16, weight='bold')
        labelfont = font.Font(size=12)
        copyfont = font.Font(size=10)
        titlefont = font.Font(size=14, weight='bold')
        totalfont = font.Font(size=24, weight='bold')
        
        #---------- TOPO -----------
#        app_lbl = ttk.Label(pframe_topo, font=appfont, text="Contar dinheiro")

        #---------- MEIO -----------

        #---Esquerda
        ttk.Label(lbl_frame1, text="Notas:", font=titlefont).grid(row=1, column=1, columnspan=2)
        linha = 2
        for key in sorted(self.notas, key=int, reverse=True):
            ttk.Label(lbl_frame1, text=key+"€").grid(row=linha, column=1, sticky=E)
            linha += 1
        lbl_totn1 = ttk.Label(lbl_frame1, text="\nTotal notas: ")
        lbl_totn2 = ttk.Label(lbl_frame1, textvariable=self.str_soma_notas)
        lbl_totn1.grid(row=10,column=1, columnspan=2)
        lbl_totn2.grid(row=11,column=1, columnspan=2)

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
        #---Direita
        ttk.Label(lbl_frame1, text="Moedas:", font=titlefont).grid(row=1, column=4, columnspan=2)
        linha = 2
        for key in sorted(self.moedas, key=float, reverse=True):
            ttk.Label(lbl_frame1, text=key+"€").grid(row=linha, column=4, sticky=E)
            linha += 1
        lbl_totm1 = ttk.Label(lbl_frame1, text="\nTotal moedas: ")
        lbl_totm2 = ttk.Label(lbl_frame1, textvariable=self.str_soma_moedas)
        lbl_totm1.grid(row=10,column=4, columnspan=2)
        lbl_totm2.grid(row=11,column=4, columnspan=2)

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
       

        #---------- FUNDO -----------
        #copyright_lbl = ttk.Label(pframe_fundo, font=copyfont, text="\n\n\n© 2016 Victor Domingos")
        tot_str1 = "Total em numerário:"
        tot_lbl1 = ttk.Label(pframe_fundo, font=labelfont, text=tot_str1)
        tot_lbl2 = ttk.Label(pframe_fundo, font=totalfont, textvariable=self.str_total)
        limpar_btn = ttk.Button(pframe_limpar, text="Limpar", command=self.limpar)

        #app_lbl.pack()
        tot_lbl1.pack()
        tot_lbl2.pack()
        limpar_btn.pack()

        lbl_frame1.pack()
        #copyright_lbl.pack()
        pframe_topo.pack(side=TOP)
        pframe_meio.pack(side=TOP)
        pframe_limpar.pack(side=BOTTOM)
        pframe_fundo.pack(side=BOTTOM)
        lbl_n500.focus()
        
        pframe_topo.focus()
        self.update_contas()
        self.gerar_menu()
        janelaCalc.mainloop()


    def representsInt(self, s):
        try: 
            int(s)
            return True
        except ValueError as e:
            print("representsInt():", e)
            messagebox.showwarning("","Por favor verifique se introduziu corretamente os valores.")
            return False

    
    def converter(self, arg):
        texto = arg.get()
        
        if texto == "":
            return 0
        elif self.representsInt(texto):
            return int(texto)
        else:
            return 0


    def limpar(self):
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
        parcela = 0.0
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


    def gerar_menu(self):
        # Menu da janela principal
        self.menu = Menu(root)
        root.config(menu=self.menu)
        
        self.helpmenu = Menu(self.menu)
        self.menu.add_cascade(label="Help", menu=self.helpmenu)

        #self.helpmenu.add_command(label="Acerca de "+__app_name__, command=about_window)
        self.helpmenu.add_command(label="Suporte da aplicação "+__app_name__, command=lambda: webbrowser.open("http://victordomingos.com/contactos/", new=1, autoraise=True))
        #self.helpmenu.add_command(label="Agradecimentos", command=thanks_window)
        self.helpmenu.add_separator()
        self.helpmenu.add_command(label="Visitar página do autor", command=lambda: webbrowser.open("http://victordomingos.com", new=1, autoraise=True))
        #root.bind('<<about-idle>>', about_dialog)
        #root.bind('<<open-config-dialog>>', config_dialog)
        #root.createcommand('tkAboutDialog', about_window)
        
        
if __name__ == "__main__":
    root = Tk()
    root.withdraw()
    janela_calculadora = calc_window(root)
    janela_calculadora.resizable(width=False, heigth=False)
    janelaCalc.focus()
    root.mainloop()


