import serial
import json
import time
from datetime import datetime
conexao=""

#Faz a procura da porta onde esta conectado op ESP32
for porta in range(10):
    try:
        conexao = serial.Serial("COM"+str(porta), 115200)
        print("Conectado na porta: ", conexao.portstr)
        break
    except serial.SerialException:
        pass

#Se a conexão for diferente de vazio
if conexao!="":
    #Cria um dicionario com os dados a serem salvo
    dicionario={}

    #Vai adicionar 10 dados de luminosidade
    cont=0
    while cont<10:
        resposta=conexao.readline()
        #O dicionario recebe a data com chave, e a resposta do ldr, depois é decodificado
        dicionario[str(datetime.now())]=[resposta.decode('utf-8')[0:3]]
        print(resposta.decode('utf-8')[0:3])
        cont+=1

    #Apos terminar, vai adicionar os dados no arquivo Json, e encerra a conexão
    with open('Temperatura.json', "w") as arq:
        json.dump(dicionario, arq)
    conexao.close()
    print("Conexão encerrada")
else:
    print("Sem portas disponíveis")