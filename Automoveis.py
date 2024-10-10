from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import *
from datetime import *
import customtkinter

class CadAuto:
    def cadaut(self):
        self.janelaAut = customtkinter.CTkToplevel()
        self.janelaAut.title('Glac - Cadastro de Veiculos')
        self.janelaAut.geometry("780x240+100+200")
        self.janelaAut.configure(background="#6F87B0")
        self.janelaAut.resizable(FALSE, FALSE)
        self.janelaAut.transient(self.window_one)
        self.janelaAut.focus_force()
        self.janelaAut.grab_set()

        # Label do codigo
        descrCod_aut = customtkinter.CTkLabel(self.janelaAut, text="Codigo")
        descrCod_aut.place(relx=0.01, rely=0.1, relwidth=0.1, relheight=0.1)

        #### entrada do codigo
        self.entradaCod_autA = customtkinter.CTkEntry(self.janelaAut)
        self.entradaCod_autA.configure(validate="key", validatecommand=self.vcmd4)
        self.entradaCod_autA.place(relx=0.1, rely=0.1, relwidth=0.05, relheight=0.1)

        # descrição do veiculo
        descrAut = customtkinter.CTkLabel(self.janelaAut, text="Automovel")
        descrAut.place(relx=0.01, rely=0.3, relwidth=0.1, relheight=0.1)

        self.entradaAutA = customtkinter.CTkEntry(self.janelaAut)
        self.entradaAutA.place(relx=0.1, rely=0.3, relwidth=0.25, relheight=0.1)

        # entry da marca
        self.entradaMarcaA = customtkinter.CTkEntry(self.janelaAut)
        self.entradaMarcaA.place(relx=0.1, rely=0.5, relwidth=0.25, relheight=0.1)

        self.entradaMarca2A = Entry()

        # botão busca
        botaoBuscaAut = customtkinter.CTkButton(self.janelaAut, text="Buscar", command=self.busca_automovelA)
        botaoBuscaAut.place(relx=0.35, rely=0.28, relwidth=0.1, relheight=0.14)

        # botao limpa
        botaoLimpaAut = customtkinter.CTkButton(self.janelaAut, text="Limpar", command=self.limpa_automovelA)
        botaoLimpaAut.place(relx=0.35, rely=0.08, relwidth=0.1, relheight=0.14)

        # botao marca
        botaoMarcaAut = customtkinter.CTkButton(self.janelaAut, text="Marca", command=self.busca_autoA)
        botaoMarcaAut.place(relx=0.01, rely=0.48, relwidth=0.09, relheight=0.14)

        #
        botaoNovoAut = customtkinter.CTkButton(self.janelaAut, text="Novo", command=self.add_automovelA)
        botaoNovoAut.place(x=30, y=180, relwidth=0.09, relheight=0.14)
        #
        botaoAlterarAut = customtkinter.CTkButton(self.janelaAut, text="Alterar", command=self.mud_automovelA)
        botaoAlterarAut.place(x=130, y=180, relwidth=0.09, relheight=0.14)
        #
        botaoApagarAut = customtkinter.CTkButton(self.janelaAut, text="Apagar", command=self.del_automovelA)
        botaoApagarAut.place(x=230, y=180, relwidth=0.09, relheight=0.14)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaAut, orient='vertical', command=self.OnVsbA)

        # Widgets - Listar veiculos
        self.listaServ = ttk.Treeview(self.janelaAut, height=8, column=("col1", "col2", "col3"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text="Codigo")
        self.listaServ.heading("#2", text="Automovel")
        self.listaServ.heading("#3", text="Marca")

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=45)
        self.listaServ.column("#2", width=180)
        self.listaServ.column("#3", width=170)
        self.listaServ.configure(yscroll=self.barra.set)
        self.listaServ.place(x=365, y=5, height=225)

        # Adiciona barra de rolagem
        self.barra.place(x=760, y=5, height=225)
        self.busca_automovelA()
        self.listaServ.bind("<Double-1>", self.OnDoubleClickA)
        self.janelaAut.mainloop()
    def variaveisA(self):
        self.cod_aut = self.entradaCod_autA.get()
        self.automovel = self.entradaAutA.get()
        self.montad = self.entradaMarca2A.get()
    def add_automovelA(self):
        self.variaveisA()
        self.conecta_Glac()
        if self.montad == '':
            msg = "É necessário escolher a marca do "
            msg += " automovel a ser cadastrado."
            messagebox.showinfo("GLAC - Automovel", msg)
            self.desconecta_Glac()
        else:
            self.cursor.execute("""
                INSERT INTO automoveis ( automovel, montad)
                VALUES ( ?, ?)""", (self.automovel, self.montad))
            self.conn.commit()
            self.desconecta_Glac()
            self.limpa_automovelA()
            self.busca_automovelA()
            msg = self.m_msgAutAdd
            msg += ""
            messagebox.showinfo("GLAC - Automovel", msg)
    def mud_automovelA(self):
        self.variaveisA()
        self.conecta_Glac()

        self.cursor.execute("""UPDATE automoveis 
        SET automovel = ?, montad = ? WHERE cod_aut = ?""",
            (self.automovel, self.montad, self.cod_aut))
        self.conn.commit()
        self.desconecta_Glac()
        self.busca_automovelA()

        msg = self.m_msgAutAlt
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def del_automovelA(self):
        self.variaveisA()
        self.conecta_Glac()

        self.cursor.execute(""" DELETE FROM automoveis WHERE cod_aut=?;""", (self.cod_aut,))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor
        self.cursor.execute("""SELECT automoveis.cod_aut, automoveis.automovel, 
        montadora.marca FROM automoveis, montadora WHERE montadora.cod = automoveis.montad  
       	ORDER BY automovel ASC;""")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.limpa_automovelA()
        msg = self.m_msgAutDel
        messagebox.showinfo("GLAC - Altera Automovel", msg)
    def carrega_automovelA(self):
        cod_aut = self.entradaCod_autA.get()
        self.conecta_Glac()

        self.entradaAutA.delete('0', 'end')
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')

        self.cursor.execute("""SELECT automovel, marca, montad 
        FROM automoveis, montadora 
        WHERE montadora.cod = automoveis.montad AND cod_aut = '%s'""" % cod_aut)
        consultaautomovel = self.cursor.fetchall()
        for i in consultaautomovel:
            self.entradaAutA.insert(0, i[0])
            self.entradaMarcaA.insert(0, i[1])
            self.entradaMarca2A.insert(0, i[2])
        self.desconecta_Glac()
    def busca_automovelA(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.entradaAutA.insert(0, '%')
        autom = self.entradaAutA.get()

        lista = self.cursor.execute("""SELECT automoveis.cod_aut, 
        automoveis.automovel, montadora.marca FROM automoveis, montadora 
        WHERE montadora.cod = automoveis.montad AND automovel LIKE '%s'
        ORDER BY automovel ASC; """ %autom)
        for i in lista:
            self.listaServ.insert("", 0, values=i)
        self.limpa_automovelA()
        self.desconecta_Glac()
    def OnDoubleClickA(self, event):
        self.limpa_automovelA()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2, col3 = self.listaServ.item(n, 'values')
            self.entradaCod_autA.insert(0, col1)
        self.carrega_automovelA()
    def OnVsbA(self, *args):
        self.listaServ.yview(*args)
    def add_autobindA(self, event):
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')
        for n in self.listaTec1.selection():
            col1, col2 = self.listaTec1.item(n, 'values')
            self.entradaMarca2A.insert(0, col1)
            self.entradaMarcaA.insert(0, col2)
        self.listatec.destroy()
    def limpa_automovelA(self):
        self.entradaCod_autA.delete('0', 'end')
        self.entradaAutA.delete('0', 'end')
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')
    def busca_autoA(self):
        # Widgets -
        self.entradaMarcaA.insert(0, '%')
        veicAuto = self.entradaMarcaA.get()

        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("320x220+100+100")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaAut)
        self.listatec.focus_force()
        self.listatec.grab_set()

        ### Widgets -
        self.listaTec1 = ttk.Treeview(self.listatec, height=5, column=("col1", "col2"))
        self.listaTec1.heading("#0", text="")
        self.listaTec1.heading("#1", text="Codigo")
        self.listaTec1.heading("#2", text='Marca')

        self.listaTec1.column("#0", width=0)
        self.listaTec1.column("#1", width=60)
        self.listaTec1.column("#2", width=200)

        # Adiciona barra de rolagem
        self.listaTec1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.96)
        # Binding da listbox
        self.listaTec1.bind('<Double-1>', self.add_autobindA)
        self.conecta_Glac()

        buscaservico = self.cursor.execute("""SELECT cod, marca FROM montadora 
              WHERE marca LIKE '%s' ORDER BY marca ASC""" % veicAuto)

        for i in buscaservico:
            self.listaTec1.insert("", END, values=i)
        self.entradaMarcaA.delete('0', 'end')
        self.entradaMarca2A.delete('0', 'end')
        self.desconecta_Glac()