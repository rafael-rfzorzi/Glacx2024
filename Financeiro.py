import customtkinter
from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import brazilcep
from brazilcep import get_address_from_cep, WebService

today = date.today()

class ConsFinan:
    def cadfinan(self):
        self.janelaFin = customtkinter.CTkToplevel()
        self.janelaFin.title("Receitas")
        self.janelaFin.geometry("795x270+120+200")
        self.janelaFin.configure(background="gray40")
        self.janelaFin.resizable(FALSE, FALSE)
        self.janelaFin.transient(self.window_one)
        self.janelaFin.focus_force()
        self.janelaFin.grab_set()

        descrCodprod = customtkinter.CTkLabel(self.janelaFin, text='Ano')
        descrCodprod.place(x=30, y=15)

        self.sel_lists_tps()

        self.entry5 = StringVar()
        self.entry5.set(today.year)
        self.entry5V = self.rows_ano_dscr

        self.entradaCodReceita = OptionMenu(self.janelaFin, self.entry5, *self.entry5V)
        self.entradaCodReceita.place(x=85, y=15)

        descrMes = customtkinter.CTkLabel(self.janelaFin, text='Mês')
        descrMes.place(x=30, y=45)

        self.entry6 = StringVar()
        mes = today.month - 1
        self.entry6.set(self.rows_meses_dscr[mes])
        self.entry6V = self.rows_meses_dscr

        self.entradaReceita = OptionMenu(self.janelaFin, self.entry6, *self.entry6V)
        self.entradaReceita.place(x=85, y=45)

        ###  Botao Carrega
        botaoAdd = customtkinter.CTkButton(self.janelaFin, text="Carregar", command=self.carrega_receita)
        botaoAdd.place(x=35, y=115)

        ###  Botao limpa
        botaolimpa = customtkinter.CTkButton(self.janelaFin, text="Limpar", command=self.limpa_receita)
        botaolimpa.place(x=35, y=150)

        ### Widgets - Listar produtos ###
        self.listaServ = ttk.Treeview(self.janelaFin, height=10,
                                      column=("col1", "col2", "col3", "col4"))
        self.listaServ.heading("#0", text="")
        self.listaServ.heading("#1", text="Codigo")
        self.listaServ.heading("#2", text="Placa")
        self.listaServ.heading("#3", text="Dia")
        self.listaServ.heading("#4", text="Valor")

        self.listaServ.column("#0", width=0)
        self.listaServ.column("#1", width=70)
        self.listaServ.column("#2", width=140)
        self.listaServ.column("#3", width=130)
        self.listaServ.column("#4", width=60)

        # Cria barra de rolagem
        self.barra = ttk.Scrollbar(self.janelaFin, orient='vertical', command=self.listaServ.yview)

        # Adiciona barra de rolagem
        self.listaServ.configure(yscroll=self.barra.set)
        self.barra.place(x=775, y=15, height=222)
        self.listaServ.place(x=220, y=15, width=555)

        self.listaServ.bind("<Double-1>", self.OnDoubleClickFinan)

        self.listaServ2 = ttk.Treeview(self.janelaFin, height=1, column=("col1"))
        self.listaServ2.heading("#0", text="")
        self.listaServ2.heading("#1", text="Total do mês")

        self.listaServ2.column("#0", width=0)
        self.listaServ2.column("#1", width=120)

        self.listaServ2.place(x=45, y=195)
        self.janelaFin.mainloop()
    def OnDoubleClickFinan(self, event):
        #self.limpa_produto()
        self.listaServ.selection()
        for n in self.listaServ.selection():
            col1, col2, col3, col4 = self.listaServ.item(n, 'values')
            self.carrega_produto()
            self.entradaCodprod.insert(END, col1)
    def carrega_receita(self):
        self.conecta_Glac()

        self.listaServ.delete(*self.listaServ.get_children())
        self.listaServ2.delete(*self.listaServ2.get_children())

        ano = self.entry5.get()
        mes = self.entry6.get()
        ano = str(ano.replace("(", "").replace(")", "").replace(",", ""))
        mes = str(mes.replace("(", "").replace(")", "").replace(",", ""))
        mes2 = ''
        if mes == "Janeiro":
            mes2 = '01'
        elif mes == "Fevereiro":
            mes2 = '02'
        elif mes == "Março":
            mes2 = '03'
        elif mes == "Abril":
            mes2 = '04'
        elif mes == "Maio":
            mes2 = '05'
        elif mes == "Junho":
            mes2 = '06'
        elif mes == "Julho":
            mes2 = '07'
        elif mes == "Agosto":
            mes2 = '08'
        elif mes == "Setembro":
            mes2 = '09'
        elif mes == "Outubro":
            mes2 = '10'
        elif mes == "Novembro":
            mes2 = '11'
        elif mes == "Dezembro":
            mes2 = '12'

        lista = self.cursor.execute("""select id_orc1, placa_orc, dia, 
            (select (sum(total)) from orcamento2 where id_orc2 = id_orc1) from orcamento1 
            where substr(dia, 7,4) = '%s' and substr(dia, 4,2) = '%s' 
            and tipoOrc != 'Orçamento' order by dia asc; """ % (ano, mes2))
        for i in lista:
            i = list(i)
            if i[3] == None:
                i[3] = float(0.00)
            print(i)

            self.listaServ.insert("", END, values=i)


        lista2 = self.cursor.execute("""SELECT sum(total)
            from orcamento1, orcamento2 WHERE substr(dia, 7,10) = '%s' and substr(dia, 4,2) = '%s'
            and tipoOrc == 'Ordem de Serviço' and id_orc2 = id_orc1; """ % (ano, mes2))
        for i in lista2:
            self.listaServ2.insert("", END, values=i)
        self.desconecta_Glac()
    def limpa_receita(self):
        self.listaServ.delete(*self.listaServ.get_children())
        self.listaServ2.delete(*self.listaServ2.get_children())