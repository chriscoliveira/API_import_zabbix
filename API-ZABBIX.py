#!/usr/bin/env python
# -*- coding: utf-8 -*-
#HENRIQUEVERSION3
import sys
import socket
from tkinter import *
from unidecode import unidecode
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
import os

path_root = os.path.abspath(os.getcwd()) #"/home/adming/RABBIX"


root = Tk()
root.title("API-ZABBIX")
root.geometry("380x610")
root.configure(background="gray")
root.resizable(0,0)

#=======================================================================================
# LABEL SEND IF SUCESS CONTANIER MAIN INVISIBLE FRAME 1 MAIN
# FUNCTION HIDE HIDE
#=======================================================================================
def verFrase():
	fraseCSV.pack()
	frame1.pack_forget()
	btnReturn.pack()

##### usar caso for dentro de sua loja #######################################################################
##############################################################################################################
##############################################################################################################
#for param in sys.argv :
#	lojaAtual = "CT"+param

##### usar caso for fora de sua loja #########################################################################
##############################################################################################################
##############################################################################################################
loja = open('ct.txt')
param = str(loja.readline())
param = re.sub('\n','',param)
lojaAtual = "CT"+param



dest_csv = "/tmp/CT"+param+".csv"
dest_txt = "/tmp/dados.txt"
path_txt = "dados.txt"	
#loja_txt = "CT"+param+".txt"

LOJAID = [['AG01','74'], ['AG02','75'], ['AG03','76'], ['AG04','77'], ['CD','95'], ['CD04','91'],
 ['CD05','89'], ['CD07','90'], ['CT03','67'], ['CT05','68'], ['CT06','61'], ['CT09','62'], ['CT13','52'],
  ['CT14','20'], ['CT15','53'], ['CT16','18'], ['CT17','63'], ['CT18','32'], ['CT20','64'], ['CT25','79'],
   ['CT27','80'], ['CT28','65'], ['CT30','69'], ['CT31','81'], ['CT32','70'], ['CT33','56'], ['CT34','54'],
    ['CT35','82'], ['CT36','66'], ['CT37','83'], ['CT38','84'], ['CT39','71'], ['CT41','17'], ['CT42','85'],
	 ['CT43','15'], ['CT44','16'], ['CT46','19'], ['CT47','57'], ['CT48','58'], ['CT49','59'], ['CT50','72'],
	  ['CT51','60'], ['CT53','73'], ['CT54','86'], ['GSB1','78']]

# vamos criar uma função de 'busca'
def encontrar(elemento):
    pos_i = 0 # variável provisória de índice
    pos_j = 0 # idem

    for i in range (len(LOJAID)): # procurar em todas as listas internas
        for j in range (i): # procurar em todos os elementos nessa lista
            if elemento in LOJAID[i][j]: # se encontrarmos elemento ('CT')
                pos_i = i # guardamos o índice i
                pos_j = j # e o índice j
                break # saímos do loop interno
            break # e do externo
    return (pos_i, pos_j) # e retornamos os índices

r = encontrar(lojaAtual) # chamamos a função e salvamos em r
IDLOJA = LOJAID[r[0]] #[r[1]]) # usa índices na lista como prova
#print(IDLOJA[1]) #retorno ID loja

#=======================================================================================
# ID GROUP AND ID TEMPLAT
#=======================================================================================

IdDoGrupo = ""
IdDoTemplate = ""

GRUPOID =[['ACCESSPOINT','39','10186'],['ACESSO','46','10186'],['ALARME','38','10186'],['BALANCA','40','10186'],
['CAMERA','37','10186'],['COLETORRM','42','10511'],['DVR','36','10694'],['EDA','41','10401'],
['IMPRESSORA','26','10437'],['LINUX','43','10001'],['WINDOWS','44','10081'],['PORTEIRO','48','10186'],
['PDV','29','11968'],['SAT','49','10186'],['SELF','55','11963'],['SWITCH','30','10451'],['TELEFONE','47','10186'],
['TERMINALCONSULTA','45','10186']]
def grupoID():

	# vamos criar uma função de 'busca'
	def encontrar(elemento2):
		pos_i = 0 # variável provisória de índice
		pos_j = 0 # idem

		for i in range (len(GRUPOID)): # procurar em todas as listas internas
			for j in range (i): # procurar em todos os elementos nessa lista
				if elemento2 in GRUPOID[i][j]: # se encontrarmos elemento ('CT')
					pos_i = i # guardamos o índice i
					pos_j = j # e o índice j
					break # saímos do loop interno
				break # e do externo
		return (pos_i, pos_j) # e retornamos os índices

	r = encontrar(variableHOST.get()) # chamamos a função e salvamos em r
	IDGRUPO = GRUPOID[r[0]] #[r[1]]) # usa índices na lista como prova
	
	IdDoGrupo = IDGRUPO[1] #Retorno ID Grupo
	IdDoTemplate = IDGRUPO[2]#Retorno ID Template

	# Cria um arquivo no modo de gravação (w)
	arquivo = open(path_txt, 'w')
	# Escreve no arquivo
	arquivo.write(str(IDLOJA[1])+"\n")
	arquivo.write(IdDoGrupo+"\n")
	arquivo.write(IdDoTemplate+"\n")
	arquivo.close()

#=======================================================================================
# LIST VISUAL D.BOX
#=======================================================================================
OptionHOST = ['ACCESSPOINT','ACESSO','ALARME','BALANCA','CAMERA','COLETORRM','DVR',
'EDA','IMPRESSORA','LINUX','WINDOWS','PORTEIRO','PDV','SAT','SELF','SWITCH','TELEFONE',
'TERMINALCONSULTA',]

#=======================================================================================
# SIMLESPACE ROOT UP
#=======================================================================================	
separator = Frame(root,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=5, pady=30)

#=======================================================================================
# FRAME 1
#=======================================================================================
frame1 = Frame(height = 420,width = 640,bg = 'MIDNIGHTBLUE')#CONTANIER-COMPONENTES
frame1.pack(side="top")

#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

title = Label(frame1, text="API-ZABBIX-XV-XVIII",background='white')
title.config(width=20)
title.config(font=("Courier",20,'bold'))
title.pack()

#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

#=======================================================================================
# D.BOX
#=======================================================================================
variableHOST = StringVar(frame1)
variableHOST.set(OptionHOST[0])

optHOST = OptionMenu(frame1, variableHOST, *OptionHOST)
optHOST.config(width=10, font=('Helvetica', 12), padx=100,pady=10, background='#81DAF5')
optHOST.pack()

#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

#=======================================================================================
# LABEL NAME STORE
#=======================================================================================
ct = Label(frame1, text="CT"+param, font="Arial 12 bold", fg='black',width=30, background='white')
ct.pack()


#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

path_csv = StringVar()

#=======================================================================================
# FUNCTION CHECK D.BOX
#=======================================================================================
teste = ""
def selecao():	
	if escolha.get() == 1:
		nome.configure(state='normal')
		ip.configure(state='normal')
		desc.configure(state='normal')
		btnEnviar.configure(state='normal')

	if escolha.get() == 2:

		try:

			nome.configure(state='disabled')
			ip.configure(state='disabled')
			desc.configure(state='disabled')
			btnEnviar.configure(state='normal')
			
			path_csv = askopenfilename(title='ESCOLHA O ARQUIVO CSV',filetypes = (("Arquivos CSV","*.csv"),("all files","*.*"))) # Isto te permite selecionar um arquivo		
			
			title.config(background="white")	
			title.config(text="GRUPO ESTÁ CORRETO?")#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			title.config(fg="red")
			optHOST.config(background="yellow")		
			btnEnviar.config(text="CONFIRMAR")
			btnEnviar.config(fg="white")
			btnEnviar.config(background='red')
			btnEnviar.configure(state='normal')
			messagebox.showinfo("Anteção", "Confira o grupo correspondente ao CSV selecionado!")
					
			#CORRETION CHIT IN CSV

			os.system("mv -v "+path_csv.replace(' ','\\ ')+" "+path_root.replace(' ','\\ ')+"/CT"+param+".csv")
			caminhoCSV = open("caminho.txt", 'w')
			caminhoCSV.writelines(path_csv.replace(' ','\\ '))
			caminhoCSV.close()
		
		except:
			title.config(text="CSV NÃO SELECIONADO!")#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
			title.config(fg="white")
			title.config(background='red')
			optHOST.config(background="#81DAF5")
			btnEnviar.configure(state='disabled')
			messagebox.showwarning("Warning","Arquivo CSV não selecionado!")
			
#=======================================================================================
# VARIABLE D.B
#=======================================================================================
escolha = IntVar()

#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

#=======================================================================================
# R.BUTTON 1 HAND
#=======================================================================================
R1 = Radiobutton(frame1, text="ENVIO MANUAL", variable=escolha, value=1, command=selecao)
R1.configure(padx=0,pady=20,width=30)
R1.pack( side='top')
#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

#=======================================================================================
# R.BUTTON 2 ARCHIVE CSV
#=======================================================================================
R2 = Radiobutton(frame1, text="ARQUIVO CSV", variable=escolha, value=2, command=selecao)
R2.configure(padx=0,pady=20,width=30)
R2.pack( side='top')

#=======================================================================================
# MESSAGE SEND CSV
#=======================================================================================
fraseCSV = Label(root, text="ARQUIVO ENVIADO\nCOM SUCESSO!")
fraseCSV.config(width=30)
fraseCSV.config(font=("Courier",20,'bold'))
fraseCSV.pack(side='top')
fraseCSV.pack_forget() #DEIXA LABEL INVISIVEL

#=======================================================================================
# SIMPLESPACE DOWN
#=======================================================================================
separatorDOWN = Frame(root,height=2, bd=1, relief=SUNKEN)
separatorDOWN.pack(fill=X, padx=5, pady=30)

#=======================================================================================
# SIMLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

#=======================================================================================
# OPTION ENTRY NAME
#=======================================================================================
Label(frame1, text="Name HOST ex: CT15PDV101",width=30,font=('bold'), background='#81DAF5').pack()
nome = Entry(frame1, state='disabled',width=30)
nome.pack()

#=======================================================================================
# SIMPLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

Label(frame1, text="IP HOST ex: 10.15.20.101",width=30,font=('bold'), background='#81DAF5').pack()
ip = Entry(frame1, state='disabled',width=30)
ip.pack()

#=======================================================================================
# SIMPLESPACE
#=======================================================================================
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

Label(frame1, text="Description ex: PDV 101",width=30,font=('bold'), background='#81DAF5').pack()
desc = Entry(frame1, state='disabled',width=30)
desc.pack()

#=======================================================================================
# SIMPLESPACE
#=======================================================================================	
separator = Frame(frame1,height=2, bd=1, relief=SUNKEN)
separator.pack(fill=X, padx=3, pady=3)

#=======================================================================================
# FUNCTION BUTTON SEND
#=======================================================================================
def btnENV():
	grupoID()	 

	arquivo = open("loja.txt", 'w')
	# Escreve no arquivo
	arquivo.write(lojaAtual)
	arquivo.close()

	if escolha.get() == 1:
		if nome.get() == "" or ip.get() == "":		
			title.config(text="PREENCHA OS CAMPOS")
			title.config(background='red')
			messagebox.showwarning("Warning","Preencha todos os campos!")
		try:
			socket.inet_aton(ip.get())#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$		
		#else:
			# Cria um arquivo no modo de gravação (w)
			arquivo = open(path_txt, 'a')

			# Escreve no arquivo	
			arquivo.writelines(unidecode(nome.get())+"\n")
			arquivo.writelines(ip.get()+"\n")
			arquivo.writelines(unidecode(desc.get())+"\n")
			arquivo.writelines(dest_csv+"\n")
			arquivo.close()
			
			os.system("cp "+path_txt+" "+dest_txt)
			#os.system("sshpass -p '@!&tenda2020#' ssh -Xt root@10.131.0.192 python /Scripts/zabbix_import/importar_csv.py "+dest_txt)
			os.system("python importar_csv.py")

			verFrase()

		except:
			title.config(background="red")
			title.config(fg="white")
			title.config(text="IP INCORRETO!")
			messagebox.showerror("Error", "Verifique seus dados!")
			#print("Verifique seus dados!")
				
#=======================================================================================
# ENVIO CSV
#=======================================================================================
	if escolha.get() == 2:		

		if os.stat("caminho.txt").st_size == 0:
			title.config(text="CSV NÃO SELECIONADO")
			title.config(background='red')							
	
		else:
			# Cria um arquivo no modo de gravação (w)
			arquivo = open(path_txt, 'a')

			# Escreve no arquivo	
			arquivo.writelines(nome.get()+"\n")
			arquivo.writelines(ip.get()+"\n")
			arquivo.writelines(desc.get()+"\n")
			arquivo.writelines(dest_csv+"\n")

			# FOREVER CLOSE ARCHIVE
			arquivo.close()

			with open("CT"+param+".csv", 'r') as f:
				with open("temp.csv", 'w') as t:
					for lines in f:
						new_line = lines.replace(",",";")
						new_lineUP = unidecode(new_line.upper())
						t.write(new_lineUP)
			f.close()
			t.close()

			os.system("mv temp.csv "+"CT"+param+".csv")
			
			#os.system("sshpass -p '@!&tenda2020#' scp "+path_txt+" root@10.131.0.192:"+dest_txt)#LA NO TOP
			os.system("cp CT"+param+".csv "+dest_csv)
			#os.system("sshpass -p '@!&tenda2020#' ssh -Xt root@10.131.0.192 python /Scripts/zabbix_import/importar_csv.py "+dest_txt)
			os.system("python importar_csv.py loja.txt")
			#os.system("sshpass -p '@!&tenda' ssh -Xt root@10.131.0.192 python /Scripts/zabbix_import/api_cria_mapa.py "+param)

			os.system("rm caminho.txt")
					
		verFrase()		

#=======================================================================================
# FUNCTION BUTTON RETURN
#=======================================================================================
def btnReturn():
	nome.delete(0, 'end')
	ip.delete(0, 'end')
	desc.delete(0, 'end')
	fraseCSV.pack_forget()
	btnReturn.pack_forget()
	separatorDOWN.pack_forget()
	btnEnviar.config(state='disabled')
	title.config(text="API-ZABBIX-XV-XVIII")
	title.config(background="white")
	title.config(fg="black")
	optHOST.config(background='#81DAF5')
	frame1.pack()	

#=======================================================================================
# BUTTON SEND MANUAL	
#=======================================================================================
btnEnviar = Button(frame1, text="ENVIAR", command=btnENV, background='#088A08',state='disabled')
btnEnviar.pack()

#=======================================================================================
# BUTTON RETURN OF THE PARTY	
#=======================================================================================
btnReturn = Button(root, text="RETORNAR", command=btnReturn, background='#088A08',state='normal')
btnReturn.pack()
btnReturn.pack_forget()

mainloop()
