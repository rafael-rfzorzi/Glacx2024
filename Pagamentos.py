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

class CadPagamento:
    def consultapag(self):
        self.sel_lists_tps()
        self.janelaPagOrc = customtkinter.CTkToplevel()
        self.janelaPagOrc.title("GlacX - Consulta de pagamentos")
        self.janelaPagOrc.geometry("790x435+120+130")
        self.janelaPagOrc.resizable(FALSE, FALSE)
        self.janelaPagOrc.transient(self.window_one)
        self.janelaPagOrc.focus_force()
        self.janelaPagOrc.grab_set()

        ### Lista de pagamentos
        self.listaPag = ttk.Treeview(self.janelaPagOrc, height=10,
            column=("col1", "col2", "col3", "col4", "col5"))
        self.listaPag.heading("#0", text="")
        self.listaPag.column("#0", width=0)
        self.listaPag.heading("#1", text='O.S')
        self.listaPag.column("#1", width=60)
        self.listaPag.heading("#2", text="Tipo")
        self.listaPag.column("#2", width=220)
        self.listaPag.heading("#3", text="Valor")
        self.listaPag.column("#3", width=120)
        self.listaPag.heading("#4", text="Data")
        self.listaPag.column("#4", width=180)
        self.listaPag.heading("#5", text="Pago")
        self.listaPag.column("#5", width=110)

        self.listaPag.place(relx=0.02, rely=0.3, relwidth=0.94)

        # Cria barra de rolagem
        self.barraMov = ttk.Scrollbar(self.janelaPagOrc, orient='vertical', command=self.listaPag.yview)
        self.barraMov.place(relx=0.96, rely=0.305, relwidth=0.02, height=221)

        self.listaPag.bind("<Double-1>" , self.OnDoubleClickpag)
        self.listaPag.configure(yscroll=self.barraMov.set)

        ### Label do saldo a ser pago
        labelValor = customtkinter.CTkLabel(self.janelaPagOrc, text="Valor Total")
        labelValor.place(x=630, y=375)

        labelCifrao = customtkinter.CTkLabel(self.janelaPagOrc, text="R$")
        labelCifrao.place(x=600, y=395)

        #### Entry do saldo a ser pago
        self.entryValorDevido = customtkinter.CTkEntry(self.janelaPagOrc)
        self.entryValorDevido.configure(validate="key")
        self.entryValorDevido.place(x=620, y=395, relwidth=0.1)

        #### Listbox do tipo de pagamento
        self.listtipopag = StringVar()
        self.listtipopag.set(self.tipos_pag[0])
        self.popupMenu = OptionMenu(self.janelaPagOrc, self.listtipopag, *self.tipos_pag)
        self.popupMenu.place(relx=0.04, rely=0.08, relwidth=0.15, height=20)

        tipoPag = customtkinter.CTkLabel(self.janelaPagOrc, text="Tipo Pagamento")
        tipoPag.place(relx=0.04, rely=0.03, relwidth=0.15)

        #### Entry data
        meslabel = customtkinter.CTkLabel(self.janelaPagOrc, text='Mês')
        meslabel.place(relx=0.2, rely=0.03, relwidth=0.12)
        self.mesvar = StringVar()
        self.mesesV = self.rows_meses_dscr
        mes = today.month - 1
        self.mesvar.set(self.rows_meses_dscr[mes])
        self.popupMenu = OptionMenu(self.janelaPagOrc, self.mesvar, *self.mesesV)
        self.popupMenu.place(relx=0.2, rely=0.08, relwidth=0.12, height=20)

        anolabel = customtkinter.CTkLabel(self.janelaPagOrc, text='Ano')
        anolabel.place(relx=0.33, rely=0.03, relwidth=0.08)
        self.anovar = StringVar()
        self.anosV = self.rows_ano_dscr
        self.anovar.set(today.year)
        self.popupMenu = OptionMenu(self.janelaPagOrc, self.anovar, *self.anosV)
        self.popupMenu.place(relx=0.33, rely=0.08, relwidth=0.08, height=20)

        ### Pago?
        pagolabel = customtkinter.CTkLabel(self.janelaPagOrc, text="Pago")
        pagolabel.place(relx=0.43, rely=0.03)
        self.entry7 = StringVar()
        self.entry7V = {"Sim", "Nao"}
        self.entry7V = sorted(self.entry7V)
        self.entry7.set("Sim")

        self.popupMenu = OptionMenu(self.janelaPagOrc, self.entry7, *self.entry7V)
        self.popupMenu.place(relx=0.43, rely=0.08, width=80, height=20)

        #### Button Inserir Registro
        btinserir1 = customtkinter.CTkButton(self.janelaPagOrc,
            text="Consulta competência/Tipo/Pago? ", command=self.carregaConsulta)
        btinserir1.place(relx=0.57, rely=0.04)

        #### Entry data
        self.mesvar2 = StringVar()
        self.mesesV2 = self.rows_meses_dscr
        mes = today.month - 1
        self.mesvar2.set(self.rows_meses_dscr[mes])
        self.popupMenu2 = OptionMenu(self.janelaPagOrc, self.mesvar2, *self.mesesV2)
        self.popupMenu2.place(relx=0.04, rely=0.2, relwidth=0.15, height=20)
        mesValor2Label = customtkinter.CTkLabel(self.janelaPagOrc, text='Mês')
        mesValor2Label.place(relx=0.04, rely=0.15, relwidth=0.15)

        self.anovar2 = StringVar()
        self.anovar2.set(today.year)
        self.popupMenu2 = OptionMenu(self.janelaPagOrc, self.anovar2, *self.rows_ano_dscr)
        self.popupMenu2.place(relx=0.2, rely=0.2, relwidth=0.12, height=20)
        anoValor2label= customtkinter.CTkLabel(self.janelaPagOrc, text="Ano")
        anoValor2label.place(relx=0.2, rely=0.15, relwidth=0.12)

        # Pago?
        self.entry72 = StringVar()
        self.entry72.set(self.sim_nao[1])
        self.popupMenu2 = OptionMenu(self.janelaPagOrc, self.entry72, *self.sim_nao)
        self.popupMenu2.place(relx=0.33, rely=0.2, relwidth=0.08, height=20)

        pagoValor2 = customtkinter.CTkLabel(self.janelaPagOrc, text="Pago")
        pagoValor2.place(relx=0.33, rely=0.15, relwidth=0.08)

        #### Button Inserir Registro
        btinserir = customtkinter.CTkButton(self.janelaPagOrc, text="Consulta Competência Pago", command=self.carregaConsulta2)
        btinserir.place(relx=0.57, rely=0.16)

        self.janelaPagOrc.mainloop()
    def add_pag(self):
        ordem = self.listaNumOrc.get()
        tipopag = self.listtipopag.get()
        valortotal = self.entryValorTotal.get()
        valordeduzir = self.entryValor.get()

        dia = self.data_forma_pag.get()
        pago = "Não"

        self.conecta_Glac()
        self.cursor.execute("""	INSERT INTO formapag 
        ( ordem, tipopag, valorpagar, valordeduzir, dia, pago)
       	VALUES ( ?, ?, ?, ?, ?, ?)""", (ordem, tipopag, valortotal,
        valordeduzir, dia, "Sim"))
        self.conn.commit()
        self.desconecta_Glac()

        self.sel_pag_ordem()

        msg = "Pagamento incluido com sucesso"
        messagebox.showinfo("GLAC - Pagamentos", msg)
        self.sel_pag_ordem()
    def mud_pag(self):
        self.conecta_Glac()
        tipopag = self.entry2.get()
        valor = self.entry3.get()
        diaA = self.entry4.get()
        pago = self.entry7.get()
        idA = self.entry9.get()

        self.cursor.execute("""UPDATE formapag SET tipopag = ?, valordeduzir = ?, dia = ?,
            pago = ? WHERE id = ? """, (tipopag, valor, diaA, pago, idA))
        self.conn.commit()

        self.desconecta_Glac()
        self.janPag2.destroy()
        self.sel_pag_ordem()
    def carregaConsulta(self):
        self.conecta_Glac()

        tipopag = self.listtipopag.get()
        valor = self.entryValorDevido.get()

        mes = self.mesvar.get()
        ano = self.anovar.get()
        pago = self.entry7.get()

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

        self.listaPag.delete(*self.listaPag.get_children())
        lista = self.cursor.execute("""
            SELECT  ordem, tipopag, valordeduzir, dia, pago
            FROM formapag WHERE tipopag = ? AND  substr(dia, 4,2) = ? AND substr(dia, 7,10) = ?
            AND pago = ? ORDER BY id ASC; """, (tipopag, mes2, ano, pago))
        for i in lista:
            print(i)
            self.listaPag.insert("", END, values=i)
        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""SELECT  SUM(valordeduzir)
            FROM formapag WHERE tipopag = ? AND  substr(dia, 4,2) = ? AND substr(dia, 7,10) = ?
            AND pago = ? ORDER BY id ASC; """, (tipopag, mes2, ano, pago))
        for i in lista2:
            print(i)
            if i == '':
                self.entryValorDevido.insert(END, "0.00")
            else:
                self.entryValorDevido.insert(END, i)
        self.desconecta_Glac()
    def carregaConsulta2(self):
        mes = self.mesvar2.get()
        ano = self.anovar2.get()
        pago = self.entry72.get()

        print(ano)
        print(mes)

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

        self.conecta_Glac()
        self.listaPag.delete(*self.listaPag.get_children())

        lista = self.cursor.execute("""
            SELECT  ordem, tipopag, valordeduzir, dia, pago
            FROM formapag WHERE  substr(dia, 4,2) = ? AND substr(dia, 7, 4) = ?
            AND pago = ? ORDER BY id ASC; """, (mes2, ano, pago))
        for i in lista:
            self.listaPag.insert("", END, values=i)

        self.entryValorDevido.delete(0, END)

        lista2 = self.cursor.execute("""
            SELECT  SUM(valordeduzir)
            FROM formapag WHERE substr(dia, 4,2) = ? AND substr(dia, 7, 4) = ?
            AND pago = ? ORDER BY id ASC; """, (mes2, ano, pago))
        for i in lista2:
            print(i)
            i = str(i)
            i = i.replace("(", "").replace(")","").replace(",","")
            self.entryValorDevido.insert(END, i)
        self.desconecta_Glac()
    def sel_pag_ordem(self):
        valortotal1 = self.entryValorTotal.get()

        numAt = self.listaNumOrc.get()
        self.entryNumAtend.insert(END, numAt)
        self.listaPag.delete(*self.listaPag.get_children())
        self.conecta_Glac()
        lista = self.cursor.execute("""SELECT  ordem, tipopag, valorpagar, valordeduzir, 
            dia, pago, id FROM formapag WHERE ordem = '%s'   ORDER BY id ASC; """ % numAt)
        for i in lista:
            self.listaPag.insert("", END, values=i)

        informe = self.cursor.execute("""SELECT SUM(valordeduzir) FROM formapag 
            WHERE ordem = '%s' AND pago = 'Sim' ORDER BY id ASC; """ % numAt)
        for i in informe:
            soma = float(i[0])
            soma = f'{i[0]:.2f}'
            self.entryValorInform.delete(0, END)
            self.entryValorInform.insert(END, soma)
            valor_devido = float(valortotal1) - float(soma)
            valor_devido = float(valor_devido)
            self.entryValorDevido.delete(0, END)
            self.entryValorDevido.insert(END, f'{valor_devido:.2f}')

        self.desconecta_Glac()