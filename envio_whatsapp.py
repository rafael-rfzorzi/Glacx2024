import webbrowser
from tkinter import *
from tkcalendar import *
import datetime
import calendar
import pyautogui as pg
from tkinter import ttk
import pyautogui
from tkinter import messagebox
import sqlite3

class Whats_envio():
    def __init__(self):
        pass
    def whats_tela(self):
        self.janelaSms = Toplevel(self.window_one)
        self.janelaSms.title("Mensagens Whatsapp")
        self.janelaSms.geometry("1000x750+70+30")
        self.janelaSms.resizable(FALSE, FALSE)

        self.janelaSms.transient(self.window_one)
        self.janelaSms.focus_force()
        self.janelaSms.grab_set()

        label_principal = Label(self.janelaSms, text="Mensagem Whatsapp")
        label_principal.place(relx=0.3, rely=0, relwidth=0.4, relheight=0.05)

        nome_frame = Label(self.janelaSms, text="Selecione a Data")
        nome_frame.place(relx=0.05, rely=0.05, relwidth=0.2, relheight=0.05)

        def busca_clienteWhats():
            self.nome_entry.delete(*self.nome_entry.get_children())

            self.conecta_Glac()
            self.lista1 = self.cursor.execute(
                """SELECT placa_orc, nome, fone1ddd, fone1  FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND dia = '%s'; """ % (
                    str(self.data_envio.get_date())))

            for i in self.lista1:
                self.nome_entry.insert("", END, values=i)
            self.desconecta_Glac()

        def envia_mensagemWhats():
            import time
            from datetime import datetime

            self.conecta_Glac()
            self.lista1 = self.cursor.execute("""SELECT  tabx, taby, intervalo1, intervalo2, 
                            x_campotexto, y_campotexto FROM whats_bot WHERE  id_whats = 1; """)
            for i in self.lista1:
                tabx = i[0]
                taby = i[1]
                intervalo1 = i[2]
                intervalo2 = i[3]
                xtexto = i[4]
                ytexto = i[5]
            self.desconecta_Glac()


            self.conecta_Glac()
            self.lista3 = self.cursor.execute(
                """SELECT placa_orc, nome, fone1ddd, fone1, dia  FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND dia = '%s'; """
                % (str(self.data_envio.get_date())))
            for x in self.lista3:
                cliente = str(x[1]).split()[0]
                dia_agenda = str(x[4])

                self.telefone = str(x[2]) + str(x[3])
                self.telefone = self.telefone.replace("-", "")
                contatos = "+55" + str(self.telefone)
                mensagem = self.mensagem_entry.get("1.0", END)
                mensagem = str(mensagem).replace("{cliente}", cliente).replace("{dia_agenda}", dia_agenda)
                webbrowser.open_new(url=f"https://web.whatsapp.com/send?phone={contatos}&text={mensagem}")
                time.sleep(intervalo1)
                pg.moveTo(xtexto, ytexto)
                pg.leftClick()
                pg.press("enter")
                time.sleep(intervalo2)
                pg.moveTo(tabx, taby)
                pg.leftClick()
            pyautogui.keyDown('alt')
            time.sleep(.2)
            pyautogui.press('tab')
            time.sleep(.2)
            pyautogui.keyUp('alt')

            messagebox.showinfo("Agenda", "Mensagens enviadas")

            self.desconecta_Glac()

        def dataenvio(event):
            busca_clienteWhats()

        self.data_envio = Calendar(self.janelaSms, text="Código", locale="pt")
        self.data_envio.place(relx=0.05, rely=0, relwidth=0.3, relheight=0.22)
        self.data_envio.bind('<<CalendarSelected>>', dataenvio)

        self.barracliente = ttk.Scrollbar(self.janelaSms, orient='vertical')  # , command=self.OnVsbC)
        self.nome_entry = ttk.Treeview(self.janelaSms, height=6,
                                       yscrollcommand=self.barracliente.set, column=("col1", "col2", "col3", "col4"))

        self.nome_entry.heading("#0", text="")
        self.nome_entry.column("#0", width=-10)
        self.nome_entry.heading("#1", text="Hora")
        self.nome_entry.column("#1", width=30)
        self.nome_entry.heading("#2", text="Nome")
        self.nome_entry.column("#2", width=70)
        self.nome_entry.heading("#3", text="DDD")
        self.nome_entry.column("#3", width=15)
        self.nome_entry.heading("#4", text="Fone")
        self.nome_entry.column("#4", width=70)

        self.nome_entry.place(relx=0.03, rely=0.25, relwidth=0.34, relheight=0.7)
        # self.listaServ.configure(yscroll=self.barracliente.set)
        # self.barracliente.place(relx=0.75, rely=0.25, relheight=0.75)


        label_msg = Label(self.janelaSms, text="Digite a mensagem")
        label_msg.place(relx=0.55, rely=0.1, relwidth=0.2, relheight=0.05)

        self.mensagem_entry = Text(self.janelaSms)
        self.mensagem_entry.place(relx=0.4, rely=0.15, relwidth=0.5, relheight=0.4)

        self.conecta_Glac()
        self.lista1 = self.cursor.execute("""SELECT  texto1, texto2, texto3 FROM config_sms; """)
        for i in self.lista1:
            i = i[1]
            i = str(i)
            self.mensagem_entry.insert(END, i.replace("/", "").replace("(", "").replace(")", "").replace("'", ""))
        self.desconecta_Glac()

        salvar_bt = Button(self.janelaSms, text="Enviar", command=envia_mensagemWhats)
        salvar_bt.place(relx=0.55, rely=0.6, relwidth=0.2)
        
        self.avisoframe = Frame(self.janelaSms)

        sair_bt = Button(self.janelaSms, text="Sair", command=self.janelaSms.destroy)
        sair_bt.place(relx=0.7, rely=0.8, relwidth=0.2)
        
        def sms_config():
            def atualiza_infos():
                self.conecta_Glac()
                self.cursor.execute(""" UPDATE whats_bot SET tabx = ?, taby = ?, intervalo1 = ?, intervalo2 = ?,
                    x_campotexto = ?, y_campotexto = ?""",
                                    (self.tabx_entry.get(), self.taby_entry.get(), self.intervalo1_entry.get(), self.intervalo2_entry.get(), self.xtexto_entry.get(), self.ytexto_entry.get()))
                self.conn.commit()
                self.desconecta_Glac()


                messagebox.showinfo("Agenda ", "Dados alterados com sucesso")
                self.janelaSms.destroy()

            self.open_win_cli2 = "cadcli"
            self.janelasmsconfig = Toplevel(self.janelaSms)
            self.janelasmsconfig.title("Config Robô")
            self.janelasmsconfig.geometry("600x300+70+30")
            self.janelasmsconfig.resizable(FALSE, FALSE)
            self.janelasmsconfig.transient(self.janelaSms)
            self.janelasmsconfig.focus_force()
            # self.janelasmsconfig.grab_set()

            Aba_frame = Label(self.janelasmsconfig, text="Coordenadas para fechar aba", bg="gray55")
            Aba_frame.place(relx=0.05, rely=0.1, relwidth=0.35, relheight=0.1)

            tabx_frame = Label(self.janelasmsconfig, text="X")
            tabx_frame.place(relx=0.1, rely=0.2, relwidth=0.1, relheight=0.1)

            self.tabx_entry = Entry(self.janelasmsconfig)
            self.tabx_entry.place(relx=0.1, rely=0.3, relwidth=0.1, relheight=0.1)

            taby_frame = Label(self.janelasmsconfig, text="Y")
            taby_frame.place(relx=0.25, rely=0.2, relwidth=0.1, relheight=0.1)

            self.taby_entry = Entry(self.janelasmsconfig)
            self.taby_entry.place(relx=0.25, rely=0.3, relwidth=0.1, relheight=0.1)

            intervalos_frame = Label(self.janelasmsconfig, text="Intervalos", bg="gray55")
            intervalos_frame.place(relx=0.45, rely=0.1, relwidth=0.35, relheight=0.1)

            intervalo1_frame = Label(self.janelasmsconfig, text="Intervalo 1")
            intervalo1_frame.place(relx=0.5, rely=0.2, relwidth=0.1, relheight=0.1)

            self.intervalo1_entry = Entry(self.janelasmsconfig)
            self.intervalo1_entry.place(relx=0.5, rely=0.3, relwidth=0.1, relheight=0.1)

            intervalo2_frame = Label(self.janelasmsconfig, text="Intervalo 2")
            intervalo2_frame.place(relx=0.65, rely=0.2, relwidth=0.1, relheight=0.1)

            self.intervalo2_entry = Entry(self.janelasmsconfig)
            self.intervalo2_entry.place(relx=0.65, rely=0.3, relwidth=0.1, relheight=0.1)

            campo_frame = Label(self.janelasmsconfig, text="Coordenadas para campo texto", bg="gray55")
            campo_frame.place(relx=0.05, rely=0.5, relwidth=0.35, relheight=0.1)

            xtexto_frame = Label(self.janelasmsconfig, text="X")
            xtexto_frame.place(relx=0.1, rely=0.6, relwidth=0.1, relheight=0.1)

            self.xtexto_entry = Entry(self.janelasmsconfig)
            self.xtexto_entry.place(relx=0.1, rely=0.7, relwidth=0.1, relheight=0.1)

            ytexto_frame = Label(self.janelasmsconfig, text="Y")
            ytexto_frame.place(relx=0.25, rely=0.6, relwidth=0.1, relheight=0.1)

            self.ytexto_entry = Entry(self.janelasmsconfig)
            self.ytexto_entry.place(relx=0.25, rely=0.7, relwidth=0.1, relheight=0.1)

            self.conecta_Glac()
            self.lista1 = self.cursor.execute("""SELECT  tabx, taby, intervalo1, intervalo2, 
                x_campotexto, y_campotexto FROM whats_bot WHERE  id_whats = 1; """)
            for i in self.lista1:
                self.tabx_entry.insert(END, i[0])
                self.taby_entry.insert(END, i[1])
                self.intervalo1_entry.insert(END, i[2])
                self.intervalo2_entry.insert(END, i[3])
                self.xtexto_entry.insert(END, i[4])
                self.ytexto_entry.insert(END, i[5])
            self.desconecta_Glac()

            salvar_bt = Button(self.janelasmsconfig, text="Atualiza infos", command=atualiza_infos)
            salvar_bt.place(relx=0.5, rely=0.6, relwidth=0.21, relheight=0.1)

            sair_bt = Button(self.janelasmsconfig, text="Sair", command=self.janelasmsconfig.destroy)
            sair_bt.place(relx=0.5, rely=0.78, relwidth=0.15, relheight=0.1)

            self.janelasmsconfig.mainloop()

        cfg_bt = Button(self.janelaSms, text="Configurar Robô", command=sms_config)
        cfg_bt.place(relx=0.4, rely=0.8, relwidth=0.2)


        self.janelaSms.mainloop()
