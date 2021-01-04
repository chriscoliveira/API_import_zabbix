#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv, re, sys
from zabbix_api import ZabbixAPI
import os
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

################### DADOS DO TXT ################### 
arquivo = open("dados.txt", 'r').read().splitlines()

GrupoIDLoja = arquivo[0]
GrupoIDGrupo = arquivo[1]
TemplateID =  arquivo[2]
nome =  arquivo[3]
descricao = arquivo[5]
iP =  arquivo[4]
fcsv =  arquivo[6]
#print("idloja"+GrupoIDLoja)
#print("idgrupo"+GrupoIDGrupo)
#print("idtemplate"+TemplateID)
#print("nome"+nome)
#print("descr"+descricao)
#print("ip"+iP)
#print(fcsv)
####################################################

zapi = ZabbixAPI(server="http://10.131.0.30/zabbix")
zapi.login("CT18","tenda123")


#################### Dados ###################
itemadd = []

if nome != "":
    itemadd1 = nome, iP, descricao
    itemadd.append(itemadd1)

if nome == "":
    itemADD = open(fcsv)
    listas = csv.reader(itemADD, delimiter=";")
    itemadd1 = []
    itemadd = []
    for lista in listas:
        itemadd1 = lista[0], lista[1], lista[2]
        itemadd.append(itemadd1)
print(itemadd)
############################################


contador = 0
#print("\n\nCadastro: "+Tipo+"\n\n")

for x in itemadd:
    nome = (itemadd[contador][0])
    iP =  (itemadd[contador][1])
    descricao =  (itemadd[contador][2])
    hostcriado = zapi.host.create({
        "host": nome,
        "status": 0,
        "description": descricao,
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": iP,
                "dns": "",
                "port": 10050
            }
        ],
        "groups": [
            {
                "groupid": GrupoIDLoja
            },
            {
                "groupid": GrupoIDGrupo
            }
        ],
        "templates": [
            {
                "templateid": TemplateID
            }
        ]
    })
    contador=contador+1
    print(nome+ " criado! id:"+hostcriado["hostids"][0])
print("\nTotal de itens cadastrados:"+str(contador))

os.system("rm -v loja.txt dados.txt")