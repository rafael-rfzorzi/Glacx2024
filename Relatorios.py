import reportlab.lib.colors
from reportlab.pdfgen import canvas
from reportlab.lib.colors import lightslategray, lightgrey, aliceblue, grey, whitesmoke
import webbrowser
from tkinter import Toplevel
from tkinter import ttk
from tkinter import *
from pdf2image import convert_from_path

class PrintRel():
    def Gerador_front(self):
        self.win_make_reports = Toplevel()
        self.win_make_reports.title("Gerador de Relatorios")
        self.win_make_reports.geometry("850x570+120+200")
        self.win_make_reports.configure(background="#37586B")
        self.win_make_reports.resizable(False, False)
        self.win_make_reports.transient(self.window_one)
        self.win_make_reports.focus_force()
        self.win_make_reports.grab_set()

        self.entry5 = StringVar()
        self.entry5.set("Valores a receber")
        self.entry5V = ["Valores a receber", "Lista de Clientes", "Imprime orçamento"]

        self.entrada = OptionMenu(self.win_make_reports, self.entry5, *self.entry5V)
        self.entrada.place(x=85, y=15, width=200, height=30)

        ###  Botao Carrega
        botaoAdd = Button(self.win_make_reports, text="Carregar")
        botaoAdd.place(x=300, y=15, width=130, height=30)

        self.win_make_reports.mainloop()
    def VarRel(self):
        self.dados_login()
        sh = self.gc.open_by_key(self.planilha_login_code)
        ws = sh.worksheet('Página1')

        nome_oficina = str("F" + str(self.linha_senha))
        rua = str("G" + str(self.linha_senha))
        bairro = str("I" + str(self.linha_senha))
        municipio = str("J" + str(self.linha_senha))
        telefone = str("H" + str(self.linha_senha))

        self.nome_oficina2 = ws.acell(nome_oficina).value
        self.rua2 = ws.acell(rua).value
        self.bairro2 = ws.acell(bairro).value
        self.municipio2 = ws.acell(municipio).value
        self.telefone2 = ws.acell(telefone).value

        self.dia_Rr = self.entradaDataorc.get()

        self.lista1_rR = self.listaCol2a.get()
        self.colquanrt1_R = self.listaCol3a.get()
        self.colunitr1_R = self.listaCol4a.get()
        self.coltotral1_R = self.listaCol5a.get()
    def Cabecalho(self):
        self.c.setFillColor(grey)
        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(220, 830, self.nome_oficina2)
        self.c.setFont("Helvetica", 11)
        self.c.drawString(220, 810, self.rua2 + "  " + self.bairro2)
        self.c.drawString(220, 790, self.municipio2 + "  " + "Telefone: " + self.telefone2 + "  " + "Tecnico:" + self.entradaTecnico.get())

        self.c.setFont("Helvetica", 8)
        self.c.drawString(400, 10, "RfZorzi Sistemas - https://www.rfzorzi.com")

        self.c.setFont("Helvetica-Bold", 24)
        #### MOLDURA E TITULOS DO RELATORIO
        try:
            self.c.drawInlineImage("logoempresa.jpg", 17, 770, 200, 70)
        except:
            self.c.drawString(220, 790, 'Seu Logo')

        self.linha = self.c
        self.linha.setFillColor(whitesmoke)
        # moldura
        self.linha.rect(15, 665, 570, 68, fill=True, stroke=False)
        self.linha.rect(15, 600, 570, 55, fill=True, stroke=False)

        self.linha.setFillColor(lightgrey)
        self.linha.rect(17, 711, 566, 1, fill=True, stroke=False)
        self.linha.rect(17, 696, 566, 1, fill=True, stroke=False)
        self.linha.rect(17, 681, 566, 1, fill=True, stroke=False)
        self.linha.rect(17, 615, 566, 1, fill=True, stroke=False)
        self.linha.rect(17, 630, 566, 1, fill=True, stroke=False)
        self.linha.setFillColor(whitesmoke)

        self.c.setFillColor(lightslategray)
        self.c.setFont("Helvetica-Bold", 12)

        self.c.drawString(15, 755, 'Entrada: ' + self.listInicio.get())
        self.c.drawString(480, 755, 'Saida: ' + self.listFim.get())

        self.c.drawString(240, 720, "Dados Do Cliente")
        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(16, 700, "Nome:")
        self.c.drawString(320, 700, "Fone:")
        self.c.drawString(435, 700, "Cpf / Cnpj:")
        self.c.drawString(16, 685, "Endereco:")
        self.c.drawString(16, 671, "Cidade:")
        self.c.drawString(540, 671, "Uf:")

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(240, 640, "Dados Do Veículo")

        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(16, 620, "Placa:")
        self.c.drawString(120, 620, "Veiculo:")
        self.c.drawString(475, 620, "Cor:")
        self.c.drawString(16, 605, "Combustivel:")
        self.c.drawString(475, 605, "Km:")

        self.c.setFont("Helvetica", 10)
        self.c.drawString(50, 700, self.listNome.get())
        self.c.drawString(355, 700, self.listFone.get())
        self.c.drawString(490, 700, self.listCpf.get())
        self.c.drawString(70, 685, self.listEndereco.get())

        self.c.drawString(70, 671, self.listMunicipio.get())
        self.c.drawString(560, 671, self.listUf.get())

        # DADOS DO AUTOMOVEL
        self.c.drawString(55, 620, self.placa.get())
        self.c.drawString(165, 620, self.listMarca.get())
        self.c.drawString(260, 620, self.listAut.get())
        self.c.drawString(500, 620, self.listCor.get())
        self.c.drawString(100, 605, self.listCombustivel.get())
        self.c.drawString(500, 605, self.entradaObs.get())
        self.c.setFont("Helvetica", 12)

        # VARIAVEIS DO RODAPE DO RELATORIO - DADOS DA EMPRESA

    def PrintOrc(self):
        try:
            webbrowser.open("file:///c:/glacx/Orcamento.pdf")
        except:
            webbrowser.open("file:///home/rfz/Orcamento.pdf")
    def imprime_orc(self):
        self.VarRel()
        # Gerar Relatorio de orçamento
        try:
            self.c = canvas.Canvas("c:\glacx\Orcamento.pdf")
        except:
            self.c = canvas.Canvas("file:///home/rfz/Orcamento.pdf")

        self.linha = self.c
        self.linha.setFillColor(whitesmoke)
        self.linha.rect(15, 540, 570, 47, fill=True, stroke=False)
        self.linha.rect(15, 490, 570, 47, fill=True, stroke=False)

        self.Cabecalho()

        self.linha.setFillColor(grey)
        self.c.drawString(15, 475, "Produtos / Servicos")

        self.c.setFont("Helvetica", 12)

        self.c.setFillColor(lightslategray)
        self.c.drawString(230, 755, self.Tipvar.get() + " Nº  " + self.listaNumOrc.get())

        self.c.setFont("Helvetica", 9)

        ####  TEXTO DE DESCRICAO DOS PROBLEMAS
        self.descp1 = self.area1.get('1.0', 'end-1c')
        self.c.drawString(40, 560, self.descp1[0:125])
        self.c.drawString(20, 545, self.descp1[125:259])
        self.c.drawString(40, 510, self.area3.get('1.0', 'end-1c')[0:125])
        self.c.drawString(20, 495, self.area3.get('1.0', 'end-1c')[125:259])

        self.c.setFont("Helvetica-Bold", 10)
        self.c.drawString(15, 575, "Problemas relatados pelo cliente")
        self.c.drawString(15, 525, "Serviços realizados")


        self.c.setFont("Helvetica-Bold", 9)
        self.c.drawString(17, 462, "Item")
        self.c.drawString(200, 462, "Descricao")
        self.c.drawString(482, 462, "Quant")
        self.c.drawString(425, 462, "Valor Unit")
        self.c.drawString(525, 462, "Total Unit")

        self.c.setFont("Helvetica", 8)

        # DESCRIÇÃO DOS ITENS DO ORÇAMENTO
        self.conecta_Glac()

        self.cursor.execute("""SELECT ordem_item, desc_item, "R$", valor, quant, "R$", total
                FROM orcamento2 WHERE id_orc2 = '%s'  """ % self.listaNumOrc.get())
        rows = self.cursor.fetchall()

        self.linha.rect(13, 470, 570, 0.5, fill=True, stroke=False)
        self.linha.rect(13, 460, 570, 0.5, fill=True, stroke=False)
        self.linha.rect(13, 460, 1, 10, fill=True, stroke=False)
        self.linha.rect(40, 460, 1, 10, fill=True, stroke=False)
        self.linha.rect(420, 460, 1, 10, fill=True, stroke=False)
        self.linha.rect(475, 460, 1, 10, fill=True, stroke=False)
        self.linha.rect(515, 460, 1, 10, fill=True, stroke=False)
        self.linha.rect(583, 460, 1, 10, fill=True, stroke=False)
        x = 462
        linhaItem = 460
        for row in rows:
            row = list(row)
            x -= 10
            self.c.drawString(25, x, str(row[0]))
            self.c.drawString(45, x, str(row[1]))
            self.c.drawString(430, x, str(row[2:4]).replace("[","").replace("]","").replace("'","").replace(",",""))
            self.c.drawString(480, x, str(row[4]))
            self.c.drawString(520, x, str(row[5:7]).replace("[","").replace("]","").replace("'","").replace(",",""))
            linhaItem -= 10
            self.linha.rect(13, linhaItem, 570, 0.5, fill=True, stroke=False)
            self.linha.rect(13, linhaItem, 1, 10, fill=True, stroke=False)
            self.linha.rect(40, linhaItem, 1, 10, fill=True, stroke=False)
            self.linha.rect(420, linhaItem, 1, 10, fill=True, stroke=False)
            self.linha.rect(475, linhaItem, 1, 10, fill=True, stroke=False)
            self.linha.rect(515, linhaItem, 1, 10, fill=True, stroke=False)
            self.linha.rect(583, linhaItem, 1, 10, fill=True, stroke=False)
        linhaItem -= 10
        self.c.drawString(500, linhaItem, "Total:" + "R$" + self.entradatotal.get())

        self.desconecta_Glac()

        self.c.showPage()

        self.c.save()
        self.PrintOrc()
    def PrintVist(self):
        webbrowser.open("file:///c:/glacx/Vistoria.pdf")
    def imprime_vist(self):
        self.VarRel()
        self.c = canvas.Canvas("c:\glacx\Vistoria.pdf")

        self.c.setFont("Helvetica-Bold", 16)
        self.c.drawString(200, 755, "Vistoria do Veiculo" + "Nº  " + self.listaNumOrc.get())

        self.linha = self.c
        self.linha.setFillColor(lightgrey)
        self.linha.rect(35, 538, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 498, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 458, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 418, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 378, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 338, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 298, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 258, 530, 20, fill=True, stroke=False)
        self.linha.rect(35, 218, 530, 20, fill=True, stroke=False)

        self.Cabecalho()
        self.c.setFont("Helvetica", 16)
        self.c.drawString(17, 568, "Itens Vistoriados")

        # Vistoria variaveis
        self.codVist_R = self.listaNumOrc.get()
        self.tanque_R = self.are1.get()
        self.odometro_R = self.are2.get()
        self.radio_R = self.are3.get()
        self.calota_R = self.are4.get()
        self.triangulo_R = self.are5.get()
        self.macaco_R = self.are6.get()
        self.estepe_R = self.are7.get()
        self.obs1_R = self.are8.get()
        self.obs2_R = self.are9.get()

        self.c.setFont("Helvetica-Bold", 14)
        #
        self.c.drawString(35, 540, "Tanque")
        self.c.drawString(35, 500, "Odometro")
        self.c.drawString(35, 460, 'Obs 1:')
        self.c.drawString(35, 420, 'Obs 2:')
        self.c.drawString(35, 380, 'Obs 3:')
        self.c.drawString(35, 340, 'Obs 4:')
        self.c.drawString(35, 300, 'Obs 5:')
        self.c.drawString(35, 260, 'Obs 6:')
        self.c.drawString(35, 220, 'Obs 7:')

        self.c.drawString(250, 540, self.tanque_R)
        self.c.drawString(200, 500, self.odometro_R)
        self.c.drawString(100, 460, self.radio_R)
        self.c.drawString(100, 420, self.calota_R)
        self.c.drawString(100, 380, self.triangulo_R)
        self.c.drawString(100, 340, self.macaco_R)
        self.c.drawString(100, 300, self.estepe_R)
        self.c.drawString(100, 260, self.obs1_R)
        self.c.drawString(100, 220, self.obs2_R)

        self.c.setFont("Helvetica-Bold", 12)
        self.c.drawString(35, 200, "Confirmo que deixei o veiculo nas condições descritas:")
        self.c.drawString(35, 170, "Assinatura:")

        # MOLDURAS DO RELATORIO
        self.c.rect(13, 155, 2, 427, fill=True, stroke=False)
        self.c.rect(14, 155, 572, 2, fill=True, stroke=False)
        self.c.rect(585, 155, 2, 427, fill=True, stroke=False)
        self.c.rect(13, 582, 572, 2, fill=True, stroke=False)

        self.c.save()

        self.PrintVist()
    def Print_lista_clientes(self):
        webbrowser.open("file:///c:/glacx/ListaClientes.pdf")
    def Imprime_lista_clientes(self):
        self.VarRel()
        # Gerar Relatorio de orçamento
        self.c = canvas.Canvas("c:\glacx\ListaClientes.pdf")
        self.c.setFont("Helvetica-Bold", 24)
        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, "SeuLogo")
        self.c.setFont("Helvetica-Bold", 14)

        self.c.drawString(250, 750, "Lista de Clientes")
        self.c.setFont("Helvetica", 12)

        self.linha = self.c
        self.linha.setFillColor(lightgrey)

        self.c.setFillColor(lightslategray)

        # MOLDURAS DO RELATORIO

        self.c.setFont("Helvetica", 10)

        self.c.setFont("Helvetica-Bold", 9)
        self.c.drawString(17, 712, "Codigo")
        self.c.drawString(70, 712, "Nome")
        self.c.drawString(240, 712, "Telefone")
        self.c.drawString(310, 712, "Endereço")
        self.linha.rect(13, 710, 560, 0.5, fill=True, stroke=False)
        self.linha.rect(13, 725, 560, 0.5, fill=True, stroke=False)
        self.linha.rect(13, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(55, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(230, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(300, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(583, 710, 1, 15, fill=True, stroke=False)


        self.c.setFont("Helvetica", 8)

        # DESCRIÇÃO
        self.conecta_Glac()

        self.cursor.execute("""SELECT  cod_cli, SUBSTR(nome, 1, 35), fone1ddd, SUBSTR(fone1, 1, 10), 
        SUBSTR(endereco, 1, 30), SUBSTR(numcasa, 1, 4), SUBSTR(municipio, 1, 20) 
        FROM clientes  ORDER BY nome ASC; """)
        rows = self.cursor.fetchall()
        x = 712
        linhaItem = 710
        for row in rows:
            row = list(row)
            x -= 12
            row2 = str(row[2]).replace("[", "").replace(",", "")
            row3 = str(row[3]).replace("[", "").replace(",", "")
            row4 = str(row[4]).replace("[", "").replace(",", "")
            row5 = str(row[5]).replace("[", "").replace(",", "")
            row6 = str(row[6]).replace("[", "").replace(",", "")

            self.c.drawString(25, x, str(row[0]))
            self.c.drawString(64, x, str(row[1]))
            self.c.drawString(240, x, row2 + row3)
            self.c.drawString(304, x, row4 + " - " + row5 + " - " + row6)
            linhaItem -= 12
            self.linha.rect(13, linhaItem, 570, 0.5, fill=True, stroke=False)
            self.linha.rect(13, linhaItem, 1, 12, fill=True, stroke=False)
            self.linha.rect(55, linhaItem, 1, 12, fill=True, stroke=False)
            self.linha.rect(230, linhaItem, 1, 12, fill=True, stroke=False)
            self.linha.rect(300, linhaItem, 1, 12, fill=True, stroke=False)
            self.linha.rect(583, linhaItem, 1, 12, fill=True, stroke=False)

        self.desconecta_Glac()

        self.c.setFont("Helvetica", 12)

        self.c.showPage()
        self.c.save()
        self.Print_lista_clientes()
    def Print_valores_a_receber(self):
        webbrowser.open("file:///c:/glacx/Valoresareceber.pdf")
    def Imprime_valores_a_receber(self):
        self.VarRel()
        # Gerar Relatorio de orçamento
        self.c = canvas.Canvas("c:\glacx\Valoresareceber.pdf")
        self.c.setFont("Helvetica-Bold", 24)
        try:
            self.c.drawInlineImage("logoempresa.jpg", 150, 770, 300, 70)
        except:
            self.c.drawString(220, 790, "SeuLogo")
        self.c.setFont("Helvetica-Bold", 14)

        self.c.drawString(250, 750, "Valores a receber")
        self.c.setFont("Helvetica", 12)

        self.linha = self.c
        self.linha.setFillColor(lightgrey)

        self.c.setFillColor(lightslategray)

        # MOLDURAS DO RELATORIO

        self.c.setFont("Helvetica", 10)

        self.c.setFont("Helvetica-Bold", 9)
        self.c.drawString(25, 712, "Nome")
        self.c.drawString(170, 712, "Numero O.S")
        self.c.drawString(230, 712, "Tipo de pagamento")
        self.c.drawString(330, 712, "Valor total")
        self.c.drawString(410, 712, "Valor pago")
        self.c.drawString(490, 712, "Valor a receber")

        self.linha.rect(13, 710, 560, 0.5, fill=True, stroke=False)
        self.linha.rect(13, 725, 560, 0.5, fill=True, stroke=False)
        self.linha.rect(11, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(168, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(228, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(328, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(408, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(488, 710, 1, 15, fill=True, stroke=False)
        self.linha.rect(573, 710, 1, 15, fill=True, stroke=False)

        self.c.setFont("Helvetica", 8)

        # Nome
        self.conecta_Glac()

        self.cursor.execute("""select distinct nome, SUBSTR(id_orc1, 1, 10), SUBSTR(tipopag, 1, 30), totalizador, 
        (select sum(valordeduzir) from formapag where id_orc1 = ordem ), 
        totalizador - (select sum(valordeduzir) from formapag where id_orc1 = ordem ) 
        from clientes, orcamento1, formapag 
        where cod_cli = cliente_orc and id_orc1 = ordem 
        order by nome asc; """)
        rows = self.cursor.fetchall()
        x = 712
        linhaItem = 710
        for row in rows:
            row = list(row)
            row1 = row[0].replace('(', '').replace(',)', '').replace("'", "").replace(")", "")
            row3 = row[2].replace('(', '').replace(',)', '').replace("'", "").replace(")", "")
            x -= 12
            self.c.drawString(25, x, row1[0:25])
            self.c.drawString(170, x, row[1])
            self.c.drawString(230, x, row3)
            self.c.drawString(330, x, "R$" + str(row[3]))
            self.c.drawString(410, x, "R$" + str(row[4]))
            self.c.drawString(490, x, "R$" + str("{:.2f}".format(round(row[5], 2))))
            linhaItem -= 12
            self.linha.rect(13, linhaItem, 560, 0.5, fill=True, stroke=False)
            self.linha.rect(11, linhaItem, 1, 15, fill=True, stroke=False)
            self.linha.rect(168, linhaItem, 1, 15, fill=True, stroke=False)
            self.linha.rect(228, linhaItem, 1, 15, fill=True, stroke=False)
            self.linha.rect(328, linhaItem, 1, 15, fill=True, stroke=False)
            self.linha.rect(408, linhaItem, 1, 15, fill=True, stroke=False)
            self.linha.rect(488, linhaItem, 1, 15, fill=True, stroke=False)
            self.linha.rect(573, linhaItem, 1, 15, fill=True, stroke=False)
        self.desconecta_Glac()


        self.c.setFont("Helvetica", 12)

        self.c.showPage()
        self.c.save()
        self.Print_valores_a_receber()

    def Print_lista_clientes_aniversariantes(self):
        pass
    def Imprime_lista_clientes_aniversariantes(self):
        pass
    def Print_clientesXveiculos(self):
        pass
    def Imprime_clientesXveiculos(self):
        pass
    def Print_ordens_por_cliente(self):
        pass
    def Imprime_ordens_por_cliente(self):
        pass
    def Print_servicos_mais_realizados(self):
        pass
    def Imprime_servicos_mais_realizados(self):
        pass