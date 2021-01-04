#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  ex_grida.py
#
#  
#
from tkinter import *
from unidecode import unidecode
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from zabbix_api import ZabbixAPI
from platform import python_version
import sys
import socket
import os
import csv, re, sys

GRUPOID =[['ACCESSPOINT','39','10186'],['ACESSO','46','10186'],['ALARME','38','10186'],['BALANCA','40','10186'],
['CAMERA','37','10186'],['COLETORRM','42','10511'],['DVR','36','10694'],['EDA','41','10401'],
['IMPRESSORA','26','10437'],['LINUX','43','10001'],['WINDOWS','44','10081'],['PORTEIRO','48','10186'],
['PDV','29','11968'],['SAT','49','10186'],['SELF','55','11963'],['SWITCH','30','10451'],['TELEFONE','47','10186'],
['TERMINALCONSULTA','45','10186']]
GRUPO = ['ACCESSPOINT','ACESSO','ALARME','BALANCA','CAMERA','COLETORRM','DVR',
'EDA','IMPRESSORA','LINUX','WINDOWS','PORTEIRO','PDV','SAT','SELF','SWITCH','TELEFONE',
'TERMINALCONSULTA',]

root = Tk()
root.title("API-ZABBIX")
root.geometry("380x610")
#root.configure(background="gray")
root.resizable(0,0)

#inicio da interface grafica
Label(root, text="Import do Zabbix").grid(row=0, column=0,columnspan=2)
#edit loja
Label(root, text="Loja").grid(row=2, column=0)
ct = Entry(root,text="CT")
ct.grid(row=2,column=1)
#drop categoria

var_categoria = StringVar()
var_categoria.set(GRUPO[0])
drop_categoria = OptionMenu(root,var_categoria,*GRUPO)
drop_categoria.grid(row=3,column=0,columnspan=2)
#radio tipo de envio csv ou manual
envio = IntVar()
rb_csv = Radiobutton(root, text="Envio de CSV", variable=envio, value=1)
rb_csv.grid(row=4,column=0)
rb_csv = Radiobutton(root, text="Preenchimento manual", variable=envio, value=0)
rb_csv.grid(row=4,column=1)
#edit nome manual
Label(root, text="Nome").grid(row=5, column=0)
nome_manual = Entry(root,text="CT",state='disabled')
nome_manual.grid(row=5,column=1)
#edit ip manual
Label(root, text="IP").grid(row=6, column=0)
ip_manual = Entry(root,text="CT",state='disabled')
ip_manual.grid(row=6,column=1)
#edit descricao manual
Label(root, text="Descricao").grid(row=7, column=0)
desc_manual = Entry(root,text="CT",state='disabled')
desc_manual.grid(row=7,column=1)


mainloop()
