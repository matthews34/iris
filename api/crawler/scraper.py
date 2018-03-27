import requests
from bs4 import BeautifulSoup
import time
import os

URL = "https://uspdigital.usp.br/mercurioweb/PatrimonioMostrar?numpat=##START_INDEX##"
unidade = input('Unidade: ').rjust(3, '0')

def folderName(): # define a unidade e o nome da pasta destino dos dados

    try:
        foldersNames = open("NomesPastas", 'r')
        lines = foldersNames.read().splitlines() # lines recebe um array com tds as linhas exceto \n
        folderName = lines[int(unidade)-1] #folderName recebe a linha equivalente à unidade digitada
        foldersNames.close()
    except: # caso não exista o arquivo "NomesPastas" no mesmo diretório onde o programa está rodando, folderName recebe apenas o código da unidade
        print('Arquivo "NomesPastas" não encontrado')
        folderName = unidade

    return folderName


inicial = int(input('Ínicio: '))
final = int(input('Fim: '))

def dataDirectory(name): # troca para a pasta com nome igual a name, se falhar, cria essa pasta

    try:
        os.chdir(name)
    except:
        os.mkdir(name)
        os.chdir(name)

def itemData(i): #função retorna a sopa da ficha do item de código i

    rURL = URL.replace("##START_INDEX##", unidade + '.' + str(i).rjust(6,'0')) # rURL recebe URL substituindo "##START_INDEX##" pelo item de código i

    pageSoup = BeautifulSoup(requests.get(rURL).text, "html.parser") # sopa da página do item

    dataSoup = pageSoup.find("table", align = 'center', cellspacing ='1') # sopa da ficha do item

    return dataSoup

def main():

    inicio = time.time()

    dataDirectory(folderName()) # seta a pasta de destino dos dados
    log = open("log_" + unidade, 'a')

    for n in range(inicial, final + 1):
        print(unidade + '.' + str(n).rjust(6, '0'))
        dataSoup = itemData(n)
        myFile = open("teste" + str(n).rjust(6, '0') + ".txt", "w")
        if dataSoup is not None:
            myFile.write(dataSoup.get_text())
        else:
            log.write(str(n).rjust(6, '0') + '\n')
        myFile.close()

    log.close()

    fim = time.time()
    tempo = fim - inicio
    print("Tempo de execução: " + str((tempo/60)//1) + ' minuto e ' + str((tempo%60)//1) + " segundos")

main()
