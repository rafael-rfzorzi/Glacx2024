from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

class CadTec:
    def cadtec(self):
        self.janelaTec = Toplevel()
        self.janelaTec.title("Tecnico")
        self.janelaTec.geometry("625x150+100+170")
        self.janelaTec.configure(background="#6F87B0")
        self.janelaTec.transient(self.window_one)
        self.janelaTec.focus_force()
        self.janelaTec.grab_set()
        self.janelaTec.resizable(FALSE, FALSE)

        ###  Botao Novo Cliente
        botaoAdd = ButtonGlac(self.janelaTec, "Novo", self.add_servT)
        botaoAdd.place(x=25, y=105, width=80, height=35)

        ### Botao Altera dados do Cliente
        botaoMud = ButtonGlac(self.janelaTec, "Alterar", self.mud_servT)
        botaoMud.place(x=125, y=105, width=80, height=35)

        ### Botao deletar dados do Cliente
        botaoDel = ButtonGlac(self.janelaTec, "Apagar", self.del_servT)
        botaoDel.place(x=225, y=105, width=80, height=35)

        ##  Botao limpa
        botaolimpa = ButtonGlac(self.janelaTec, "Limpar", self.limpa_servicoT)
        botaolimpa.place(x=220, y=15, width=90, height=35)

        ###  Botao busca Cabeça
        botaobusca = ButtonGlac(self.janelaTec, '>>', self.busca_servicoT)
        botaobusca.place(x=280, y=50, width=30, height=25)

        ###  Botao busca Carregar
        botaoCarregar = ButtonGlac(self.janelaTec, "Carregar", self.carrega_servicoT)
        botaoCarregar.place(x=130, y=15, width=90, height=35)

        descrCod = LabelGlac(self.janelaTec, "Codigo", '#4A71B2')
        descrCod.place(x=2, y=20, width=80, height=25)

        self.entradaCod = Entry(self.janelaTec)
        self.entradaCod.place(x=80, y=20, width=40, height=25)

        descrTec = LabelGlac(self.janelaTec, "Tecnico", '#4A71B2')
        descrTec.place(x=2, y=50, width=80, height=25)

        self.entradaTec = Entry(self.janelaTec)
        self.entradaTec.place(x=80, y=50, width=200, height=25)

        # Widgets - Listar tecnicos
        self.listaServ = ttk.Treeview(self.janelaTec, height=6, column=("col1", "col2"))
        self.listaServ.heading("#0", text="")
        self.listaServ.column("#0", width=0)
        self.listaServ.heading("#1", text="Codigo")
        self.listaServ.column("#1", width=55)
        self.listaServ.heading("#2", text="Tecnico")
        self.listaServ.column("#2", width=220)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaTec, orient='vertical',
                                   command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.place(x=325, y=20, height=122)
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=600, y=21, height=122)
        self.listaServ.bind("<Double-1>", self.OnDoubleClickT)

        self.conecta_Glac()

        lista = self.cursor.execute("SELECT cod, tecnico FROM tecnico  ORDER BY tecnico ASC; ")
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
        self.janelaTec.mainloop()
    def add_tecnicobind(self, event):
        self.codServ1.delete(0, END)

        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaTecnico.insert(END, col2)

        self.listatec.destroy()
    def OnTec(self, *args):
        self.listaServ.yview(*args)
    def limpa_servicoT(self):
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)
    def mud_servT(self):
        self.conecta_Glac()

        cod_sp = self.entradaCod.get()
        servprod = self.entradaTec.get()

        self.cursor.execute("""
            UPDATE tecnico SET tecnico = ? WHERE cod = ?""", (servprod, cod_sp))
        self.conn.commit()

        self.listaServ.delete(*self.listaServ.get_children())
        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)

        self.desconecta_Glac()
    def OnDoubleClickT(self, event):
        self.limpa_servicoT()
        self.listaServ.selection()

        for n in self.listaServ.selection():
            col1, col2 = self.listaServ.item(n, 'values')
            self.entradaCod.insert(END, col1)

        self.carrega_servicoT()
    def del_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        cod_sp = self.entradaCod.get()
        self.cursor.execute("""
        DELETE FROM tecnico WHERE cod = ? """, (cod_sp,))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT cod, tecnico FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)

        self.desconecta_Glac()
    def carrega_servicoT(self):
        cod_sp = self.entradaCod.get()
        self.conecta_Glac()

        sp = self.cursor

        self.entradaTec.delete(0, END)

        sp.execute("SELECT tecnico FROM tecnico WHERE cod = '%s'" % cod_sp)
        consultaserv = self.cursor.fetchall()
        for i in consultaserv:
            i = str(i);
            i = i.replace('(', '');
            i = i.replace(')', '');
            i = i.replace("'", "");
            i = i.replace(',', '');
            i = i.replace('{', '');
            i = i.replace('}', '')
            self.entradaTec.insert(END, i)

        self.desconecta_Glac()
    def busca_servicoT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())

        self.entradaTec.insert(END, '%')
        servprod = self.entradaTec.get()
        servico = self.cursor

        servico.execute("""SELECT cod, tecnico FROM tecnico WHERE tecnico LIKE '%s'  """ % servprod)
        buscaservico = self.cursor.fetchall()
        for i in buscaservico:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)

        self.desconecta_Glac()
    def add_servT(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        codinf = self.cursor.execute("""select MAX(cod) + 1 from tecnico """)
        for i in codinf:
            self.entradaCod.insert(END, i)

        servprod = self.entradaTec.get()
        cod_sp = self.entradaCod.get()

        self.cursor.execute("""
    		INSERT INTO tecnico (cod, tecnico) VALUES (?, ?)""", (cod_sp, servprod))
        self.conn.commit()

        lista = self.cursor.execute("""
        SELECT * FROM tecnico ORDER BY tecnico ASC;
        """)
        for i in lista:
            self.listaServ.insert("", END, values=i)
        self.entradaCod.delete(0, END)
        self.entradaTec.delete(0, END)

        self.desconecta_Glac()