import customtkinter
from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class CadMarcaProd:
    def cadmarcaprod(self):
        self.janelaM = customtkinter.CTkToplevel()
        self.janelaM.title("Marca dos Produtos")
        self.janelaM.geometry("870x200+30+250")
        self.janelaM.resizable(FALSE, FALSE)
        self.janelaM.transient(self.window_one)
        self.janelaM.focus_force()
        self.janelaM.grab_set()

        descrCod = customtkinter.CTkLabel(self.janelaM, text="Codigo")
        descrCod.place(x=5, y=20)

        self.entradaCod = customtkinter.CTkEntry(self.janelaM)
        self.entradaCod.place(x=85, y=20, relwidth=0.05)

        #  Botao Carrega marca
        botaoAdd = ButtonGlac(self.janelaM, "Carregar", self.carrega_marca_prod)
        botaoAdd.place(x=145, y=15, width=130, height=30)

        ###  Botao limpa automovel
        botaolimpa = ButtonGlac(self.janelaM, "Limpar", self.limpa_marca_prod)
        botaolimpa.place(x=275, y=15, width=80, height=30)

        descrMarca = customtkinter.CTkLabel(self.janelaM, text="Marca")
        descrMarca.place(x=5, y=50)

        self.entradaMarca = customtkinter.CTkEntry(self.janelaM)
        self.entradaMarca.place(x=85, y=50)

        ###  Botao busca automovel
        botaobusca = ButtonGlac(self.janelaM, "Buscar", self.busca_marca_prod)
        botaobusca.place(x=285, y=45, width=70, height=30)

        descrDescricao = customtkinter.CTkLabel(self.janelaM, text="Descricao")
        descrDescricao.place(x=5, y=90)

        self.entradaDescricao = customtkinter.CTkEntry(self.janelaM)
        self.entradaDescricao.place(x=85, y=90)

        # Botao adicionar
        botaoAdd = ButtonGlac(self.janelaM, "Novo", self.add_marca_prod)
        botaoAdd.place(x=45, y=150, width=85, height=30)

        # botao mudar
        botaoMud = ButtonGlac(self.janelaM, "Alterar", self.mud_marca_prod)
        botaoMud.place(x=130, y=150, width=85, height=30)

        # botao deletar
        botaoDel = ButtonGlac(self.janelaM, " Apagar ", self.del_marca_prod)
        botaoDel.place(x=215, y=150, width=85, height=30)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.janelaM, height=7,
                                      column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text="Codigo")
        self.listaServ.heading("#2", text="Marca")
        self.listaServ.heading("#3", text="Descricao")

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=65)
        self.listaServ.column("#2", width=200)
        self.listaServ.column("#3", width=220)
        self.listaServ.place(x=360, y=20)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaM, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=845, y=20, width=20, height=160)

        lista = self.cursor.execute("""SELECT cod_marca, marca, descricao 
        FROM marcaprod ORDER BY marca ASC ;""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickMarc)
        self.desconecta_Glac()
        self.janelaM.mainloop()
    def OnDoubleClickMarc(self, event):
        self.limpa_marca_prod()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_marca_prod()
    def mud_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
     		UPDATE marcaprod SET marca = ? WHERE cod_marca = ?""", (marca, cod_marca))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE marcaprod SET descricao = ? WHERE cod_marca = ?""", (descricao, cod_marca))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        listacod = self.cursor.execute("""SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in listacod:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def carrega_marca_prod(self):
        cod_marca = self.entradaCod.get()
        self.conecta_Glac()

        marcaprod = self.cursor

        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)

        marcaprod.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultamarcaprod = self.cursor.fetchall()
        for i in consultamarcaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarca.insert(END, i)

        descricao = self.cursor
        descricao.execute("SELECT descricao FROM marcaprod WHERE cod_marca = '%s'" % cod_marca)
        consultadescricao = self.cursor.fetchall()
        for i in consultadescricao:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

        self.desconecta_Glac()
    def del_marca_prod(self):

        conn = sqlite3.connect("glac.db")
        cursor = self.conn.cursor()
        cod_marca = self.entradaCod.get()
        self.cursor.execute("""
     		DELETE FROM marcaprod WHERE cod_marca=?""", (cod_marca,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_marca, marca, descricao FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        conn.close()
    def limpa_marca_prod(self):
        self.entradaCod.delete(0, END)
        self.entradaMarca.delete(0, END)
        self.entradaDescricao.delete(0, END)
    def add_marca_prod(self):
        self.conecta_Glac()

        cod_marca = self.entradaCod.get()
        marca = self.entradaMarca.get()
        descricao = self.entradaDescricao.get()
        self.listaServ.delete(*self.listaServ.get_children())
        self.cursor.execute("""
     		INSERT INTO marcaprod ( marca, descricao)
     		VALUES ( ?, ?)""",  (marca, descricao))
        self.conn.commit()
        lista = self.cursor.execute("""
             SELECT cod_marca, marca, descricao 
             FROM marcaprod ORDER BY marca ASC ;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def busca_marca_prod(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaMarca.insert(END, '%')
        self.conecta_Glac()
        marca = self.entradaMarca.get()
        marcap = self.cursor

        marcap.execute("SELECT * FROM marcaprod "
                       "WHERE marca LIKE '%s'" % marca)
        buscamarca = self.cursor.fetchall()
        for i in buscamarca:
            self.listaServ.insert("", END, values=i)
        self.entradaMarca.delete(0, END)

        self.desconecta_Glac()