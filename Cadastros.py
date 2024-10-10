import customtkinter
from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class Cads():
    def cademp(self):
        self.janelaEmp = customtkinter.CTkToplevel()
        self.janelaEmp.title('Glacx - Cadastro da empresa')
        self.janelaEmp.configure(background="gray20")
        self.janelaEmp.geometry("410x250+250+250")
        self.janelaEmp.resizable(FALSE, FALSE)
        self.janelaEmp.transient(self.window_one)
        self.janelaEmp.focus_force()
        self.janelaEmp.grab_set()

        descrNomeServ = customtkinter.CTkLabel(self.janelaEmp, text="Estabelecimento")
        descrNomeServ.place(relx=0.2, rely=0.05, relwidth=0.6)

        self.entradaCod_emp = customtkinter.CTkEntry(self.janelaEmp)

        #  Descrição e Entrada Nome
        descrNome = customtkinter.CTkLabel(self.janelaEmp, text="Nome")
        descrNome.place(x=10, y=53, width=80)

        self.entradaNome_emp = Listbox(self.janelaEmp, height=1)
        self.entradaNome_emp.place(x=85, y=53, width=300)

        #  Descrição e Entrada Enedereco
        descrEndereco = LabelGlac(self.janelaEmp, "Endereco")
        descrEndereco.place(x=10, y=83, width=80)

        self.entradaEndereco_emp = Listbox(self.janelaEmp, height=1)
        self.entradaEndereco_emp.place(x=85, y=83, width=300)

        #  Descrição e Entrada Bairro
        descrBairro = LabelGlac(self.janelaEmp, "Bairro")
        descrBairro.place(x=10, y=103, width=80)

        self.entradaBairro_emp = Listbox(self.janelaEmp, height=1)
        self.entradaBairro_emp.place(x=85, y=103, width=300)

        #  Descrição e Entrada Municipio
        descrMunicipio = LabelGlac(self.janelaEmp, "Cidade")
        descrMunicipio.place(x=10, y=123, width=80)

        self.entradaMunicipio_emp = Listbox(self.janelaEmp, height=1)
        self.entradaMunicipio_emp.place(x=85, y=123, width=220)

        #  Descrição e Entrada UF
        descrUf = LabelGlac(self.janelaEmp, "Uf")
        descrUf.place(x=315, y=123, width=30)

        self.entradaUf_emp = Listbox(self.janelaEmp, height=1)
        self.entradaUf_emp.place(x=350, y=123, width=30)

        #  Descrição e Entrada Fone
        descrFone = LabelGlac(self.janelaEmp, "Fone")
        descrFone.place(x=10, y=143, width=80)

        self.entradaFone_emp = Listbox(self.janelaEmp, height=1)
        self.entradaFone_emp.place(x=85, y=143, width=140)

        #  Descrição e Entrada Cep
        descrCep = LabelGlac(self.janelaEmp, "Cep")
        descrCep.place(x=230, y=143, width=40)

        self.entradaCep_emp = Listbox(self.janelaEmp, height=1)
        self.entradaCep_emp.place(x=270, y=143, width=115)

        #  Descrição e Entrada Cpf
        descrCpf = LabelGlac(self.janelaEmp, "Cnpj")
        descrCpf.place(x=10, y=163, width=80)

        self.entradaCpf_emp = Listbox(self.janelaEmp, height=1)
        self.entradaCpf_emp.place(x=85, y=163, width=140)

        #  Descrição e Entrada Rg
        descrRg = LabelGlac(self.janelaEmp, "Cpf")
        descrRg.place(x=230, y=163, width=40)

        self.entradaRg_emp = Listbox(self.janelaEmp, height=1)
        self.entradaRg_emp.place(x=270, y=163, width=115)

        #  Descrição e Entrada Obs
        descrObs = LabelGlac(self.janelaEmp, "Obs")
        descrObs.place(x=10, y=193, width=80)

        self.entradaObs_emp = Listbox(self.janelaEmp, height=1)
        self.entradaObs_emp.place(x=85, y=193, width=300)

        self.conecta_Glac()

        lista = self.cursor.execute("""SELECT cod_emp FROM empresa; """)
        for i in lista:
            self.entradaCod_emp.insert(i, END)

        self.desconecta_Glac()

        self.carrega_empresa()
        self.janelaEmp.mainloop()
    def busca_fornecE(self):
        self.conecta_Glac()
        ### Widgets - Listar tecnicos ###
        self.entradaFornec.insert(END, '%')
        veicAuto = self.entradaFornec.get()

        self.listatec = Tk()
        self.listatec.title("Fornecedores - GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("310x240+150+180")
        self.listatec.resizable(FALSE, FALSE)

        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10, column=("col1", "col2"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text="Cod")
        self.listatec1.heading("#2", text="Fornecedor")

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=60)
        self.listatec1.column("#2", width=220)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.listatec, orient='vertical',
                               command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=280, y=12, width=25, height=220)

        self.listatec1.place(x=5, y=5)

        self.cursor.execute("""SELECT cod_forn, fornecedor 
            FROM fornecedores ORDER BY fornecedor ASC""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)

            # Binding da listbox
        self.listatec1.bind('<Double-1>', self.add_autobind)

        self.entradaFornec.delete(0, END)
        self.entradaIdFornec.delete(0, END)
        self.desconecta_Glac()
    def busca_marcaE(self):
        self.conecta_Glac()
        ### Widgets - Listar tecnicos ###

        self.entradaMarcaprod.insert(END, '%')

        veicAuto = self.entradaMarcaprod.get()

        self.listatec = Tk()
        self.listatec.title("Marcas - GLAC  ")
        self.listatec.geometry("310x240+150+180")
        self.listatec.resizable(FALSE, FALSE)

        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10,
                                      column=("col1", "col2"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text="Cod")
        self.listatec1.heading("#2", text="Marca")

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=60)
        self.listatec1.column("#2", width=220)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.listatec, orient='vertical',
                               command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=280, y=6, width=30, height=225)

        self.listatec1.place(x=5, y=5)

        self.cursor.execute("""
            SELECT cod_marca, marca FROM marcaprod ORDER BY marca ASC""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)

            # Binding da listbox
        self.listatec1.bind('<Double-1>', self.add_autobind2)

        self.entradaMarcaprod.delete(0, END)
        self.entradaIdMarcaprod.delete(0, END)
        self.desconecta_Glac()
    def pagaOrdem(self):
        self.sel_lists_tps()
        self.janelaPagOrc = Toplevel(self.window_one)
        self.janelaPagOrc.title("GlacX - Formas de Pagamento")
        self.janelaPagOrc.geometry("800x420+100+150")
        self.janelaPagOrc.resizable(FALSE, FALSE)
        self.janelaPagOrc.transient(self.window_one)
        self.janelaPagOrc.focus_force()


        ###  Frame Moldura
        frame3 = GradientFrame(self.janelaPagOrc)
        frame3.configure(background='gray50')
        frame3.place(relwidth=1, relheight=1)

        # Label do numero de atendimento
        labelNumAtend = LabelGlac(self.janelaPagOrc, "NumAtend")
        labelNumAtend.place(relx=0.03, rely=0.01, relwidth=0.17, height=20)

        # Entry do numero de atendimento
        self.entryNumAtend = Listbox(self.janelaPagOrc, height=1)
        self.entryNumAtend.configure(bg='lightgray', font=('Verdana', '8', 'bold'))
        self.entryNumAtend.place(relx=0.17, rely=0.01, width=80, height=20)

        # Label do valor total
        labelValorTotal = LabelGlac(frame3, "Valor Total")
        labelValorTotal.place(relx=0.03, rely=0.06, relwidth=0.17, height=20)

        # Entry do valor total
        self.text = self.entradatotal.get()
        self.text = self.text.replace("R$","").replace("(","").replace(")","")
        self.text = float(self.text)
        self.text = f'{self.text:.2f}'
        self.entryValorTotal = Entry(frame3)
        self.entryValorTotal.place(relx=0.17, rely=0.06, width=80, height=20)
        self.entryValorTotal.insert(END, self.text)

        ### Label do valor a ser inserido
        labelValor = LabelGlac(frame3, "Valor")
        labelValor.place(relx=0.475, rely=0.01, width=80, height=20)
        labelCifrao = LabelGlac(frame3, "R$")
        labelCifrao.place(relx=0.475, rely=0.05, width=20, height=25)

        #### Entry do valor a ser inserido
        self.entryValor = Entry(frame3)
        self.entryValor.configure(validate='key')
        self.entryValor.place(relx=0.5, rely=0.06, width=60, height=20)
        self.entryValor.insert(END, f'{00.00:.2f}')

        # Listbox do tipo de pagamento
        self.listtipopag = StringVar()
        self.listtipopag.set("Dinheiro")

        self.popupMenu = OptionMenu(frame3, self.listtipopag, *self.tipos_pag)
        self.popupMenu.place(relx=0.588, rely=0.06, width=100, height=22)

        tipopaglabel = LabelGlac(frame3, "Tipo Pagamento")
        tipopaglabel.place(relx=0.588, rely=0.01, width=100, height=20)

        #### Data frame
        framedata = LabelGlac(frame3, 'Data')
        framedata.place(relx=0.72, rely=0.01, width=100, height=20)
        self.data_forma_pag = DateEntry(frame3, locale='pt_BR')
        self.data_forma_pag.place(relx=0.72, rely=0.06, width=100, height=22)

        #### Button Inserir Registro
        btinserir3 = ButtonGlac(frame3, "Inserir", self.add_pag)
        btinserir3.place(relx=0.86, rely=0.04, width=90, height=35)

        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(frame3, height=14,
            column=("col1", "col2", "col3", "col4", "col5", "col6", "col7"))
        self.listaPag.heading("#0", text="")
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text='O.S')
        self.listaPag.column("#1", width=50)
        self.listaPag.heading("#2", text="Tipo")
        self.listaPag.column("#2", width=130)
        self.listaPag.heading("#3", text="Valor Pagamento")
        self.listaPag.column("#3", width=160)
        self.listaPag.heading("#4", text="ValorDeduzir")
        self.listaPag.column("#4", width=140)
        self.listaPag.heading("#5", text="Data")
        self.listaPag.column("#5", width=100)
        self.listaPag.heading("#6", text="Pago")
        self.listaPag.column("#6", width=78)
        self.listaPag.heading("#7", text="")
        self.listaPag.column("#7", width=78)
        self.listaPag.place(relx=0.03, rely=0.12)

        # Cria barra de rolagem
        self.barraMov = ttk.Scrollbar(frame3, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.952, rely=0.124, width=20, height=300)

        self.listaPag.bind("<Double-1>", self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        ### Label do saldo a ser pago
        labelValor = LabelGlac(frame3, "ValorDevido")
        labelValor.place(x=640, y=365, width=100, height=25)
        labelCifrao = LabelGlac(frame3, "R$")
        labelCifrao.place(x=640, y=385, width=30, height=25)

        #### Entry do saldo a ser pago
        self.entryValorDevido = Entry(frame3)
        self.entryValorDevido.configure(validate="key")
        self.entryValorDevido.place(x=670, y=385, width=70, height=25)

        ### Label do saldo ja pago
        labelValor2 = LabelGlac(frame3, "Valor Pago")
        labelValor2.place(x=500, y=365, width=100, height=25)
        labelCifrao2 = LabelGlac(frame3, "R$")
        labelCifrao2.place(x=500, y=385, width=30, height=25)

        #### Entry do saldo ja pago
        self.entryValorInform = Entry(frame3)
        self.entryValorInform.configure(validate="key")
        self.entryValorInform.place(x=530, y=385, width=70, height=25)
        self.sel_pag_ordem()

        self.janelaPagOrc.mainloop()
    def OnDoubleClickpag(self, event):
        self.listaPag.selection()
        self.janPag2 = Toplevel()
        self.janPag2.title("GlacX")
        self.janPag2.geometry("590x60+170+300")
        self.janPag2.configure(background='gray55')
        self.janPag2.resizable(FALSE, FALSE)
        self.janPag2.transient(self.janelaPagOrc)
        self.janPag2.focus_force()
        self.janPag2.grab_set()

        ###  Frame Moldura
        frame3 = GradientFrame(self.janPag2).place(relwidth=1, relheight=1)

        ## Entry NUm Atend
        label1 = LabelGlac(self.janPag2, "Nº O.S")
        label1.place(x=5, y=8, width=50, height=25)

        self.entry1 = Listbox(self.janPag2, width=8, height=1)
        self.entry1.place(x=5, y=30, width=50, height=25)

        #### Listbox do tipo de pagamento
        labelTipopag2 = LabelGlac(self.janPag2, "Tipo de Pagamento")
        labelTipopag2.place(x=65, y=8, width=130, height=25)

        self.entry2 = StringVar()
        self.entry2V = {"Debito", "Credito", "Dinheiro", "Boleto",
            "ChequePre", "ChequeVista", "Crediario", "Promissoria",
            "Desconto", "Avista"}
        self.entry2V = sorted(self.entry2V)
        self.popupMenu = OptionMenu(self.janPag2, self.entry2, *self.entry2V)
        self.popupMenu.place(x=65, y=30, width=130, height=25)

        #### Valor da parcela
        label1 = LabelGlac(self.janPag2, "Valor")
        label1.place(x=205, y=8, width=80, height=25)

        self.entry3 = Entry(self.janPag2)
        self.entry3.place(x=205, y=30, width=80, height=25)

        ### dia
        label1 = LabelGlac(self.janPag2, "Data/Pagam")
        label1.place(x=295, y=8, width=120, height=25)

        self.entry4 = DateEntry(self.janPag2, locale='pt_BR')
        self.entry4.place(x=295, y=30, width=120, height=25)

        ### Pago?
        label1 = LabelGlac(self.janPag2, "Pago")
        label1.place(x=425, y=8, width=65, height=25)

        self.entry7 = StringVar()
        self.entry7V = {"Sim", "Nao"}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set("Sim")
        self.popupMenu = OptionMenu(self.janPag2, self.entry7, *self.entry7V)
        self.popupMenu.place(x=425, y=30, width=65, height=25)

        ### Alterar registro
        button5 = ButtonGlac(self.janPag2, "Alterar", self.mud_pag)
        button5.place(x=500, y=25, height=33)

        self.entry9 = Entry(self.janPag2)

        for n in self.listaPag.selection():
            col1, col2, col3, col4, col5, col6, col7 = self.listaPag.item(n, 'values')
            self.entry1.insert(END, col1)
            self.entry2.set(col2)
            self.entry3.insert(END, col4)
            self.entry4.delete(0, END)
            self.entry4.insert(END, col5)
            self.entry7.set(col6)
            self.entry9.insert(END, col7)

        self.janPag2.mainloop()
    def procedServ(self):
        ### Widgets - Listar Orçamentos ###
        self.listaOrc = Toplevel()
        self.listaOrc.title(" GLAC  ")
        self.listaOrc.geometry("300x100+110+100")
        self.listaOrc.configure(background="gray50")
        self.listaOrc.resizable(FALSE, FALSE)
        self.listaOrc.transient(self.window_one)
        self.listaOrc.focus_force()
        self.listaOrc.grab_set()

        frame_win = GradientFrame(self.listaOrc).place(relwidth=1, relheight=1)

        MensLabel = LabelGlac(self.listaOrc, "Atualizar valor hora")
        MensLabel.place(relx=0.1, rely=0.1, relwidt=0.8)

        self.listaNomeO = Entry(self.listaOrc)
        self.listaNomeO.place(relx=0.2, rely=0.6, width=80, height=27)

        botaoBuscaNome = ButtonGlac(self.listaOrc, "Atualizar", self.procedServF)
        botaoBuscaNome.place(relx=0.5, rely=0.6, height=35)
    def procedServF(self):
        valorServ = self.listaNomeO.get()
        Serv = 's'
        self.conecta_Glac()
        self.cursor.execute("""UPDATE servprod SET valor = ? WHERE sp = ?""", (valorServ, Serv))
        self.conn.commit()

        self.desconecta_Glac()
        msg = "Valor atualizado com sucesso.\n "
        messagebox.showinfo("GLAC", msg)
        self.listaOrc.destroy()