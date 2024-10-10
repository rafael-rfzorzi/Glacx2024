import customtkinter
from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class CadServ:
    def cadserv(self):
        self.janelaServ = customtkinter.CTkToplevel()
        self.janelaServ.title("Serviços")
        self.janelaServ.geometry("960x380+10+130")
        self.janelaServ.resizable(FALSE, FALSE)
        self.janelaServ.transient(self.window_one)
        self.janelaServ.focus_force()

        descrCod = customtkinter.CTkLabel(self.janelaServ, text="Codigo")
        descrCod.place(x=10, y=15)

        self.entradaCod = customtkinter.CTkEntry(self.janelaServ)
        self.entradaCod.place(x=80, y=15, relwidth=0.05)

        ###  Botao Carrega servico
        botaoAdd = ButtonGlac(self.janelaServ, "Carregar", self.carrega_servicoS)
        botaoAdd.place(x=145, y=15, width=130, height=35)

        ###  Botao limpa servico
        botaolimpa = ButtonGlac(self.janelaServ, "Limpar", self.limpa_servicoS)
        botaolimpa.place(x=275, y=15, width=70, height=35)

        descrServ = customtkinter.CTkLabel(self.janelaServ, text="Serviços")
        descrServ.place(x=10, y=60)

        self.entradaServ = customtkinter.CTkEntry(self.janelaServ)
        self.entradaServ.place(x=80, y=60, relwidth=0.35)

        ###  Botao busca SERVICO
        botaolimpa = ButtonGlac(self.janelaServ, "Buscar", self.busca_servicoS)
        botaolimpa.place(x=345, y=15, width=70, height=35)

        descrHor = customtkinter.CTkLabel(self.janelaServ, text="Horas")
        descrHor.place(x=6, y=110)

        self.entradaHor = customtkinter.CTkEntry(self.janelaServ)
        self.entradaHor.place(x=80, y=110, relwidth=0.04)

        descrCustohora = customtkinter.CTkLabel(self.janelaServ, text="Custo")
        descrCustohora.place(x=140, y=110)

        self.entradaCustohora = customtkinter.CTkEntry(self.janelaServ)
        self.entradaCustohora.place(x=210, y=110, relwidth=0.04)

        descrValorhora = customtkinter.CTkLabel(self.janelaServ, text="Valor")
        descrValorhora.place(x=270, y=110)

        self.entradaValorhora = customtkinter.CTkEntry(self.janelaServ)
        self.entradaValorhora.place(x=335, y=110, relwidth=0.04)

        descrTipoServ = customtkinter.CTkLabel(self.janelaServ, text="Tipo")
        descrTipoServ.place(x=445, y=15)

        self.entradaTipoServ = customtkinter.CTkEntry(self.janelaServ)
        self.entradaTipoServ.place(x=525, y=15, relwidth=0.25)

        descrSistemaServ = customtkinter.CTkLabel(self.janelaServ, text="Sistema")
        descrSistemaServ.place(x=445, y=45)

        self.entradaSistemaServ = customtkinter.CTkEntry(self.janelaServ)
        self.entradaSistemaServ.place(x=525, y=45, relwidth=0.25)

        descrDescricao = customtkinter.CTkLabel(self.janelaServ, text="Marca")
        descrDescricao.place(x=445, y=75)

        self.entradaDescricao = customtkinter.CTkEntry(self.janelaServ)
        self.entradaDescricao.place(x=525, y=75, relwidth=0.25)

        descrVeic = ButtonGlac(self.janelaServ, "Veiculo", self.busca_serv_veicS)
        descrVeic.place(x=445, y=105, width=80, height=35)

        self.entradaVeic = customtkinter.CTkEntry(self.janelaServ)
        self.entradaVeic.place(x=525, y=105, relwidth=0.25)

        botaoAdd = ButtonGlac(self.janelaServ, "Novo", self.add_servS)
        botaoAdd.place(x=800, y=20, width=90, height=35)

        botaoMudServ = ButtonGlac(self.janelaServ, "Alterar", self.mud_servS)
        botaoMudServ.place(x=800, y=55, width=90, height=35)

        botaoDel = ButtonGlac(self.janelaServ, "Apagar", self.del_servS)
        botaoDel.place(x=800, y=90, width=90, height=35)

        ### Widgets - Listar veiculos
        self.listaServ = ttk.Treeview(self.janelaServ, height=10,
                                      column=("col1", "col2", "col3", "col4", "col5", "col6",
                                              "col7", "col8", "col9"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text="Codigo")
        self.listaServ.heading("#2", text="Serviços")
        self.listaServ.heading("#3", text="Horas")
        self.listaServ.heading("#4", text="Custo")
        self.listaServ.heading("#5", text="Valor")
        self.listaServ.heading("#6", text="Marca")
        self.listaServ.heading("#7", text="Veiculo")
        self.listaServ.heading("#8", text="Tipo")
        self.listaServ.heading("#9", text="Sistema")

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=230)
        self.listaServ.column("#3", width=45)
        self.listaServ.column("#4", width=57)
        self.listaServ.column("#5", width=55)
        self.listaServ.column("#6", width=100)
        self.listaServ.column("#7", width=145)
        self.listaServ.column("#8", width=110)
        self.listaServ.column("#9", width=145)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaServ, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=935, y=150, height=225)

        self.conecta_Glac()

        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
         descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  
         WHERE sp = "s" ORDER BY servprod ASC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.listaServ.place(x=-10, y=150)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickS)
        self.desconecta_Glac()

        self.janelaServ.mainloop()
    def OnDoubleClickS(self, event):
        self.limpa_servicoS()
        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6, col7, col8, col9 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)
        self.carrega_servicoS()
    def mud_servS(self):
        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()

        self.conecta_Glac()
        self.cursor.execute("""UPDATE servprod 
        SET servprod = ?, hor = ?, custo = ?, valor = ?, tiposerv = ?, sistemaserv = ?,
        descricao = ?, id_marcaprod = ? 
        WHERE cod_sp = ?""", (servprod, hor, custo, valor, tiposerv, sistemaserv,
                              descricao, veic, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
        descricao, id_marcaprod, tiposerv, sistemaserv FROM servprod  
        WHERE sp = "S" ORDER BY servprod ASC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
    def limpa_servicoS(self):
        self.entradaCod.delete(0, END)
        self.entradaServ.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaVeic.delete(0, END)
    def del_servS(self):
        self.conecta_Glac()
        cod_sp = self.entradaCod.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()
        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
        descricao, tiposerv, sistemaserv FROM servprod  
        WHERE sp = "S" ORDER BY cod_sp DESC;""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
    def carrega_servicoS(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        self.entradaServ.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaHor.delete(0, END)
        self.entradaCustohora.delete(0, END)
        self.entradaValorhora.delete(0, END)
        self.entradaTipoServ.delete(0, END)
        self.entradaSistemaServ.delete(0, END)
        self.entradaVeic.delete(0, END)

        self.cursor.execute("""SELECT servprod, hor, custo, valor, tiposerv, sistemaserv,
            descricao, id_marcaprod FROM servprod WHERE cod_sp = '%s'""" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            self.entradaServ.insert(END, i[0])
            self.entradaHor.insert(END, i[1])
            self.entradaCustohora.insert(END, i[2])
            self.entradaValorhora.insert(END, i[3])
            self.entradaTipoServ.insert(END, i[4])
            self.entradaSistemaServ.insert(END, i[5])
            self.entradaDescricao.insert(END, i[6])
            self.entradaVeic.insert(END, i[7])

            self.desconecta_Glac()
    def busca_serv_veicS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaVeic.insert(END, '%')
        veic = self.entradaVeic.get()

        self.conecta_Glac()
        self.cursor.execute("""SELECT cod_sp, servprod, hor, custo, valor, descricao, id_marcaprod,
            tiposerv, sistemaserv FROM servprod WHERE id_marcaprod LIKE '%s'  """ % veic)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaVeic.delete(0, END)
        self.desconecta_Glac()
    def busca_servicoS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaServ.insert(END, '%')
        self.conecta_Glac()

        servprod = self.entradaServ.get()
        self.cursor.execute("""SELECT cod_sp, servprod, hor, custo, valor, descricao,
        id_marcaprod, tiposerv, sistemaserv FROM servprod 
        WHERE servprod LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaServ.delete(0, END)

        self.desconecta_Glac()
    def add_servS(self):
        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        servprod = self.entradaServ.get()
        hor = self.entradaHor.get()
        custo = self.entradaCustohora.get()
        valor = self.entradaValorhora.get()
        tiposerv = self.entradaTipoServ.get()
        sistemaserv = self.entradaSistemaServ.get()
        descricao = self.entradaDescricao.get()
        veic = self.entradaVeic.get()
        id_marcaprod = self.entradaDescricao.get()

        self.conecta_Glac()
        self.cursor.execute("""INSERT INTO servprod ( servprod, hor, custo, valor, tiposerv, 
        sistemaserv, sp, descricao, id_marcaprod) VALUES ( ?, ?, ?, ?, ?, ?, "S", ?, ?)""",
        (servprod, hor, custo, valor, tiposerv, sistemaserv, descricao, id_marcaprod))
        self.conn.commit()
        lista = self.cursor.execute("""SELECT cod_sp, servprod, hor, custo , valor, 
        descricao , id_marcaprod, tiposerv, sistemaserv FROM servprod  
        WHERE sp = "S" ORDER BY cod_sp DESC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()