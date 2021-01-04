#!/usr/bin/env python
# -*- coding: utf-8 -*-
import csv, json ,re, sys
from zabbix_api import ZabbixAPI

Tipo = "Mapa"
#loja = open('loja.txt')
#for param in sys.argv :
#	LOJA = param
#usuario = open('usuario.txt')
#user = str(usuario.readline())
#user = re.sub('\n','',user)
loja = open('ct.txt')
LOJA = str(loja.readline())
LOJA = re.sub('\n','',LOJA)


zapi = ZabbixAPI(server="http://10.131.0.30/zabbix")
zapi.login("USUARIO_API","tenda123")

#LOJA=user.replace("CT","")

espaco = [70,125,180,235,290,345,400,455,510,565,620,675,730,785,840,895,950,1005,1060,1115,1170,1225,1280,1335,1390,1445,1500,1555,1610,1665,1720,1775,1830,1885,1940,1995,2050]

linhas = [125,225,325,425,525,625,725,825,925,1025,1125,1225,1325,1425,1525,1625,1725,1825,1925]

LogoTenda = 193

item_linha = linhas[0]

srv_linha = 30
srv_nome = "SRV"+"*"+LOJA+"*"
srv_img = 149
srv_id = []

pdv_linha = linhas[0]
pdv_nome = "CT"+LOJA+"PDV"
pdv_img = 194
pdv_id = []

sat_linha = linhas[1]
sat_nome = "CT"+LOJA+"SAT"
sat_img = 192
sat_id = []

tc_linha = linhas[2]
tc_nome = "CT"+LOJA+"BSP"
tc_img = 190
tc_id = []

lin_linha = linhas[3]
lin_nome = "CT"+LOJA
lin_img = 189
lin_id = []

win_linha = linhas[4]
win_nome = "CT"+LOJA
win_img = 188
win_id = []

imp_linha = linhas[5]
imp_nome = "CT"+LOJA+"I"
imp_img = 196
imp_id = []

dvr_linha = 605
dvr_nome = "CT"+LOJA+"DVR"
dvr_img = 195
dvr_id = []

sw_linha = linhas[6]
sw_nome = "CT"+LOJA+"-"
sw_img = 153
sw_id = []

tip_linha = linhas[7]
tip_nome = "CT"+LOJA+"TIP"
tip_img = 77
tip_id = []

rub_linha1 = linhas[8]
rub_linha2 = linhas[9]
rub_nome = "CT"+LOJA+"EDA"
rub_img = 197
rub_id = []

cam_linha = linhas[6]
cam_nome = "CT"+LOJA+"CAM"
cam_img = 191
cam_id = []




dados = {}
dados['selementid']= 1
dados['elementtype']= 4
dados['iconid_off']= 193
dados['x']=50
dados['y']=20
json_tmp = []
json_tmp.append(dados)

'''
################### busca info dos PDVS
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona

json_tmp1 = {}

pdvs = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + pdv_nome + '*'},
    'searchWildcardsEnabled': True
})


contpdvs = 0
if pdvs:
	linha_PDV = item_linha
	print 'PDVs encontrados!'
        for pdv in pdvs:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = pdv_img
            if (contpdvs == 25 or contpdvs == 50 or contpdvs == 75 or contpdvs == 100):
                contpdvs = 0
            if (cont < 25 ):
                dados['x'] = espaco[contpdvs]
		dados['y'] = item_linha
            if (cont > 24 and cont < 50 ):
                dados['x'] = espaco[contpdvs]
		dados['y'] = item_linha + 100
            info1['hostid'] = pdv['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            contpdvs = contpdvs + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')


'''
################### busca info dos sat
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

sats = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + sat_nome + '*'},
    'searchWildcardsEnabled': True
})



if sats:
	item_linha = item_linha + 100
	linha_SAT = item_linha
	print 'SATs encontrados!'
        for sat in sats:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = sat_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = sat['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')


'''
################### busca info dos tc
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

tcs = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + tc_nome + '*'},
    'searchWildcardsEnabled': True
})



if tcs:
	item_linha = item_linha + 100
	linha_TCS = item_linha
	print 'Busca precos encontrados!'
        for tc in tcs:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = tc_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = tc['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')

'''
################### busca info dos lin
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

lins = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + lin_nome + '*'},
    'groupids': 43,
    'searchWildcardsEnabled': True
})



if lins:
	item_linha = item_linha + 100
	linha_LIN = item_linha
	print 'Maquinas Linux encontradas!'
        for lin in lins:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = lin_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = lin['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')

'''
################### busca info dos win
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

wins = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + win_nome + '*'},
    'groupids': 44,
    'searchWildcardsEnabled': True
})



if wins:
	item_linha = item_linha + 100
	linha_WIN = item_linha
	print 'Maquinas Windows encontradas!'
        for win in wins:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = win_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = win['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')


'''
################### busca info dos imp
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

imps = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + imp_nome + '*'},
    'searchWildcardsEnabled': True
})



if imps:
	item_linha = item_linha + 100
	linha_IMP = item_linha
	print 'Impressoras encontradas!'
        for imp in imps:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = imp_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = imp['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')

'''
################### busca info dos dvr
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

dvrs = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + dvr_nome + '*'},
    'searchWildcardsEnabled': True
})


cont = 11
if dvrs:
	print 'DVRs encontrados!'
        for dvr in dvrs:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = dvr_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = dvr['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')


'''
################### busca info dos sw
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

sws = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + sw_nome + '*'},
    'searchWildcardsEnabled': True
})



if sws:
	item_linha = item_linha + 100
	linha_SW = item_linha
	print 'Switchs encontrado!'
        for sw in sws:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = sw_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = sw['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')



'''
################### busca info dos tip
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

tips = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + tip_nome + '*'},
    'searchWildcardsEnabled': True
})



if tips:
	item_linha = item_linha + 100
	linha_TIP = item_linha
	print 'Telefones IP encontrados!'
        for tip in tips:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = tip_img
            dados['x'] = espaco[cont]
            dados['y'] = item_linha
            info1['hostid'] = tip['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')


'''
################### busca info dos rub
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

rubs = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + rub_nome + '*'},
    "sortfield": "name",
    'searchWildcardsEnabled': True
})

linha_final_rub = 0
contrub = 0
if rubs:
        item_linha = item_linha + 100
	linha_RUB = item_linha
	print 'Rubs encontrados!'
        for rub in rubs:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = rub_img
            if (contrub == 25 or contrub == 50 or contrub == 75 or contrub == 100):
                contrub = 0
            if (cont < 25 ):
                dados['x'] = espaco[contrub]
		dados['y'] = item_linha
		linha_final_rub = item_linha
            if (cont > 24 and cont < 50 ):
                dados['x'] = espaco[contrub]
		dados['y'] = item_linha + 100
		linha_final_rub = item_linha + 100
            if (cont > 49 and cont < 75 ):
                dados['x'] = espaco[contrub]
		dados['y'] = item_linha + 200
		linha_final_rub = item_linha + 200
            if (cont > 74 and cont < 100 ):
                dados['x'] = espaco[contrub]
		dados['y'] = item_linha + 300
		linha_final_rub = item_linha + 300
            info1['hostid'] = rub['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            contrub = contrub + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')


'''
################### busca info dos cam
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

cams = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + cam_nome + '*'},
    'searchWildcardsEnabled': True
})

contcams = 0
if cams:
        item_linha = linha_final_rub + 100
	linha_CAM = item_linha
	print 'Cameras encontradas!'
        for cam in cams:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = cam_img
            if (contcams == 25 or contcams == 50 or contcams == 75 or contcams == 100):
                contcams = 0
            if (cont < 25 ):
                dados['x'] = espaco[contcams]
		dados['y'] = item_linha
            if (cont > 24 and cont < 50 ):
                dados['x'] = espaco[contcams]
		dados['y'] = item_linha + 100
            if (cont > 49 and cont < 75 ):
                dados['x'] = espaco[contcams]
		dados['y'] = item_linha + 200
            if (cont > 74 and cont < 100 ):
                dados['x'] = espaco[contcams]
		dados['y'] = item_linha + 300
            info1['hostid'] = cam['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            contcams = contcams + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
	if (cont < 50):
		qtde_cams = item_linha + 100
	if (cont < 75):
		qtde_cams = item_linha + 200
	if (cont < 100):
		qtde_cams = item_linha + 300
	if (cont < 125):
		qtde_cams = item_linha + 400
else:
    print ('host não encontrado')


'''
################### busca info dos srv
'''
cont=0
dados = {} #dados recebidos da query no for
info1 = {} #recebe os ids do zabbix
info = [] #recebe infos com os ids e adiciona
json_tmp1 = {}

srvs = zapi.host.get({
    'output': ['host', 'name', 'status'], #atribui a variavel host os campos selecionados
    'search': {'host': '*' + srv_nome + '*'},
    'searchWildcardsEnabled': True
})


cont = 10
if srvs:
	print 'Servidores encontrados!'
        for srv in srvs:
            dados['selementid'] = '1'
            dados['elementtype'] = 0
            dados['iconid_off'] = srv_img
            dados['x'] = espaco[cont]
            dados['y'] = srv_linha
            info1['hostid'] = srv['hostid']
            info.append(info1)
            dados['elements'] =  info
            cont = cont + 1
            json_tmp.append(dados)
            dados = {}
            element = {}
            info = []
            info1 = {}
else:
    print ('host não encontrado')


'''
################# adiciona os shapes
'''
linha_s = [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400]
espaco_s = [0,620,630]

dados = {}
dados['text']= "Tenda Atacado CT"+LOJA+" Monitoramento Zabbix"
dados['type']= 0
dados['x']= 150
dados['y']= 20
dados['width']= 300
dados['height']= 80
dados['border_type']= 0
dados['font']= 9
dados['font_size']= 25
dados['font_color']= "FF0000"
json_shapes = []
json_shapes.append(dados)

dados = {}
conts = 0
if pdvs:
    dados['text']= "PDV"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_PDV
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if sats:
    dados['text']= "SAT"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_SAT
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if tcs:
    dados['text']= "Terminal Consulta"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_TCS
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if lins:
    dados['text']= "Maquina\nLinux"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_LIN
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if wins:
    dados['text']= "Maquina\nWindows"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_WIN
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if imps:
    dados['text']= "Impress."
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_IMP
    linha_dvr = linha_IMP
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if dvrs:
    dados['text']= "DVRS"
    dados['type']= 0
    dados['x']= 600
    dados['y']= linha_dvr
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    json_shapes.append(dados)
    dados = {}
if cams:
    dados['text']= "Cameras"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_CAM
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if sws:
    dados['text']= "Switch"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_SW
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if tips:
    dados['text']= "Telefone"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_TIP
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if rubs:
    dados['text']= "EDA"
    dados['type']= 0
    dados['x']= 0
    dados['y']= linha_RUB
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}
if srvs:
    dados['text']= "Servidores"
    dados['type']= 0
    dados['x']= 500
    dados['y']= 0
    dados['width']= 50
    dados['height']= 100
    dados['border_type']= 0
    dados['font']= 9
    dados['font_size']= 11
    dados['font_color']= "FF0000"
    conts = conts + 1
    json_shapes.append(dados)
    dados = {}


pdv_json = {"name":"Mapa_LOJA_CT"+LOJA,"width": 1800,"height": qtde_cams + 100}

pdv_json['selements'] = json_tmp

pdv_json['shapes'] = json_shapes

print ("\n\n\nMapa Criado "+LOJA)
#print( pdv_json )

#salva os dados em json
with open('resultado.json','w') as f:
    json.dump(pdv_json, f,indent=4)


#apaga o mapa se ja existir

mapas = zapi.map.get({
        "output": [
		"sysmapid",
		"name"
	]
})

#print(mapas)


if mapas:
	for mapa in mapas:
		idmapa = mapa['sysmapid']
		nomemapa = mapa['name']
		if (nomemapa == "Mapa_LOJA_CT"+LOJA):
			zapi.map.delete([idmapa])
			print("Mapa " +nomemapa+ " deletado!")

#cria o mapa
mapa = zapi.map.create(pdv_json)

