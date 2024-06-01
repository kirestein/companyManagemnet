import customtkinter as ctk
from settings import *
import tkinter as tk
import tkinter.messagebox
import requests
# import tkcalendar as cal
from tkcalendar import Calendar, DateEntry
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass

ctk.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

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
        # self.register_employees.grid(row=0, column=1, rowspan=3, columnspan=3 ,padx=20, pady=20, sticky='nsew')
        # self.register_employees.grid_columnconfigure((0,1,2,3), weight=1)
        RegisterEmployee(self)
        print('entrou')
    
        
        
        
    #     self.protocol('WM_DELETE_WINDOW', self.on_close)
        
    # def on_close(self):
    #     self.master.deiconify()
    #     self.destroy()
    
class RegisterEmployee(ctk.CTkScrollableFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=COMPLEMENTAR_GREEN, width=250, corner_radius=10)
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
        self.frame_1 = ctk.CTkFrame(self, fg_color=COMPLEMENTAR_GREEN)
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
                          foreground='white', borderwidth=2)
        self.birthday.grid(row=2, column=2, padx=20, pady=20)
        self.frame_cep = ctk.CTkFrame(self, fg_color=COMPLEMENTAR_GREEN, border_color='#eee')
        self.frame_cep.grid(row=2, column=3, padx=5, pady=20)
        self.frame_cep.grid_columnconfigure((0, 1), weight=1)
        self.cep_var = ctk.StringVar()
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
        self.frame_4 = ctk.CTkFrame(self, fg_color=COMPLEMENTAR_GREEN)
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
        self.frame_4_1 = ctk.CTkEntry(self, fg_color=COMPLEMENTAR_GREEN, border_color=COMPLEMENTAR_GREEN)
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
        self.frame_6 = ctk.CTkFrame(self, fg_color=COMPLEMENTAR_GREEN)
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
        self.frame_6_1 = ctk.CTkFrame(self, fg_color=COMPLEMENTAR_GREEN)
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
        
    def back(self):
        self.grid_forget()
        self.home.tab.grid(row=0, column=1, padx=20, pady=20, sticky='nsew')
        
        
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
    
# class Main(ctk.CTkFrame):
#     def __init__(self, parent):
#         super().__init__(master=parent, fg_color=WHITE, width=140)
#         self.grid(rowspan=3, column=0, sticky='nsew', padx=10, pady=10, )
#         self.columnconfigure((0,1,2,3), weight=1)
#         self.rowconfigure((0,1,2,3), weight=1, uniform='a')
#         # self.pack(side='left', expand=True, fill='x', padx=10, pady=10)
#         # self.place(relx=0, rely=0, relwidth=0.4, relheight=0.9)
        
#         self.label = ctk.CTkLabel(self, text='Olá', text_color=BLACK)
#         self.label.grid(row=0, column=0)
        # self.pack(pady=10)
        
# class MainRight(ctk.CTkFrame):
#     def __init__(self, parent):
#         super().__init__(master=parent, fg_color=GREEN)
#         self.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)
#         # self.pack(side='right', expand=True, fill='x', padx=10, pady=10)
#         # self.place(relx=0.5, rely=0, relwidth=0.4, relheight=0.9)
        
#         self.label = ctk.CTkLabel(self, text='Bom dia', text_color=BLACK)
#         self.label.grid(row=0, column=1)
#         # self.pack(pady=10)
    
    
class Footer(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent, fg_color=DARK_GRAY)
        self.grid(column=1, row=3, columnspan=3, sticky='nsew', padx=10, pady=10)
        # self.pack(side='bottom', expand=True, fill='x', padx=10, pady=10)
        # self.place(rely=0.9, relwidth=1, relheight=0.1)