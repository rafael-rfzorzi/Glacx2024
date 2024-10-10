import customtkinter
#from tkWidgetsRfzorzi.widgets_Glac import *
from tkinter import ttk
from tkcalendar import *
from tkinter import messagebox
from tkinter import *
from datetime import *
import platform
import webbrowser
from Funcionalidades import Functions
from Cadastro.Clientes import CadCli
from Cadastro.Automoveis import CadAuto
from Cadastro.Fornecedores import CadForn
from Pagamentos import CadPagamento
from Cadastro.Produtos import CadProd
from Cadastro.Estoque import CadEstoque
from Financeiro import ConsFinan
from Cadastro.Servicos import CadServ
from Cadastro.Tecnicos import CadTec
from Cadastro.Marcas import CadMarcaProd
from Relatorios import PrintRel
from Cadastros import Cads
from tktooltip import ToolTip
from envio_sms import *
from envio_whatsapp import *

window_one = Tk()
plataforma = platform.system()
today = date.today()

class PrimaryWindow(Functions, Cads, CadTec, CadForn, CadServ, CadEstoque, ConsFinan, CadProd, CadPagamento, CadAuto, CadCli, CadMarcaProd, PrintRel, Whats_envio, SMS_envio):
    def __init__(self):
        customtkinter.set_appearance_mode("Dark")
        customtkinter.set_default_color_theme("dark-blue")
        self.login_screen()
    def login_screen(self):
        self.window_one = window_one
        self.window_one.title("Login - Glac")
        self.window_one.geometry("700x500+250+150")
        self.window_one.configure(background='#456E96')
        self.window_one.resizable(False, False)
        self.frame_login()
    def tela_cadastro(self):
        self.clear_screen_login()
        # Label data
        self.descrData2 = customtkinter.CTkFrame(self.window_one)
        self.descrData2.pack(pady=30, padx=30, fill="both", expand=True)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="GlacX Oficinas", font=("Roboto", 40, "bold"))
        self.descrData3.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="Login", font=("Roboto", 24))
        self.descrData3.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="RfZorzi")
        self.descrData3.place(relx=0.35, rely=0.95, relwidth=0.3, relheight=0.05)

        # entrys
        self.cadastrese_user = customtkinter.CTkEntry(self.descrData2, placeholder_text="Insira um e-mail valido para cadastro")
        self.cadastrese_user.place(relx=0.3, rely=0.37, relwidth=0.4, relheight=0.06)
        self.email = self.cadastrese_user.get()

        # entrys
        self.cadastrese_senha = customtkinter.CTkEntry(self.descrData2, placeholder_text="Insira uma senha que ira lembrar", show="*")
        self.cadastrese_senha.place(relx=0.3, rely=0.44, relwidth=0.4, relheight=0.06)
        # Botoes
        self.cadastrese = customtkinter.CTkButton(self.descrData2, text='Submeter', command=self.submeter_login)
        self.cadastrese.place(relx=0.35, rely=0.51, relwidth=0.3, relheight=0.07)
    def frame_login(self):
        # Label data
        self.descrData2 = customtkinter.CTkFrame(self.window_one)
        self.descrData2.pack(pady=30, padx=30, fill="both", expand=True)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="GlacX Oficinas", font=("Roboto", 40, "bold"))
        self.descrData3.place(relx=0.25, rely=0.05, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="Login", font=("Roboto", 24))
        self.descrData3.place(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.1)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2, text="RfZorzi")
        self.descrData3.place(relx=0.35, rely=0.95, relwidth=0.3, relheight=0.05)

        # entrys
        self.insert_user = customtkinter.CTkEntry(self.descrData2, placeholder_text="Insira o e-mail cadastrado", border_color="#2cb67d")
        self.insert_user.place(relx=0.35, rely=0.37, relwidth=0.3, relheight=0.06)
        # entrys
        self.insert_senha = customtkinter.CTkEntry(self.descrData2, placeholder_text="Insira sua senha", show="*", border_color="#2cb67d")
        self.insert_senha.place(relx=0.35, rely=0.44, relwidth=0.3, relheight=0.06)

        # Botoes
        self.loginBot = customtkinter.CTkButton(self.descrData2, text='Login', command=self.autentica_login, border_color="#7f5af0",
                                                corner_radius=12, border_width=2)
        self.loginBot.place(relx=0.35, rely=0.51, relwidth=0.3, relheight=0.08)

        # Label data
        self.descrData3 = customtkinter.CTkLabel(self.descrData2,
                                                 text="Ainda não é cadastrado? Avalie gratuitamente!! ")
        self.descrData3.place(relx=0.25, rely=0.65, relwidth=0.5, relheight=0.05)

        # Botoes
        self.avaliar = customtkinter.CTkButton(self.descrData2, text='cadastre-se', command=self.tela_cadastro)
        self.avaliar.place(relx=0.35, rely=0.71, relwidth=0.3, relheight=0.06)
        self.verifica_atualizacao()

        self.window_one.mainloop()
    def tela(self):
        self.window_one.title("Orçamento e Ordem de Serviço - Glac")
        self.window_one.geometry("1124x760+0+0")
        self.window_one.resizable(TRUE, TRUE)
        self.window_one.minsize(width=970, height=700)

        self.validaEntradas()
        self.tela_frame1()
        self.tela_frame2()
        self.tela_frame3()
        self.aba1()
        self.aba3()
        self.aba4()
        self.tela_frame4()
        self.menus()
    def tela_frame1(self):
        self.clear_screen_login()
        self.top = customtkinter.CTkFrame(self.window_one)
        self.top.place(relx=0.01, rely=0.01, relwidth=0.98, relheight=0.09)

        self.ClientBot = customtkinter.CTkButton(self.top, text='Clientes', command=self.customer_registration, corner_radius=12)
        self.ClientBot.place(relx=0.01, rely=0.2, relwidth=0.1, relheight=0.6)
        ToolTip(self.ClientBot, "Cadastro dos clientes")

        self.FornecBot = customtkinter.CTkButton(self.top, text='Fornecedores', command=self.cadforn, corner_radius=12)
        self.FornecBot.place(relx=0.12, rely=0.2, relwidth=0.1, relheight=0.6)
        ToolTip(self.FornecBot, "Cadastro dos fornecedores")

        self.ProdutosBot = customtkinter.CTkButton(self.top, text='Produtos',  command=self.cadprod, corner_radius=12)
        self.ProdutosBot.place(relx=0.23, rely=0.2, relwidth=0.1, relheight=0.6)
        ToolTip(self.ProdutosBot, "Cadastro dos Produtos")

        self.ServBot = customtkinter.CTkButton(self.top, text='Serviços', command=self.cadserv, corner_radius=12)
        self.ServBot.place(relx=0.34, rely=0.2, relwidth=0.1, relheight=0.6)
        ToolTip(self.ServBot, "Cadastro dos Serviços oferecidos")

        self.botaoCarregaOrc = customtkinter.CTkButton(self.top, text='Busca O.S', command=self.busca_orc, border_color="#7f5af0",
                corner_radius=12, border_width=2)
        self.botaoCarregaOrc.place(relx=0.47, rely=0.2, relwidth=0.12, relheight=0.6)
        ToolTip(self.botaoCarregaOrc, "Consulta e edição dos Orçamentos e Ordens de serviço já salvos.")

        def site_rfz():
            webbrowser.open("https://www.rfzorzi.com")
        self.logoBot = customtkinter.CTkButton(self.top, text="www.rfzorzi.com", command=site_rfz, corner_radius=12)
        self.logoBot.place(relx=0.86, rely=0.2, relwidth=0.12, relheight=0.6)
    def tela_frame2(self):
        self.top2 = customtkinter.CTkFrame(self.window_one)
        self.top2.place(relx=0.01, rely=0.11, relwidth=0.98, relheight=0.21)

        self.FrameCliente = customtkinter.CTkFrame(self.top2)
        self.FrameCliente.place(relx=0, rely=0.01, relwidth=0.6, relheight=0.98)

        # Caixa de Seleção de Orçamento ou Ordem de Serviço
        self.Tipvar = customtkinter.StringVar(value="Orçamento")  # set initial value
        popupMenu = customtkinter.CTkOptionMenu(self.top2, values=["Orçamento", "Ordem de serviço"],
                                                variable=self.Tipvar)
        popupMenu.place(relx=0.44, rely=0, relwidth=0.15, relheight=0.2)

        self.cdCli = customtkinter.CTkLabel(self.FrameCliente, text='Codigo')
        self.cdCli.place(relx=0, rely=0.02, relwidth=0.15, relheight=0.13)

        self.entradaCod_cli = customtkinter.CTkEntry(self.FrameCliente)
        self.entradaCod_cli.configure(validate="key", validatecommand=self.vcmd6)
        self.entradaCod_cli.place(relx=0.16, rely=0.02, relwidth=0.1, relheight=0.13)

        self.lbNome = customtkinter.CTkLabel(self.FrameCliente, text='Nome')
        self.lbNome.place(relx=0.27, rely=0.02, relwidth=0.1, relheight=0.13)

        self.listNome = customtkinter.CTkEntry(self.FrameCliente)
        self.listNome.place(relx=0.38, rely=0.02, relwidth=0.33, relheight=0.13)

        self.lbEndereco = customtkinter.CTkLabel(self.FrameCliente, text='Logradouro')
        self.lbEndereco.place(relx=0, rely=0.2, relwidth=0.15, relheight=0.13)

        self.listEndereco = customtkinter.CTkEntry(self.FrameCliente)
        self.listEndereco.place(relx=0.16, rely=0.2, relwidth=0.55, relheight=0.13)

        self.lbMun = customtkinter.CTkLabel(self.FrameCliente, text='Municipio')
        self.lbMun.place(relx=0, rely=0.38, relwidth=0.15, relheight=0.13)

        self.listMunicipio = customtkinter.CTkEntry(self.FrameCliente)
        self.listMunicipio.place(relx=0.16, rely=0.38, relwidth=0.45, relheight=0.13)

        self.lbUf = customtkinter.CTkLabel(self.FrameCliente, text='Uf')
        self.lbUf.place(relx=0.62, rely=0.38, relwidth=0.02, relheight=0.13)

        self.listUf = customtkinter.CTkEntry(self.FrameCliente)
        self.listUf.place(relx=0.66, rely=0.38, relwidth=0.05, relheight=0.13)

        self.lbCpfCnpj = customtkinter.CTkLabel(self.FrameCliente, text='Cpf/Cnpj')
        self.lbCpfCnpj.place(relx=0, rely=0.56, relwidth=0.15, relheight=0.13)

        self.listCpf = customtkinter.CTkEntry(self.FrameCliente)
        self.listCpf.place(relx=0.16, rely=0.56, relwidth=0.25, relheight=0.13)

        self.lbFone = customtkinter.CTkLabel(self.FrameCliente, text='Fone')
        self.lbFone.place(relx=0.42, rely=0.56, relwidth=0.1, relheight=0.13)

        self.listFone = customtkinter.CTkEntry(self.FrameCliente)
        self.listFone.place(relx=0.53, rely=0.56, relwidth=0.18, relheight=0.13)

        self.lbObs = customtkinter.CTkLabel(self.FrameCliente, text='Observação')
        self.lbObs.place(relx=0, rely=0.74, relwidth=0.15, relheight=0.13)

        self.listObs = customtkinter.CTkEntry(self.FrameCliente)
        self.listObs.place(relx=0.16, rely=0.74, relwidth=0.55, relheight=0.13)

        self.descrData = customtkinter.CTkLabel(self.top2, text="Data")
        self.descrData.place(relx=0.45, rely=0.25, relwidth=0.04, relheight=0.15)
        ToolTip(self.descrData, "Data da entrada do veiculo na oficina.")

        self.entradaDataorc = DateEntry(self.top2, locale="pt_BR")
        self.entradaDataorc.place(relx=0.49, rely=0.25, relwidth=0.09, relheight=0.15)


        self.lbOrc = customtkinter.CTkLabel(self.top2, text='Atendimento Nº')
        self.lbOrc.place(relx=0.45, rely=0.48, relwidth=0.13, relheight=0.1)

        self.lbOrc2 = customtkinter.CTkLabel(self.top2, text='')
        self.lbOrc2.place(relx=0.45, rely=0.58, relwidth=0.13, relheight=0.12)

        self.listaNumOrc = customtkinter.CTkEntry(self.top2)
        self.listaNumOrc.place(relx=0.48, rely=0.59, relwidth=0.07, relheight=0.1)

        self.botaoAbreOrc = customtkinter.CTkButton(self.FrameCliente, text='Salvar', command=self.abre_orc
                                                    , border_color="#7f5af0",
                                                    corner_radius=12, border_width=2
                                                    )
        self.botaoAbreOrc.place(relx=0.73, rely=0.73, relwidth=0.12, relheight=0.25)

        self.botaoFechaOrc = customtkinter.CTkButton(self.FrameCliente, text='Encerrar', command=self.limpa_cliente
                                                     , border_color="#7f5af0",
                                                     corner_radius=12, border_width=2
                                                     )
        self.botaoFechaOrc.place(relx=0.86, rely=0.73, relwidth=0.12, relheight=0.25)

        self.FrameAut2 = customtkinter.CTkFrame(self.top2)
        self.FrameAut2.place(relx=0.6, rely=0.002, relwidth=0.1, relheight=1)

        self.entradaCod_aut = Listbox(self.FrameAut2, width=11, height=9, bg="gray35", fg="gray90", font=('Verdana', '8', 'bold'))
        self.entradaCod_aut.bind('<Button-1>', self.carrega_automovel)
        self.entradaCod_aut.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

        self.FrameAut = customtkinter.CTkFrame(self.top2)
        self.FrameAut.place(relx=0.7, rely=0.002, relwidth=0.29, relheight=1)

        self.lbPlaca = customtkinter.CTkLabel(self.FrameAut, text='Placa')
        self.lbPlaca.place(relx=0, rely=0.02, relwidth=0.18, relheight=0.13)

        self.placa = customtkinter.CTkEntry(self.FrameAut)
        self.placa.place(relx=0.19, rely=0.02, relwidth=0.3, relheight=0.13)

        self.lbVeiculo = customtkinter.CTkLabel(self.FrameAut, text='Veiculo')
        self.lbVeiculo.place(relx=0, rely=0.2, relwidth=0.18, relheight=0.13)

        self.listAut = customtkinter.CTkEntry(self.FrameAut)
        self.listAut.place(relx=0.19, rely=0.2, relwidth=0.5, relheight=0.13)

        self.lbAno = customtkinter.CTkLabel(self.FrameAut, text='Ano')
        self.lbAno.place(relx=0.7, rely=0.2, relwidth=0.1, relheight=0.13)

        self.listAno = customtkinter.CTkEntry(self.FrameAut)
        self.listAno.configure(validate="key", validatecommand=self.vcmd4)
        self.listAno.place(relx=0.81, rely=0.2, relwidth=0.15, relheight=0.13)

        self.lbMarca = customtkinter.CTkLabel(self.FrameAut, text='Marca')
        self.lbMarca.place(relx=0, rely=0.38, relwidth=0.18, relheight=0.13)

        self.listMarca = customtkinter.CTkEntry(self.FrameAut)
        self.listMarca.place(relx=0.19, rely=0.38, relwidth=0.7, relheight=0.13)

        self.lbFuel = customtkinter.CTkLabel(self.FrameAut, text='Combust')
        self.lbFuel.place(relx=0, rely=0.56, relwidth=0.18, relheight=0.13)

        self.listCombustivel = customtkinter.CTkEntry(self.FrameAut)
        self.listCombustivel.place(relx=0.19, rely=0.56, relwidth=0.51, relheight=0.13)

        self.lbKm = customtkinter.CTkLabel(self.FrameAut, text='Km')
        self.lbKm.place(relx=0.7, rely=0.56, relwidth=0.1, relheight=0.13)

        self.entradaObs = customtkinter.CTkEntry(self.FrameAut)
        self.entradaObs.configure(validate="key", validatecommand=self.vcmd9float)
        self.entradaObs.place(relx=0.81, rely=0.56, relwidth=0.15, relheight=0.13)

        self.lbCor = customtkinter.CTkLabel(self.FrameAut, text='Cor')
        self.lbCor.place(relx=0, rely=0.74, relwidth=0.18, relheight=0.13)

        self.listCor = customtkinter.CTkEntry(self.FrameAut)
        self.listCor.place(relx=0.19, rely=0.74, relwidth=0.7, relheight=0.13)
    def tela_frame3(self):
        self.abas = ttk.Notebook(self.window_one)
        self.abas.place(relx=0.01, rely=0.33, relwidth=0.98, relheight=0.56)

        self.frame_aba1 = customtkinter.CTkFrame(self.abas)
        self.frame_aba3 = customtkinter.CTkFrame(self.abas)
        self.frame_aba4 = customtkinter.CTkFrame(self.abas)
        #self.frame_aba5 = Frame(self.abas, background="#37586B")
        #self.label5 = Label(self.frame_aba5).pack(padx=850, pady=225)
        self.abas.add(self.frame_aba1, text="Atendimento")
        self.abas.add(self.frame_aba3, text="Itens")
        self.abas.add(self.frame_aba4, text="Ficha de vistoria")
        # self.abas.add(self.frame_aba5, text="Revisões")
    def tela_frame4(self):
        self.top4 = customtkinter.CTkFrame(self.window_one)
        self.top4.place(relx=0.01, rely=0.9, relwidth=0.98, relheight=0.1)

        # Tecnico de reparo
        self.lbTecnico = customtkinter.CTkLabel(self.top4, text='Tecnico')
        self.lbTecnico.place(relx=0.01, rely=0.2, relwidth=0.11, relheight=0.3)

        self.entradaTecnico = customtkinter.CTkEntry(self.top4)
        self.entradaTecnico.place(relx=0.01, rely=0.5, relwidth=0.11, relheight=0.3)

        self.botaotec = customtkinter.CTkButton(self.top4, text=u'\u2315', command=self.busca_tecnico)
        self.botaotec.place(relx=0.13, rely=0.5, relwidth=0.04, relheight=0.3)

        self.botaoImprimirOrc = customtkinter.CTkButton(self.top4, text="Imprimir", command=self.imprime_orc)
        self.botaoImprimirOrc.place(relx=0.92, rely=0.15, relwidth=0.07, relheight=0.7)

        self.entradatotal = customtkinter.CTkEntry(self.top4)
        self.entradatotal2 = Entry(self.top4)
        self.entradatotal.place(relx=0.856, rely=0.3, relwidth=0.06, relheight=0.4)

        self.descrtotal = customtkinter.CTkButton(self.top4, text="Total R$", command=self.total_orc)
        self.descrtotal.place(relx=0.79, rely=0.3, relwidth=0.065, relheight=0.4)

        #  Label Licença
        licenciamento = customtkinter.CTkLabel(self.top4, text="Licenciado para: " + self.licenciado)
        licenciamento.place(relx=0.35, rely=0.6, relwidth=0.3, relheight=0.4)

        def funcpag():
            if self.listaNumOrc.get() == "":
                msg = "É necessário que um Orçamento ou Ordem de Serviço esteja " \
                      "devidamente carregada na tela!!!"
                messagebox.showinfo("GLAC", msg)
            else:
                self.pagaOrdem()

        # Botao Forma de Pagamento
        formapag = customtkinter.CTkButton(self.top4, text="Forma de Pagamento  $$$", command=funcpag)
        formapag.place(relx=0.4, rely=0.1, relwidth=0.2, relheight=0.5)
    def menus(self):
        menubar = Menu(self.window_one)
        self.window_one.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)
        filemenu3 = Menu(menubar)
        filemenu4 = Menu(menubar)
        filemenu5 = Menu(menubar)
        filemenu6 = Menu(menubar)


        def quit():
            self.window_one.destroy()

        def helpme():
            msg = "Ajuda"
            msg += ""
            messagebox.showinfo("GLAC ", msg)

        def sobre():
            msg = "GlacX -        rafaelserafim.rfzorzi@gmail.com           \n "
            msg += "RfZorzi - https://www.facebook.com/rfzorzi/ - Brazil"
            messagebox.showinfo("GLAC ", msg)
        def manual():
            webbrowser.open("https://docs.google.com/document/d/1AyvAEJngBzOGpq5lXcxnNRDQrJxjVW30qvurceokePU/edit?usp=sharing")
        def modo_claro():
            customtkinter.set_appearance_mode("light")
            customtkinter.set_default_color_theme("dark-blue")
        def modo_escuro():
            customtkinter.set_appearance_mode("Dark")
            customtkinter.set_default_color_theme("dark-blue")

        menubar.add_cascade(label="Cadastro", menu=filemenu)
        menubar.add_cascade(label="Consulta", menu=filemenu2)
        menubar.add_cascade(label="Relatorios", menu=filemenu3)
        menubar.add_cascade(label="Procedimentos", menu=filemenu4)
        menubar.add_cascade(label="Mensageria", menu=filemenu6)
        menubar.add_cascade(label="Ajuda", menu=filemenu5)

        filemenu.add_command(label="Automoveis", command=self.cadaut)
        filemenu.add_command(label="Clientes", command=self.customer_registration)
        filemenu.add_command(label="Fornecedores", command=self.cadforn)
        filemenu.add_command(label="Produtos", command=self.cadprod)
        filemenu.add_command(label="Marca Produtos", command=self.cadmarcaprod)
        filemenu.add_command(label="Serviços", command=self.cadserv)
        filemenu.add_command(label="Tecnico", command=self.cadtec)

        filemenu.add_command(label="Sair", command=quit)
        filemenu2.add_command(label="Consulta_Receitas", command=self.cadfinan)
        filemenu2.add_command(label="Consulta_Pagamentos", command=self.consultapag)
        filemenu3.add_command(label="Orcamento", command=self.imprime_orc)
        filemenu3.add_command(label="Imprimir Vistoria", command=self.imprime_vist)
        filemenu3.add_command(label="Lista de Clientes", command=self.Imprime_lista_clientes)
        filemenu3.add_command(label="Valores a receber", command=self.Imprime_valores_a_receber)
        #filemenu3.add_command(label="Gerador de relatorios", command=self.Gerador_front)
        #filemenu4.add_command(label=self.m_Proced_Lanc, command=self.cadest)
        filemenu4.add_command(label="Atualiza Serviços", command=self.procedServ)
        filemenu4.add_command(label="Modo tema claro", command=modo_claro)
        filemenu4.add_command(label="Modo tema escuro", command=modo_escuro)
        filemenu5.add_command(label="Sobre", command=sobre)
        filemenu5.add_command(label="Manual de uso do sistema", command=manual)
        filemenu6.add_command(label="Envios de SMS", command=self.sms_tela)
        filemenu6.add_command(label="Envios de Whatsapp", command=self.whats_tela)
    def aba1(self):
        self.DescrProbLB = Label(self.frame_aba1,
            text='Descreva aqui o problema relatado pelo cliente e/ou serviço solicitado')
        self.area1 = customtkinter.CTkTextbox(self.frame_aba1, border_color="#7f5af0", corner_radius=12, border_width=2)
        self.area2 = Entry(self.frame_aba1)
        self.DescrProb2LB = Label(self.frame_aba1,
            text='Descreva aqui o(s) serviço(s) autorizados e realizado(s)')
        self.area3 = customtkinter.CTkTextbox(self.frame_aba1, border_color="#7f5af0", corner_radius=12, border_width=2)
        self.area4 = Entry(self.frame_aba1)
        self.descrInicio = customtkinter.CTkLabel(self.frame_aba1, text='Data inicial')
        self.listInicio = DateEntry(self.frame_aba1, locale="pt_BR")
        ToolTip(self.listInicio, "Data de inicio da manutenção no veiculo.")

        self.descrFim = customtkinter.CTkLabel(self.frame_aba1, text='Data final')
        self.listFim = DateEntry(self.frame_aba1, locale="pt_BR")
        ToolTip(self.listFim, "Data de finalização da manutenção no veiculo.")

        self.DescrProbLB.place(relx=0.25, rely=0.06, relwidth=0.5, relheight=0.08)
        self.area1.place(relx=0.05, rely=0.18, relwidth=0.9, relheight=0.2)
        #self.area2.place(relx=0.05, rely=0.285, relwidth=0.9, relheight=0.1)
        self.DescrProb2LB.place(relx=0.3, rely=0.51, relwidth=0.4, relheight=0.08)
        self.area3.place(relx=0.05, rely=0.63, relwidth=0.9, relheight=0.2)
        #self.area4.place(relx=0.05, rely=0.735, relwidth=0.9, relheight=0.1)
        self.descrInicio.place(relx=0.05, rely=0.055, relwidth=0.09, relheight=0.08)
        self.listInicio.place(relx=0.14, rely=0.055, relwidth=0.1, relheight=0.08)
        self.descrFim.place(relx=0.05, rely=0.505, relwidth=0.09, relheight=0.08)
        self.listFim.place(relx=0.14, rely=0.505, relwidth=0.1, relheight=0.08)
    def aba3(self):
        self.descrCol4572 = customtkinter.CTkFrame(self.frame_aba3)
        self.descrCol4572.place(relx=0.01, rely=0.043, relwidth=1, relheight=0.7)

        self.descrCol2 = customtkinter.CTkLabel(self.descrCol4572, text='Serviços / Produtos')
        self.descrCol2.place(relx=0.08, rely=0.05, relwidth=0.455, relheight=0.07)

        self.descrCodI = customtkinter.CTkLabel(self.descrCol4572, text='Código')
        self.descrCodI.place(relx=0.61, rely=0.05, relwidth=0.05, relheight=0.07)

        self.descrCol3 = customtkinter.CTkLabel(self.descrCol4572, text='Valor Unit')
        self.descrCol3.place(relx=0.699, rely=0.05, relwidth=0.08, relheight=0.07)

        self.descrQuant = customtkinter.CTkButton(self.descrCol4572, text='Quant', command=self.altera_itens_orc_quant2)
        self.descrQuant.place(relx=0.785, rely=0.05, relwidth=0.08, relheight=0.07)

        self.descrTotalItem = customtkinter.CTkLabel(self.descrCol4572, text='Total Item')
        self.descrTotalItem.place(relx=0.87, rely=0.05, relwidth=0.078, relheight=0.07)


        self.listaCol2a = customtkinter.CTkEntry(self.descrCol4572)
        self.listaCol2a.place(relx=0.1, rely=0.13, relwidth=0.455, relheight=0.08)

        self.botaoBuscaSP1 = customtkinter.CTkButton(self.descrCol4572, text=u'\u2315', command=self.busca_servico1)
        self.botaoBuscaSP1.place(relx=0.56, rely=0.13, relwidth=0.035, relheight=0.08)

        self.codServ1 = customtkinter.CTkEntry(self.descrCol4572)
        self.codServ1.configure(validate="key", justify='center', validatecommand=self.vcmd6)
        self.codServ1.place(relx=0.61, rely=0.13, relwidth=0.05, relheight=0.08)

        self.botaoAddServicos1 = customtkinter.CTkButton(self.descrCol4572, text='>', command=self.add_servico1)
        self.botaoAddServicos1.place(relx=0.66, rely=0.13, relwidth=0.035, relheight=0.08)

        self.listaCol3a = customtkinter.CTkEntry(self.descrCol4572)
        self.listaCol3a.configure(validate="key", validatecommand=self.vcmd4float, justify='center')
        self.listaCol3a.place(relx=0.79, rely=0.13, relwidth=0.07, relheight=0.08)

        self.listaCol4a = customtkinter.CTkEntry(self.descrCol4572)
        self.listaCol4a.configure(validate="key", justify='right')
        self.listaCol4a.place(relx=0.699, rely=0.13, relwidth=0.08, relheight=0.08)

        self.listaCol5a = customtkinter.CTkEntry(self.descrCol4572)
        self.listaCol5a.configure(validate="key")
        self.listaCol5a.place(relx=0.87, rely=0.13, relwidth=0.078, relheight=0.08)

        self.botaoAddServicos2 = customtkinter.CTkButton(self.descrCol4572, text="Add", command=self.add_itens_orc)
        self.botaoAddServicos2.place(relx=0.95, rely=0.13, relwidth=0.04, relheight=0.08)

        self.barraServProd = Scrollbar(self.frame_aba3, orient='vertical', command=self.OnVsb_Orc2)
        self.listaServProd = ttk.Treeview(self.frame_aba3, height=10,
                column=("col1", "col2", "col3", "col4", "col5", "col6"), yscrollcommand=self.barraServProd.set)
        self.listaServProd.heading("#0", text="")
        self.listaServProd.heading("#1", text='Item')
        self.listaServProd.heading("#2", text='Serviços')
        self.listaServProd.heading("#3", text='Codigo')
        self.listaServProd.heading("#4", text='Valor')
        self.listaServProd.heading("#5", text='Quant')
        self.listaServProd.heading("#6", text='Valor Total')
        self.listaServProd.column("#0", width=1)
        self.listaServProd.column("#1", width=10)
        self.listaServProd.column("#2", width=450)
        self.listaServProd.column("#3", width=35)
        self.listaServProd.column("#4", width=50)
        self.listaServProd.column("#5", width=25)
        self.listaServProd.column("#6", width=50)
        self.listaServProd.configure(yscroll=self.barraServProd.set)
        self.listaServProd.bind('<Double-1>', self.altera_itens_orc)
        self.listaServProd.bind('<Return>', self.altera_itens_orc)
        self.listaServProd.bind('<Delete>', self.altera_itens_orc_deletabt2)

        self.listaServProd.place(relx=0.01, rely=0.24, relwidth=0.96, relheight=0.72)
        self.barraServProd.place(relx=0.97, rely=0.24, relheight=0.72)
    def aba4(self):
        self.frameProb = customtkinter.CTkFrame(self.frame_aba4)
        self.descrTanq = customtkinter.CTkLabel(self.frame_aba4, text="Tanque")
        self.are1 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrOdom = customtkinter.CTkLabel(self.frame_aba4, text="Odometro")
        self.are2 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrRad = customtkinter.CTkLabel(self.frame_aba4, text="Interior")
        self.are3 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrCalot = customtkinter.CTkLabel(self.frame_aba4, text="Lataria")
        self.are4 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrtri = customtkinter.CTkLabel(self.frame_aba4, text="Obs")
        self.are5 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrMacaco = customtkinter.CTkLabel(self.frame_aba4, text="Obs")
        self.are6 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrEst = customtkinter.CTkLabel(self.frame_aba4, text="Obs")
        self.are7 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrAre8 = customtkinter.CTkLabel(self.frame_aba4, text="Obs")
        self.are8 = customtkinter.CTkEntry(self.frame_aba4)
        self.descrAre9 = customtkinter.CTkLabel(self.frame_aba4, text="Obs")
        self.are9 = customtkinter.CTkEntry(self.frame_aba4)
        self.botaoImprimirVist = customtkinter.CTkButton(self.frame_aba4, text="Imprimir")
        self.botaoImprimirVist.configure(command=self.imprime_vist)

        self.frameProb.place(relx=0, rely=0, relwidth=1, relheight=1)
        self.descrTanq.place(relx=0.52, rely=0.34, relwidth=0.21, relheight=0.1)
        self.are1.place(relx=0.73, rely=0.34, relwidth=0.1, relheight=0.1)
        self.descrOdom.place(relx=0.52, rely=0.46, relwidth=0.21, relheight=0.1)
        self.are2.place(relx=0.73, rely=0.46, relwidth=0.1, relheight=0.1)
        self.descrRad.place(relx=0.02, rely=0.34, relwidth=0.21, relheight=0.1)
        self.are3.place(relx=0.23, rely=0.34, relwidth=0.25, relheight=0.1)
        self.descrCalot.place(relx=0.02, rely=0.46, relwidth=0.21, relheight=0.1)
        self.are4.place(relx=0.23, rely=0.46, relwidth=0.25, relheight=0.1)
        self.descrtri.place(relx=0.02, rely=0.58, relwidth=0.21, relheight=0.1)
        self.are5.place(relx=0.23, rely=0.58, relwidth=0.25, relheight=0.1)
        self.descrMacaco.place(relx=0.02, rely=0.7, relwidth=0.21, relheight=0.1)
        self.are6.place(relx=0.23, rely=0.7, relwidth=0.25, relheight=0.1)
        self.descrEst.place(relx=0.02, rely=0.82, relwidth=0.21, relheight=0.1)
        self.are7.place(relx=0.23, rely=0.82, relwidth=0.25, relheight=0.1)
        self.descrAre8.place(relx=0.52, rely=0.58, relwidth=0.21, relheight=0.1)
        self.are8.place(relx=0.73, rely=0.58, relwidth=0.25, relheight=0.1)
        self.descrAre9.place(relx=0.52, rely=0.7, relwidth=0.21, relheight=0.1)
        self.are9.place(relx=0.73, rely=0.7, relwidth=0.25, relheight=0.1)
        self.botaoImprimirVist.place(relx=0.02, rely=0.06, relwidth=0.1, relheight=0.1)
    def aba5(self):
        self.frameProb = GradientFrame(self.frame_aba5)
        self.frameProb.place(relx=0, rely=0, relwidth=1, relheight=1)

        self.frameProb2 = Frame(self.frame_aba5)
        self.frameProb2.place(relx=0.1, rely=0.1, relwidth=0.39, relheight=0.82)

        self.Revisao_label = Label(self.frame_aba5, text= "Itens de Revisão:")
        self.Revisao_label.place(relx=0.2, rely=0.1, relwidth=0.2, relheight=0.1)

        self.alinhamento_calibragem_checkin = Checkbutton(self.frame_aba5, text="Alinhamento e Calibragem")
        self.alinhamento_calibragem_checkin.place(relx=0.1, rely=0.2, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.1, rely=0.28, relwidth=0.39, relheight=0.08)
        self.suspensao_amortecedores_label = Checkbutton(self.frame_aba5, text="Suspensão e amortecedores ", bg='gray')
        self.suspensao_amortecedores_label.place(relx=0.1, rely=0.28, relheight=0.08)

        self.fluido_freio_label = Checkbutton(self.frame_aba5, text="Fluido de freio ")
        self.fluido_freio_label.place(relx=0.1, rely=0.36, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.1, rely=0.44, relwidth=0.39, relheight=0.08)
        self.fluido_freio_label = Checkbutton(self.frame_aba5, text="Troca de Oleo ", bg='gray')
        self.fluido_freio_label.place(relx=0.1, rely=0.44, relheight=0.08)

        self.fluido_freio_label = Checkbutton(self.frame_aba5, text="Agua Radiador ")
        self.fluido_freio_label.place(relx=0.1, rely=0.52, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.1, rely=0.6, relwidth=0.39, relheight=0.08)
        self.fluido_freio_label = Checkbutton(self.frame_aba5, text="Luzes ", bg='gray')
        self.fluido_freio_label.place(relx=0.1, rely=0.6, relheight=0.08)

        self.bateria_label = Checkbutton(self.frame_aba5, text="Bateria ")
        self.bateria_label.place(relx=0.1, rely=0.68, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.1, rely=0.76, relwidth=0.39, relheight=0.08)
        self.sistema_freio_label = Checkbutton(self.frame_aba5, text="Sistema de freios ", bg='gray')
        self.sistema_freio_label.place(relx=0.1, rely=0.76, relheight=0.08)

        self.embreagem_label = Checkbutton(self.frame_aba5, text="Sistema de embreagem ")
        self.embreagem_label.place(relx=0.1, rely=0.84, relheight=0.08)

        #############

        self.frameProb2 = Frame(self.frame_aba5)
        self.frameProb2.place(relx=0.51, rely=0.1, relwidth=0.39, relheight=0.82)

        self.ProximaRevisao_label = LabelGlac(self.frame_aba5, "Proxima Revisão:")
        self.ProximaRevisao_label.place(relx=0.6, rely=0.1, relwidth=0.2, relheight=0.1)

        self.alinhamento_calibragem_prox_rev = Checkbutton(self.frame_aba5, text="Alinhamento e Calibragem", justify="left")
        self.alinhamento_calibragem_prox_rev.place(relx=0.51, rely=0.2, relheight=0.08)

        self.alinhamento_calibragem_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.alinhamento_calibragem_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.2, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.51, rely=0.28, relwidth=0.39, relheight=0.08)
        self.suspensao_amortecedores_label_prox_rev = Checkbutton(self.frame_aba5, text="Suspensão e amortecedores ", bg="gray", justify="left")
        self.suspensao_amortecedores_label_prox_rev.place(relx=0.51, rely=0.28, relheight=0.08)

        self.suspensao_amortecedores_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.suspensao_amortecedores_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.28, relheight=0.08)

        self.fluido_freio_label_prox_rev = Checkbutton(self.frame_aba5, text="Fluido de freio ", justify="left")
        self.fluido_freio_label_prox_rev.place(relx=0.51, rely=0.36, relheight=0.08)

        self.fluido_freio_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.fluido_freio_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.36, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.51, rely=0.44, relwidth=0.39, relheight=0.08)
        self.troca_oleo_label_prox_rev = Checkbutton(self.frame_aba5, text="Troca de Oleo ", bg="gray", justify="left")
        self.troca_oleo_label_prox_rev.place(relx=0.51, rely=0.44, relheight=0.08)

        self.troca_oleo_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.troca_oleo_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.44, relheight=0.08)

        self.agua_label_prox_rev = Checkbutton(self.frame_aba5, text="Agua Radiador ", justify="left")
        self.agua_label_prox_rev.place(relx=0.51, rely=0.52, relheight=0.08)

        self.agua_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.agua_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.52, relheight=0.08)

        self.agua_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.agua_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.44, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.51, rely=0.6, relwidth=0.39, relheight=0.08)
        self.luzes_label_prox_rev = Checkbutton(self.frame_aba5, text="Luzes ", bg="gray")
        self.luzes_label_prox_rev.place(relx=0.51, rely=0.6, relheight=0.08)

        self.luzes_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.luzes_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.6, relheight=0.08)

        self.bateria_label_prox_rev = Checkbutton(self.frame_aba5, text="Bateria ")
        self.bateria_label_prox_rev.place(relx=0.51, rely=0.68, relheight=0.08)

        self.bateria_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.bateria_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.68, relheight=0.08)

        frameaba5 = Frame(self.frame_aba5, bg="gray")
        frameaba5.place(relx=0.51, rely=0.76, relwidth=0.39, relheight=0.08)
        self.sistema_freio_label_prox_rev = Checkbutton(self.frame_aba5, text="Sistema de freios ", bg="gray")
        self.sistema_freio_label_prox_rev.place(relx=0.51, rely=0.76, relheight=0.08)

        self.sistema_freio_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.sistema_freio_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.76, relheight=0.08)

        self.sistema_embreagem_label_prox_rev = Checkbutton(self.frame_aba5, text="Sistema de embreagem ")
        self.sistema_embreagem_label_prox_rev.place(relx=0.51, rely=0.84, relheight=0.08)

        self.sistema_embreagem_label_prox_rev_date = DateEntry(self.frame_aba5, locale="pt_BR")
        self.sistema_embreagem_label_prox_rev_date.place(relx=0.8, relwidth=0.1, rely=0.84, relheight=0.08)

PrimaryWindow()