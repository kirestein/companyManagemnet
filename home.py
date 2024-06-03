import customtkinter as ctk
from settings import *
import tkinter as tk
import tkinter.messagebox
import requests
import locale
from datetime import datetime
from variaveis import *
from PIL import Image, ImageTk
# import tkcalendar as cal
from tkcalendar import Calendar, DateEntry
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

ctk.set_appearance_mode("Light")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

locale.setlocale(locale.LC_TIME, '')

class Home(ctk.CTkToplevel):
    width = 1200
    height = 790
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=RED)
        self.title('Cadastro de Funcionários')
        self.geometry(f"{self.width}x{self.height}")
        self.iconbitmap('empty.ico')
        self.change_title_bar_color()
        
        # configure grid
        self.columnconfigure(0, weight=0)
        self.columnconfigure((1,2,3), weight=1)
        # self.columnconfigure(1, weight=0)
        self.rowconfigure((0,1,2), weight=1, uniform='a')
        self.rowconfigure(3,weight=0)
        
        
        
        #! left frame
        self.left_frame = ctk.CTkFrame(self, width=60, corner_radius=5)
        self.left_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.left_frame.grid_rowconfigure(4, weight=1)
        self.aniversariantes_label = ctk.CTkLabel(self.left_frame, text='Aniversariantes do mês', font=ctk.CTkFont(size=20, family=FONT, weight='bold'), justify='center', anchor='w')
        self.aniversariantes_label.grid(row=0, column=0, padx=40, pady=(20,10))
        
        
        #! Tabview 1
        self.tab = ctk.CTkTabview(self, width=100, corner_radius=10)
        self.tab.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        self.tab.add('Cadastros')
        self.tab.add('Gerenciamento')
        self.tab.tab('Cadastros').grid_columnconfigure((0,1), weight=1) # configure grid of individual tabs
        self.tab.tab('Cadastros').grid_rowconfigure((0,1), weight=1)
        self.tab.tab('Gerenciamento').grid_columnconfigure(0, weight=1) # configure grid of individual tabs
        
        self.btn_register_employee = ctk.CTkButton(
            self.tab.tab('Cadastros'),
            text='Cadastrar Funcionário',
            command=self.register_employees
        )
        self.btn_register_employee.grid(row=0, column=0, padx=10, pady=10)
        
        self.btn_register_job_salaies = ctk.CTkButton(
            self.tab.tab('Cadastros'),
            text='Cadastrar Cargos e Salários',
        )
        self.btn_register_job_salaies.grid(row=0, column=1, padx=10, pady=10)
        
        self.btn_register_forms = ctk.CTkButton(
            self.tab.tab('Cadastros'),
            text='Cadastrar formulário'
        )
        self.btn_register_forms.grid(row=1, column=0, padx=10, pady=10)
        
        Footer(self)
        
    def change_title_bar_color(self):
        try:
            HWND = windll.user32.GetParent(self.winfo_id())
            DWMWA_ATTRIBUTE = 35
            COLOR = TITLE_HEX_COLOR
            windll.dwmapi.DwmSetWindowAttribute(HWND,DWMWA_ATTRIBUTE, byref(c_int(COLOR)), sizeof(c_int))
        except:
            print('ola')
            
    def register_employees(self):
        self.tab.grid_forget()
        RegisterEmployee(self)
        print('entrou')
    
        
        
        
    #     self.protocol('WM_DELETE_WINDOW', self.on_close)
        
    # def on_close(self):
    #     self.master.deiconify()
    #     self.destroy()
    
class RegisterEmployee(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE, width=250, corner_radius=10)
        self.grid(row=0, column=1, rowspan=3, columnspan=3 ,padx=20, pady=20, sticky='nsew')
        self.grid_columnconfigure((0,1,2,3), weight=1)        
        
        self.home = parent
        EmployeeData(self)
        Trainee(self)
        Documentation(self)
        ContractData(self)
        
        self.btn_save = ctk.CTkButton(self, anchor='center', width=400,command=self.save, font=ctk.CTkFont(size=20), text='Save')
        self.btn_save.grid(row=27, column=1, columnspan=2, padx=20, pady=20)
        
    def save(self):
        pass
        
class EmployeeData(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE, width=250, corner_radius=10, border_color=DARK_GRAY, border_width=1)
        
        self.grid(row=0, column=1, rowspan=3, columnspan=3 ,padx=20, pady=20, sticky='nsew')
        self.grid_columnconfigure((0,1,2,3), weight=1)        
        self.home = parent
        
        # self.register_employees.grid_forget()

        font = ctk.CTkFont(family=FONT, size=20)
        self.btn_return = ctk.CTkButton(self, text='🔙', command=self.back, font=font, width=80)
        self.btn_return.grid(row=0, column=0,padx=20, pady=20)
        self.title = ctk.CTkLabel(self, text='DADOS DO FUNCIONÁRIO', font=ctk.CTkFont(size=20, family=FONT, weight='bold'), justify='center', anchor='w')
        self.title.grid(row=0, column=1, columnspan=2, padx=20, pady=20)
        # self.frame_title = ctk.CTkFrame(self)
        # self.frame_title.grid(row=0, column=3, padx=20, pady=20)
        # self.frame_title.grid_columnconfigure((0, 1), weight=1)
        # self.btn_plus = ctk.CTkButton(self.frame_title, text='➕')
        
        
        #* line 1
        self.frame_1 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_1.grid(row=1, column=0, padx=20, pady=20)
        self.frame_1.grid_columnconfigure((0,1), weight=1)
        self.number = ctk.CTkEntry(self.frame_1, width=60, placeholder_text='Nº')
        self.number.grid(row=0, column=0, padx=1, pady=20)
        self.company = ctk.CTkEntry(self.frame_1, width=140, placeholder_text='Nome da Empresa')
        self.company.grid(row=0, column=1, padx=1, pady=20)
        self.tag_name = ctk.CTkEntry(self, width=200, placeholder_text='Nome no crachá')
        self.tag_name.grid(row=1, column=1, padx=20, pady=20)
        self.tag_lastname = ctk.CTkEntry(self,width=200, placeholder_text='Sobrenome no Crachá')
        self.tag_lastname.grid(row=1, column=2, padx=20, pady=20)
        self.email = ctk.CTkEntry(self, width=200, placeholder_text='e-mail do funcionário')
        self.email.grid(row=1, column=3, padx=20, pady=20)
        
        #* line 2
        self.full_name = ctk.CTkEntry(self, width=400, placeholder_text='Nome')
        self.full_name.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
        
        #? create a option menu with date, using DateEntry
        self.birthday = DateEntry(self, background='darkblue',
                          foreground='white', borderwidth=2, locale=locale.getlocale()[0])
        self.birthday.grid(row=2, column=2, padx=20, pady=20)
        self.frame_cep = ctk.CTkFrame(self, fg_color=WHITE, border_color='#eee')
        self.frame_cep.grid(row=2, column=3, padx=5, pady=20)
        self.frame_cep.grid_columnconfigure((0, 1), weight=1)
        self.cep_var = ctk.StringVar(value='CEP')
        self.cep = ctk.CTkEntry(self.frame_cep, width=80, placeholder_text='CEP', textvariable=self.cep_var)
        self.cep.grid(row=0, column=0, padx=20, pady=20)
        self.btn_search = ctk.CTkButton(self.frame_cep, text='Buscar', command=self.get_address_from_cep, width=60)
        self.btn_search.grid(row=0, column=1, padx=5, pady=20)
        
        self.cep.bind('<KeyRelease>', self.cep_changed)
        #* line 3
        # creating the variable to address
        self.address_street = ctk.StringVar(value='Endereço')
        self.address_neighboor = ctk.StringVar(value='Bairro')
        self.address_city = ctk.StringVar(value='Cidade')
        self.address_state = ctk.StringVar(value='UF')
        
        self.street = ctk.CTkEntry(self, width=200, placeholder_text='Endereço', textvariable=self.address_street)
        self.street.grid(row=3, column=0, padx=20, pady=20)
        self.neighboor = ctk.CTkEntry(self, width=200, placeholder_text='Bairro', textvariable=self.address_neighboor)
        self.neighboor.grid(row=3, column=1, padx=20, pady=20)
        self.city = ctk.CTkEntry(self, width=200, placeholder_text='Cidade', textvariable=self.address_city)
        self.city.grid(row=3, column=2, padx=20, pady=20)
        self.state_uf = ctk.CTkEntry(self, width=200, placeholder_text='UF', textvariable=self.address_state)
        self.state_uf.grid(row=3, column=3, padx=5, pady=20)
        
        #* line 4
        self.frame_4 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_4.grid(row=4, column=0, padx=1, pady=20)
        self.frame_4.grid_columnconfigure((0, 1), weight=1)
        self.number = ctk.CTkEntry(self.frame_4, width=80, placeholder_text='Nº')
        self.number.grid(row=0, column=0, padx=10, pady=20)
        self.complement = ctk.CTkEntry(self.frame_4, width=80, placeholder_text='Comp')
        self.complement.grid(row=0, column=1, padx=10, pady=20)
        self.phone_number = ctk.CTkEntry(self, width=200, placeholder_text='Telefone')
        self.phone_number.grid(row=4, column=1, padx=20, pady=20)
        self.mobile = ctk.CTkEntry(self, width=200, placeholder_text='Celular')
        self.mobile.grid(row=4, column=2, padx=20, pady=20)
        self.frame_4_1 = ctk.CTkEntry(self, fg_color=WHITE, border_color=WHITE)
        self.frame_4_1.grid(row=4, column=3, padx=20, pady=20)
        self.frame_4_1.grid_columnconfigure((0,1), weight=1)
        self.naturalness = ctk.CTkEntry(self.frame_4_1, width=90, placeholder_text='Naturalidade')
        self.naturalness.grid(row=0, column=0, padx=1, pady=20)
        self.nationality = ctk.CTkEntry(self.frame_4_1, width=90, placeholder_text='Nacionalidade')
        self.nationality.grid(row=0, column=1, padx=1, pady=20)
        
        #* line 5
        self.father = ctk.CTkEntry(self, width=400, placeholder_text='Nome do pai')
        self.father.grid(row=5, column=0, columnspan=2, padx=20, pady=20)
        self.mother = ctk.CTkEntry(self, width=400, placeholder_text='Nome do mãe')
        self.mother.grid(row=5, column=2, columnspan=2, padx=20, pady=20)
        
        #* line 6
        self.frame_6 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_6.grid(row=6, column=0, columnspan=2, padx=20, pady=20)
        self.frame_6.grid_columnconfigure((0,1,2), weight=1)
        marital_status_var = ctk.StringVar(value='Solteiro')
        gender_var = ctk.StringVar(value='Masculino')
        self.marital_status = ctk.CTkOptionMenu(self.frame_6, values=['Solteiro', 'Casado', 'União Estável', 'Separado', 'Divorciado', 'Viúvo'], variable=marital_status_var, width=100)
        self.marital_status.grid(row=0, column=0, padx=1, pady=20)
        self.gender = ctk.CTkOptionMenu(self.frame_6, values=['Masculino', 'Feminino', 'Não Binário'], variable=gender_var, width=100)
        self.gender.grid(row=0, column=1, padx=5, pady=20)
        self.graduation = ctk.CTkEntry(self.frame_6, width=100, placeholder_text='Grau de instrução')
        self.graduation.grid(row=0, column=2, padx=5, pady=20)
        self.frame_6_1 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_6_1.grid(row=6, column=2, columnspan=2, padx=10, pady=20)
        self.frame_6_1.grid_columnconfigure((0,1,2), weight=1)
        self.skin_color = ctk.CTkEntry(self.frame_6_1, width=120, placeholder_text='Cor de pele')
        self.skin_color.grid(row=0, column=0, padx=5, pady=20)
        self.meal = ctk.CTkEntry(self.frame_6_1, width=120, placeholder_text='Refeição')
        self.meal.grid(row=0, column=1, padx=5, pady=20)
        self.transport = ctk.CTkEntry(self.frame_6_1, width=120, placeholder_text='Vale Transporte')
        self.transport.grid(row=0, column=2, padx=5, pady=20)
        
        #* line 7
        self.acident_label = ctk.CTkLabel(self, width=200, text='Contato de emergência: ')
        self.acident_label.grid(row=7, column=0, padx=20, pady=20)
        self.contact_name = ctk.CTkEntry(self, width=400, placeholder_text='Nome do contato')
        self.contact_name.grid(row=7, column=1, columnspan=2, padx=20, pady=20)
        self.contact_phone = ctk.CTkEntry(self, width=200, placeholder_text='Telefone')
        self.contact_phone.grid(row=7, column=3, padx=20, pady=20)
        
        #* line 8
        self.dependents = []
        self.dependents_frame = ctk.CTkFrame(self, fg_color=WHITE)
        self.dependents_frame.grid(row=8, column=0, columnspan=4, padx=20, pady=20)
        self.dependents_frame.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.dependent_name = ctk.CTkEntry(self.dependents_frame, width=200, placeholder_text='Nome do dependente')
        self.dependent_name.grid(row=0, column=0, padx=20, pady=20)
        self.dependent_birthday = DateEntry(self.dependents_frame, background='darkblue', foreground='white', borderwidth=2, locale=locale.getlocale()[0])
        self.dependent_birthday.grid(row=0, column=1, padx=20, pady=20)
        self.dependent_cpf = ctk.CTkEntry(self.dependents_frame, width=80, placeholder_text='CPF')
        self.dependent_cpf.grid(row=0, column=2, padx=20, pady=20)
        relation = ctk.StringVar(value='Conjugê')
        self.relation = ctk.CTkOptionMenu(self.dependents_frame, width=100, values=['Conjugê', 'Filho', 'Filha', 'Pai', 'Mãe', 'Irmão', 'Irmã', 'Outro'], variable=relation)
        self.relation.grid(row=0, column=3, padx=20, pady=20)
        
        self.dependent_cpf.bind('<KeyRelease>', self.format_cpf)
        font_btn = ctk.CTkFont(size=20)
        self.btn_add_dependent = ctk.CTkButton(self.dependents_frame, text='+', font=font_btn, command=self.new_dependent, width=30)
        self.btn_add_dependent.grid(row=0, column=4, padx=20, pady=20)
        
        
    def back(self):
        self.home.grid_forget()
        self.home.home.tab.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        
        
    def on_date_select(self):
        selected_date = self.calendar.get_date()
        self.birthday.set(selected_date)
        
    def cep_changed(self, *args):
        self.cep_var.set(self.cep.get())
        print(self.cep_var.get())
        
    def get_address_from_cep(self, *args):
        # print(self.cep_var.get())
        response = requests.get(f'http://viacep.com.br/ws/{self.cep_var.get()}/json/')
        if response.status_code == 200 and response.text.strip():
            data = response.json()
            # self.address_data.update(data)
            self.address_street.set(data['logradouro'])
            self.address_neighboor.set(data['bairro'])
            self.address_city.set(data['localidade'])
            self.address_state.set(data['uf'])
            return data
        else:
            print(f"Error: Unable to get address for CEP {self.cep_var.get()}")
            return None
        
    def format_cpf(self, *args):
        text = self.dependent_cpf.get().replace(".", "").replace("-", "")[:11]
        new_text = ""
        
        if len(text) <= 11:
            for index, char in enumerate(text):
                if not char.isdigit():
                    continue
                if index in [2, 5]:
                    new_text += char + "."
                elif index == 8:
                    new_text += char + "-"
                else:
                    new_text += char
            self.dependent_cpf.delete(0, "end")
            self.dependent_cpf.insert(0, new_text)
            
    def new_dependent(self):
        self.dependents.append(
            {
                'name': self.dependent_name.get(),
                'birthday': self.dependent_birthday.get(),
                'cpf': self.dependent_cpf.get(),
                'relation': self.relation.get()
            }
        )
        self.dependent_name.delete(0, 500)
        self.dependent_cpf.delete(0, 20)
        print(self.dependents)
    
class Trainee(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE, width=250, corner_radius=10, border_color=DARK_GRAY, border_width=1)
        self.grid(row=9, column=0, rowspan=3, columnspan=3 ,padx=20, pady=20, sticky='nsew')
        self.grid_columnconfigure((0,1,2,3), weight=1)        
        self.home = parent

        self.title = ctk.CTkLabel(self, text='   DADOS  BÁSICOS PARA EMISSÃO DE CONTRATO DE ESTÁGIO', font=ctk.CTkFont(size=20, family=FONT, weight='bold'), justify='center', anchor='center')
        self.title.grid(row=0, column=0, columnspan=4, padx=20, pady=20, sticky='nsew')
        
        #* line 1
        self.frame_cep = ctk.CTkFrame(self, fg_color=WHITE, border_color='#eee')
        self.frame_cep.grid(row=1, column=0, padx=5, pady=20)
        self.frame_cep.grid_columnconfigure((0,1), weight=1)
        self.cep_var = ctk.StringVar(value='CEP')
        self.cep = ctk.CTkEntry(self.frame_cep, width=100, placeholder_text='CEP', textvariable=self.cep_var)
        self.cep.grid(row=0, column=0, padx=20, pady=20)
        self.btn_search = ctk.CTkButton(self.frame_cep, text='Buscar', command=self.get_address_from_cep, width=80)
        self.btn_search.grid(row=0, column=1, padx=5, pady=20)
        
        self.cep.bind('<KeyRelease>', self.cep_changed)
        
        self.address_street = ctk.StringVar(value='Endereço')
        self.address_neighboor = ctk.StringVar(value='Bairro')
        self.address_city = ctk.StringVar(value='Cidade')
        self.address_state = ctk.StringVar(value='UF')
        
        self.street = ctk.CTkEntry(self, width=150, placeholder_text='Endereço', textvariable=self.address_street)
        self.street.grid(row=1, column=1, padx=20, pady=20)
        self.neighboor = ctk.CTkEntry(self, width=120, placeholder_text='Bairro', textvariable=self.address_neighboor)
        self.neighboor.grid(row=1, column=2, padx=20, pady=20)
        self.city = ctk.CTkEntry(self, width=120, placeholder_text='Cidade', textvariable=self.address_city)
        self.city.grid(row=1, column=3, padx=20, pady=20)
        self.state_uf = ctk.CTkEntry(self, width=50, placeholder_text='UF', textvariable=self.address_state)
        self.state_uf.grid(row=1, column=4, padx=5, pady=20)
        
        #* line 2
        self.life_insurance_policy = ctk.CTkEntry(self, width=200, placeholder_text='Apólice de seguro de vida')
        self.life_insurance_policy.grid(row=2, column=0, padx=5, pady=20)
        self.college = ctk.CTkEntry(self, width=100, placeholder_text='Instituição de ensino')
        self.college.grid(row=2, column=1, padx=5, pady=20)
        self.course = ctk.CTkEntry(self, width=200, placeholder_text='Nome do curso')
        self.course.grid(row=2, column=2, padx=10, pady=20)
        self.training_period = ctk.CTkEntry(self, width=100, placeholder_text='Período estagiário')
        self.training_period.grid(row=2, column=3, padx=5, pady=20)
        self.ra = ctk.CTkEntry(self, width=100, placeholder_text='RA')
        self.ra.grid(row=2, column=4, padx=5, pady=20)
        
        
        
        
    def cep_changed(self, *args):
        self.cep_var.set(self.cep.get())
        print(self.cep_var.get())
        
    def get_address_from_cep(self, *args):
        # print(self.cep_var.get())
        response = requests.get(f'http://viacep.com.br/ws/{self.cep_var.get()}/json/')
        if response.status_code == 200 and response.text.strip():
            data = response.json()
            # self.address_data.update(data)
            self.address_street.set(data['logradouro'])
            self.address_neighboor.set(data['bairro'])
            self.address_city.set(data['localidade'])
            self.address_state.set(data['uf'])
            return data
        else:
            print(f"Error: Unable to get address for CEP {self.cep_var.get()}")
            return None
        
class Documentation(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE, width=250, corner_radius=10, border_color=DARK_GRAY, border_width=1)
        self.grid(row=12, column=0, rowspan=3, columnspan=3 ,padx=20, pady=20, sticky='nsew')
        self.grid_columnconfigure((0,1,2,3), weight=1)
        
        self.title = ctk.CTkLabel(self, text='DOCUMENTAÇÃO', font=ctk.CTkFont(size=20, family=FONT, weight='bold'), justify='center', anchor='center')
        self.title.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky='nsew')
        
        #* line 1
        self.frame_line_1 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_line_1.grid(row=1, column=0, columnspan=3, padx=20, pady=20, sticky='W')
        self.frame_line_1.grid_columnconfigure((0,1,2), weight=1)
        self.identity = ctk.CTkEntry(self.frame_line_1, width=80, placeholder_text='RG')
        self.identity.grid(row=0, column=0, padx=20, pady=20)
        self.agency = ctk.CTkEntry(self.frame_line_1, width=80, placeholder_text='Orgão emissor')
        self.agency.grid(row=0, column=1, padx=20, pady=20)
        self.issue_date = DateEntry(self.frame_line_1, background='darkblue',
                          foreground='white', borderwidth=2, locale=locale.getlocale()[0])
        self.issue_date.grid(row=0, column=2, padx=20, pady=20)
        # criar um botão para adicionar foto e um frame que irá exibir a foto salva, a foto que será exibida deverá vir do banco de dados, ao salvar a foto, ela deverá ser convertida em base64 e ao ser pega do banco de dados deverá ser transformada em imagem
        
        #* line 2
        self.frame_line_2 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_line_2.grid(row=2, column=0, columnspan=3, padx=20, pady=20, sticky='W')
        self.frame_line_2.grid_columnconfigure((0,1,2), weight=1)
        self.cpf = ctk.CTkEntry(self.frame_line_2, width=80, placeholder_text='CPF')
        self.cpf.grid(row=0, column=0, padx=20, pady=20)
        self.cpf.bind('<KeyRelease>', self.format_cpf)
        self.pis = ctk.CTkEntry(self.frame_line_2, width=100, placeholder_text='PIS/PASEP')
        self.pis.grid(row=0, column=1, padx=20, pady=20)
        self.reservist = ctk.CTkEntry(self.frame_line_2, width=100, placeholder_text='Reservista')
        self.reservist.grid(row=0, column=2, padx=20, pady=20)
        
        #* line 3
        self.frame_line_3 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_line_3.grid(row=3, column=0, columnspan=2, padx=20, pady=20, sticky='W')
        self.frame_line_3.grid_columnconfigure((0,1), weight=1)
        self.ctps = ctk.CTkEntry(self.frame_line_3, width=80, placeholder_text='CTPS')
        self.ctps.grid(row=0, column=0, padx=20, pady=20)
        self.series = ctk.CTkEntry(self.frame_line_3, width=80, placeholder_text='Série')
        self.series.grid(row=0, column=1, padx=20, pady=20)
        
        #* line 4
        self.frame_line_4 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_line_4.grid(row=4, column=0, columnspan=3, padx=20, pady=20, sticky='W')
        self.frame_line_4.grid_columnconfigure((0,1,2), weight=1)
        self.voter_id = ctk.CTkEntry(self.frame_line_4, width=80, placeholder_text='Título de eleitor')
        self.voter_id.grid(row=0, column=0, padx=20, pady=20)
        self.voter_section = ctk.CTkEntry(self.frame_line_4, width=100, placeholder_text='Seção')
        self.voter_section.grid(row=0, column=1, padx=20, pady=20)
        self.voter_district = ctk.CTkEntry(self.frame_line_4, width=100, placeholder_text='Zona')
        self.voter_district.grid(row=0, column=2, padx=20, pady=20)
        
        #* line 5
        self.drivers_license = ctk.CTkEntry(self, width=200, placeholder_text='Nº Habilitação')
        self.drivers_license.grid(row=5, column=0, padx=20, pady=20)
        self.category = ctk.CTkEntry(self, width=200, placeholder_text='Categoria')
        self.category.grid(row=5, column=1, padx=20, pady=20)
        self.shipping_date = DateEntry(self, background='darkblue', foreground='white', borderwidth=2, locale=locale.getlocale()[0])
        self.shipping_date.grid(row=5, column=2, padx=20, pady=20)
        self.expiration_date = DateEntry(self, background='darkblue', foreground='white', borderwidth=2, locale=locale.getlocale()[0])
        self.expiration_date.grid(row=5, column=3, padx=20, pady=20)
        
        #* line 6
        self.frame_line_6 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_line_6.grid(row=6, column=0, columnspan=2, padx=20, pady=20, sticky='W')
        self.frame_line_6.grid_columnconfigure((0,1), weight=1)
        self.health_plan = ctk.CTkEntry(self.frame_line_6, width=80, placeholder_text='Plano de Saúde')
        self.health_plan.grid(row=0, column=0, padx=20, pady=20)
        self.health_plan_id = ctk.CTkEntry(self.frame_line_6, width=100, placeholder_text='Nº carteirinha')
        self.health_plan_id.grid(row=0, column=1, padx=20, pady=20)
        
        
        
        
    def format_cpf(self, *args):
        text = self.cpf.get().replace(".", "").replace("-", "")[:11]
        new_text = ""
        
        if len(text) <= 11:
            for index, char in enumerate(text):
                if not char.isdigit():
                    continue
                if index in [2, 5]:
                    new_text += char + "."
                elif index == 8:
                    new_text += char + "-"
                else:
                    new_text += char
            self.cpf.delete(0, "end")
            self.cpf.insert(0, new_text)
       
class ContractData(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=WHITE, width=250, border_color=DARK_GRAY, border_width=1)
        self.grid(row=19, column=0, columnspan=3, padx=20, pady=20)
        self.columnconfigure((0,1,2,3), weight=1)
        
        self.title = ctk.CTkLabel(self, text='DADOS DE CONTRATAÇÃO', font=ctk.CTkFont(size=20, family=FONT, weight='bold'), justify='center', anchor='center')
        self.title.grid(row=0, column=1, columnspan=2, padx=20, pady=20, sticky='nsew')
        
        #* line 1
        self.job_position = ctk.CTkOptionMenu(self, width=200, values=['a', 'b', 'c'])
        self.job_position.grid(row=1, column=0, padx=20, pady=20)
        self.job_time = ctk.CTkEntry(self, width=200, placeholder_text='Horário')
        self.job_time.grid(row=1, column=1, padx=20, pady=20)
        self.job_start = DateEntry(self, background='darkblue', foreground='white', borderwidth=2, locale=locale.getlocale()[0])
        self.job_start.grid(row=1, column=2, padx=20, pady=20)
        self.job_end = DateEntry(self, background='darkblue', foreground='white', borderwidth=2, locale=locale.getlocale()[0])
        self.job_end.grid(row=1, column=3, padx=20, pady=20)
        
        #* line 2
        self.bank_id = ctk.CTkEntry(self, width=200, placeholder_text='Banco')
        self.bank_id.grid(row=2, column=0, padx=20, pady=20)
        self.bank_agency = ctk.CTkEntry(self, width=200, placeholder_text='Agência')
        self.bank_agency.grid(row=2, column=1, padx=20, pady=20)
        self.bank_account = ctk.CTkEntry(self, width=200, placeholder_text='Conta')
        self.bank_account.grid(row=2, column=2, padx=20, pady=20)
        self.account_type = ctk.CTkEntry(self, width=200, placeholder_text='Tipo de conta')
        self.account_type.grid(row=2, column=3, padx=20, pady=20)
        
        #* line 3
        self.job_function = ctk.CTkEntry(self, width=200, placeholder_text='Seg Função')
        self.job_function.grid(row=3, column=0, padx=20, pady=20)
        self.job_salary = ctk.CTkEntry(self, width=200, placeholder_text='Salário')
        self.job_salary.grid(row=3, column=1, padx=20, pady=20)
        self.frame_line_3 = ctk.CTkFrame(self, fg_color=WHITE)
        self.frame_line_3.grid(row=3, column=2, columnspan=2, padx=20, pady=20)
        self.frame_line_3.grid_columnconfigure((0,1,2), weight=1)
        self.time_label = ctk.CTkLabel(self.frame_line_3, text='Carga Horária: ')
        self.time_label.grid(row=0, column=0, padx=20, pady=20)
        self.week = ctk.CTkEntry(self.frame_line_3, placeholder_text='Semanal', width=60)
        self.week.grid(row=0, column=1, padx=20, pady=20)
        self.month = ctk.CTkEntry(self.frame_line_3,  width=60, placeholder_text='Mensal')
        self.month.grid(row=0, column=2, padx=20, pady=20)
        
        #* line 4
        self.link = ctk.CTkRadioButton(self, text='Posui acúmulo', width=200, command=self.link_true)
        self.link.grid(row=4, column=0, padx=20, pady=20)
        self.frame_line_4 = ctk.CTkFrame(self)
        # self.frame_line_4.grid(row=4, column=1, padx=20, pady=20, sticky='w')
        self.frame_line_4.grid_columnconfigure((0,1,2,3,4), weight=1)
        self.company = ctk.CTkEntry(self.frame_line_4, width=80, placeholder_text='Empresa')
        self.company.grid(row=0, column=0, padx=20, pady=20)
        self.subject = ctk.CTkEntry(self.frame_line_4, width=80, placeholder_text='Disciplina')
        self.subject.grid(row=0, column=1, padx=20, pady=20)
        self.cat = ctk.CTkEntry(self.frame_line_4, width=80, placeholder_text='Cat')
        self.cat.grid(row=0, column=2, padx=20, pady=20)
        self.weekly_classes = ctk.CTkEntry(self.frame_line_4, width=80, placeholder_text='Aulas semanais')
        self.weekly_classes.grid(row=0, column=3, padx=20, pady=20)
        self.btn_clear = ctk.CTkButton(self.frame_line_4, width=30, text='🗑️', command=self.clear)
        self.btn_clear.grid(row=0, column=4, padx=20, pady=20)
        
        #* line 5
        self.family_salary_1 = ctk.CTkEntry(self, width=200, placeholder_text='Salário família 1')
        self.family_salary_1.grid(row=5, column=0, padx=20, pady=20)
        self.family_salary_2 = ctk.CTkEntry(self, width=200, placeholder_text='Salário família 2')
        self.family_salary_2.grid(row=5, column=1, padx=20, pady=20)
        self.family_salary_3 = ctk.CTkEntry(self, width=200, placeholder_text='Salário família 3')
        self.family_salary_3.grid(row=5, column=2, padx=20, pady=20)
        self.family_salary_4 = ctk.CTkEntry(self, width=200, placeholder_text='Salário família 4')
        self.family_salary_4.grid(row=5, column=3, padx=20, pady=20)        
        
        #* line 6
        self.parenting_1 = ctk.CTkEntry(self, width=200, placeholder_text='Parentesco 1')
        self.parenting_1.grid(row=6, column=0, padx=20, pady=20)
        self.parenting_2 = ctk.CTkEntry(self, width=200, placeholder_text='Parentesco 2')
        self.parenting_2.grid(row=6, column=1, padx=20, pady=20)
        self.parenting_3 = ctk.CTkEntry(self, width=200, placeholder_text='Parentesco 3')
        self.parenting_3.grid(row=6, column=2, padx=20, pady=20)
        self.parenting_4 = ctk.CTkEntry(self, width=200, placeholder_text='Parentesco 4')
        self.parenting_4.grid(row=6, column=3, padx=20, pady=20)
        
        #* line 7
        self.irpf_1 = ctk.CTkEntry(self, width=200, placeholder_text='IRPF 1')
        self.irpf_1.grid(row=7, column=0, padx=20, pady=20)
        self.irpf_2 = ctk.CTkEntry(self, width=200, placeholder_text='IRPF 2')
        self.irpf_2.grid(row=7, column=1, padx=20, pady=20)
        self.irpf_3 = ctk.CTkEntry(self, width=200, placeholder_text='IRPF 3')
        self.irpf_3.grid(row=7, column=2, padx=20, pady=20)
        self.irpf_4 = ctk.CTkEntry(self, width=200, placeholder_text='IRPF 4')
        self.irpf_4.grid(row=7, column=3, padx=20, pady=20)
        
    def link_true(self):
        if self.link:
            self.frame_line_4.grid(row=4, column=1, columnspan=3, padx=20, pady=20, sticky='w')
        else:
            self.frame_line_4.grid_forget()
        
class RegisterJobSalary(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, width=250)
        self.grid(row=0, column=1, rowspan=3, columnspan=3 ,padx=20, pady=20, sticky='nsew')
        self.grid_columnconfigure((0,1,2), weight=1)
        
        self.home = parent
        
        font = ctk.CTkFont(family=FONT, size=20)
        self.btn_return = ctk.CTkButton(self, text='🔙', command=self.back, font=font, width=80)
        self.btn_return.grid(row=0, column=0,padx=20, pady=20)

        self.title = ctk.CTkLabel(self, text='Cadastro de Cargos & Salários', width=400, anchor='center', justify='center', font=ctk.CTkFont(size=40))
        self.title.grid(row=0, column=1, columnspan=2, padx=20, pady=20)
        
        self.position = ctk.CTkEntry(self, width=600, placeholder_text='Cargo')
        self.position.grid(row=1, column=0, columnspan=3, padx=20, pady=20)
        
        self.salary = ctk.CTkEntry(self, width=200, placeholder_text='Salário')
        self.salary.grid(row=2, column=0, padx=20, pady=20)
        self.bonus = ctk.CTkEntry(self, width=200, placeholder_text='Bônus')
        self.bonus.grid(row=2, column=1, padx=20, pady=20)
        self.workload = ctk.CTkEntry(self, width=200, placeholder_text='Carga Horária')
        self.workload.grid(row=2, column=2, padx=20, pady=20)
        
        
        self.save = ctk.CTkButton(self, text='Salvar', command=self.save)
        self.save.grid(row=5, column=0, padx=20, pady=20, sticky='w')
        
    def save(self):
        pass
    
    def back(self):
        self.grid_forget()
        self.home.tab.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        
class RegisterForm(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, width=250)
        self.grid(row=0, column=1, rowspan=3, columnspan=3 ,padx=20, pady=20, sticky='nsew')
        self.grid_columnconfigure((0,1), weight=1)
        
        self.home = parent
        
        font = ctk.CTkFont(family=FONT, size=20)
        self.btn_return = ctk.CTkButton(self, text='🔙', command=self.back, font=font, width=80)
        self.btn_return.grid(row=0, column=0,padx=20, pady=20)

        self.title = ctk.CTkLabel(self, text='Cadastro parâmetros para formulário', width=400, anchor='center', justify='center', font=ctk.CTkFont(size=40))
        self.title.grid(row=0, column=1, padx=20, pady=20)
        
        self.param_name = ctk.CTkEntry(self, width=200, placeholder_text='Parâmetro')
        self.param_name.grid(row=1, column=0, padx=20, pady=20)
        param_type = ctk.StringVar(value='entrada')
        self.param_type = ctk.CTkComboBox(self, width=200, values=['entrada', 'saída', 'ambos'], variable=param_type)
        self.param_type.grid(row=2, column=0, padx=20, pady=20)
        self.btn_save = ctk.CTkButton(self, text='Save', command=self.save)
        
        
    def back(self):
        self.grid_forget()
        self.home.tab.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        
    def save(self):
        pass
    
    
    
class Footer(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GRAY)
        self.grid(column=1, row=3, columnspan=3, sticky='nsew', padx=10, pady=10)
        self.grid_columnconfigure((0,1,2,3), weight=1)
        self.time_label = ctk.CTkLabel(self, fg_color=DARK_GRAY, font=ctk.CTkFont(size=12))
        self.time_label.grid(row=0, column=0, padx=20, pady=20)
        self.weather_label = ctk.CTkLabel(self, fg_color=DARK_GRAY, font=ctk.CTkFont(size=12))
        self.weather_label.grid(row=0, column=1, padx=20, pady=20, sticky='e')
        
        self.developed_by = ctk.CTkLabel(self, text='Developed by: St3in Tech')
        self.developed_by.grid(row=1, column=0, columnspan=2, padx=20, pady=20)
        
        self.update_time()
        self.update_weather()
        
        
    def update_time(self):
        self.now = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        self.time_label.configure(text=self.now)
        self.time_label.after(1000, self.update_time)
        
    def update_weather(self):
        response = requests.get(f'http://apiadvisor.climatempo.com.br/api/v1/weather/locale/3477/current?token={API_KEY}')
        data = response.json()
        temp = data['data']['temperature']
        condition = data['data']['condition']
        humidity = data['data']['humidity']
        self.weather_label.configure(text=f'Temperatura: {temp}°C - Condição do tempo: {condition} - humidade relativa: {humidity}')
        self.after(18000000, self.update_weather) # update each 5 hours
        
        
# Home()