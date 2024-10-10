import customtkinter
from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class CadCli:
    def customer_registration(self):
        self.open_win_cli = "cadcli"
        self.janelaCli = customtkinter.CTkToplevel(self.window_one)
        self.janelaCli.title("Cadastro de Clientes")
        self.janelaCli.configure(background='#456E96')
        self.janelaCli.geometry("890x670+70+30")
        self.janelaCli.resizable(FALSE, FALSE)
        self.janelaCli.minsize(width=820, height=650)
        self.janelaCli.transient(self.window_one)
        self.janelaCli.focus_force()
        self.janelaCli.configure(bg='#37586B')

        tit_cli = customtkinter.CTkLabel(self.janelaCli, text="Cadastro do Cliente")
        tit_cli.place(relx=0.01, rely=0.02, relwidth=0.65, relheight=0.03)

        tit_cli = customtkinter.CTkLabel(self.janelaCli, text="Pesquisa Cliente")
        tit_cli.place(relx=0.67, rely=0.02, relwidth=0.32, relheight=0.03)

        framecli = customtkinter.CTkFrame(self.janelaCli, border_color="#7f5af0",
                                              corner_radius=12, border_width=2)
        framecli.place(relx=0.01, rely=0.05, relwidth=0.65, relheight=0.93)

        framelistcli = customtkinter.CTkFrame(self.janelaCli, border_color="#7f5af0",
                                              corner_radius=12, border_width=2)
        framelistcli.place(relx=0.67, rely=0.05, relwidth=0.32, relheight=0.93)

        tituloVeiculos = customtkinter.CTkLabel(self.janelaCli, text="Veiculos do Cliente")
        tituloVeiculos.place(relx=0.03, rely=0.56, relwidth=0.61, relheight=0.03)

        # 'Entry Código'
        self.PesquisaCliente = customtkinter.CTkEntry(self.janelaCli)
        self.PesquisaCliente.place(relx=0.73, rely=0.1, relwidth=0.2, relheight=0.03)

        #  Botao busca Cabeça
        botaobusca = customtkinter.CTkButton(self.janelaCli, text=u'\u2315', command=self.busca_clienteC)
        botaobusca.place(relx=0.69, rely=0.09, relwidth=0.04, relheight=0.05)


        # 'Label Codigo'
        codPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Codigo")
        codPeLabel.place(relx=0.02, rely=0.07, relwidth=0.05, relheight=0.03)

        # 'Entry Código'
        self.codPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.codPeEntry.configure(validate="key", validatecommand=self.vcmd8)
        self.codPeEntry.place(relx=0.02, rely=0.1, relwidth=0.05, relheight=0.03)

        # 'Label Data de Nascimento'
        nascPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Nasc")
        nascPeLabel.place(relx=0.38, rely=0.15, relwidth=0.1, relheight=0.03)

        # 'Entry Dia'
        self.nascDiaPeEntry = DateEntry(self.janelaCli, locale="pt_BR", fg='gray45')
        self.nascDiaPeEntry.place(relx=0.38, rely=0.18, relwidth=0.1, relheight=0.03)

        # 'Label Cpf'
        self.cnpj_mat_str = StringVar()
        self.cnpj_mat_strV = {"CNPJ", "CPF"}
        self.cnpj_mat_str.set("CNPJ")
        self.cnpj_mat_lb = OptionMenu(self.janelaCli, self.cnpj_mat_str, *self.cnpj_mat_strV)
        self.cnpj_mat_lb.place(relx=0.49, rely=0.15, relwidth=0.16, relheight=0.03)

        self.cnpj_mat_ent = customtkinter.CTkEntry(self.janelaCli)
        self.cnpj_mat_ent.configure(validate="key")
        self.cnpj_mat_ent.bind("<KeyRelease>", self.format_cpf_cnpj)
        self.cnpj_mat_ent.place(relx=0.49, rely=0.18, relwidth=0.16, relheight=0.03)

        # 'Label Nome do Cliente'
        nomePeLabel = customtkinter.CTkLabel(self.janelaCli, text="Nome")
        nomePeLabel.place(relx=0.02, rely=0.15, relwidth=0.35, relheight=0.03)

        # 'Entry Nome Do Cliente'
        self.nomePeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.nomePeEntry.place(relx=0.02, rely=0.18, relwidth=0.35, relheight=0.03)

        # 'Label Logradouro'
        logradPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Endereco")
        logradPeLabel.place(relx=0.02, rely=0.23, relwidth=0.35, relheight=0.03)

        # 'Entry Logradouro'
        self.logradPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.logradPeEntry.place(relx=0.02, rely=0.26, relwidth=0.35, relheight=0.03)

        # 'Label Numero'
        numPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Numero")
        numPeLabel.place(relx=0.38, rely=0.23, relwidth=0.06, relheight=0.03)

        # 'Entry Numero'
        self.numPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.numPeEntry.place(relx=0.38, rely=0.26, relwidth=0.06, relheight=0.03)

        # 'Label Complemento'
        complemPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Complemento")
        complemPeLabel.place(relx=0.45, rely=0.23, relwidth=0.2, relheight=0.03)

        # 'Entry Complemento'
        self.complemPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.complemPeEntry.place(relx=0.45, rely=0.26, relwidth=0.2, relheight=0.03)

        # 'Label Cep'
        cepPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Cep")
        # cepPeLabel.place(relx=0.02, rely=0.4, relwidth=0.11, relheight=0.02)

        # 'Botao Cep'
        cepPeBt = customtkinter.CTkButton(self.janelaCli, text='Cep', command=self.cep)
        cepPeBt.place(relx=0.02, rely=0.3, relwidth=0.1, relheight=0.04)

        # 'Entry Cep'
        self.cepPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.cepPeEntry.configure(validate="key", validatecommand=self.vcmd8)
        self.cepPeEntry.place(relx=0.02, rely=0.34, relwidth=0.1, relheight=0.03)

        # 'Label Bairro'
        bairroPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Bairro")
        bairroPeLabel.place(relx=0.13, rely=0.31, relwidth=0.2, relheight=0.03)

        # 'Entry Bairro'
        self.bairroPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.bairroPeEntry.place(relx=0.13, rely=0.34, relwidth=0.2, relheight=0.03)

        # 'Label Municipio'
        cidadePeLabel = customtkinter.CTkLabel(self.janelaCli, text="Cidade")
        cidadePeLabel.place(relx=0.34, rely=0.31, relwidth=0.25, relheight=0.03)

        # 'Entry Municipio'
        self.cidadePeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.cidadePeEntry.place(relx=0.34, rely=0.34, relwidth=0.25, relheight=0.03)

        # 'Label UF'
        ufPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Uf")
        ufPeLabel.place(relx=0.61, rely=0.31, relwidth=0.04, relheight=0.03)

        # 'Entry UF'
        self.ufPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.ufPeEntry.place(relx=0.61, rely=0.34, relwidth=0.04, relheight=0.03)

        # 'Label Fone'
        fone1Pelabel = customtkinter.CTkLabel(self.janelaCli, text='Telefone Principal')
        fone1Pelabel.place(relx=0.02, rely=0.39, relwidth=0.13, relheight=0.03)

        # 'Entry Fone 1'
        self.fone1PeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.fone1PeEntry.configure(validatecommand=self.vcmd2, validate="key")
        self.fone1PeEntry.place(relx=0.02, rely=0.42, relwidth=0.03, relheight=0.03)

        self.fone1PeEntry2 = customtkinter.CTkEntry(self.janelaCli)
        self.fone1PeEntry2.configure(validatecommand=self.vcmd12, validate="key")
        self.fone1PeEntry2.place(relx=0.05, rely=0.42, relwidth=0.1, relheight=0.03)

        # 'Label Fone 2'
        fone2Pelabel = customtkinter.CTkLabel(self.janelaCli, text='Telefone Secundário')
        fone2Pelabel.place(relx=0.16, rely=0.39, relwidth=0.13, relheight=0.03)

        # 'Entry Fone 2'
        self.fone2PeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.fone2PeEntry.configure(validate="key", validatecommand=self.vcmd2)
        self.fone2PeEntry.place(relx=0.16, rely=0.42, relwidth=0.03, relheight=0.03)

        self.fone2PeEntry2 = customtkinter.CTkEntry(self.janelaCli)
        self.fone2PeEntry2.configure(validate="key", validatecommand=self.vcmd12)
        self.fone2PeEntry2.place(relx=0.19, rely=0.42, relwidth=0.1, relheight=0.03)

        # 'Entry RG'
        self.rgPeEntry = Entry(self.janelaCli)

        # 'Label Obs'
        obsPeLabel = customtkinter.CTkLabel(self.janelaCli, text="Obs")
        obsPeLabel.place(relx=0.3, rely=0.39, relwidth=0.17, relheight=0.03)

        # 'Entry Obs'
        self.obsPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.obsPeEntry.place(relx=0.3, rely=0.42, relwidth=0.17, relheight=0.03)

        # 'Label E-mail'
        emailPeLabel = customtkinter.CTkLabel(self.janelaCli, text='E-mail')
        emailPeLabel.place(relx=0.48, rely=0.39, relwidth=0.17, relheight=0.03)

        # 'Entry E-mail'
        self.emailPeEntry = customtkinter.CTkEntry(self.janelaCli)
        self.emailPeEntry.place(relx=0.48, rely=0.42, relwidth=0.17, relheight=0.03)



        # 'Botao Abrir atendimento
        botaoOpen = customtkinter.CTkButton(self.janelaCli, text="Abre O.S", command=self.carrega_cliente3, corner_radius=12)
        botaoOpen.place(relx=0.02, rely=0.5, relwidth=0.09, relheight=0.04)
        # 'Botao Novo Cliente'
        botaoAdd = customtkinter.CTkButton(self.janelaCli, text="Novo", command=self.add_clienteC, corner_radius=12)
        botaoAdd.place(relx=0.12, rely=0.5, relwidth=0.08, relheight=0.04)
        # Botao Altera dados do Cliente
        botaoMud = customtkinter.CTkButton(self.janelaCli, text="Alterar", command=self.mud_clienteC, corner_radius=12)
        botaoMud.place(relx=0.2, rely=0.5, relwidth=0.08, relheight=0.04)
        # Botao deletar dados do Cliente
        botaoDel = customtkinter.CTkButton(self.janelaCli, text="Apagar", command=self.deletar_window_c, corner_radius=12)
        botaoDel.place(relx=0.28, rely=0.5, relwidth=0.08, relheight=0.04)
        #  Botao limpa
        botaolimpa = customtkinter.CTkButton(self.janelaCli, text="Fechar", command=self.limpa_clienteC, corner_radius=12)
        botaolimpa.place(relx=0.37, rely=0.5, relwidth=0.08, relheight=0.04)

        self.barracliente = ttk.Scrollbar(framelistcli, orient='vertical', command=self.OnVsbC)
        self.listaServ = ttk.Treeview(framelistcli, height=6,
            yscrollcommand=self.barracliente.set, column=("col1", "col2"))

        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=1)
        self.listaServ.heading("#1", text="Codigo")
        self.listaServ.column("#1", width=40)
        self.listaServ.heading("#2", text="Nome")
        self.listaServ.column("#2", width=185)

        self.listaServ.place(relx=0.05, rely=0.15, relwidth=0.85, relheight=0.75)
        self.listaServ.configure(yscroll=self.barracliente.set)
        self.barracliente.place(relx=0.9, rely=0.15, relheight=0.75)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickC)
        self.list_cadcli()

        # Moldura veiculos
        self.entradaVeiculo2 = customtkinter.CTkEntry(self.janelaCli)
        self.entradaMontadora2 = customtkinter.CTkEntry(self.janelaCli)
        self.codEquipEntry = customtkinter.CTkEntry(self.janelaCli)
        self.fabrModeloEquipEntry = customtkinter.CTkEntry(self.janelaCli)
        self.nomeIdEquipEntry = customtkinter.CTkEntry(self.janelaCli)

        serialEquipLabel = customtkinter.CTkLabel(self.janelaCli, text="Placa")
        serialEquipLabel.place(relx=0.03, rely=0.6, relwidth=0.09, relheight=0.04)

        self.serialEquipEntry = customtkinter.CTkEntry(self.janelaCli)
        self.serialEquipEntry.place(relx=0.03, rely=0.64, relwidth=0.09, relheight=0.04)

        ##### Veiculo
        descrVeiculo = customtkinter.CTkButton(self.janelaCli, text="Veiculo", command=self.busca_auto_c)
        descrVeiculo.place(relx=0.13, rely=0.6, relwidth=0.13, relheight=0.04)
        self.nomeEquipEntry = customtkinter.CTkEntry(self.janelaCli)
        self.nomeEquipEntry.place(relx=0.13, rely=0.64, relwidth=0.13, relheight=0.04)

        marcaEquipLabel = customtkinter.CTkLabel(self.janelaCli, text="Marca")
        marcaEquipLabel.place(relx=0.27, rely=0.6, relwidth=0.11, relheight=0.04)

        self.marcaEquipEntry = customtkinter.CTkEntry(self.janelaCli)
        self.marcaIdEquipEntry = customtkinter.CTkEntry(self.janelaCli)
        self.marcaEquipEntry.place(relx=0.27, rely=0.64, relwidth=0.11, relheight=0.04)

        corEquipLabel = customtkinter.CTkLabel(self.janelaCli, text="Cor")
        corEquipLabel.place(relx=0.39, rely=0.6, relwidth=0.09, relheight=0.04)

        self.corvar = StringVar(self.janelaCli)
        self.coresV = {"Branco", "Amarelo", "Verde",
                       "Bege", "Azul", "Laranja",
                       "Vermelho", "Verde", "Cinza",
                       "Preto", "Marrom", "Bordo",
                       "Prata", "Grafite", "Dourado",
                       "Outro"}

        self.corvar.set("Branco")

        self.popupMenu = OptionMenu(self.janelaCli, self.corvar, *self.coresV)
        self.popupMenu.place(relx=0.39, rely=0.64, relwidth=0.09, relheight=0.04)

        combEquipLabel = customtkinter.CTkLabel(self.janelaCli, text="Combustivel")
        combEquipLabel.place(relx=0.49, rely=0.6, relwidth=0.1, relheight=0.04)

        self.combvar = StringVar()
        self.combV = {"Gasolina", "Alcool", "Diesel",
                      "Flex", "Gasolina_e_Gas", "Alcool_e_Gas",
                      "Flex_e_Gas"}
        self.combvar.set("Gasolina")

        self.popupMenu = OptionMenu(self.janelaCli, self.combvar, *self.combV)
        self.popupMenu.place(relx=0.49, rely=0.64, relwidth=0.1, relheight=0.04)

        # Label Ano
        fab_ano_eq_lb = customtkinter.CTkLabel(self.janelaCli, text="Ano")
        fab_ano_eq_lb.place(relx=0.6, rely=0.6, relwidth=0.05, relheight=0.04)
        # Entry Ano
        self.fabrAnoEquipEntry = customtkinter.CTkEntry(self.janelaCli)
        self.fabrAnoEquipEntry.place(relx=0.6, rely=0.64, relwidth=0.05, relheight=0.04)

        #  Botoes automoveis
        botaoAdd2 = customtkinter.CTkButton(self.janelaCli, text="Novo", command=self.add_veiculoC
                                            ,corner_radius=12)
        botaoAdd2.place(relx=0.02, rely=0.92, relwidth=0.07, relheight=0.04)

        botaoMud2 = customtkinter.CTkButton(self.janelaCli, text="Alterar", command=self.mud_autoC
                                            ,corner_radius=12)
        botaoMud2.place(relx=0.1, rely=0.92, relwidth=0.07, relheight=0.04)

        botaoDel2 = customtkinter.CTkButton(self.janelaCli, text="Apagar", command=self.deletar_window_placa_c
                                            ,corner_radius=12)
        botaoDel2.place(relx=0.18, rely=0.92, relwidth=0.07, relheight=0.04)

        self.listaPlaca = ttk.Treeview(self.janelaCli, height=5,
            column=("col1", "col2", "col3", "col4", "col5", "col6"))
        self.listaPlaca.heading("#0", text="")
        self.listaPlaca.column("#0", width=0)
        self.listaPlaca.heading("#1", text="Placa")
        self.listaPlaca.column("#1", width=60)
        self.listaPlaca.heading("#2", text="Veiculo")
        self.listaPlaca.column("#2", width=100)
        self.listaPlaca.heading("#3", text="Montadora")
        self.listaPlaca.column("#3", width=100)
        self.listaPlaca.heading("#4", text="Cor")
        self.listaPlaca.column("#4", width=80)
        self.listaPlaca.heading("#5", text="Combustivel")
        self.listaPlaca.column("#5", width=80)
        self.listaPlaca.heading("#6", text="Ano")
        self.listaPlaca.column("#6", width=60)

        # Cria barra de rolagem
        self.barra = Scrollbar(self.janelaCli, orient='vertical', command=self.listaPlaca.yview)
        # Adiciona barra de rolagem
        self.listaPlaca.configure(yscroll=self.barra.set)
        self.barra.place(relx=0.63, rely=0.703, relwidth=0.02, relheight=0.2)

        self.listaPlaca.place(relx=0.02, rely=0.7, relwidth=0.62, relheight=0.2)
        #    Binding da listbox
        self.listaPlaca.bind('<Double-1>', self.bind_autoC)

        framecli = GradientFrame(self.janelaCli, "gray10", "gray10")
        framecli.place(relx=0, rely=0, relwidth=0.01, relheight=1)

        self.janelaCli.mainloop()
    def list_cadcli(self):
        self.conecta_Glac()
        self.lista1 = self.cursor.execute("""SELECT  cod_cli, nome
                    FROM clientes  ORDER BY nome ASC; """)
        for i in self.lista1:
            self.listaServ.insert("", END, values=i)
        self.desconecta_Glac()
    def add_autobindC(self, event):
        # codServ1.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.listatec1.selection()
        for n in self.listatec1.selection():
            col1, col2, col3 = self.listatec1.item(n, 'values')
            self.nomeEquipEntry.insert(END, col2)
            self.marcaEquipEntry.insert(END, col3)
            self.entradaVeiculo2.insert(END, col1)

        cod = self.entradaVeiculo2.get()

        self.conecta_Glac()

        self.cursor.execute(
            """SELECT montad FROM automoveis WHERE cod_aut LIKE '%s'""" % cod)
        addservico1cod = self.cursor.fetchall()
        for i in addservico1cod:
            self.marcaEquipEntry.insert(END, i)

        self.desconecta_Glac()
        self.listatec.destroy()
    def add_clienteC(self):
        self.conecta_Glac()
        self.listaServ.delete(*self.listaServ.get_children())
        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""INSERT INTO clientes 
        (nome, nascdia, endereco, numcasa, complemento, bairro, 
        municipio, uf, fone1ddd, fone1, fone2ddd, fone2, cep, cpf, email, obs)
        VALUES ( ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        (self.cadcli_nome, self.cadcli_nascdia,
         self.cadcli_endereco, self.cadcli_numcasa, self.cadcli_complemento,
         self.cadcli_bairro, self.cadcli_municipio, self.cadcli_uf, self.cadcli_fone1ddd,
         self.cadcli_fone1, self.cadcli_fone2ddd, self.cadcli_fone2, self.cadcli_cep,
         self.cadcli_cpf, self.cadcli_email, self.cadcli_obs))
        self.conn.commit()

        msg = "Cadastro de cliente salvo"
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.limpa_clienteC()
        self.desconecta_Glac()

        self.list_cadcli()
    def add_veiculoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()
        motor = '0'
        self.conecta_Glac()
        self.cursor.execute("""INSERT INTO frota ( idcliente, placa, veiculo, montadora, 
        ano, combust, cor) VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
        (self.cadcli_cod, self.cadcli_placa, self.cadcli_montadora, self.cadcli_veiculo,
         self.cadcli_ano, self.cadcli_combust, self.cadcli_cor))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
        FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        msg = self.m_msgAutAdd
        messagebox.showinfo("GLAC ", msg)
    def busca_clienteC(self):
        self.conecta_Glac()
        self.listaServ.delete(*self.listaServ.get_children())

        self.PesquisaCliente.insert(END, '%')
        nome = self.PesquisaCliente.get()
        self.cursor.execute("""SELECT cod_cli, nome FROM clientes 
        WHERE nome LIKE '%s' ORDER BY nome ASC""" % nome)
        buscanomecli = self.cursor.fetchall()
        for i in buscanomecli:
            self.listaServ.insert("", END, values=i)

        self.limpa_clienteC()
        self.desconecta_Glac()
    def bind_autoC(self, event):
        # codServ1.delete(0, END)
        global col1, col3, col2
        self.limpa_entryautoC()
        self.listaPlaca.selection()

        for n in self.listaPlaca.selection():
            col1, col2, col3, col4, col5, col6 = self.listaPlaca.item(n, 'values')

        self.serialEquipEntry.insert(END, col1)
        self.nomeEquipEntry.insert(END, col3)
        self.marcaEquipEntry.insert(END, col2)
        self.entradaVeiculo2.insert(END, 0)
        self.codEquipEntry.insert(END, 0)
        self.corvar.set(col4)
        self.combvar.set(col5)
        self.fabrAnoEquipEntry.insert(END, col6)
    def carrega_clienteC(self):
        cod_cli = self.codPeEntry.get()
        self.limpa_clienteC2()
        self.conecta_Glac()

        self.cursor.execute("""SELECT UPPER(nome), nascdia, numcasa, UPPER(complemento),
            UPPER(email), UPPER(endereco), UPPER(bairro), UPPER(municipio), UPPER(uf),
            fone1ddd, fone1, fone2ddd, fone2, cep, cpf, rg, UPPER(obs)
            FROM clientes WHERE cod_cli = '%s'""" % cod_cli)
        consultacli = self.cursor.fetchall()
        for i in consultacli:
            self.nomePeEntry.insert(END, i[0])
            self.nascDiaPeEntry.insert(END, i[1])
            self.numPeEntry.insert(END, i[2])
            self.complemPeEntry.insert(END, i[3])
            self.emailPeEntry.insert(END, i[4])
            self.logradPeEntry.insert(END, i[5])
            self.bairroPeEntry.insert(END, i[6])
            self.cidadePeEntry.insert(END, i[7])
            self.ufPeEntry.insert(END, i[8])
            self.fone1PeEntry.insert(END, i[9])
            self.fone1PeEntry2.insert(END, i[10])
            self.fone2PeEntry.insert(END, i[11])
            self.fone2PeEntry2.insert(END, i[12])
            self.cepPeEntry.insert(END, i[13])
            self.cnpj_mat_ent.insert(END, i[14])
            self.obsPeEntry.insert(END, i[16])

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
    	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)
        self.desconecta_Glac()
    def OnVsbC(self, *args):
        self.listaServ.yview(*args)
    def OnMouseWheelC(self, event):
        self.listaServ.yview("scroll", event.delta, "units")
        return "break"
    def OnDoubleClickC(self, *args):
        self.limpa_clienteC()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.codPeEntry.insert(END, col1)

        self.carrega_clienteC()
    def mud_autoC(self):
        self.variaveisCliente()
        self.variaveisVeiculo()

        cod_cli = self.codPeEntry.get()
        self.conecta_Glac()

        self.cursor.execute(""" UPDATE frota SET veiculo = ?, ano = ?, placa = ?,
            idcliente = ?, combust = ?, montadora = ?, cor = ? WHERE placa = ? AND idcliente = ?""",
                            (self.cadcli_veiculo, self.cadcli_ano, self.cadcli_placa, cod_cli,
                             self.cadcli_combust, self.cadcli_montadora,
                             self.cadcli_cor, self.cadcli_placa, cod_cli))
        self.conn.commit()

        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.entradaVeiculo2.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.entradaMontadora2.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
            	    FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)

        self.desconecta_Glac()
        msg = self.m_msgVeiculoAlt
        msg += ""
        messagebox.showinfo("GLAC ", msg)
        self.carrega_clienteC()
    def mud_clienteC(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.conecta_Glac()

        self.variaveisCliente()
        self.variaveisVeiculo()

        self.cursor.execute("""UPDATE clientes SET nome = ?, endereco = ?, bairro = ?, 
        municipio = ?, uf = ?, cep = ?, cpf = ?, obs = ?, email = ?, fone1ddd = ?,
        fone1 = ?, fone2ddd = ?, fone2 = ?, complemento = ?, numcasa = ?, nascdia = ?
        WHERE cod_cli = ?""",(self.cadcli_nome, self.cadcli_endereco, self.cadcli_bairro,
        self.cadcli_municipio, self.cadcli_uf, self.cadcli_cep, self.cadcli_cpf,
        self.cadcli_obs, self.cadcli_email, self.cadcli_fone1ddd,
        self.cadcli_fone1, self.cadcli_fone2ddd, self.cadcli_fone2, self.cadcli_complemento,
        self.cadcli_numcasa, self.cadcli_nascdia, self.cadcli_cod))

        self.conn.commit()
        self.desconecta_Glac()

        self.list_cadcli()
        msg = "Dados alterados com sucesso"
        msg += ""
        messagebox.showinfo("GLAC - Clientes", msg)
    def limpa_entryautoC(self):
        self.serialEquipEntry.delete(0, END)
        self.nomeEquipEntry.delete(0, END)
        self.marcaEquipEntry.delete(0, END)
        self.fabrAnoEquipEntry.delete(0, END)
    def limpa_clienteC(self):
        self.codPeEntry.delete(0, END)
        self.limpa_clienteC2()
    def limpa_clienteC2(self):
        self.nomePeEntry.delete(0, END)
        self.nascDiaPeEntry.delete(0, END)
        self.logradPeEntry.delete(0, END)
        self.numPeEntry.delete(0, END)
        self.complemPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)
        self.fone1PeEntry.delete(0, END)
        self.fone1PeEntry2.delete(0, END)
        self.fone2PeEntry.delete(0, END)
        self.fone2PeEntry2.delete(0, END)
        self.cepPeEntry.delete(0, END)
        self.cnpj_mat_ent.delete(0, END)
        self.obsPeEntry.delete(0, END)
        self.emailPeEntry.delete(0, END)
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.limpa_entryautoC()
    def del_clienteC(self):
        cod_cli = self.codPeEntry.get()

        self.conecta_Glac()
        self.cursor.execute("""DELETE FROM frota WHERE idcliente=?""", (cod_cli,))
        self.conn.commit()

        self.cursor.execute("""DELETE FROM clientes WHERE cod_cli=?""", (cod_cli,))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaPlaca.delete(*self.listaPlaca.get_children())

        self.desconecta_Glac()
        self.list_cadcli()

        self.listaPlaca.delete(*self.listaPlaca.get_children())
        self.limpa_clienteC()
    def del_placaC(self):
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        cod_cli = self.codPeEntry.get()
        placa = self.serialEquipEntry.get()
        self.conecta_Glac()
        self.cursor.execute("""DELETE FROM frota 
        WHERE placa =? AND idcliente = ?""", (placa, cod_cli))
        self.conn.commit()
        self.listaPlaca.delete(*self.listaPlaca.get_children())
        self.cursor.execute("""SELECT placa, veiculo , montadora, cor, combust, ano
        FROM frota WHERE frota.idcliente = '%s' """ % cod_cli)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listaPlaca.insert("", END, values=row)
        self.desconecta_Glac()
        self.limpa_entryautoC()
        self.listatec.destroy()
    def variaveisCliente(self):
        self.cadcli_cod = self.codPeEntry.get()
        self.cadcli_nome = self.nomePeEntry.get()
        self.cadcli_nascdia = self.nascDiaPeEntry.get()
        self.cadcli_endereco = self.logradPeEntry.get()
        self.cadcli_numcasa = self.numPeEntry.get()
        self.cadcli_complemento = self.complemPeEntry.get()
        self.cadcli_bairro = self.bairroPeEntry.get()
        self.cadcli_municipio = self.cidadePeEntry.get()
        self.cadcli_uf = self.ufPeEntry.get()
        self.cadcli_fone1ddd = self.fone1PeEntry.get()
        self.cadcli_fone1 = self.fone1PeEntry2.get()
        self.cadcli_fone2ddd = self.fone2PeEntry.get()
        self.cadcli_fone2 = self.fone2PeEntry2.get()
        self.cadcli_cep = self.cepPeEntry.get()
        self.cadcli_cpf = self.cnpj_mat_ent.get()
        self.cadcli_email = self.emailPeEntry.get()
        self.cadcli_obs = self.obsPeEntry.get()
    def variaveisVeiculo(self):
        self.cadcli_veiculoId = self.codEquipEntry.get()
        self.cadcli_MontadoraId = self.entradaMontadora2.get()
        self.cadcli_veiculo = self.nomeEquipEntry.get()
        self.cadcli_ano = self.fabrAnoEquipEntry.get()
        self.cadcli_placa = self.serialEquipEntry.get()
        self.cadcli_montadora = self.marcaEquipEntry.get()
        self.cadcli_combust = self.combvar.get()
        self.cadcli_cor = self.corvar.get()
    def cep(self):
        self.logradPeEntry.delete(0, END)
        self.bairroPeEntry.delete(0, END)
        self.cidadePeEntry.delete(0, END)
        self.ufPeEntry.delete(0, END)

        cep = str(self.cepPeEntry.get())
        cep = cep[0:5] + "-" + cep[5:]
        cep = str(cep)
        try:
            endcep = brazilcep.get_address_from_cep(cep, webservice=WebService.APICEP)

            self.logradPeEntry.insert(END, endcep['street'])
            self.bairroPeEntry.insert(END, endcep['district'])
            self.cidadePeEntry.insert(END, endcep['city'])
            self.ufPeEntry.insert(END, endcep['uf'])

        except:
            messagebox.showinfo('Mensagem', 'Houve um erro ao procurar este CEP!!')
    def busca_auto_c(self, *args):
        # Widgets - Listar tecnicos #
        self.nomeEquipEntry.insert(END, '%')

        veicAuto = self.nomeEquipEntry.get()

        self.listatec = Toplevel()
        self.listatec.title(" GLAC  ")
        self.listatec.configure(background='gray75')
        self.listatec.geometry("405x235+100+150")
        self.listatec.resizable(FALSE, FALSE)
        self.listatec.transient(self.janelaCli)
        self.listatec.focus_force()
        self.listatec.grab_set()
        ##########
        self.listatec1 = ttk.Treeview(self.listatec, height=10,
            column=("col1", "col2", "col3"))
        self.listatec1.heading("#0", text="")
        self.listatec1.heading("#1", text='Cod')
        self.listatec1.heading("#2", text="Automovel")
        self.listatec1.heading("#3", text="Marca")

        self.listatec1.column("#0", width=0)
        self.listatec1.column("#1", width=40)
        self.listatec1.column("#2", width=180)
        self.listatec1.column("#3", width=150)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.listatec, orient='vertical',
                                   command=self.listatec1.yview)

        # Adiciona barra de rolagem
        self.listatec1.configure(yscroll=self.barra.set)
        self.barra.place(x=377, y=6, height=220)
        self.listatec1.place(x=5, y=5)
        self.conecta_Glac()
        self.cursor.execute("""SELECT cod_aut, automovel, marca 
        FROM automoveis, montadora WHERE montadora.cod = automoveis.montad
        AND automovel LIKE '%s' ORDER BY automovel ASC""" % veicAuto)
        rows = self.cursor.fetchall()
        for row in rows:
            self.listatec1.insert("", END, values=row)
        self.listatec1.bind('<Double-1>', self.add_autobindC)
        self.desconecta_Glac()
    def deletar_window_c(self):
        res = messagebox.askquestion('Deletar cliente', 'Deseja realmente deletar este registro?')
        if res == 'no':
            res = ''
        else:
            self.del_clienteC()
            messagebox.showinfo('Mensagem', 'Registro deletado com sucesso!!')
    def deletar_window_placa_c(self):
        res = messagebox.askquestion('Deletar veiculo', 'Deseja realmente deletar este registro?')
        if res == 'no':
            res = ''
        else:
            self.del_placaC()
            messagebox.showinfo('Mensagem', 'Registro deletado com sucesso!!')