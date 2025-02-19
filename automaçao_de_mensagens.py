import pywhatkit as kit
import pandas as pd
#armazena as informaços das pessoas
dados = {'nome':[],'idade':[],'numero':[]}

while True: #inicia o lope perguntado nome é idade é numero de telefone
    nome = str(input('nome\n=>'))
    idade = int(input('idade\n=>'))
    numero = input('numero de telefone\n=>')#eu quer ver se consigo fazer que o codigo envie uma mensgem para todos os numeros salvos
    
    dados['nome'].append(nome)
    dados['idade'].append(idade)
    dados['numero'].append(numero)

    df = pd.DataFrame(dados)
    print(df)
    continuar = input('vamos continuar?[s/n]\n=>')
    if continuar.lower()== 'n':
       planilha= input('salvar as informaços em uma planilha s/n\n=>')
       if planilha.lower()== 's':
           df.to_excel('meu_arquivo.xlsx', index=False) #cria uma planilha com todas as informaços das pessas
           break
