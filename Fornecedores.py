import customtkinter
from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class CadForn:
    def cadforn(self):
        self.win_for = customtkinter.CTkToplevel()
        self.win_for.title("Fornecedores")
        self.win_for.configure(background="#6F87B0")
        self.win_for.geometry("705x270+100+250")
        self.win_for.resizable(FALSE, FALSE)
        self.win_for.transient(self.window_one)
        self.win_for.focus_force()
        self.open_win_cli = "cadfor"

        dscr_cd_for = customtkinter.CTkLabel(self.win_for, text="Codigo")
        dscr_cd_for.place(relx=0.01, rely=0.03, relwidth=0.1, relheight=0.07)

        self.entr_cd_for = customtkinter.CTkEntry(self.win_for)
        self.entr_cd_for.place(relx=0.11, rely=0.03, relwidth=0.05, relheight=0.07)

        # Fornecedor
        dscr_for = customtkinter.CTkLabel(self.win_for, text="Fornecedor")
        dscr_for.place(relx=0.01, rely=0.13, relwidth=0.1, relheight=0.07)

        self.entr_for = customtkinter.CTkEntry(self.win_for)
        self.entr_for.place(relx=0.11, rely=0.13, relwidth=0.27, relheight=0.07)

        # Fone
        dscr_fone = customtkinter.CTkLabel(self.win_for, text="Fone...")
        dscr_fone.place(relx=0.01, rely=0.23, relwidth=0.1, relheight=0.07)

        self.entr_fone = customtkinter.CTkEntry(self.win_for)
        self.entr_fone.place(relx=0.11, rely=0.23, relwidth=0.1, relheight=0.07)

        self.cnpj_mat_str = StringVar()
        self.cnpj_mat_strV = {"CNPJ", "CPF"}
        self.cnpj_mat_str.set("CNPJ")
        self.cnpj_mat_lb = OptionMenu(self.win_for, self.cnpj_mat_str, *self.cnpj_mat_strV)
        self.cnpj_mat_lb.place(relx=0.22, rely=0.23, relwidth=0.1, relheight=0.07)

        self.entr_cnpj = customtkinter.CTkEntry(self.win_for)
        self.entr_cnpj.configure(validate="key")
        self.entr_cnpj.bind("<KeyRelease>", self.format_cpf_cnpj)
        self.entr_cnpj.place(relx=0.32, rely=0.23, relwidth=0.16, relheight=0.07)

        self.entr_cep = customtkinter.CTkEntry(self.win_for)
        self.entr_cep.place(relx=0.11, rely=0.33, relwidth=0.1, relheight=0.07)

        dscr_end = customtkinter.CTkLabel(self.win_for, text="Endereco")
        dscr_end.place(relx=0.01, rely=0.43, relwidth=0.1, relheight=0.07)

        self.entr_end = customtkinter.CTkEntry(self.win_for)
        self.entr_end.place(relx=0.11, rely=0.43, relwidth=0.35, relheight=0.07)

        dscr_mun = customtkinter.CTkLabel(self.win_for, text="Cidade")
        dscr_mun.place(relx=0.01, rely=0.53, relwidth=0.1, relheight=0.07)

        self.entr_mun = customtkinter.CTkEntry(self.win_for)
        self.entr_mun.place(relx=0.11, rely=0.53, relwidth=0.35, relheight=0.07)

        dscr_obs = customtkinter.CTkLabel(self.win_for, text="Observacao")
        dscr_obs.place(relx=0.01, rely=0.63, relwidth=0.15, relheight=0.07)

        self.entr_dscr = customtkinter.CTkEntry(self.win_for)
        self.entr_dscr.place(relx=0.16, rely=0.63, relwidth=0.3, relheight=0.07)

        bt_ld_f = ButtonGlac(self.win_for, "Carregar", self.carrega_fornecedor)
        bt_ld_f.place(relx=0.17, rely=0, relwidth=0.11, relheight=0.13)

        bt_cl_f = ButtonGlac(self.win_for, "Limpar", self.limpa_fornecedor)
        bt_cl_f.place(relx=0.28, rely=0, relwidth=0.11, relheight=0.13)

        bt_busc_for = ButtonGlac(self.win_for, "Buscar", self.busca_fornecedor)
        bt_busc_for.place(relx=0.39, rely=0.11, relwidth=0.11, relheight=0.12)

        bt_cep_for = ButtonGlac(self.win_for, "Cep", self.cepForn)
        bt_cep_for.place(relx=0.01, rely=0.31, relwidth=0.1, relheight=0.11)

        bt_nv_for = ButtonGlac(self.win_for, "Novo", self.add_fornec)
        bt_nv_for.place(relx=0.1, rely=0.8, relwidth=0.1, relheight=0.13)

        bt_alt_for = ButtonGlac(self.win_for, "Alterar", self.mud_fornec)
        bt_alt_for.place(relx=0.2, rely=0.8, relwidth=0.1, relheight=0.13)

        bt_del_for = ButtonGlac(self.win_for, "Apagar", self.del_fornec)
        bt_del_for.place(relx=0.3, rely=0.8, relwidth=0.1, relheight=0.13)

        # Widgets - Listar
        self.list_g = ttk.Treeview(self.win_for, height=12, column=("col1", "col2", "col3", "col4"))
        self.list_g.heading("#0", text="")
        self.list_g.column("#0", width=0)
        self.list_g.heading("#1", text="Codigo")
        self.list_g.column("#1", width=40)
        self.list_g.heading("#2", text="Fornecedores")
        self.list_g.column("#2", width=120)
        self.list_g.heading("#3", text="Fone")
        self.list_g.column("#3", width=70)
        self.list_g.heading("#4", text="Cidade")
        self.list_g.column("#4", width=100)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.win_for, orient='vertical', command=self.list_g.yview)

        # Adiciona barra de rolagem
        self.list_g.configure(yscroll=self.barra.set)
        self.barra.place(x=685, y=12, height=245)
        self.list_g.place(x=355, y=12, height=245)
        self.list_g.bind("<Double-1>", self.OnDoubleClickForn)

        self.list_fornec()
    def list_fornec(self):
        self.conecta_Glac()
        lista = self.cursor.execute("""SELECT cod_forn, fornecedor, fone, municipio 
                FROM fornecedores ORDER BY fornecedor ASC;""")

        rows = self.cursor.fetchall()
        for row in rows:
            self.list_g.insert("", END, values=row)

        self.desconecta_Glac()

    def var_fornec(self):
        self.cod_forn = self.entr_cd_for.get()
        self.fornecedor = self.entr_for.get()
        self.fone = self.entr_fone.get()
        self.cnpj = self.entr_cnpj.get()
        self.cep = self.entr_cep.get()
        self.endereco = self.entr_end.get()
        self.municipio = self.entr_mun.get()
        self.descricao = self.entr_dscr.get()

    def OnDoubleClickForn(self, event):
        self.limpa_fornecedor()
        self.list_g.selection()

        for n in self.list_g.selection():
            col1, col2, col3, col4 = self.list_g.item(n, 'values')
            self.entr_cd_for.insert(END, col1)
        self.carrega_fornecedor()

    def mud_fornec(self):
        self.var_fornec()
        self.conecta_Glac()
        self.cursor.execute("""UPDATE fornecedores SET 
        fornecedor = ?, fone = ?, cnpj = ?, cep = ?, endereco = ?, municipio = ?,
        descricao = ? WHERE cod_forn = ?""",
        (self.fornecedor, self.fone, self.cnpj, self.cep, self.endereco, self.municipio,
         self.descricao, self.cod_forn))
        self.conn.commit()
        self.list_g.delete(*self.list_g.get_children())
        self.desconecta_Glac()

        self.list_fornec()
        msg = "Dados do fornecedor alterados com sucesso"
        messagebox.showinfo("GLAC ", msg)

    def limpa_fornecedor(self):
        self.entr_cd_for.delete(0, END)
        self.entr_for.delete(0, END)
        self.entr_fone.delete(0, END)
        self.entr_cnpj.delete(0, END)
        self.entr_cep.delete(0, END)
        self.entr_end.delete(0, END)
        self.entr_mun.delete(0, END)
        self.entr_dscr.delete(0, END)

    def del_fornec(self):
        self.conecta_Glac()

        cod_forn = self.entr_cd_for.get()
        self.cursor.execute("""DELETE FROM fornecedores WHERE cod_forn=?""", (cod_forn,))
        self.conn.commit()
        self.list_g.delete(*self.list_g.get_children())
        self.desconecta_Glac()

        self.list_fornec()
        msg = "Fornecedor excluido com sucesso.  :("
        messagebox.showinfo("GLAC ", msg)

    def carrega_fornecedor(self):
        self.conecta_Glac()
        cod_forn = self.entr_cd_for.get()

        self.limpa_fornecedor()
        self.cursor.execute("""SELECT fornecedor, fone, cnpj, cep, endereco, municipio, descricao 
            FROM fornecedores WHERE cod_forn = '%s'""" % cod_forn)
        consultafornec = self.cursor.fetchall()
        for i in consultafornec:
            self.entr_cd_for.insert(END, cod_forn)
            self.entr_for.insert(END, i[0])
            self.entr_fone.insert(END, i[1])
            self.entr_cnpj.insert(END, i[2])
            self.entr_cep.insert(END, i[3])
            self.entr_end.insert(END, i[4])
            self.entr_mun.insert(END, i[5])
            self.entr_dscr.insert(END, i[6])
        self.desconecta_Glac()

    def cepForn(self):
        self.entr_end.delete(0, END)
        self.entr_mun.delete(0, END)
        try:
            self.cep = self.entr_cep.get()
            endereco = get_address_from_cep(self.cep, webservice=WebService.APICEP)

            self.entr_end.insert(END, endereco['logradouro'])
            self.entr_end.insert(END, ' - ')
            self.entr_end.insert(END, endereco['bairro'])

            self.entr_mun.insert(END, endereco['cidade'])
            self.entr_mun.insert(END, ' - ')
            self.entr_mun.insert(END, endereco['uf'])
        except:
            msg = "Cep não encontrado"
            messagebox.showinfo("GLAC ", msg)

    def busca_fornecedor(self):
        self.conecta_Glac()

        self.entr_for.insert(END, '%')
        self.list_g.delete(*self.list_g.get_children())
        fornecedor = self.entr_for.get()

        lista = self.cursor.execute("""SELECT cod_forn, fornecedor, fone, municipio 
        FROM fornecedores WHERE fornecedor LIKE '%s' ORDER BY fornecedor ASC;""" % fornecedor)
        rows = self.cursor.fetchall()
        for row in rows:
            self.list_g.insert("", END, values=row)
            self.entr_for.delete(0, END)
        self.desconecta_Glac()

    def add_fornec(self):
        self.conecta_Glac()
        self.list_g.delete(*self.list_g.get_children())
        self.var_fornec()

        self.cursor.execute("""INSERT INTO fornecedores 
        (fornecedor, fone, cnpj, cep, endereco, municipio, descricao)
        VALUES ( ?, ?, ?, ?, ?, ?, ?)""",
        (self.fornecedor, self.fone, self.cnpj, self.cep, self.endereco,
         self.municipio, self.descricao))
        self.conn.commit()
        self.desconecta_Glac()

        self.list_fornec()
        msg = "Novo fornecedor incluido com sucesso"
        messagebox.showinfo("GLAC ", msg)