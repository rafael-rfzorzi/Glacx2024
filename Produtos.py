import customtkinter
from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class CadProd:
    def cadprod(self):
        self.janelaProd = customtkinter.CTkToplevel()
        self.janelaProd.title("Produtos")
        self.janelaProd.geometry("860x240+65+180")
        self.janelaProd.resizable(FALSE, FALSE)
        self.janelaProd.transient(self.window_one)
        self.janelaProd.focus_force()

        descrCodprod = customtkinter.CTkLabel(self.janelaProd, text="Codigo")
        descrCodprod.place(x=10, y=5)

        self.entradaCodprod = customtkinter.CTkEntry(self.janelaProd)
        self.entradaCodprod.place(x=80, y=5, relwidth=0.07)

        descrProd = customtkinter.CTkLabel(self.janelaProd, text="Produtos")
        descrProd.place(x=10, y=33)

        self.entradaProd = customtkinter.CTkEntry(self.janelaProd)
        self.entradaProd.place(x=80, y=33, relwidth=0.22)

        botaoAdd = ButtonGlac(self.janelaProd, "Carregar", self.carrega_produtoP)
        botaoAdd.place(x=150, y=2, width=115, height=31)

        botaolimpa = ButtonGlac(self.janelaProd, "Limpar", self.limpa_produtoP)
        botaolimpa.place(x=285, y=2, width=70, height=31)

        botaolimpa = ButtonGlac(self.janelaProd, "Buscar", self.busca_produtoP)
        botaolimpa.place(x=285, y=32, width=70, height=30)

        descrIdMarcaprod = ButtonGlac(self.janelaProd, "Marca", self.busca_marcaP)
        descrIdMarcaprod.place(x=2, y=60, width=100, height=30)

        self.entradaIdMarcaprod = customtkinter.CTkEntry(self.janelaProd)

        self.entradaMarcaprod = customtkinter.CTkEntry(self.janelaProd)
        self.entradaMarcaprod.place(x=105, y=62, relwidth=0.25)

        descrIdFornec = ButtonGlac(self.janelaProd, "Fornecedor", self.busca_fornecP)
        descrIdFornec.place(x=2, y=90, width=100, height=30)

        self.entradaIdFornec = Entry(self.janelaProd)

        self.entradaFornec = customtkinter.CTkEntry(self.janelaProd)
        self.entradaFornec.place(x=105, y=93, relwidth=0.25)

        self.descrCusto = customtkinter.CTkLabel(self.janelaProd, text="Custo")
        self.descrCusto.place(x=10, y=122)

        self.entradaCusto = customtkinter.CTkEntry(self.janelaProd)
        self.entradaCusto.configure(validate="key", validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=83, y=122, relwidth=0.1)

        descrValor = customtkinter.CTkLabel(self.janelaProd, text="Valor")
        descrValor.place(x=180, y=122)

        self.entradaValor = customtkinter.CTkEntry(self.janelaProd)
        self.entradaValor.configure(validate="key", validatecommand=self.vcmd8float)
        self.entradaValor.place(x=240, y=123, relwidth=0.1)

        descrDescricao = customtkinter.CTkLabel(self.janelaProd, text="Descrição")
        descrDescricao.place(x=10, y=150)

        self.entradaDescricao = customtkinter.CTkEntry(self.janelaProd)
        self.entradaDescricao.place(x=83, y=153, relwidth=0.27)

        botaoAdd = ButtonGlac(self.janelaProd, "Novo", self.add_produtoP)
        botaoAdd.place(x=50, y=190, width=80, height=35)

        botaoMudServ = ButtonGlac(self.janelaProd, "Alterar", self.mud_produtoP)
        botaoMudServ.place(x=150, y=190, width=80, height=35)

        botaoDel = ButtonGlac(self.janelaProd, "Apagar", self.del_produtoP)
        botaoDel.place(x=250, y=190, width=80, height=35)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.janelaProd,
                                      height=10, column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=0)
        self.listaServ.heading("#1", text="Codigo")
        self.listaServ.column("#1", width=60)
        self.listaServ.heading("#2", text="Produtos")
        self.listaServ.column("#2", width=220)
        self.listaServ.heading("#3", text="")
        self.listaServ.column("#3", width=25)
        self.listaServ.heading("#4", text="Custo")
        self.listaServ.column("#4", width=70)
        self.listaServ.heading("#5", text="")
        self.listaServ.column("#5", width=25)
        self.listaServ.heading("#6", text="Valor")
        self.listaServ.column("#6", width=80)

        self.conecta_Glac()

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaProd, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=840, y=5, height=220)

        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor 
             FROM servprod WHERE sp = "P" ORDER BY servprod ASC ; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.listaServ.place(x=360, y=5)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickP)
        self.desconecta_Glac()
        self.janelaProd.mainloop()
    def add_produtoP(self):
        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        tipser = 'Peça'
        hora = '1'

        self.conecta_Glac()
        self.cursor.execute("""INSERT INTO servprod ( servprod, id_marcaprod, id_fornec, 
        custo, valor, sp, descricao, tiposerv, hor)	VALUES ( ?, ?, ?, ?, ?, "P", ?, ?, ?)""",
        (servprod, id_marcaprod, id_fornec, custo, valor, descricao, tipser, hora))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())

        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor 
            FROM servprod WHERE sp = "P" AND  servprod LIKE '%s' 
            ORDER BY servprod ASC;""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
        msg = "Novo produto incluido com sucesso"
        messagebox.showinfo("GLAC ", msg)
    def busca_produtoP(self):
        self.conecta_Glac()
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaProd.insert(END, '%')
        servprod = self.entradaProd.get()
        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor 
        FROM servprod WHERE sp = "P" AND  servprod LIKE '%s' 
        ORDER BY servprod ASC;""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
            self.entradaProd.delete(0, END)
        self.desconecta_Glac()
    def busca_marcaP(self):
        def add_autobind(event):
            listaServ1.selection()
            for n in listaServ1.selection():
                col1, col2 = listaServ1.item(n, 'values')
                self.entradaIdMarcaprod.insert(0, col1)
                self.entradaMarcaprod.insert(0, col2)
            listatec.destroy()

        def OnTec(*args):
            listaServ1.yview(*args)

        # Widgets - Listar tecnicos
        self.entradaMarcaprod.insert(END, '%')
        veicAuto = self.entradaMarcaprod.get()

        listatec = Tk()
        listatec.title("Marcas - GLAC  ")
        listatec.geometry("315x235")
        listatec.resizable(TRUE, TRUE)

        ### Widgets - Listar produtos ###
        listaServ1 = ttk.Treeview(listatec, height=10, column=("col1", "col2"))
        listaServ1.heading("#0", text="")
        listaServ1.column("#0", width=0)
        listaServ1.heading("#1", text=self.m_Codigo)
        listaServ1.column("#1", width=60)
        listaServ1.heading("#2", text="Marca")
        listaServ1.column("#2", width=220)

        listaServ1.place(x=10, y=5)
        listaServ1.bind("<Double-1>", add_autobind)

        # Cria barra de rolagem
        barra12 = Scrollbar(listatec, orient='vertical', command=OnTec)
        barra12.place(x=292, y=6, width=20, height=220)
        listaServ1.configure(yscroll=barra12.set)


        self.conecta_Glac()
        self.cursor.execute("""SELECT cod_marca, marca FROM marcaprod 
        WHERE cod_marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            listaServ1.insert("", END, values=i)
        self.desconecta_Glac()

        self.entradaMarcaprod.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
    def busca_fornecP(self):
        def add_autobind(event):
            listaServ1.selection()
            for n in listaServ1.selection():
                col1, col2 = listaServ1.item(n, 'values')
                self.entradaIdFornec.insert(0, col1)
                self.entradaFornec.insert(0, col2)
            listatec.destroy()
        def OnTec(*args):
            listaServ1.yview(*args)
        ### Widgets - Listar tecnicos ###
        self.entradaFornec.insert(END, '%')
        veicAuto = self.entradaFornec.get()

        listatec = Tk()
        listatec.title("Fornecedores - GLAC  ")
        listatec.geometry("310x240")
        listatec.resizable(TRUE, TRUE)

        ### Widgets - Listar produtos ###
        listaServ1 = ttk.Treeview(listatec, height=10, column=("col1", "col2"))
        listaServ1.heading("#0", text="")
        listaServ1.column("#0", width=0)
        listaServ1.heading("#1", text=self.m_Codigo)
        listaServ1.column("#1", width=60)
        listaServ1.heading("#2", text="Marca")
        listaServ1.column("#2", width=220)

        listaServ1.place(x=10, y=5)
        listaServ1.bind("<Double-1>", add_autobind)

        # Cria barra de rolagem
        barra12 = Scrollbar(listatec, orient='vertical', command=OnTec)
        barra12.place(x=292, y=6, width=20, height=220)
        listaServ1.configure(yscroll=barra12.set)

        self.conecta_Glac()
        self.cursor.execute("""SELECT cod_forn, fornecedor FROM fornecedores WHERE fornecedor 
        LIKE '%s' ORDER BY fornecedor ASC""" % veicAuto)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            listaServ1.insert("", END, values=i)
        self.desconecta_Glac()

        self.entradaFornec.delete(0, END)
        self.entradaIdFornec.delete(0, END)
    def carrega_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        prod = self.cursor

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaFornec.delete(0, END)

        prod.execute("SELECT servprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaprod = self.cursor.fetchall()
        for i in consultaprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaProd.insert(END, i)

        idmarca = self.cursor
        idmarca.execute("SELECT id_marcaprod FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaIdMarcaprod.insert(END, i)

        mm = self.entradaIdMarcaprod.get()
        marca = self.cursor
        marca.execute("SELECT marca FROM marcaprod WHERE cod_marca = '%s'" % mm)
        consultaidmarca = self.cursor.fetchall()
        for i in consultaidmarca:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaMarcaprod.insert(END, i)

        idfornec = self.cursor
        idfornec.execute("SELECT id_fornec FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            self.entradaIdFornec.insert(END, i)

        ff = self.entradaIdFornec.get()
        fornec = self.cursor
        fornec.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % ff)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaFornec.insert(END, i)

        custo = self.cursor
        custo.execute("SELECT custo FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultacusto = self.cursor.fetchall()
        for i in consultacusto:
            self.entradaCusto.insert(END, i)

        valor = self.cursor
        valor.execute("SELECT valor FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultavalor = self.cursor.fetchall()
        for i in consultavalor:
            self.entradaValor.insert(END, i)

        descrprod = self.cursor
        descrprod.execute("SELECT descricao FROM servprod WHERE cod_sp = '%s'" % cod_sp)
        consultadescrprod = self.cursor.fetchall()
        for i in consultadescrprod:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaDescricao.insert(END, i)

            self.desconecta_Glac()
    def del_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        self.cursor.execute("""
     		DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" ORDER BY servprod ASC;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Produto excluido com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def limpa_produtoP(self):
        self.conecta_Glac()

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.entradaCodprod.delete(0, END)

        self.desconecta_Glac()
    def mud_produtoP(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        tipser = 'Peça'
        hora = '1'

        self.cursor.execute("""
     		UPDATE servprod SET servprod = ?  WHERE cod_sp = ?""", (servprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
             		UPDATE servprod SET tiposerv = ? WHERE cod_sp = ?""", (tipser, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
                     		UPDATE servprod SET hor = ? WHERE cod_sp = ?""", (hora, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET id_marcaprod = ? WHERE cod_sp = ?""", (id_marcaprod, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
             UPDATE servprod SET id_fornec = ? WHERE cod_sp = ?""", (id_fornec, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET custo = ? WHERE cod_sp = ?""", (custo, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET valor = ? WHERE cod_sp = ?""", (valor, cod_sp))
        self.conn.commit()
        self.cursor.execute("""
     		UPDATE servprod SET descricao = ? WHERE cod_sp = ?""", (descricao, cod_sp))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
     		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
     		WHERE sp = "P" ORDER BY servprod ASC;
     		""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        msg = "Produto alterado com sucesso"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
    def OnDoubleClickP(self, event):
        self.limpa_produtoP()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)

        self.carrega_produtoP()