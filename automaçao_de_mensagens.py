from win10toast import ToastNotifier
import pyautogui
import time
import pywhatkit as kit
import pandas as pd
#armazena as informaços das pessoas
dados = {'nome':[],'idade':[],'numero':[]}

while True: #inicia o lope perguntado nome é idade é numero de telefone
    nome = str(input('nome\n=>'))
    idade = int(input('idade\n=>'))
    numero = input('numero de telefone, digite o numero que voocê usa em seu WhatsApp \nex:+554999999999 \n=>')#eu quer ver se consigo fazer que o codigo envie uma mensgem para todos os numeros salvos
    
    dados['nome'].append(nome)
    dados['idade'].append(idade)
    dados['numero'].append(numero)
   
    df = pd.DataFrame(dados)
    print(df)
    continuar = input('vamos continuar?[s/n]\n=>')
    if continuar.lower()== 'n':
       planilha= input('salvar as informaços em uma planilha s/n\n=>')
       if planilha.lower()== 's':
           for numero in dados['numero']:
             try:# aqui pedi ajuda para o cht gpt mais ainda tive que arrumar pq tava dando erro 
                kit.sendwhatmsg_instantly(numero, 'Isso é uma mensagem de teste, obrigado por participar!')
                print(f"📨 Mensagem enviada para {numero}")
                time.sleep(5)  # Aguarda um tempo para evitar sobrecarga

                # Fecha a aba do WhatsApp Web
                pyautogui.hotkey('ctrl', 'w')  
                time.sleep(3)  # Aguarda um tempo antes de enviar para o próximo
             except Exception as e:
                print(f"⚠️ Erro ao enviar mensagem para {numero}: {e}")
           toaster = ToastNotifier()
           toaster.show_toast(
                    "Notificação",
                    "tarefa concluida",
                    threaded=True,
                    icon_path=None,
                    duration=3)
           df.to_excel('meu_arquivo.xlsx', index=False) #cria uma planilha com todas as informaços das pessas
           break
