from tkinter import *
from tkinter.font import BOLD, ITALIC
from tkinter import messagebox 
from tkinter import ttk
import mysql.connector 
from mysql.connector import Error
global vselSN
global hostX, userX, passwordX, databaseX, cursorX 

#Dados para conexão com o banco de dados
hostX = 'localhost'
userX = 'root'
passwordX = 'acesso123'
databaseX = 'academico'
tabela_dp = 'alunos'
chavep_dp = 'id_aluno'

# Lista de mensagens
mensagem_bd = ['Erro de Conexão ao banco de dados.',
               'Erro ao criar banco de dados.',
               'Erro ao criar tabela no banco de dados.',
               'Registro cadastrado com sucesso',
               'Erro ao cadastrar o registro',
               'Erro ao deletar o cadastro',
               'Deseja deletar o registro selecionado?']

def conectar():
    global banco
    try:
        banco = mysql.connector.connect(
            host = hostX, 
            user = userX,
            password = passwordX)
        #print('Conexão 0: ', banco)
    except Error as erro:
        print(mensagem_bd[0])








def validar_campos():
    if (e_descricao.get() == ''):
        messagebox.showerror(title='ERRO', message='Campo de Descrição não pode ficar vazio')
        
    if(e_local.get() == ''):
        messagebox.showerror(title='ERRO', message='Campo de Local não pode ficar vazio')
        
    if(e_vrevento.get() == ''):
     messagebox.showerror(title='ERRO', message='Campo de Valor do evento não pode ficar vazio')
     
    if(e_faixaetaria.get() == ''):
         messagebox.showerror(title='ERRO', message='Campo de Faixa etária não pode ficar vazio')
         
    if(e_informacao.get() == ''):
         messagebox.showerror(title='ERRO', message='Campo de Informação não pode ficar vazio')  
          
    if(e_contatos_t1.get() == ''):
         messagebox.showerror(title='ERRO', message='Campo de Contatos 1  não pode ficar vazio')
           
    if(e_contatos_t2.get() == ''):
         messagebox.showerror(title='ERRO', message='Campo de Contatos 2 não pode ficar vazio') 
         
    if(e_mail.get() == ''):
         messagebox.showerror(title='ERRO', message='Campo de Email não pode ficar vazio')
  
def salvar_evento():

    messagebox.showinfo(title='Salvar', message='Você clicou no botão de Salvar')
    validar_campos()


def excluir_evento():

    messagebox.showwarning(title='Exclusão', message='Você clicou no botão de Excluir')



def selValor():

    global vselSN

    vselSN = varSN.get()

    if (vselSN == 'N'):

        e_vrevento['state'] = 'disable'

    else:

        e_vrevento['state'] = 'normal'

lista_tipo = ['Saúde & Fitness',
              'Evento na SmartFit Academia',
              'Palestra',
              'Aula experimental',
              'Feira',
              'Religioso',
              'Curso',
              'Show',
              'Exposições artísticas',
              'Corrida',
              'Campeonato',
              'Jogos']


def converte_minuscula(event):
    vemail = e_mail.get()
    e_mail.delete(0,'end')
    e_mail.insert(0,vemail.lower())

cor_fundo = '#000000'

cor_fundo_roxo = '#8309B6'

cor_fundo_laranja = '#FF7A00'

cor1 = '#c3c3c3'

cor2 = '#c3c3c3'

cor3 = '#000000'

cor4 = '#c3c3c3'

cor5 = '#c3c3c3'

cor_bg_botao = '#080808'

cor_fg_botao = '#fae8e8'



l_fonte = 'Roboto'

caixa_combo_diasx = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31']
caixa_combo_mesx = ['01','02','03','04','05','06','07','08','09','10','11','12']
caixa_combo_anosx = ['2022']

caixa_combo_horax = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24',]
caixa_combo_minutosx = ['01','02','03','04','05','06','07','08','09','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25','26','27','28','29','30','31','32','33','34','35','36','37',]


form = Tk()

form.title('Controle de eventos')

form.geometry('800x450')

form.configure(bg=cor_fundo)



frame_1 = Frame(form, width=790, height=75, bg=cor1, pady=0, padx=0, relief="flat")

frame_1.place(x=5, y=5)



frame_2 = Frame(form, width=790, height=95, bg=cor2, pady=0, padx=0, relief="flat")

frame_2.place(x=5, y=85)



frame_3 = Frame(form, width=790, height=70, bg=cor4, pady=0, padx=0, relief="flat")

frame_3.place(x=5, y=185)



frame_4 = Frame(form, width=790, height=100, bg=cor5, pady=0, padx=0, relief="flat")

frame_4.place(x=5, y=260)



l_descricao = Label(frame_1, text='Descrição', font=(l_fonte, 12), bg=cor1, fg=cor3)

l_descricao.place(x=38, y=10)



e_descricao = Entry(frame_1, font=(l_fonte, 12), relief='solid', bg=cor1, fg=cor3)

e_descricao.place(x=120, y=10, width=550, height=25)



l_local = Label(frame_1, text='Local do evento', font=(l_fonte, 12), bg=cor1, fg=cor3)

l_local.place(x=0, y=40)



e_local = Entry(frame_1, font=(l_fonte, 12), relief='solid', bg=cor1, fg=cor3)

e_local.place(x=120, y=40, width=650, height=25)



l_data = Label(frame_2, text='Data do evento', font=(l_fonte, 12), bg=cor2, fg=cor3)

l_data.place(x=0, y=5)

escolher_data = StringVar()
caixa_combo_dias = ttk.Combobox(frame_2, textvariable=escolher_data)
caixa_combo_dias['values']=caixa_combo_diasx
caixa_combo_dias.place(x=175, y=5, width=45, height=20)

escolher_mes= StringVar()
caixa_combo_mes = ttk.Combobox(frame_2, textvariable=escolher_mes)
caixa_combo_mes['values']=caixa_combo_mesx
caixa_combo_mes.place(x=222, y=5, width=45, height=20)

escolher_anos = StringVar()
caixa_combo_anos = ttk.Combobox(frame_2, textvariable=escolher_anos)
caixa_combo_anos['values']=caixa_combo_anosx
caixa_combo_anos.place(x=269, y=5, width=55, height=20)




l_hora = Label(frame_2, text='Hora do evento', font=(l_fonte, 12), bg=cor2, fg=cor3)

l_hora.place(x=355, y=5)


escolher_hora = StringVar()
caixa_combo_hora = ttk.Combobox(frame_2, textvariable=escolher_hora)
caixa_combo_hora['values']=caixa_combo_horax
caixa_combo_hora.place(x=480, y=5, width=45, height=20)

escolher_minutos= StringVar()
caixa_combo_minutos = ttk.Combobox(frame_2, textvariable=escolher_minutos)
caixa_combo_minutos['values']=caixa_combo_minutosx
caixa_combo_minutos.place(x=535, y=5, width=45, height=20)




l_vr_cobrado = Label(frame_2, text='É cobrado?', font=(l_fonte, 12), bg=cor2, fg=cor3)

l_vr_cobrado.place(x=0, y=35)



varSN = StringVar()

r1 = Radiobutton(frame_2, text="Sim", command=selValor, variable=varSN, value='S', bg=cor2,font=(l_fonte,'12'))

r1.place(x=100, y=35)



r2 = Radiobutton(frame_2, text="Não", command=selValor, variable=varSN, value='N', bg=cor2, font=(l_fonte,'12'))

r2.place(x=100, y=55)



l_vr_evento = Label(frame_2, text='Valor do evento', font=(l_fonte, 12), bg=cor2, fg=cor3)

l_vr_evento.place(x=350, y=35)



e_vrevento = Entry(frame_2, font=(l_fonte, 12), relief='solid', bg=cor2, fg=cor3)

e_vrevento.place(x=480, y=35, width=200, height=25)



l_faixaetaria = Label(frame_2, text='Faixa etária', font=(l_fonte, 12), bg=cor2, fg=cor3)

l_faixaetaria.place(x=375, y=65)



e_faixaetaria = Entry(frame_2, font=(l_fonte, 12), relief='solid', bg=cor2, fg=cor3)

e_faixaetaria.place(x=480, y=65, width=200, height=25)



l_tpevento = Label(frame_3, text='Tipo do evento', font=(l_fonte, 12), bg=cor4, fg=cor3)

l_tpevento.place(x=0, y=5)

t_evento = StringVar()
caixa_combo_t = ttk.Combobox(frame_3, textvariable=t_evento)
caixa_combo_t['values']=lista_tipo
caixa_combo_t.place(x=110, y=5, width=189, height=25)



l_informacao = Label(frame_3, text='Informações', font=(l_fonte, 12), bg=cor4, fg=cor3)

l_informacao.place(x=20, y=35)



e_informacao = Entry(frame_3, font=(l_fonte, 12), relief='solid', bg=cor4, fg=cor3)

e_informacao.place(x=120, y=35, width=600, height=25)

#

l_contatos = Label(frame_4, text='Contatos', font=(l_fonte, 20, BOLD), bg=cor5, fg=cor3)

l_contatos.place(x=38, y=0)



l_telefone1 = Label(frame_4, text='Celular', font=(l_fonte, 12), bg=cor5, fg=cor3)

l_telefone1.place(x=58, y=35)



e_contatos_t1 = Entry(frame_4, font=(l_fonte, 12), relief='solid', bg=cor5, fg=cor3)

e_contatos_t1.place(x=120, y=35, width=200, height=25)



l_telefone2 = Label(frame_4, text='Celular', font=(l_fonte, 12), bg=cor5, fg=cor3)

l_telefone2.place(x=420, y=35)



e_contatos_t2 = Entry(frame_4, font=(l_fonte, 12), relief='solid', bg=cor5, fg=cor3)

e_contatos_t2.place(x=480, y=35, width=200, height=25)



l_email = Label(frame_4, text='E-mail', font=(l_fonte, 12), bg=cor5, fg=cor3)

l_email.place(x=58, y=65)



e_mail = Entry(frame_4, font=(l_fonte, 12), relief='solid', bg=cor5, fg=cor3)

e_mail.place(x=120, y=65, width=560, height=25)
e_mail.bind("<FocusOut>", converte_minuscula)



# Botões

#img_bt_inserir=PhotoImage(file = r"D:\Giuliano\Lógica de programação\Python\dist\Projeto Academico\salvar.png")

#img_bt_excluir=PhotoImage(file=r"D:\Giuliano\Lógica de programação\Python\dist\Projeto Academico\excluir-16.png")

#img_bt_sair=PhotoImage(file=r"D:\Giuliano\Lógica de programação\Python\dist\Projeto Academico\sair-24.png")



botao_inserir = Button(form, text='Salvar', relief='groove',command=salvar_evento,font=(l_fonte,'12', BOLD), fg=cor_bg_botao, activeforeground='orange')

botao_inserir.place(x=500, y=400, width=80, height=30)



botao_excluir = Button(form, text='Excluir',  relief='groove', command=excluir_evento,font=(l_fonte,'12', BOLD), fg=cor_bg_botao, activeforeground='orange')

botao_excluir.place(x=600, y=400, width=80, height=30)



botao_sair = Button(form, text='Sair', relief='groove',command=quit, font=(l_fonte,'12', BOLD), fg=cor_bg_botao, activeforeground='orange')

botao_sair.place(x=700, y=400, width=80, height=30)



form.mainloop()
