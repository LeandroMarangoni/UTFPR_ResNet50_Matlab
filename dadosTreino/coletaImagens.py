#Importa as bibliotecas
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

driver = webdriver.Chrome() # Cria uma instância Web
def scroll_to_bottom():
        last_height = driver.execute_script('\
        return document.body.scrollHeight')
    
        while True:
            driver.execute_script('\
            window.scrollTo(0,document.body.scrollHeight)')
            time.sleep(3)
    
            new_height = driver.execute_script('\
            return document.body.scrollHeight')
            try:
                driver.find_element_by_css_selector(".YstHxe input").click()
                time.sleep(3)
    
            except:
                pass
    
            if new_height == last_height:
                break
    
            last_height = new_height

def buscaAnimais(animais, nImagens):
    query = animais #O que vai ser buscado no Google Imagens
    driver.maximize_window() #Maximiza a tela do navegador
    driver.get('https://images.google.com/') #Abre o Google Imagens
    box = driver.find_element_by_xpath('//*[@id="sbtc"]/div/div[2]/input') #Procura a caixa de pesquisa na página
    box.send_keys(query) #Insere as palavras chaves na caixa
    box.send_keys(Keys.ENTER) #Pressiona enter para realizar a pesquisa

    scroll_to_bottom()

    for i in range(1, nImagens):
        try:
            img = driver.find_element_by_xpath( #Procura o elemento da imagem na página HTML
                '//*[@id="islrg"]/div[1]/div[' +
            str(i) + ']/a[1]/div[1]/img')
            img.screenshot('Download-Location' +  #Tira o print e salva com nome adequado na pasa
                        query + ' (' + str(i) + ').png')
            time.sleep(0.2) #Delay para evitar erros
        except:
            continue #Caso não encontre o elemento, passa pra próxima

extintos = ('Ariranha','Lobo Guará', 'Onça Pintada') #Tupla com os animais em risco de extinção
nreconhecidos = ('Cachorro','Gato','Cavalo') #Tupla com os animais sem risco de extinção

for animais in extintos:  #Para cada animal em risco na tupla...
    path = './' + animais #Diretório com o nome do animal
    os.makedirs(path) #Cria uma pasta com esse diretório 
    os.chdir(path) #Acessa a pasta para salvar as imagens internamente
    
    buscaAnimais(animais, 15) #Busca e printa as imagens do animal em risco

    os.chdir('../') #Volta para a pasta original para os próximos animais
    
os.makedirs('./Não Reconhecido') #Cria uma pasta para os animais sem risco
os.chdir('./Não Reconhecido')  #Acessa a pasta para salvar as imagens internamente
for animais in nreconhecidos:  #Para cada animal em risco na tupla
    buscaAnimais(animais, 15) #Busca e printa as imagens do animal sem risco
driver.close()