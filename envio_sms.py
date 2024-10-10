import tkinter.messagebox
from tkinter import *
from tkcalendar import *
import datetime
import calendar
import requests

from tkinter import ttk

class SMS_envio():
    def sms_tela(self):
        self.janelaSms = Toplevel(self.window_one)
        self.janelaSms.title("Mensagens SMS")
        self.janelaSms.geometry("1000x750+70+30")
        self.janelaSms.resizable(FALSE, FALSE)

        self.janelaSms.transient(self.window_one)
        self.janelaSms.focus_force()
        self.janelaSms.grab_set()


        def busca_clienteW():
            self.nome_entry.delete(*self.nome_entry.get_children())

            self.conecta_Glac()
            self.lista1 = self.cursor.execute("""SELECT placa_orc, nome, fone1ddd, fone1  FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND dia = '%s'; """ % (str(self.data_envio.get_date())))

            for i in self.lista1:
                self.nome_entry.insert("", END, values=i)
            self.desconecta_Glac()

        def envia_mensagemSms():
            import time
            from datetime import datetime

            self.conecta_Glac()
            self.lista1 = self.cursor.execute("""SELECT  texto1, texto2, texto3, texto4 FROM config_sms; """)
            for i in self.lista1:
                texto1 = i[0]
                texto2 = i[1]
                texto3 = i[2]
                texto4 = i[3]
                self.lista3 = self.cursor.execute("""SELECT placa_orc, nome, fone1ddd, fone1, dia  FROM orcamento1, clientes WHERE  cod_cli = cliente_orc AND dia = '%s'; """
                        % (str(self.data_envio.get_date())))
                for x in self.lista3:
                    cliente = str(x[1]).split()[0]
                    dia_agenda = str(x[4])

                    self.telefone = str(x[2]) + str(x[3])
                    self.telefone = self.telefone.replace("-", "")
                    msg1 = str(texto2).replace("/", "").replace("(", "").replace(")", "").replace("'", "").replace(
                        "{cliente}", cliente).replace("{dia_agenda}", dia_agenda)
                    msg1 = msg1[:140]
                    contatos = str(self.telefone)
                    http_sms = str('http://api.facilitamovel.com.br/api/simpleSend.ft?user=' + texto1
                                   + '&password=' + texto3 + '&destinatario=' + contatos + "&msg=" + msg1 + texto4)

                    requests.post(http_sms)
                    #r = requests.post(http_sms)

                    mensagem23.insert(0, dia_agenda + " - " +  str(cliente) + " - Mensagem enviada")

            self.desconecta_Glac()

        def dataenvio(event):
            busca_clienteW()

        self.data_envio = Calendar(self.janelaSms, text="Código", locale="pt")
        self.data_envio.place(relx=0.05, rely=0.05, relwidth=0.3, relheight=0.27)
        self.data_envio.bind('<<CalendarSelected>>', dataenvio)

        self.barracliente = ttk.Scrollbar(self.janelaSms, orient='vertical')  # , command=self.OnVsbC)
        self.nome_entry = ttk.Treeview(self.janelaSms, height=6, yscrollcommand=self.barracliente.set, column=("col1", "col2", "col3", "col4"))

        self.nome_entry.heading("#0", text="")
        self.nome_entry.column("#0", width=-10)
        self.nome_entry.heading("#1", text="Placa")
        self.nome_entry.column("#1", width=30)
        self.nome_entry.heading("#2", text="Nome")
        self.nome_entry.column("#2", width=120)
        self.nome_entry.heading("#3", text="DDD")
        self.nome_entry.column("#3", width=15)
        self.nome_entry.heading("#4", text="Fone")
        self.nome_entry.column("#4", width=50)

        self.nome_entry.place(relx=0.03, rely=0.35, relwidth=0.45, relheight=0.6)

        label_msg = Label(self.janelaSms, text="Digite a mensagem")
        label_msg.place(relx=0.65, rely=0.05, relwidth=0.2, relheight=0.05)

        self.mensagem_entry = Text(self.janelaSms)
        self.mensagem_entry.place(relx=0.5, rely=0.1, relwidth=0.45, relheight=0.2)

        mensagem23 = Listbox(self.janelaSms, height=8)
        mensagem23.place(relx=0.5, rely=0.45, relwidth=0.45)

        salvar_bt = Button(self.janelaSms, text="Enviar", command=envia_mensagemSms)
        salvar_bt.place(relx=0.65, rely=0.7, relwidth=0.2)

        self.conecta_Glac()
        self.lista1 = self.cursor.execute("""SELECT  texto1, texto2, texto3 FROM config_sms; """)
        for i in self.lista1:
            i = i[1]
            i = str(i)
            self.mensagem_entry.insert(END, i[:150].replace("/","").replace("(","").replace(")","").replace("'",""))
        self.desconecta_Glac()

        sair_bt = Button(self.janelaSms, text="Sair", command=self.janelaSms.destroy)
        sair_bt.place(relx=0.8, rely=0.8, relwidth=0.15)

        def sms_config():
            def atualiza_infos():
                self.conecta_Glac()
                self.cursor.execute(""" UPDATE config_sms SET texto1 = ?, texto2 = ?, texto3 = ?, texto4 = ? """,
                                    (self.user_entry.get(), self.sms_entry.get("1.0", END), self.senha_entry.get(), self.ha_entry.get()))
                self.conn.commit()
                self.desconecta_Glac()

                tkinter.messagebox.showinfo("Agenda ", "Dados alterados com sucesso")
                self.janelaSms.destroy()

            self.open_win_cli2 = "cadcli"
            self.janelasmsconfig = Toplevel(self.janelaSms)
            self.janelasmsconfig.title("Config SMS")
            self.janelasmsconfig.geometry("600x300+70+30")
            self.janelasmsconfig.resizable(FALSE, FALSE)
            self.janelasmsconfig.transient(self.janelaSms)
            self.janelasmsconfig.focus_force()
            # self.janelasmsconfig.grab_set()

            nome_frame = Label(self.janelasmsconfig, text="Texto a ser enviado")
            nome_frame.place(relx=0.05, rely=0, relwidth=0.7, relheight=0.1)

            self.sms_entry = Text(self.janelasmsconfig)
            self.sms_entry.place(relx=0.05, rely=0.1, relwidth=0.7, relheight=0.3)

            user_frame = Label(self.janelasmsconfig, text="Usuário:")
            user_frame.place(relx=0.05, rely=0.45, relwidth=0.2, relheight=0.1)

            self.user_entry = Entry(self.janelasmsconfig)
            self.user_entry.place(relx=0.25, rely=0.45, relwidth=0.4, relheight=0.1)

            senha_frame = Label(self.janelasmsconfig, text="Senha:")
            senha_frame.place(relx=0.05, rely=0.55, relwidth=0.2, relheight=0.1)

            self.senha_entry = Entry(self.janelasmsconfig, show="*")
            self.senha_entry.place(relx=0.25, rely=0.55, relwidth=0.4, relheight=0.1)

            ha_frame = Label(self.janelasmsconfig, text="Hash:")
            ha_frame.place(relx=0.05, rely=0.65, relwidth=0.2, relheight=0.1)

            self.ha_entry = Entry(self.janelasmsconfig)
            self.ha_entry.place(relx=0.25, rely=0.65, relwidth=0.4, relheight=0.1)

            self.conecta_Glac()
            self.lista1 = self.cursor.execute("""SELECT  texto2, texto1, texto3, texto4 FROM config_sms; """)
            for i in self.lista1:
                self.sms_entry.insert(END, i[0])
                self.user_entry.insert(END, i[1])
                self.senha_entry.insert(END, i[2])
                self.ha_entry.insert(END, i[3])
            self.desconecta_Glac()

            salvar_bt = Button(self.janelasmsconfig, text="Atualiza infos", command=atualiza_infos)
            salvar_bt.place(relx=0.75, rely=0.1, relwidth=0.21, relheight=0.1)

            sair_bt = Button(self.janelasmsconfig, text="Sair", command=self.janelasmsconfig.destroy)
            sair_bt.place(relx=0.81, rely=0.7, relwidth=0.15, relheight=0.1)

            self.janelasmsconfig.mainloop()

        cfg_bt = Button(self.janelaSms, text="Configurar", command=sms_config)
        cfg_bt.place(relx=0.5, rely=0.8, relwidth=0.15)

        self.janelaSms.mainloop()