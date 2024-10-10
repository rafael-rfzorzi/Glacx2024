from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class CadEstoque:
    def cadest(self):
        self.janelaEst = Toplevel()
        self.janelaEst.title(self.m_Estoque)
        self.janelaEst.geometry("790x355+100+150")
        self.janelaEst.configure(background="gray50")
        self.janelaEst.resizable(FALSE, FALSE)
        self.janelaEst.transient(self.janela)
        self.janelaEst.focus_force()
        self.janelaEst.grab_set()

        self.conecta_Glac()
        abas = ttk.Notebook(self.janelaEst)
        self.frame_aba1 = Frame(abas)
        self.frame_aba1.configure(background="gray40")
        self.frame_aba2 = Frame(abas)
        self.frame_aba2.configure(background="gray40")
        frame_aba1 = self.frame_aba1
        frame_aba2 = self.frame_aba2

        label1 = Label(frame_aba1).pack(padx=390, pady=155)
        label2 = Label(frame_aba2).pack(padx=390, pady=155)

        abas.add(frame_aba1, text=self.m_Cadastro + ' ' + self.m_Produtos)
        abas.add(frame_aba2, text=self.m_MovimentaEst)
        abas.place(x=0, y=0)

        frameProb = GradientFrame(frame_aba1)
        frameProb.place(x=0, y=0, relwidth=1, relheight=1)

        descrCodprod = LabelGlac(frame_aba1, self.m_Codigo)
        descrCodprod.place(x=2, y=15, width=80, height=25)

        ## Label produtos
        descrProd = LabelGlac(frame_aba1, self.m_Produtos)
        descrProd.place(x=2, y=45, width=80, height=25)

        ###  Botao Carrega
        botaoAdd = ButtonGlac(frame_aba1, self.m_Carregar, self.carrega_produtoE)
        botaoAdd.place(x=140, y=5, width=90, height=35)

        ###  Botao limpa
        botaolimpa = ButtonGlac(frame_aba1, self.m_Limpar, self.limpa_produtoE)
        botaolimpa.place(x=260, y=5, width=70, height=35)

        ###  Botao busca
        botaoBusca = ButtonGlac(frame_aba1, self.m_Buscar, self.busca_produtoE)
        botaoBusca.place(x=260, y=40, width=70, height=33)

        ### Botao Marca Produto
        descrIdMarcaprod = ButtonGlac(frame_aba1, self.m_Marca, self.busca_marcaE)
        descrIdMarcaprod.place(x=2, y=70, width=98, height=35)

        ## Entry codigo
        self.entradaCodprod = Entry(frame_aba1)
        self.entradaCodprod.configure(validate="key", validatecommand=self.vcmd6)
        self.entradaCodprod.place(x=80, y=15, width=60, height=25)

        ## Entry descrição Produto
        self.entradaProd = Entry(frame_aba1)
        self.entradaProd.place(x=80, y=45, width=180, height=25)

        self.entradaIdMarcaprod = Entry(frame_aba1)
        # widget oculto, sem place

        self.entradaMarcaprod = Entry(frame_aba1)
        self.entradaMarcaprod.place(x=100, y=75, width=230, height=25)

        descrIdFornec = ButtonGlac(frame_aba1, self.m_Fornecedor, self.busca_fornecE)
        descrIdFornec.place(x=2, y=102, width=98, height=33)

        self.entradaIdFornec = Entry(frame_aba1)

        self.entradaFornec = Entry(frame_aba1)
        self.entradaFornec.place(x=100, y=105, width=230, height=25)

        descrCusto = LabelGlac(frame_aba1, self.m_Custo_R)
        descrCusto.place(x=2, y=135, width=85, height=25)

        self.entradaCusto = Entry(frame_aba1)
        self.entradaCusto.configure(validate="key", validatecommand=self.vcmd8float)
        self.entradaCusto.place(x=87, y=135, width=80, height=25)

        descrValor = LabelGlac(frame_aba1, self.m_Valor_R)
        descrValor.place(x=162, y=135, width=85, height=25)

        self.entradaValor = Entry(frame_aba1)
        self.entradaValor.configure(validate="key", validatecommand=self.vcmd8float)
        self.entradaValor.place(x=247, y=135, width=82, height=25)

        descrDescricao = LabelGlac(frame_aba1, self.m_Descricao)
        descrDescricao.place(x=16, y=175, width=312, height=25)

        self.entradaDescricao = Entry(frame_aba1)
        self.entradaDescricao.place(x=16, y=195, width=312, height=25)

        botaoAdd = ButtonGlac(frame_aba1, self.m_Novo, self.add_produtoE)
        botaoAdd.place(x=30, y=270, width=80, height=35)

        botaoMudServ = ButtonGlac(frame_aba1, self.m_Alterar, self.mud_produtoE)
        botaoMudServ.place(x=130, y=270, width=80, height=35)

        botaoDel = ButtonGlac(frame_aba1, self.m_Apagar, self.del_produtoE)
        botaoDel.place(x=230, y=270, width=80, height=35)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(frame_aba1, height=10,
            column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text=self.m_Codigo)
        self.listaServ.heading("#2", text=self.m_Produtos)
        self.listaServ.heading("#3", text="")
        self.listaServ.heading("#4", text=self.m_Custo_R)
        self.listaServ.heading("#5", text="")
        self.listaServ.heading("#6", text=self.m_Valor_R)

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=60)
        self.listaServ.column("#2", width=140)
        self.listaServ.column("#3", width=25)
        self.listaServ.column("#4", width=65)
        self.listaServ.column("#5", width=25)
        self.listaServ.column("#6", width=85)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(frame_aba1, orient='vertical', command=self.listaServ.yview)
        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=755, y=17, height=300)

        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor 
        FROM servprod WHERE sp = "P" ORDER BY servprod ASC ; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.listaServ.place(x=340, y=15, width=418, height=300)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickE)

        # Cabeçalho dos itens_orc 1 A 10 - Aba 2
        frameItens = GradientFrame(frame_aba2)
        frameItens.place(x=0, y=0, relwidth=1, relheight=1)

        # Produto
        produto_aba2label = LabelGlac(frame_aba2, self.m_Produtos)
        produto_aba2label.place(x=10, y=2, width=180, height=20)

        self.codproduto2 = Entry(frame_aba2)

        self.produto_aba2 = Entry(frame_aba2)
        self.produto_aba2.place(x=10, y=20, width=180, height=25)

        #### Entrada
        quant_aba2label = LabelGlac(frame_aba2, self.m_Entrada)
        quant_aba2label.place(x=10, y=50, width=80, height=25)

        self.quant_aba2 = Entry(frame_aba2)
        self.quant_aba2.configure(validate="key", validatecommand=self.vcmd8float)
        self.quant_aba2.place(x=90, y=50, width=100, height=25)
        self.quant_aba2.insert(END, 0)

        #### Saida
        saida_aba2label = LabelGlac(frame_aba2, self.m_Saida)
        saida_aba2label.place(x=10, y=80, width=80, height=25)

        self.saida_aba2 = Entry(frame_aba2)
        self.saida_aba2.configure(validate="key", validatecommand=self.vcmd8float)
        self.saida_aba2.place(x=90, y=80, width=100, height=25)
        self.saida_aba2.insert(0, 0)

        #### Custo
        custo_aba2label = LabelGlac(frame_aba2, self.m_Custo_R)
        custo_aba2label.place(x=10, y=110, width=80, height=25)

        self.custo_aba2 = Entry(frame_aba2)
        self.custo_aba2.configure(validate="key", validatecommand=self.vcmd8float)
        self.custo_aba2.place(x=90, y=110, width=100, height=25)

        #### Data
        data_aba2label = LabelGlac(frame_aba2, self.m_Data + self.m_Pontinhos + self.m_DataMasc)
        data_aba2label.place(x=10, y=140, width=180, height=25)

        self.dia_aba2 = DateEntry(frame_aba2, locale='pt_BR')
        self.dia_aba2.place(x=90, y=140, height=25)

        #### Lote
        lote_aba2label = LabelGlac(frame_aba2, self.m_Lote)
        lote_aba2label.place(x=10, y=170, width=80, height=25)

        self.lote_aba2 = Entry(frame_aba2)
        self.lote_aba2.place(x=90, y=170, width=100, height=25)

        #### Validade
        valid_aba2label = LabelGlac(frame_aba2, self.m_Validade)
        valid_aba2label.place(x=10, y=200, width=80, height=25)

        self.diaV_aba2 = DateEntry(frame_aba2, locale='pt_BR')
        self.diaV_aba2.place(x=90, y=200, height=25)

        darEntrada = ButtonGlac(frame_aba2, self.m_InserirRegistro, self.add_movE)
        darEntrada.place(x=40, y=280, width=140, height=35)

        quantestlabel = LabelGlac(frame_aba2, self.m_Quant + ' ' + self.m_Estoque)
        quantestlabel.place(x=430, y=290, width=150, height=25)

        self.quantest = Entry(frame_aba2)
        self.quantest.place(x=580, y=290, width=100, height=25)

        ### Widgets - Listar produtos ###
        self.listaMov = ttk.Treeview(frame_aba2, height=10,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaMov.heading("#0", text="")
        self.listaMov.heading("#1", text=self.m_Lote)
        self.listaMov.heading("#2", text="Entr")
        self.listaMov.heading("#3", text="Said")
        self.listaMov.heading("#4", text="Custo")
        self.listaMov.heading("#5", text=self.m_Data)
        self.listaMov.heading("#6", text="Forn")
        self.listaMov.heading("#7", text=self.m_Validade)

        self.listaMov.column("#0", width=1)
        self.listaMov.column("#1", width=65)
        self.listaMov.column("#2", width=60)
        self.listaMov.column("#3", width=60)
        self.listaMov.column("#4", width=60)
        self.listaMov.column("#5", width=110)
        self.listaMov.column("#6", width=80)
        self.listaMov.column("#7", width=110)

        # Cria barra de rolagem
        self.barraMov = ttk.Scrollbar(frame_aba2, orient='vertical', command=self.listaMov.yview)

        # Adiciona barra de rolagem
        self.listaMov.configure(yscroll=self.barraMov.set)
        self.barraMov.place(x=755, y=20, height=220)

        # Adiciona barra de rolagem
        self.listaMov.place(x=210, y=20)
        self.listaMov.bind("<Double-1>", self.OnDoubleClickE)

        self.desconecta_Glac()
        self.janelaEst.mainloop()
    def add_movE(self):
        self.conecta_Glac()

        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""INSERT INTO movim_prod ( cod_p, entrada, custo, dia, 
        lote, diaV, fornecedor, saida) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)""",
        (cod2, quant, custo, dia, lote, diaV, fornecedor, saida))
        self.conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""SELECT lote, entrada, saida, custo, dia, 
            fornecedores.fornecedor, diaV FROM movim_prod, fornecedores	
    	    WHERE cod_p = '%s' and movim_prod.fornecedor = fornecedores.cod_forn 
    	    ORDER BY id ASC; """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) 
            from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)

        self.desconecta_Glac()
    def add_produtoE(self):
        self.conecta_Glac()
        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()

        self.cursor.execute("""
            INSERT INTO servprod ( servprod, id_marcaprod, id_fornec, custo, valor, sp, descricao)
        	VALUES ( ?, ?, ?, ?, ?, "P", ?)""",
                       (servprod, id_marcaprod, id_fornec, custo, valor, descricao))
        self.conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        	SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
        	WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
        	""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
    def OnDoubleClickE(self, event):
        self.limpa_produtoE()
        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2, col3, col4, col5, col6 = self.listaServ.item(n, 'values')
            self.entradaCodprod.insert(END, col1)
        self.carrega_produtoE()
    def mud_produtoE(self):
        self.conecta_Glac()

        cod_sp = self.entradaCodprod.get()
        servprod = self.entradaProd.get()
        id_marcaprod = self.entradaIdMarcaprod.get()
        id_fornec = self.entradaIdFornec.get()
        custo = self.entradaCusto.get()
        valor = self.entradaValor.get()
        descricao = self.entradaDescricao.get()
        self.cursor.execute("""UPDATE servprod SET servprod = ?, id_marcaprod = ?, 
        id_fornec = ?, custo = ?, valor = ?, descricao = ? WHERE cod_sp = ?""",
        (servprod, id_marcaprod, id_fornec, custo, valor, descricao, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor 
        FROM servprod WHERE sp = "P" ORDER BY servprod ASC; """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
    def limpa_produtoE(self):
        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.entradaCodprod.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)
    def del_produtoE(self):
        self.conecta_Glac()
        cod_sp = self.entradaCodprod.get()
        self.cursor.execute("""DELETE FROM servprod WHERE cod_sp=?""", (cod_sp,))
        conn.commit()
        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""SELECT cod_sp, servprod, "R$", custo, "R$", valor
        FROM servprod WHERE sp = "P" ORDER BY servprod ASC;	""")
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
    def carrega_produtoE(self):
        self.conecta_Glac()
        cod_sp = self.entradaCodprod.get()
        prod = self.cursor
        cod2 = self.codproduto2.get()

        self.entradaProd.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.entradaCusto.delete(0, END)
        self.entradaValor.delete(0, END)
        self.entradaDescricao.delete(0, END)
        self.entradaMarcaprod.delete(0, END)
        self.entradaFornec.delete(0, END)
        self.codproduto2.delete(0, END)
        self.produto_aba2.delete(0, END)
        self.custo_aba2.delete(0, END)
        self.quantest.delete(0, END)
        self.listaMov.delete(*self.listaMov.get_children())

        self.codproduto2.insert(END, cod_sp)
        self.cursor.execute("""SELECT servprod, id_marcaprod, marca, id_fornec, custo,
        valor, servprod.descricao
        FROM servprod, marcaprod WHERE cod_marca = id_marcaprod AND cod_sp = '%s'""" % cod_sp)
        consultaprod = self.cursor.fetchall()
        for i in consultaprod:
            self.entradaProd.insert(END, i[0])
            self.produto_aba2.insert(END, i[0])
            self.entradaIdMarcaprod.insert(END, i[1])
            self.entradaMarcaprod.insert(END, i[2])
            self.entradaIdFornec.insert(END, i[3])
            self.entradaCusto.insert(END, i[4])
            self.custo_aba2.insert(END, i[4])
            self.entradaValor.insert(END, i[5])
            self.entradaDescricao.insert(END, i[6])

        ff = self.entradaIdFornec.get()
        self.cursor.execute("SELECT fornecedor FROM fornecedores WHERE cod_forn = '%s'" % ff)
        consultaidfornec = self.cursor.fetchall()
        for i in consultaidfornec:
            self.entradaFornec.insert(END, i[0])

        self.cursor.execute("""SELECT lote, entrada, saida, custo, dia, 
        fornecedor, diaV FROM movim_prod WHERE cod_p = '%s' ORDER BY id ASC; """ % cod_sp)
        listam = self.cursor.fetchall()
        for i in listam:
            self.listaMov.insert("", END, values=i)

        lista2 = self.cursor.execute("""select Sum(entrada) - Sum(saida) 
        from movim_prod where cod_p = '%s'""" % cod_sp)
        consultalista2 = self.cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)
    def busca_produtoE(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.entradaProd.insert(END, '%')
        servprod = self.entradaProd.get()

        self.conecta_Glac()

        lista = self.cursor.execute("""
       		SELECT cod_sp, servprod, "R$", custo, "R$", valor FROM servprod
       		WHERE sp = "P" AND  servprod LIKE '%s' ORDER BY servprod ASC;
       		""" % servprod)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaProd.delete(0, END)

        self.desconecta_Glac()
    def add_movF(self):
        self.conecta_Glac()
        cursor = self.conn.cursor()
        cod2 = self.codproduto2.get()
        prod2 = self.produto_aba2.get()
        dia = self.dia_aba2.get()
        lote = self.lote_aba2.get()
        diaV = self.diaV_aba2.get()
        quant = self.quant_aba2.get()
        custo = self.custo_aba2.get()
        fornecedor = self.entradaIdFornec.get()
        saida = self.saida_aba2.get()
        self.listaMov.delete(*self.listaMov.get_children())

        self.cursor.execute("""INSERT INTO movim_prod ( cod_p, entrada, custo, dia,	
        lote, diaV, fornecedor, saida) VALUES ( ?, ?, ?, ?, ?, ?, ?, ?)""",
        (cod2, quant, custo, dia, lote, diaV, fornecedor, saida))
        conn.commit()

        msg = "Movimentação realizada.\n "
        msg += ""
        messagebox.showinfo("GLAC - Estoque", msg)

        lista1 = self.cursor.execute("""SELECT  lote, entrada, saida, custo, dia, 
        fornecedores.fornecedor, diaV, mesV, anoV 
        FROM movim_prod WHERE cod_p = '%s' 
        INNER JOIN movim_prod.fornecedor = fornecedores.cod_forn ORDER BY id ASC; """ % cod2)
        for i in lista1:
            self.listaMov.insert("", END, values=i)

        self.quantest.delete(0, END)

        self.cursor.execute("""select Sum(entrada) - Sum(saida) 
        from movim_prod where cod_p = '%s'""" % cod2)
        consultalista2 = cursor.fetchall()
        for i in consultalista2:
            self.quantest.insert(END, i)
        self.desconecta_Glac()
    def add_autobind(self, event):
        self.listatec1.selection()

        for n in self.listatec1.selection():
            col1, col2 = self.listatec1.item(n, 'values')
            self.entradaFornec.insert(END, col2)
            self.entradaIdFornec.insert(END, col1)

        self.listatec.destroy()
    def OnTec(self, *args):
        self.listatec1.yview(*args)
    def add_autobind2(self, event):
        self.listatec1.selection()
        for n in self.listatec1.selection():
            col1, col2 = self.listatec1.item(n, 'values')
            self.entradaMarcaprod.insert(END, col2)
            self.entradaIdMarcaprod.insert(END, col1)

        self.listatec.destroy()